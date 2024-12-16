
import random
users = [
    {
        'username': 'Пользователь',
        'password': 'qwerty',
        'role': 'user',
        'history': [],
        'created_at': '16-12-24'
    },
    {
        'username': 'Админ',
        'password': '777',
        'role': 'admin'
    },
]

books = [
    { 'title': 'Железное пламя', 'author': 'Ребекка Яррос', 'genre': 'Роман', 'rental': 50},
    {'title': 'Дракон не дремлет', 'author': 'Джон М. Форд', 'genre': 'Роман', 'rental': 50},
    {'title': 'Часодеи', 'author': 'Наталья Щерба', 'genre': 'Фэнтези', 'rental': 40},
    {'title': 'Тайна Чёрного дракона', 'author': 'Анна Джейн', 'genre': 'Роман', 'rental': 40},
    {'title': 'Твоё сердце будет разбито', 'author': 'Анна Джейн', 'genre': 'Роман', 'rental': 45},
    {'title': 'Мара и Морок', 'author': 'Лия Арден', 'genre': '"Фэнтези","Приключения"', 'rental': 75},
    {'title': 'Ни Сы', 'author': 'Джен Синсеро', 'genre': 'Психология', 'rental': 35},
    {'title': 'Из крови и пепла', 'author': 'Дженнифер Арментроут', 'genre': 'Приключения', 'rental': 70},
    {'title': 'Преступление и наказание', 'author': 'Фёдор Достоевский', 'genre': 'Роман', 'rental': 40},
    {'title': 'Приключения Шерлока Холмса', 'author': 'Конан Дойл', 'genre': 'Детектив', 'rental': 59},
    {'title': 'Тайный дневник Верити', 'author': 'Колин Гувер', 'genre': 'Триллер', 'rental': 25}
]

def filter_by_price(b, login):
    max_rental = input("Введите максимальную цену проката: ")
    while not max_rental.isdigit():
        max_rental = input("Ввести можно только числа! ")
    min_rental = input("Введите минимальную цену проката: ")
    while not min_rental.isdigit():
        min_rental = input("Ввести можно только числа! ")

    min_rental, max_rental = int(min_rental), int(max_rental)
    result = list(filter(lambda x: max_rental >= x['rental'] >= min_rental, b))
    for book in result:
        print(f'Название книги: {book["title"]}, Автор: {book["author"]}, Цена: {book["rental"]} рублей')
    menu_user(b, login)


def sort_books(b, login):
    order = input("Чтобы отсортировать по возрастанию цены за прокат, введите 'возр'. Или 'убыв', если по убыванию: ")
    while order not in ['возр', 'убыв']:
        order = input("Ввести можно только 'возр' или 'убыв': ")
    if order == 'возр':
        sorted_books = sorted(b, key=lambda x: x['rental'])
    else:
        sorted_books = sorted(b, key=lambda x: x['rental'], reverse=True)

    for book in sorted_books:
        print(f'Название книги: {book["title"]}, Автор: {book["author"]}, Цена за прокат: {book["rental"]} рублей')
    menu_user(b, login)


def menu_user(b, login):
    print('-----------------------------------------------------')
    print(
        'Выберите действие:\n1. Просмотреть каталог книг\n2. Найти книгу и взять\n3. Сортировать книги по цене\n4. Выйти'
        '\n5. Отфильтровать по цене\n6. Просмотр истории взятия книг\n7. Обновить профиль')
    print('-----------------------------------------------------')
    action = input()
    if action not in '1234567':
        while action not in '1234567':
            action = input('Такого действия нет! Попробуйте еще раз: ')
    match action:
        case '1':
            for book in b:
                print(f'Название книги: {book["title"]}, Автор: {book["author"]}, Цена: {book["rental"]} рублей')
            menu_user(b, login)
        case '4':
            start(b)
        case '5':
            filter_by_price(b, login)
        case '3':
            sort_books(b, login)
        case '6':
            for user in users:
                if user['username'] == login:
                    if not user['history']:
                        print('История взятия книг пуста')
                    else:
                        print("Вы брали книги: ", end='')
                        print(user['history'], sep=', ')
                    menu_user(b, login)
                    break
        case '2':
            book_title = input("Введите название книги: ")
            titles = [book['title'] for book in books]
            while book_title not in titles:
                book_title = input("Книги с таким названием не существует! ")
            days = input(f"На сколько дней вы хотите взять книгу '{book_title}' (от 1 до 10)? ")
            while not days.isdigit():
                print('Книга взята (⁠≧⁠▽⁠≦⁠) !')
                menu_user(b, login)
        case '3':
            title = input("Введите название книги для изменения статуса: ")
            for book in b:
                if book['title'] == title:
                    book['available'] = not book['available']
                    status = "доступна" if book['available'] else "недоступна"
                    print(f"Статус книги '{title}' изменен на '{status}'.")
                    break
        case '4':
            start(b)

def menu_admin(b):
    global books
    print('------------')
    print('Выберите действие:\n1. Добавление новой книги\n2. Изменение цену проката книги\n3. Удаление книги\n'
          '4. Создание нового читателя Выйти\n5. Выйти')
    print('-----------------------------------------------------')
    answer = input()
    if answer not in '12345':
        while answer not in '12345':
            answer = input('Такого действия нет! Попробуйте еще раз: ')
    match answer:
        case '1':
            new_book = input('Введите название новой книги: ')
            new_rental = input('Введите цену проката новой книги')
            while not new_rental.isdigit():
                new_rental = input('Ввести можно только циферки (⁠@⁠_⁠@⁠)! ')
            new_rental = int(new_rental)
            books.append({'title': new_book, 'rental': new_rental})
            print('Добавлена новая книга (⁠≧⁠▽⁠≦⁠)')
            menu_admin(b)
        case '2':
            book_title = input('Введите название книги: ')
            titles = []
            for i in book_title:
                book_title = input('Такой книги нет (⁠｡⁠ŏ⁠﹏⁠ŏ⁠) !')
            new_rental = input("Введите новую цену проката: ")
            while not new_rental.isdigit():
                new_rental = input("Ввести можно только циферки (⁠@⁠_⁠@⁠)")
            new_rental = int(new_rental)
            for t in range(len(books) - 1):
                if book_title in books[t]['title']:
                    books[t]['price'] = new_rental
                    print('Цена изменена')
            menu_admin(b)
        case '3':
            book_title = input('Введите название книги, которую надо удалить: ')
            titles = []
            for i in book_title:
                book_title = input('Такой книги нет (⁠｡⁠ŏ⁠﹏⁠ŏ⁠) !')
            for j in range(len(books) - 1):
                if books in books[j]['title']:
                    del books[j]
                    print('Тип номера удален!')
            menu_admin(b)
        case '4':
            new_user = input('Введите логие нового читателя: ')
            new_passw = input('Введите пароль:')
            users.append({new_user = '',  })
        case '5':
            start(b)




def start(b):
    print('Добро пожаловать на сайт библиотеки! \nПожалуйста, авторизуйтесь. Чтобы выйти - напишите "Библиотека" в логине')
    login = input("Введите логин: ")
    if login == 'Библиотека':
        print('До новых встреч!')
        return
    password = input("Введите пароль: ")
    for i in users:
        if i['username'] == login:
            if i['password'] == password:
                if i['role'] == 'admin':
                    menu_admin(b)
                    break
                else:
                    menu_user(b, login)
                    break
    print('Неверно введен пароль или логин!')
    start(b)

start(books)