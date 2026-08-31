## What is up my dude

This is the start of something new maybe...

``` 
// textModFuncs.h
#ifndef TEXT_MODIFICATION_FUNCS
#define TEXT_MODIFICATION_FUNCS

#include<string>

inline constexpr std::string someText = "This some text, quite literally.";

void ModifyText(std::string& text);
void SwapTextPtrs(std::string*& textOnePtr, std::string*& textTwoPtr);

#endif

// textModFuncs.cpp
#include "./textModFuncs.h";
#include<string>

void ModifyText(std::string& text, std::string targetText) {
	text = targetText;
}

// not sure why i included this tbh
void SwapTextPtrs(std::string*& textOnePtr, std::string*& textTwoPtr) {
	std::string& tempPtr = textOnePtr;
	textOnePtr = textTwoPtr;
	textTwoPtr = tempPtr;
}

// main.cpp
#include<iostream>;
#include<string>;
#include "./textModeFuncs.h";


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
