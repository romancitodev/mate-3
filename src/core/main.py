import inspect
from types import FrameType
from typing import Callable
from rich.console import Console


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
