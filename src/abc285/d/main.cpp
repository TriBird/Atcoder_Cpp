#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)

int main() {
	int n;
	cin >> n;

	// 入力処理、木構造でもっとく
	map<string,string> to;
	vector<string> s(n), t(n);
	rep(i,n) cin >> s[i] >> t[i];
	rep(i,n) to[s[i]] = t[i];
	
	set<string> used;
	
	// 変換前ユーザ名で探索
	for (string ss : s) {
		string ns = ss;

		// 一度通ったところは判定しない
		while (!used.count(ns)) {
			used.insert(ns);

			// 木構造の途中にあるかもだから探索（内部はdfs?）
			auto it = to.find(ns);
			// 変換先が見つからなかったらサイクルになる心配もないよね
			if (it == to.end()) break;

			// 変換先と変換元が衝突してたらだめだよ
			ns = it->second;
			if (ns == ss) {
				cout << "No" << endl;
				return 0;
			}
		}
	}
	cout << "Yes" << endl;
	return 0;
}

