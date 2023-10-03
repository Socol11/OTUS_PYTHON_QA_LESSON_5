import json
import pandas as pd


# Чтение файла с пользователями
with open('users.json', 'r') as us:
    users = json.load(us)

# Создание нового списка пользователей (список словарей) с четырьмя параметрами для каждого
users_list = list()
user_dict = dict()
for user in users:
    user_dict['name'] = user['name']
    user_dict['gender'] = user['gender']
    user_dict['address'] = user['address']
    user_dict['age'] = user['age']
    user_dict['books'] = []
    users_list.append(user_dict)
    user_dict = dict()

# Чтение файла с книгами
books = pd.read_csv('books.csv')

# Создание списка книг с параметрами каждой книги (список словарей)
chosen_books = list()
book_dict = dict()

for i in range(books.shape[0]):
    book_dict['title'] = books.loc[i]['Title']
    book_dict['author'] = books.loc[i]['Author']
    book_dict['pages'] = int(books.loc[i]['Pages'])
    book_dict['genre'] = books.loc[i]['Genre']
    chosen_books.append(book_dict)
    book_dict = dict()

# Собираем итоговый массив (распределение книг между пользователями)
n = 0
for i in range(len(chosen_books)):
    if n < len(users_list) - 1:
        users_list[n]['books'].append(chosen_books[i])
        n += 1
    else:
        users_list[n]['books'].append(chosen_books[i])
        n = 0

# Записываем итоговый результат в файл ,json
with open('result_1.json', 'w') as f:
    json.dump(users_list, f, default=str)

# Читаем записанный результат для проверки
with open('result_1.json', 'r') as res:
    result = json.load(res)
