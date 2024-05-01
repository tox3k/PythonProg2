"""
Иногда бывает важно сгенерировать какие то табличные данные по заданным характеристикам.
К примеру, если вы будете работать тестировщиками, вам может потребоваться добавить
    в тестовую БД такой правдоподобный набор данных (покупки за сутки, набор товаров в магазине,
    распределение голосов в онлайн голосовании).

Давайте этим и займёмся!

Представим, что наша FrontEnd команда делает страницу сайта УЕФА с жеребьевкой команд
    по группам на чемпионате Европы.

Условия жеребьёвки такие:
Есть N групп.
В каждую группу попадает 1 "сильная" команда, 1 "слабая" команда и 2 "средние команды".

Задача: написать функцию generate_data, которая на вход принимает количество групп (от 4 до 16ти)
    и генерирует данные, которыми заполняет 2 таблицы:
        1. таблицу со списком команд (столбцы "номер команды", "Название", "страна", "сила команды")
        2. таблицу с результатами жеребьёвки (столбцы "номер команды", "номер группы")

Таблица с данными называется `uefa_commands` и `uefa_draw`
"""
import sqlite3
import math
from faker import Faker # Генератор случайных слов
from faker.providers import address

GROUP_TITLES = []
GROUP_COUNTRIES = []
GROUP_POWERS = ['сильная','средняя','средняя','слабая'] * 25
def generate_group_data():
    fake = Faker()
    fake.add_provider(address)
    for _ in range(100):
        GROUP_TITLES.append(fake.word().capitalize())
        GROUP_COUNTRIES.append(fake.country())



def generate_test_data(c: sqlite3.Cursor, number_of_groups: int) -> None:
    group_number = 1
    for i in range(number_of_groups * 4):
        group_number = math.ceil(float(i + 1) / 4)
        c.execute(f'INSERT INTO uefa_commands(command_number, command_name, command_country, command_level) VALUES(\'{i}\', \'{GROUP_TITLES[i]}\', \'{GROUP_COUNTRIES[i]}\', \'{GROUP_POWERS[i]}\')')
        c.execute(f'INSERT INTO uefa_draw(command_number, group_number) VALUES(\'{i}\', \'{group_number}\')')


#Иногда генереруются неадекватные названия, поэтому возможно придется перезаупститься

def main():
    with sqlite3.Connection('hw.db') as con:
        cur = con.cursor()
        generate_test_data(cur, 10)

if __name__ == '__main__':
    generate_group_data()
    main()