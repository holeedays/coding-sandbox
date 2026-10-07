console.log("Hello World!");


const mainContainer: HTMLDivElement | null = document.querySelector("main") as HTMLDivElement | null;

if (mainContainer !== null) {
    mainContainer.setAttribute("style", "width: 100%; height: 100%");
    mainContainer.style.background = "#000000";
    mainContainer.style.color = "#ffffff";
    mainContainer.style.textAlign = "center";
    mainContainer.style.alignContent = "center";
    mainContainer.innerHTML = "HELLO WORLD";
}
