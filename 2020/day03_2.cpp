// packages
#include <iostream>
#include <string>
#include <fstream>

// namespaces
using namespace std;

/*
	Connor DeJohn
	July 25 2022
	Advent of Code 2020
	
	answer: 1592662500
*/

int main() {
	ifstream infile("day03.txt");
	string line;
	
	// declare variables
	int xpos, ypos, k, xtemp, right, down;
	xpos = ypos = k = 0;
	double prod = 1;
	bool pa = false;
	
	// define tobogan slope
	int slopes[5][2] = {{1,1}, {3,1}, {5,1}, {7,1}, {1,2}};
	
	// check each tobogan slope
	for (int i = 0; i < 5; i++) {
		
		// read in for readability
		right = slopes[i][0];
		down = slopes[i][1];
		
		pa = false;
		while (infile >> line) {
			// handle the down 2
			if (((down % 2) == 0) && pa) {
				pa = false;
				continue;
			} else {
				pa = true;
			}
			
			// get current xpos column
			xtemp = xpos % line.length();
			
			// check value at current pos
			if (line[xtemp] == '#') {
				k++;
			}
			
			//move - only need right because down is 1
			xpos += right;
		}
		
		//cout << "The tobogan hit " << k << " trees.\n";
		
		// calculate output
		prod *= k;
		
		// reset for next go
		xpos = ypos = k = 0;
		infile.clear();
		infile.seekg(0);
	}
	cout<<fixed << "final: " << prod << "\n"; // output
	return 0;
}