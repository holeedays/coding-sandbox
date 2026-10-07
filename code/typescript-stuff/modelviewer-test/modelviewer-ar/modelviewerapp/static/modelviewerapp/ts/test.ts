console.log("Hello world");

class IndexPage {
    constructor() {

    }

    public init(): void {
        const mainContainer: HTMLDivElement | null = document.querySelector<HTMLDivElement>("main");
        if (mainContainer === null)
            return;

        mainContainer.setAttribute(
            "style", 
            combineStrings(
                "; ",
                "width: 100%",
                "height: 100%",
                "background: #000000",
                "color: #ffffff",
                "text-align: center",
                "align-content: center",
                "font-size: 20px",
                "font-weight: bold",
                "font-family: helvetica"
            )
        );
        mainContainer.innerHTML = "Hello World!";
    }   
}

function combineStrings(sep: string, ...strs: string[]): string {
    let finalStr: string = "";
    strs.forEach((str: string) => finalStr += (sep + str));
    return finalStr;
}

const indexPage: IndexPage = new IndexPage();
indexPage.init();
