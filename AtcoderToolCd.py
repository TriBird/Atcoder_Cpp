# AtcoderToolCd.py
#!/usr/bin/env python3
import sys
from AtcoderToolUtil import save_contest_id

def main():
    if len(sys.argv) != 2:
        print("Usage: accd <contest_id>")
        sys.exit(1)
    cid = sys.argv[1]
    save_contest_id(cid)
    # 印字されたパスを使って shell 側で cd できます
    print(f"src/{cid}")

if __name__ == "__main__":
    main()
