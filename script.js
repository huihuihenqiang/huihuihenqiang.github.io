document.addEventListener("DOMContentLoaded", function () {
    const leavesContainer = document.getElementById("leaves-container");

    function createLeaf() {
        const leaf = document.createElement("div");
        leaf.className = "leaves";
        leaf.style.left = Math.random() * window.innerWidth + "px";
        leaf.style.top = -20 + "px"; // Start leaves above the viewport
        leavesContainer.appendChild(leaf);

        anime({
            targets: leaf,
            translateY: [0, window.innerHeight + 20],
            rotate: () => anime.random(-30, 30) + "deg",
            duration: () => anime.random(5000, 10000),
            easing: "linear",
            delay: () => anime.random(0, 500), // Add a random delay to simulate a more natural falling effect
            complete: () => {
                leaf.remove();
                createLeaf();
            },
        });
    }

    // Create initial leaves
    for (let i = 0; i < 50; i++) {
        createLeaf();
    }
});
