#!/usr/bin/env python3
import os
import sys
import subprocess
from AtcoderToolUtil import save_contest_id

def main():
		if len(sys.argv) != 2:
				print("Usage: acinit <contest_id>")
				sys.exit(1)
		cid = sys.argv[1]
		root = os.getcwd()
		src_dir = os.path.join(root, "src")
		os.makedirs(src_dir, exist_ok=True)

		contest_dir = os.path.join(src_dir, cid)
		os.makedirs(contest_dir, exist_ok=False)

		# 問題 a～g を順次ダウンロード
		for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
				task_dir = os.path.join(contest_dir, letter)
				os.makedirs(task_dir, exist_ok=True)
				
				url = f"https://atcoder.jp/contests/{cid}/tasks/{cid}_{letter}"
				try:
						subprocess.run(
								["oj", "download", url],
								cwd=task_dir,
								check=True
						)
				except subprocess.CalledProcessError:
						# 問題が存在しない場合はスキップ
						continue

		tpl_path = os.path.join(root, "template.cpp")
		with open(tpl_path) as f:
				tpl = f.read()

		# 各ディレクトリの main.cpp をテンプレートで上書き
		for entry in os.listdir(contest_dir):
				prob_dir = os.path.join(contest_dir, entry)
				main_cpp = os.path.join(prob_dir, "main.cpp")
				with open(main_cpp, "w") as out:
						out.write(tpl)

		save_contest_id(cid)

if __name__ == "__main__":
		main()
