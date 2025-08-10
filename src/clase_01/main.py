"""📚 Clase 01 - Introducción a NumPy

Este módulo contiene los ejercicios básicos de NumPy.
"""

from typing import Callable
import numpy as np
import inspect
from rich.console import Console


def ejercicio_1() -> np.ndarray:
    """🎯 Ejercicio 1: Crear matriz básica"""

    resultado = np.array([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=np.int8)
    print(
        f"{resultado.shape} - {resultado.size} - {resultado.size * resultado.itemsize} bytes"
    )
    return resultado


def ejercicio_2() -> np.ndarray:
    """🎯 Ejercicio 2: Usar arange y reshape"""
    resultado = np.arange(100, 200, 10).reshape(5, 2)
    return resultado


def ejercicio_3() -> np.ndarray:
    """🎯 Ejercicio 3: Obtener la 3er columna de cada matriz"""
    matriz = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]], dtype=np.int8)
    print(f"3er columna de la matriz:\n{matriz[:, 2]}")
    return matriz[:, 2]


def ejercicio_4() -> np.ndarray:
    """🎯 Ejercicio 4: Crear matriz llena de un valor específico"""
    resultado = np.full((5,), fill_value=10)
    return resultado


def ejercicio_5() -> float:
    """🎯 Ejercicio 5: Generar un número aleatorio"""
    resultado = np.random.uniform()
    return resultado


def ejercicio_6() -> np.ndarray:
    """🎯 Ejercicio 6: Crear matriz con numeros pares"""
    resultado = np.arange(10, 51, 2)
    return resultado


def ejercicio_7() -> np.ndarray:
    """🎯 Ejercicio 7: Crear matriz con números aleatorios con dist normal"""
    resultado = np.random.randn(25)
    return resultado


def ejercicio_8() -> np.ndarray:
    """🎯 Ejercicio 8: Reshape de matriz aleatoria"""
    resultado = ejercicio_7()
    resultado = resultado.reshape(5, 5)
    return resultado


def ejercicio_9() -> np.ndarray:
    """🎯 Ejercicio 9: ..."""
    m = np.array(
        [
            [3, 6, 9, 12],
            [15, 18, 21, 24],
            [27, 30, 33, 36],
            [39, 42, 45, 48],
            [51, 54, 57, 60],
        ]
    )

    resultado = m[::2, 1::2]
    return resultado


def ejercicio_10() -> tuple[np.ndarray, np.ndarray]:
    """🎯 Ejercicio 10: ..."""
    left = np.array([[5, 6, 9], [21, 18, 27]])
    right = np.array([[15, 33, 24], [4, 7, 1]])
    total_sum = left + right
    print(total_sum)
    total_power = total_sum**2
    print(total_power)
    return total_sum, total_power


def ejercicio_11() -> list[np.ndarray]:
    """🎯 Ejercicio 11: ..."""
    matrix = np.arange(10, 34, 1).reshape(8, 3)
    print(matrix)
    matrix = np.split(matrix, 4)
    return matrix


def ejercicio_12() -> tuple[np.ndarray, np.ndarray]:
    """🎯 Ejercicio 12: ..."""
    mp = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
    max_y_axis = np.min(mp, axis=1)
    max_x_axis = np.max(mp, axis=0)
    print("Impresion del eje 1:")
    print(max_y_axis)
    print("Impresion del eje 0:")
    print(max_x_axis)
    return max_y_axis, max_x_axis


def main() -> None:
    """🚀 Función principal de la clase 01"""

    console = Console()

    current_module = inspect.currentframe()
    if current_module:
        module_globals = current_module.f_globals
        ejercicios = [
            func
            for name, func in module_globals.items()
            if name.startswith("ejercicio_") and callable(func)
        ]

        def extract_number(func):
            name = func.__name__
            return int(name.split("_")[1])

        ejercicios.sort(key=extract_number)

        for ejercicio in ejercicios:
            console.print("\n" + "=" * 40)
            run_exercise(ejercicio)

    console.print("\n" + "=" * 40)
    console.log("✅ ¡Todos los ejercicios completados!")


def run_exercise(exercise: Callable):
    console = Console()

    console.print(f"🚀 Ejecutando {exercise.__name__} ...", style="bold green")
    console.print(exercise.__doc__, style="dim")
    console.print("-" * 40)
    console.print("Logs de la función:", style="dim")
    result = exercise()
    console.print("-" * 40)
    console.print(f"📊 Resultado de {exercise.__name__}", style="blue")
    console.print(f"{result = }")


if __name__ == "__main__":
    main()
