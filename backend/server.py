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
def get_recipes(ingredient_name, filter_by_gluten, filter_by_dairy):
    recipes = requests.get(
        f"https://recipes-goodness.herokuapp.com/recipes/{ingredient_name}").json()["results"]
    if filter_by_gluten == "true":
        recipes = get_non_gluten_recipes(recipes)
    if filter_by_dairy == "true":
        recipes = get_non_dairy_recipes(recipes)

    recipes = filter_relevant_data_from_recipes(recipes)

    return {"recipes" :recipes}


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
