import json
import csv


USERS_JSON = 'users.json'
BOOKS_CSV = 'books.csv'
RESULT_3_JSON = 'result_3.json'


def read_from_json(json_file: str) -> dict:
    """Чтение json-файлов"""
    with open(json_file, 'r') as f:
        data = json.load(f)
        return data


def create_users_list(users: dict) -> list:
    """Создание нового списка пользователей (список словарей) с четырьмя параметрами для каждого"""
    users_list = list()
    for user in users:
        users_list.append({
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age'],
            'books': []
        })
    return users_list


def read_books(csv_file: str) -> list:
    """Чтение файла с книгами и создание списка книг с параметрами каждой книги (список словарей)"""
    with open(csv_file) as f:
        books = csv.reader(f)
        next(books)    # Пропускаем заголовок с названиями столбцов
        return list(books)


def create_books_list(books: list) -> list:
    """Создание списка книг - список словарей с параметрами книг"""
    books_list = list()
    for i in books:
        books_list.append({
            'title': i[0],
            'author': i[1],
            'pages': int(i[3]),
            'genre': i[2]
        })
    return books_list


def create_result_users_list(users_list: list, books_list: list) -> list:
    """Собираем итоговый массив (распределение книг между пользователями)"""
    books = iter(books_list)    # Сначала делаем генератор из списка словарей с книгами
    while True:    # Многократно проходим по списку пользователей, распределяя по одной книге за итерацию
        try:
            for user in users_list:
                user['books'].append(next(books))
        except StopIteration:  # Отлавливаем исключение StopIteratiion и, в случае его возникновения, останавливаем цикл
            break
    return users_list


def write_result_file(users_list: list):
    """Записываем итоговый результат в файл .json"""
    with open(RESULT_3_JSON, 'w') as f:
        json.dump(users_list, f, default=str)


if __name__ == "__main__":
    read_users = read_from_json(USERS_JSON)
    create_users_list = create_users_list(read_users)
    read_books = read_books(BOOKS_CSV)
    create_books_list = create_books_list(read_books)
    create_result_users_list = create_result_users_list(create_users_list, create_books_list)
    write_result_file(create_result_users_list)
    read_from_json(RESULT_3_JSON)
