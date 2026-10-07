console.log("Hello world");
class IndexPage {
    constructor() {
    }
    init() {
        const mainContainer = document.querySelector("main");
        if (mainContainer === null)
            return;
        mainContainer.setAttribute("style", combineStrings("; ", "width: 100%", "height: 100%", "background: #000000", "color: #ffffff", "text-align: center", "align-content: center", "font-size: 20px", "font-weight: bold", "font-family: helvetica"));
        mainContainer.innerHTML = "Hello World!";
    }
}
function combineStrings(sep, ...strs) {
    let finalStr = "";
    strs.forEach((str) => finalStr += (sep + str));
    return finalStr;
}
const indexPage = new IndexPage();
indexPage.init();
export {};
//# sourceMappingURL=test.js.map