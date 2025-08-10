from typing import Callable


def log(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Ejecutado {func.__name__} con resultado: {result}")
        return result

    wrapper.__name__ = func.__name__

    return wrapper
