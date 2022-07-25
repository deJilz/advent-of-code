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
	// declare variables
	ifstream infile("day02.txt");
	string bounds, ch, passwrd;
	int low_b, high_b, k, delim;
	
	// loop through each line - taking advantage of the space seperator
	while (infile >> bounds >> ch >> passwrd) {
		// find splitter
		delim = bounds.find("-");
		// get low bound
		low_b = stoi(bounds.substr(0, delim));
		// get high bound
		high_b = stoi(bounds.substr(delim+1, string::npos));
		// check low and high - XOR on the condition
		if (!(passwrd[low_b-1] == ch[0]) != !(passwrd[high_b-1] == ch[0])) {
			k++;
		}
	}
	cout << "Correct password count: " << k;
}