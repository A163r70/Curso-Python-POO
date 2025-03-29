"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 21 de marzo de 2025
Descripción:
- Kids drink toddy.
- Teens drink coke.
- Young adults drink beer.
- Adults drink whisky.
Make a function that receive age, and return what they drink.
Rules:

- Children under 14 old.
- Teens under 18 old.
- Young under 21 old.
- Adults have 21 or more.
"""
def people_with_age_drink(age)->str:
    """
    Función que calcula que bebida tomará dependiendo de la edad.
    :param age: La edad de la persona.
    :return: La bebida que puede tomar.
    """
    if age < 14:
        return "Drink toddy"
    elif age < 18:
        return "Drink coke"
    elif age < 21:
        return "Drink beer"
    elif age >= 21:
        return "Drink whisky"

if __name__ == '__main__':
    print(people_with_age_drink(13))
    print(people_with_age_drink(14))
    print(people_with_age_drink(15))
    print(people_with_age_drink(18))
    print(people_with_age_drink(21))
    print(people_with_age_drink(20))
    print(people_with_age_drink(0))
    print(people_with_age_drink(25))