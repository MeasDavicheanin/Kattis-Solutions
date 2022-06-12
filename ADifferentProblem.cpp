#include<bits/stdc++.h>
using namespace std;
int main() {
	long long a, b;
	while (cin >> a >> b) {
		if (b - a < 0) {
			cout << (b - a)*-1 << endl;
		}
		else {
			cout << b - a << endl;
		}
	}
	return 0;
}