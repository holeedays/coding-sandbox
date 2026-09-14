#include<string>;
#include<vector>;

#ifndef TEST
#define TEST 

void modifyString(std::string& string, std::string& newString);

class Player {
	public:
		std::string name;
		float health;
		std::vector<std::string> abilities;

		// constructor here...
		Player(std::string name, float health);
};

#endif