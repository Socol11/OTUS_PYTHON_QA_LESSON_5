import json
import csv


def read_users(file):
    """Чтение файла с пользователями"""
    with open(file, 'r') as us:
        users = json.load(us)
        return users


def create_users_list(users):
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


def read_books(file):
    """Чтение файла с книгами и создание списка книг с параметрами каждой книги (список словарей)"""
    f = open('books.csv')
    books = csv.reader(f)
    next(books)    # Пропускаем заголовок с названиями столбцов
    return books


def create_books_list(books):
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


def create_result_users_list(users_list, chosen_books):
    """Собираем итоговый массив (распределение книг между пользователями)"""
    books = iter(chosen_books)    # Сначала делаем генератор из списка словарей с книгами
    while True:    # Многократно проходим по списку пользователей, распределяя по одной книге за итерацию
        try:
            for user in users_list:
                user['books'].append(next(books))
        except StopIteration:  # Отлавливаем исключение StopIteratiion и, в случае его возникновения, останавливаем цикл
            break
    return users_list


def write_result_file(users_list):
    """Записываем итоговый результат в файл .json"""
    with open('result_3.json', 'w') as f:
        json.dump(users_list, f, default=str)


def read_result_file(file):
    """Читаем записанный результат для проверки"""
    with open('result_3.json', 'r') as res:
        result = json.load(res)
        return result


read_users = read_users('users.json')
create_users_list = create_users_list(read_users)
read_books = read_books('books.csv')
create_books_list = create_books_list(read_books)
create_result_users_list = create_result_users_list(create_users_list, create_books_list)
write_result_file(create_result_users_list)

# Сравниваем результаты работы разных вариантов кода (получились идентичными)
assert read_result_file('result_1.json') == read_result_file('result_2.json') == read_result_file('result_3.json')
