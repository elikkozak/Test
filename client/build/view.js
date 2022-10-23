"use strict";
class ViewModule {
    renderPage(result) {
        $(".recipes-container").empty();
        const source = $("#recipe-template").html();
        const template = Handlebars.compile(source);
        const newHTML = template(result);
        $(".recipes-container").append(newHTML);
    }
}
