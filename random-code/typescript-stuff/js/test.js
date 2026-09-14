"use strict";
// this is the start of something new
Object.defineProperty(exports, "__esModule", { value: true });
const helloWorldLiteral = "Hello World";
console.log(helloWorldLiteral);
const someNumberArray = [1, 2, 3, 4, 5, 432];
// we made this into a property :)
const logNumbersSqred = (someNumberArray) => {
    for (let i = 0; i < someNumberArray.length; i++) {
        // need to run this or the strict compiler won't shut up...
        const number = someNumberArray[i];
        if (number !== undefined)
            console.log(Math.pow(number, 2));
    }
};
logNumbersSqred(someNumberArray);
;
class MyClass {
    customButton;
    constructor(func) {
        this.customButton = {
            button: document.createElement("button"),
            function: func
        };
    }
    changeFuncOfButton(overrideFunc) {
        if (this.customButton === null) {
            console.warn("Custom button is not initialized");
            return;
        }
        const button = this.customButton.button;
        this.customButton = {
            button: button,
            function: overrideFunc
        };
    }
}
//# sourceMappingURL=test.js.map