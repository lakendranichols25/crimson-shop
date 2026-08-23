// ==========================================
// CRIMSON SHOP - IMAGE PROTECTION
// ==========================================

document.addEventListener("DOMContentLoaded", function () {

    // Disable right-click on images
    document.addEventListener("contextmenu", function (event) {
        if (event.target.closest("img")) {
            event.preventDefault();
        }
    });

    // Prevent images from being dragged
    document.querySelectorAll("img").forEach(function (image) {

        image.setAttribute("draggable", "false");

        image.addEventListener("dragstart", function (event) {
            event.preventDefault();
        });

    });

    // Prevent common save/view shortcuts
    document.addEventListener("keydown", function (event) {

        // Ctrl + S
        if (event.ctrlKey && event.key.toLowerCase() === "s") {
            event.preventDefault();
        }

        // Ctrl + U
        if (event.ctrlKey && event.key.toLowerCase() === "u") {
            event.preventDefault();
        }

        // Ctrl + Shift + I
        if (
            event.ctrlKey &&
            event.shiftKey &&
            event.key.toLowerCase() === "i"
        ) {
            event.preventDefault();
        }

        // Ctrl + Shift + J
        if (
            event.ctrlKey &&
            event.shiftKey &&
            event.key.toLowerCase() === "j"
        ) {
            event.preventDefault();
        }

        // F12
        if (event.key === "F12") {
            event.preventDefault();
        }

    });

});