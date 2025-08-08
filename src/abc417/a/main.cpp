#include <bits/stdc++.h>
using namespace std;
int main(){
    int a, b, c;
    string text;
    cin >> a >> b >> c;
    cin >> text;

    // textの先頭からb文字、末尾からc文字を削除
    text = text.substr(b, text.size() - b - c);
    cout << text << endl;

    return 0;
}