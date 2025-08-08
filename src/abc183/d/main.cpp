#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)

int main(){
	int N, W;
	cin >> N >> W;

	vector<int> timeline;
	timeline.resize(200000, 0);

	// imos法っていうらしい
	rep(i, N){
		int s, t, p;
		cin >> s >> t >> p;
		timeline[s] -= p;
		timeline[t] += p;
	}

	// こっちで実際の値を計算していく、O(N)
	rep(i, (int)timeline.size()){
		timeline[i] += i == 0 ? W : timeline[i-1];
		if(timeline[i] < 0){
			cout << "No" << endl;
			return 0;
		}
	}

	cout << "Yes" << endl;
	return 0;
}