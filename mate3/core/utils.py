"""🛠️ Utilidades Core para Mate3 - Ultra Minimalista

Solo funciones esenciales para tests.
"""

import numpy as np

def assert_array_equal(a: np.ndarray, b: np.ndarray, message: str = "") -> None:
    """Verifica que dos arrays sean iguales."""
    try:
        np.testing.assert_array_equal(a, b)
        if message:
            print(f"✅ {message}")
    except AssertionError as e:
        if message:
            print(f"❌ {message}")
        print(f"Expected: {b}")
        print(f"Got: {a}")
        raise e
