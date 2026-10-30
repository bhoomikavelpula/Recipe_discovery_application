document.addEventListener("DOMContentLoaded", function () {
    const recipeCards = document.querySelectorAll(".recipe-card");
    const modal = document.getElementById("recipe-modal");
    const modalTitle = document.getElementById("modal-title");
    const modalImage = document.getElementById("modal-image");
    const modalInstructions = document.getElementById("modal-instructions");
    const closeModal = document.querySelector(".close");

    // Recipe data for instructions (for demonstration)
    const recipes = {{ recipes | tojson }}; // Pass recipes to JavaScript

    // Open modal on recipe card click
    recipeCards.forEach(card => {
        card.addEventListener("click", function () {
            const recipeId = parseInt(card.getAttribute("data-id"));
            const recipe = recipes.find(r => r.id === recipeId);

            if (recipe) {
                modalTitle.textContent = recipe.title;
                modalImage.src = recipe.image;
                modalInstructions.textContent = recipe.instructions;
                modal.style.display = "block";
            }
        });
    });

    // Close modal on close button click
    closeModal.addEventListener("click", function () {
        modal.style.display = "none";
    });

    // Close modal when clicking outside of it
    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});
