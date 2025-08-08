#!/usr/bin/env python3
import os
import sys
import subprocess
import pty
from AtcoderToolUtil import load_contest_id

def run_test_with_ansi(cmd, cwd):
    """疑似PTYを開いてoj testを実行し、ANSIカラー付き出力を取得"""
    master_fd, slave_fd = pty.openpty()
    proc = subprocess.Popen(
        cmd,
        cwd=cwd,
        stdin=subprocess.DEVNULL,
        stdout=slave_fd,
        stderr=slave_fd,
        text=True
    )
    os.close(slave_fd)

    output = ""
    try:
        while True:
            chunk = os.read(master_fd, 1024)
            if not chunk:
                break
            output += chunk.decode("utf-8", errors="ignore")
    except OSError:
        pass
    finally:
        os.close(master_fd)

    proc.wait()
    return output, proc.stdout

def main():
		cid = load_contest_id()
		if not cid:
				print("No contest ID found. Run acinit or accd first.")
				sys.exit(1)

		prob = sys.argv[1] if len(sys.argv) > 1 else None
		base = os.path.join(os.getcwd(), "src", cid)

		targets = []
		if prob:
				targets = [os.path.join(base, prob)]
		else:
				for d in sorted(os.listdir(base)):
						path = os.path.join(base, d)
						if os.path.isdir(path):
								targets.append(path)

		last_main = None
		for d in targets:
				main_cpp = os.path.join(d, "main.cpp")
				exe = os.path.join(d, "main")
				subprocess.run(
						["g++", main_cpp, "-std=c++17", "-O2", "-o", exe],
						check=True
				)

				out, _ = run_test_with_ansi(["oj", "test", "-c", exe], cwd=d)
				print(out, end="")  # ANSIカラー付きでそのまま表示

				lines = [l for l in out.strip().splitlines() if l]
				if not lines:
						sys.exit(1)
				last_line = lines[-2]
				print("last_line: ",  lines[-2])
				if "FAILURE" in last_line:
						sys.exit(1)
				if "SUCCESS" in last_line:
						last_main = main_cpp
				else:
						# 不明な出力
						sys.exit(1)

		if last_main:
				subprocess.run(
						f'cat "{last_main}" | iconv -f UTF-8 -t CP932 | clip.exe',
						shell=True,
						check=True
				)
				print(f"Copied source of {last_main} to clipboard.")

if __name__ == "__main__":
		main()
