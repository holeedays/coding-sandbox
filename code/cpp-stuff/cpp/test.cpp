#include<iostream>
#include<string>
#include<vector>

#include<windows.h>
#pragma comment(lib, "user32.lib") // need this to include windows.h without explicitly changing options in the linker
#include<thread>
#include<chrono>
#include "../headers/test.h"


// just random stuff I'm doing
/*
void randomCodeSetOne() {
	std::string a { "Hello World!" };
	std::string b { "Bye World!" };

	std::cout<<"Before Text Conversion:"<<a<<'\n';
	modifyString(a, b);
	std::cout<<"After Text Conversion:"<<b<<'\n';
}
*/

Player* p1 = nullptr;
// equivalent to start
void init() {
	// the "new" keyword here returns a pointer and allocates the class instance to the heap, preventing it from being destroyed when left out of scope
	// Player* p1 = new Player("Geoffrey Williams", 101.2);
	p1 = new Player("Geoffrey Williams", 101.2);
	std::cout<<"Health of "<<p1->name<<": "<<p1->health<<'\n';
}
// all frame-based methods go in this function
void update() {	
	if (!p1) {
		std::cout<<"Player one doesn't exist, cannot proceed"<<'\n';
		return;
	}
	// get an alias to our player one
	Player& playerOne = *p1;
	Vector2 playerInput { playerOne.getInput() };
	if (playerInput.x != 0 || playerInput.y != 0) {
		std::cout<<playerInput.x<<", "<<playerInput.y<<'\n';
	}
}

void updateThread(float targetFPS) {
	// direct initialization (e.g. using curly braces) does not allow narrow conversion/casting... compiler throws error
	// we can just do this instead
	int targetFrameDurationMS = (int) 1.0/targetFPS*1000.0;	
	while (true) {
		// do whatever
		update();
		
		// pause thread for our target frame count per second
		std::this_thread::sleep_for(
			std::chrono::milliseconds(targetFrameDurationMS)
		);
	}
}

int main() {
	float fps { 60.0 };
	init(); // init our player
	updateThread(fps); // creates controlled polling of our current thread (like a draw-like function)
	
	return 1;
}

void modifyString(std::string& string, std::string& newString) {
	string = newString;	
}

Player::Player(std::string name, float health) : 
	name(name), 
	health(health)
{
	std::cout<<name<<" Has Spawned!"<<'\n';
} 

Vector2 Player::getInput() {
	Vector2 input {0 , 0};
	// bitwise check with largest 16 bit int; equivalent to checking whether the key is pressed or not (only works IF capslock/shift/etc keys are not pressed
	// along with the target key)
	if ((GetKeyState('W') & 0x8000) || (GetKeyState(VK_UP) & 0x8000)) {
		input.y = -1;
	}
	if ((GetKeyState('S') & 0x8000) || (GetKeyState(VK_DOWN) & 0x8000)) {
		input.y = 1;
	}
	if ((GetKeyState('A') & 0x8000) || (GetKeyState(VK_LEFT) & 0x8000)) {
		input.x = -1;
	}
	if ((GetKeyState('W') & 0x8000) || (GetKeyState(VK_RIGHT) & 0x8000)) {
		input.x = 1;
	}
	
	return input;
}
