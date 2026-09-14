#include<iostream>;
#include<string>;
#include<vector>;
#include "../headers/test.h"; 

// just random stuff I'm doing
void randomCodeSetOne() {
	std::string a { "Hello World!" };
	std::string b { "Bye World!" };

	std::cout<<"Before Text Conversion:"<<a<<'\n';
	modifyString(a, b);
	std::cout<<"After Text Conversion:"<<b<<'\n';
}
// class creation example
void randomCodeSetTwo() {
	// the "new" keyword here returns a pointer and allocates the class instance to the heap, preventing it from being destroyed when left out of scope
	//Player* p1 = new Player("Geoffrey Williams", 101.2);
	Player p1("Geoffrey Williams", 101.2);

	std::cout<<"Health of "<<p1.name<<": "<<p1.health<<'\n'; 
}

int main() {
	randomCodeSetTwo();

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
