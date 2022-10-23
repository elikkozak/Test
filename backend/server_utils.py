import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def get_ingredients_from_table(table_name):
    try:
        with connection.cursor() as cursor:
            query = f'SELECT * FROM {table_name};'
            cursor.execute(query)
            result = cursor.fetchall()
            result = list(map(lambda ingredient: ingredient["name"], result))
            return result
    except TypeError as e:
        return (e)


def get_gluten_ingredients():
    return get_ingredients_from_table("gluten")


def get_dairy_ingredients():
    return get_ingredients_from_table("dairy")


def is_recipe_free_from_allergic_ingredients(recipe, allergic_ingredients):
    ingredients_list = recipe["ingredients"]
    return set(ingredients_list).isdisjoint(allergic_ingredients)


def get_non_gluten_recipes(recipes):
    allergic_ingredients = get_gluten_ingredients()
    recipes = list(filter(lambda recipe: is_recipe_free_from_allergic_ingredients(
        recipe, allergic_ingredients), recipes))
    return recipes


def get_non_dairy_recipes(recipes):
    allergic_ingredients = get_dairy_ingredients()
    recipes = list(filter(lambda recipe: is_recipe_free_from_allergic_ingredients(
        recipe, allergic_ingredients), recipes))
    return recipes


def create_recipe_obj(recipe_data):
    return {

        "title": recipe_data["title"],
        "thumbnail": recipe_data["thumbnail"],
        "ingredients": recipe_data["ingredients"],
        "href":recipe_data["href"]
    }
