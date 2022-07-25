// packages
#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>

// namespaces
using namespace std;

/*
	Connor DeJohn
	July 24 2022
	Advent of Code 2020
*/

int main() {
	ifstream infile("day02.txt");
	string bounds, ch, passwrd;
	
	int low_b, high_b, delim, cnt, k;
	
	while (infile >> bounds >> ch >> passwrd) {
		// find splitter
		delim = bounds.find("-");
		// get low bound
		low_b = stoi(bounds.substr(0, delim));
		// get high bound
		high_b = stoi(bounds.substr(delim+1, string::npos));
		// get ch occurance in passwrd
		cnt = std::count(passwrd.begin(), passwrd.end(), ch[0]);
		// check if it falls within
		if ((low_b <= cnt) && (cnt <= high_b)) {
			k++;
		}
	}
	cout << "Correct password count: " << k;
}