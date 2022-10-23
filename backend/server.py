from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import requests
from server_utils import *


app = FastAPI()

app.mount("/client/build", StaticFiles(directory="client/build"), name="static")


@app.get("/sanity")
def root():
    return "OK"


@app.get("/")
def root():
    return FileResponse("./client/build/index.html")


@app.get("/recipes")
def get_recipes(ingredientName, filterByGluten="false", filterByDairy="false"):
    try:
        ingredientName = ingredientName or "avocado"
        recipes = requests.get(
            f"https://recipes-goodness.herokuapp.com/recipes/{ingredientName}").json()["results"]
        if filterByGluten == "true":
            recipes = get_non_gluten_recipes(recipes)
        if filterByDairy == "true":
            recipes = get_non_dairy_recipes(recipes)

        recipes_data_list = [create_recipe_obj(
            recipe_data) for recipe_data in recipes]

        return {"recipes": recipes_data_list}
    except Exception as e:
        return e


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
