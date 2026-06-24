const resultBtn = document.getElementById("result");
const inputField = document.getElementById("inputField");
const maxValue = 1000;
const columnBackground = document.getElementById("columnBackground");

resultBtn.addEventListener("click", () => {
    const inputToInt = Number(inputField.value);

    if (isNaN(inputToInt) || inputToInt <= 0) {
        columnBackground.style.height = "0px";
        return;
    }

    const ratio = Math.min(inputToInt / maxValue, 1);
    columnBackground.style.height = (ratio * 200) + "px";
});