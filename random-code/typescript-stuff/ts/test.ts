
// this is the start of something new

const helloWorldLiteral: string = "Hello World";
console.log(helloWorldLiteral);

const someNumberArray: number[] = [1, 2, 3, 4, 5, 432];


// we made this into a property :)
const logNumbersSqred: (someNumberArray: number[]) => void = (someNumberArray: number[]) => {
	for (let i=0; i<someNumberArray.length; i++) {
		// need to run this or the strict compiler won't shut up...
		const number: number | undefined = someNumberArray[i];
		
		if (number !== undefined)
			console.log(Math.pow(number, 2));
	}
};


logNumbersSqred(someNumberArray);

/* NOTE: These things require a local live server */
interface CustomButtonInterface {
	button: HTMLButtonElement,
	function: () => void
};

class MyClass {
	protected customButton: CustomButtonInterface | null; 

	constructor(func: () => void) {
		this.customButton = {
			button: document.createElement("button"),
			function: func
		};
	}

	public changeFuncOfButton(overrideFunc: () => void): void {
		if (this.customButton === null) {
			console.warn("Custom button is not initialized");
			return;
		}

		const button: HTMLButtonElement = this.customButton.button;
		this.customButton = {
			button: button,
			function: overrideFunc
		};
	}
}
