"""Clase 04"""

from io import StringIO
import re
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

import inspect
from src.core.main import run_exercises_from_main, cache_req

URL = "https://www.worldometers.info/world-population/population-by-country/"


@cache_req("./cache/worldometers.html")
def get(url: str) -> str:
    req = requests.get(URL)
    return req.text


def ejercicio_1():
    text = get(URL)
    html = BeautifulSoup(text, features="lxml")
    data = html.find_all("table")[0]
    pop = pd.read_html(StringIO(str(data)))[0]
    _exported_csv = pop.to_csv("./src/clase_04/pop.csv", index=None, header=True)


# A partir de aca, vienen todos lo ejercicios de regex
def ejercicio_2():
    data = "bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot"
    return re.findfall("b[ao]t", data)


def ejercicio_3():
    data = """Maria tiene 5 años, y su hermana Valeria tiene 2.
Rita y Pedro, sus primos, tienen 3."""
    return re.findall(r"[A-Z]\w+", data)


def ejercicio_4():
    data = """Office of Research Administration: (734) 647-6333 | 4325 North Quad
Office of Budget and Financial Administration: (734) 647-8044 | 309 Maynard, Suite 205
Health Informatics Program: (734) 763-2285 | 333 Maynard, Suite 500
Office of the Dean: (734) 647-3576 | 4322 North Quad
UMSI Engagement Center: (734) 763-1251 | 777 North University
Faculty Adminstrative Support Staff: (734) 764-9376 | 4322 North Quad"""
    return re.findall(r'\(\d{3}\) \d{3}-\d{4}', data)

def main():
    """Run all exercises"""
    module = inspect.currentframe()
    run_exercises_from_main(module)


if __name__ == "__main__":
    main()
