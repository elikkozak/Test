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
            result = list(map(lambda ingredient: ingredient["name"],result))
            return result
    except TypeError as e:
        return(e)

def get_gluten_ingredients():
    return get_ingredients_from_table("gluten")
    

def get_dairy_ingredients():
    return get_ingredients_from_table("dairy")



def get_non_gluten_recipes(recipes):
    pass


def get_non_dairy_recipes(recipes):
    pass


if __name__ == "__main__":
    print(get_gluten_ingredients())
    print(get_dairy_ingredients())