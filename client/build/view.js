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
//     menu: [
//       { name: "Google", link: "http://google.com" },
//       { name: "Facebook", link: "http://facebook.com" },
//       { name: "Instagram", link: "http://nstagram.com" },
//       { name: "Twitter", link: "http://twitter.com" },
//     ]
//   };
//   const source = $('#menu-template').html();
//   const template = Handlebars.compile(source);
//   const newHTML = template(menuData);
//   // append our new html to the page
//   $('.menu').append(newHTML);
