"""
Вы работаете программистом в IT отделе ГИБДД.
    Ваш отдел отвечает за обслуживание камер,
    которые фиксируют превышения скорости и выписывают автоматические штрафы.
За последний месяц к вам пришло больше тысячи жалоб на ошибочно назначенные штрафы,
    из которых около 100 были признаны и правда ошибочными.

Список из дат и номеров автомобилей ошибочных штрафов прилагается к заданию,
    пожалуйста удалите записи об этих штрафах из таблицы `table_fees`
"""
import sqlite3
import pandas as pd

def delete_wrong_fees(c: sqlite3.Cursor, wrong_fees_file: str) -> None:
    data = pd.read_csv(wrong_fees_file)
    truck_numbers = list(data['car_number'].array)
    timestamps = list(data['timestamp'].array)
    wrong_fee_pairs = zip(truck_numbers, timestamps)

    for truck_number, timestamp in wrong_fee_pairs:
        c.execute(f'DELETE FROM table_fees WHERE timestamp=\'{timestamp}\' AND truck_number=\'{truck_number}\'')


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        delete_wrong_fees(cursor, "wrong_fees.csv")

