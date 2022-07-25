// packages
#include <iostream>
#include <string>
#include <fstream>
#include <vector>

// namespaces
using namespace std;

/*
	Connor DeJohn
	July 24 2022
	Advent of Code 2020
*/

int main() {
	ifstream file;
	string fname = "day01.txt", str;
	file.open(fname);
	
	vector<int> v = {};
	while (getline(file, str)){
		v.push_back(stoi(str));
    }
	
	// loop through array
	int r = v.size();
	for (int i = 0; i < r; i++) {
		for (int k = 0; k < r; k++) {
			if ((v.at(i) + v.at(k)) == 2020) {
				cout << "[*] Ans: " << (v.at(i) * v.at(k)) << "\n";
			}
		}
	}
}