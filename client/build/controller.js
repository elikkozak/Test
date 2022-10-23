"use strict";
(function () {
    const data = new Data();
    const render = new ViewModule();
    $("#search-btn").on("click", function () {
        let ingredientName = $("#ingredient-input").val();
        let filterByGluten = $("#gluten-checkbox").is(":checked");
        let filterByDairy = $("#dairy-checkbox").is(":checked");
        data.generateRecipes(ingredientName, filterByGluten, filterByDairy).then((result) => {
            render.renderPage(result);
        });
    });
    $(".recipes-container").on("click", ".recipe-img", function (e) {
        if (e.target && e.target.parentElement.className === "recipe-card") {
            const ingredients = e.target.parentElement.children[2];
            const ingredientsList = ingredients.getElementsByTagName('ul')[0];
            const ingredientName = ingredientsList.getElementsByTagName('li')[0].textContent;
            alert(ingredientName);
        }
    });
})();
