import json
import csv


# Чтение файла с пользователями
with open('users.json', 'r') as us:
    users = json.load(us)

# Создание нового списка пользователей (список словарей) с четырьмя параметрами для каждого
users_list = list()
for user in users:
    users_list.append({
        'name': user['name'],
        'gender': user['gender'],
        'address': user['address'],
        'age': user['age'],
        'books': []
    })

# print(users_list)
# print(len(users_list))

# Чтение файла с книгами и создание списка книг с параметрами каждой книги (список словарей)
chosen_books = list()
with open('books.csv') as csvfile:
    books = csv.reader(csvfile)
    next(books)    # Пропускаем заголовок с названиями столбцов
    for i in books:
        chosen_books.append({
            'title': i[0],
            'author': i[1],
            'pages': int(i[3]),
            'genre': i[2]
        })

# Собираем итоговый массив (распределение книг между пользователями)
books = iter(chosen_books)    # Сначала делаем генератор из списка словарей с книгами

while True:    # Многократно проходим по списку пользователей, распределяя по одной книге за итерацию
    try:
        for i in range(len(users_list)):
            users_list[i]['books'].append(next(books))
    except StopIteration:    # Отлавливаем исключение StopIteratiion и, в случае его возникновения, останавливаем цикл
        break

# Записываем итоговый результат в файл ,json
with open('result_2.json', 'w') as f:
    json.dump(users_list, f, default=str)

# Читаем записанный результат для проверки
with open('result_2.json', 'r') as res:
    result = json.load(res)
