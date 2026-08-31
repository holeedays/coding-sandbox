## What is up my dude

This is the start of something new maybe...

``` 
// textModFuncs.h
#ifndef TEXT_MODIFICATION_FUNCS
#define TEXT_MODIFICATION_FUNCS

inline constexpr std::string someText = "This some text, quite literally.";

std::string ModifyText(std::string& text);

#endif

// textModFuncs.cpp
#include "textModFuncs.h";

std::string ModifyText(std::string& text, std::string targetText) {
	text = targetText;
}


// main.cpp
#include <iostream>;
#include <string>;
#include "textModeFuncs.h";


int main() {
	// I'm not even sure if this is valid c++ code :/

	std::string helloWorldText {"Hello World"}

	std::cout<<helloWorldText<<"\n";

	// rvalue here is fine
	ModifyText(helloWorldText, "Bye World");

	std::cout<<helloWorldText<<"\n";

	return 0;
}

```
