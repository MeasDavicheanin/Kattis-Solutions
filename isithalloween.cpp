#include<bits/stdc++.h>
using namespace std;
int main() {
	string s;
	getline(cin,s);
	if (s[0] == 'O' && s[1] == 'C' && s[2] == 'T' && s[4] == '3' && s[5] == '1') {
		cout << "yup" << endl;
	}
	else if (s[0] == 'D' && s[1] == 'E' && s[2] == 'C' && s[4] == '2' && s[5] == '5') {
		cout << "yup" << endl;
	}
	else {
		cout << "nope" << endl;
	}
	return 0;
}