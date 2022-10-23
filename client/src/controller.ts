(function(){
    const data: Data = new Data();
    const render: ViewModule  = new ViewModule();


    $("#search-btn").on("click", function(){
        let ingredientName: string = <string> $("#ingredient-input").val()
        let filterByGluten: boolean = $("#gluten-checkbox").is(":checked")
        let filterByDairy: boolean = $("#dairy-checkbox").is(":checked")
        data.generateRecipes(ingredientName, filterByGluten, filterByDairy).then((result:any) => {
            render.renderPage(result)             
        })        
    
})}
)()