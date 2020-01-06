#include <bits/stdc++.h>

using namespace std;

int main() {
	string s[100];
	for (int i = 0; i < 100; i++) {
		cin >> s[i];
	}
	string res = "";
	int l = 50;
	int carry = 0;
	for (int i = l - 1; i >= 0; i--) {
		int n = carry;
		for (int j = 0; j < 100; j++) {
			n += (int) (s[j][i] - '0');
		}
		//cout << n << endl; For debugging
		string ns = to_string(n);
		res.push_back(ns[ns.size() - 1]);
		string c = ns.substr(0, ns.size() - 1);
		if (!c.empty())
			carry = stoi(c);
		else
			carry = 0;
	}
	if (carry != 0)
		res += to_string(carry);
	cout << endl;
	for (int i = res.size() - 1; i >= res.size() - 10; i--) {
		cout << res[i];
	}
	return 0;
}