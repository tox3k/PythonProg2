<h2>Забыли импортировать модуль datetime</h2>
````Python
import datetime 
````


````Python
class Person:
    def __init__(self, name: str, year_of_birth: int, address: str = '') -> None:
        self.name: str = name
        self.yob: int = year_of_birth
        self.address: str = address

    def get_age(self) -> int:
        now: datetime.datetime = datetime.datetime.now()
````

<h2>Перепутали местами текущий год и год рождения</h2>
````Python
#return self.yob - now.year
return now.year - self.yob 
````

````Python
def get_name(self) -> str:
    return self.name
````

<h2>Вместо присвоения аргумента функции, присвоили свойство само себе</h2>
````Python
def set_name(self, name: str) -> None:
    #self.name = self.name 
    self.name = name
````

<h2>Использовали оператор сравнения вместо оператора присвоения</h2>
````Python
def set_address(self, address: str) -> None:
    #self.address == address 
    self.address = address 
````

````Python
def get_address(self) -> str:
    return self.address
````

<h2>Вместа проверки свойства объекта проверяли несуществующую переменную</h2>
````Python
def is_homeless(self) -> bool:
    '''
    returns True if address is not set, false in other case
    '''
    #return address is None
    return self.address is None 
````
