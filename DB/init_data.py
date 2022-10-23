import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


dairy_ingredients = ["Cream", "Cheese", "Milk", "Butter",
                     "Creme", "Ricotta", "Mozzarella", "Custard", "Cream Cheese"]
gluten_ingredients = ["Flour", "Bread", "spaghetti", "Biscuits", "Beer"]


def insert_to_dairy_table(dairy_ingredients):
    with connection.cursor() as cursor:
        query = "INSERT INTO dairy(name) VALUES(%s)"
        data = list([(ingredient_name)
                    for ingredient_name in dairy_ingredients])
        cursor.executemany(query, data)
        connection.commit()


def insert_to_gluten_table(gluten_ingredients):
    with connection.cursor() as cursor:
        query = "INSERT INTO gluten(name) VALUES(%s)"
        data = list([(ingredient_name)
                    for ingredient_name in gluten_ingredients])
        cursor.executemany(query, data)
        connection.commit()


def insert_to_tables():
    insert_to_dairy_table(dairy_ingredients)
    insert_to_gluten_table(gluten_ingredients)


if __name__ == "__main__":
    insert_to_tables()
