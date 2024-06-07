## Телефоны какого цвета чаще всего покупают?
```
SELECT phone_color, max(sold_count) FROM table_checkout
```
Берем строку с максимальным значением sold_count
### Ответ: Violet, 1120 шт

## Какие телефоны чаще покупают: красные или синие?
```
SELECT phone_color, max(sold_count) FROM table_checkout 
WHERE phone_color='Red' OR phone_color='Blue'
```
Берем большее из синих и красных по столбцу sold_count
### Ответ: Red, 64шт

## Какой самый непопулярный цвет телефона?
```
SELECT phone_color, min(sold_count) FROM table_checkout
```
Берем меньший из всех по столбцу sold_count
### Ответ: Goldenrod, 2шт