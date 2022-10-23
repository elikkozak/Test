class ViewModule{
    renderPage(result:any){
        $(".recipes-container").empty()
        const source = $("#recipe-template").html();
        const template = Handlebars.compile(source);
        const newHTML = template(result);
        $(".recipes-container").append(newHTML);

    
    }


}
