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
})();
