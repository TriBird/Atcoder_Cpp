# AtcoderToolUtil.py
#!/usr/bin/env python3
import os
import json

CONTEST_FILE = os.path.join(os.path.dirname(__file__), "contest.json")

def save_contest_id(contest_id):
    data = {"contest_id": contest_id}
    with open(CONTEST_FILE, "w") as f:
        json.dump(data, f)

def load_contest_id():
    try:
        with open(CONTEST_FILE) as f:
            data = json.load(f)
        return data.get("contest_id")
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    # テスト用
    import sys
    if len(sys.argv)==2:
        save_contest_id(sys.argv[1])
        print("saved:", load_contest_id())
    else:
        print("current:", load_contest_id())
