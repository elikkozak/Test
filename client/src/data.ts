class Data{
    async generateRecipes(ingredientName:string, filterByGluten:boolean, filterByDairy:boolean){
        let dataPlayers = await $.get(`/recipes?ingredientName=${ingredientName}&filterByGluten=${filterByGluten}&filterByDairy=${filterByDairy}`);
        return dataPlayers
    }
}