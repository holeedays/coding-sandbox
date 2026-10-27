#include <iostream>
#include <string>

// placeholder for value
template <int16_t len>
// trying to emulate a print function here
void print(const char* (&argv)[len], const std::string& sep = "\n") {
	// note to self, you cannot do a for (... : argv) {} loop with standard argv
	for (int i = 0; i < len; i++) {
		std::cout << argv[i] << sep;
	}
}

int main() {
	const char* argv[] = { "Hello", "World", "How", "Are", "You", "Doing", "Today", "?" };
	print(argv, " ");
	return 0;
}