"""Clase 02"""

from pathlib import Path
import pandas as pd
import numpy as np
import inspect
from src.core.main import run_exercises_from_main


def is_float(f):
    try:
        float(f)
        return True
    except ValueError:
        return False


def ejercicio_1():
    """Ejercicio 1"""
    s = pd.Series(np.random.randn(10)).to_list()
    serie_1 = pd.Series([1, 2, 3, 4, 5])
    serie_2 = pd.Series([9, 8, 7, 6, 5])
    print(serie_1, serie_2)
    print(serie_1 + serie_2)
    print(serie_1 - serie_2)
    print(serie_1 * serie_2)
    print(serie_1 / serie_2)
    print(serie_1 == serie_2)

    data = pd.Series(["100", "200", "python", "300.15", "500.8"])
    data = pd.Series(map(float, filter(is_float, data)))

    print(data)

    return s


def ejercicio_2():
    students = {"Juan": 9, "María": 6.5, "Pedro": 4, "Carmen": 8.5, "Luis": 5}
    s = pd.Series(students)
    data = pd.Series(
        [s.min(), s.max(), s.mean(), s.std()], index=["min", "max", "avg", "std"]
    )
    approbed = s[s > 6].sort_values(ascending=False)
    return data, approbed


def ejercicio_3():
    ventas = {
        "Enero": 305000,
        "Febrero": 356000,
        "Marzo": 283000,
        "Abril": 339000,
        "Mayo": 139000,
        "Junio": 257000,
    }
    gastos = {
        "Enero": 220000,
        "Febrero": 234000,
        "Marzo": 181000,
        "Abril": 207000,
        "Mayo": 102000,
        "Junio": 203000,
    }
    data = pd.DataFrame({"Ventas": ventas, "Gastos": gastos})
    data.index.names = ["Mes"]
    print(data)
    s = pd.Series(data["Ventas"] - data["Gastos"])
    print(s)
    return data, s


def ejercicio_4():  # Bonus
    animals = pd.DataFrame(
        [[0, 1], [2, 3]], index=["cat", "dog"], columns=["weight", "height"]
    )
    print(animals)
    animals = animals.stack()
    print(animals)
    animals = animals.unstack(level=-1)
    print(animals)
    df = pd.DataFrame(
        {
            "foo": ["one", "one", "one", "two", "two", "two"],
            "bar": ["A", "B", "C", "A", "B", "C"],
            "baz": [1, 2, 3, 4, 5, 6],
            "zoo": ["x", "y", "z", "q", "w", "t"],
        }
    )
    print(df.pivot(index="foo", columns="bar", values="zoo"))

# A partir de aca, son los ejercicios del cuaderno 2.4

def ejercicio_5():
    headers = ['user_id', 'gender', 'age', 'ocupation', 'zip']
    users = pd.read_table('./src/clase_02/db/users.txt', engine='python', sep='::', header=None, names=headers)
    print(users)


def main():
    """Run all exercises"""
    module = inspect.currentframe()
    run_exercises_from_main(module)
