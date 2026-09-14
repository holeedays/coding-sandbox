#include<string>
#include<vector>

#ifndef TEST
#define TEST 

void modifyString(std::string& string, std::string& newString);

struct Vector2 {
	int x;
	int y;
};

class Player {
	public:
		std::string name;
		float health;
		std::vector<std::string> abilities;

		// constructor here...
		Player(std::string name, float health);
		
		void move();
		Vector2 getInput();
};

#endif