## What is up my dude

This is the start of something new maybe...

``` 
#include <iostream>
#include <string>



std::string ModifyText(std::string& text) {
	text = "Bye World"
}


int main() {
	// I'm not even sure if this is valid c++ code :/

	std::string helloWorldText {"Hello World"}

	std::cout<<helloWorldText<<"\n";

	ModifyText(helloWorldText);

	std::cout<<helloWorldText<<"\n";

	return 0;
}

```
