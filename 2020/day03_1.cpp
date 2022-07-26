// packages
#include <iostream>
#include <string>
#include <fstream>
//#include <algorithm>

// namespaces
using namespace std;

/*
	Connor DeJohn
	July 25 2022
	Advent of Code 2020
*/

int main() {
	ifstream infile("day03.txt");
	string line;
	// define tobogan slope
	int right = 3;
	//int down = 1;
	
	// declare variables
	int xpos, ypos, k, xtemp;
	xpos = ypos = k = 0;
	
	while (infile >> line) {
		// get current xpos column
		xtemp = xpos % line.length();
		
		// check value at current pos
		if (line[xtemp] == '#') {
			k++;
		}
		
		//move - only need right because down is 1
		xpos += right;
	}
	
	cout << "The tobogan hit " << k << " trees.";
	return 0;
}