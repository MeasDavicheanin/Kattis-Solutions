#include<bits/stdc++.h>
using namespace std;
int main() {
	int n;
	double sum=0;
	cin >> n;
	for (int i = 0;i < n; i++) {
		double q, y;
		cin >> q >> y;
		sum += q * y;
	}
	cout << fixed << setprecision(3) << endl;
	cout << sum << endl;
	return 0;
}