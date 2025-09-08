from types import FrameType
from typing import Callable
from rich.console import Console
from pathlib import Path
import time
from functools import wraps

def cache_req(path: str, max_age: int = 3600):
    """
    Cachea peticiones
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            return _handle(path, max_age, func, *args, **kwargs)

        return wrapper

    if callable(path):
        func = path
        path = f"./cache/{func.__name__}"
        max_age = 3600
        return decorator(func)

    return decorator
def _handle(path: str, max_age: int, func: Callable, *args, **kwargs):
    file = Path(path)
    current_time = time.time()
    if file.exists():
        file_age = current_time - file.stat().st_mtime
        if file_age < max_age:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
    print("Getting new fresh data")
    data = func(*args, **kwargs)
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)
    return data

def log(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Ejecutado {func.__name__} con resultado: {result}")
        return result

    wrapper.__name__ = func.__name__

    return wrapper


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


def run_exercises_from_main(module: FrameType) -> None:
    console = Console()

    if module:
        module_globals = module.f_globals
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
