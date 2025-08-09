"""🧪 Tests para la Clase 01

Tests unitarios para verificar la implementación de los ejercicios.
Para agregar nuevos tests, simplemente añade métodos test_* a la clase TestClase01
o crea funciones test_* fuera de la clase.
"""

import pytest
import numpy as np
from mate3.clases.clase_01 import *


class TestClase01:
    """Tests para la clase 01"""

    def test_ejercicio_1(self):
        """Test para ejercicio 1: Crear matriz básica"""
        resultado = ejercicio_1()
        esperado = np.array([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=np.int8)
        np.testing.assert_array_equal(resultado, esperado)
        assert resultado.dtype == np.int8

    def test_ejercicio_2(self):
        """Test para ejercicio 2: Usar arange y reshape"""
        resultado = ejercicio_2()
        esperado = np.arange(100, 200, 10).reshape(5, 2)
        np.testing.assert_array_equal(resultado, esperado)
        assert resultado.shape == (5, 2)

    def test_ejercicio_3(self):
        """Test para ejercicio 3: Iterar e imprimir columnas (sin retorno)"""
        resultado = ejercicio_3()
        esperado = np.array([33, 66, 99], dtype=np.int8)
        np.testing.assert_array_equal(resultado, esperado)

    def test_ejercicio_4(self):
        """Test para ejercicio 4: Crear matriz llena de un valor específico"""
        resultado = ejercicio_4()
        esperado = np.full((5,), fill_value=10)
        np.testing.assert_array_equal(resultado, esperado)
        assert resultado.shape == (5,)
        assert all(resultado == 10)

    def test_ejercicio_5(self):
        """Test para ejercicio 5: Generar un número aleatorio"""
        resultado = ejercicio_5()
        assert isinstance(resultado, float)
        assert 0.0 <= resultado <= 1.0

    def test_ejercicio_6(self):
        """Test para ejercicio 6: Crear matriz con números pares"""
        resultado = ejercicio_6()
        esperado = np.arange(10, 51, 2)
        np.testing.assert_array_equal(resultado, esperado)
        # Verificar que todos son pares
        assert all(num % 2 == 0 for num in resultado)
        # Verificar rango correcto
        assert resultado[0] == 10
        assert resultado[-1] == 50

    def test_ejercicio_7(self):
        """Test para ejercicio 7: Crear matriz con números aleatorios con dist normal"""
        resultado = ejercicio_7()
        assert isinstance(resultado, np.ndarray)
        assert resultado.shape == (25,)
        assert resultado.dtype == np.float64

    def test_ejercicio_8(self):
        """Test para ejercicio 8: Reshape de matriz aleatoria"""
        # Configurar seed para reproducibilidad en el test
        np.random.seed(42)
        resultado = ejercicio_8()
        assert isinstance(resultado, np.ndarray)
        assert resultado.shape == (5, 5)
        assert resultado.dtype == np.float64

    def test_ejercicio_9(self):
        """Test para ejercicio 9: ..."""
        resultado = ejercicio_9()
        esperado = np.array([[6, 12], [30, 36], [54, 60]], dtype=np.int8)
        np.testing.assert_array_equal(resultado, esperado)

    def test_ejercicio_10(self):
        """Test para ejercicio 10: ..."""
        suma, potencia = ejercicio_10()
        np.testing.assert_array_equal(suma, np.array([[20, 39, 33], [25, 25, 28]]))
        np.testing.assert_array_equal(
            potencia, np.array([[400, 1521, 1089], [625, 625, 784]])
        )

    def test_ejercicio_11(self):
        """Test para ejercicio 11: ..."""
        matrix = ejercicio_11()
        expected = [
            np.array([[10, 11, 12], [13, 14, 15]]),
            np.array([[16, 17, 18], [19, 20, 21]]),
            np.array([[22, 23, 24], [25, 26, 27]]),
            np.array([[28, 29, 30], [31, 32, 33]]),
        ]
        np.testing.assert_array_equal(matrix, expected)

    def test_ejercicio_12(self):
        y, x = ejercicio_12()
        y_expected = [34, 12, 53]
        x_expected = [82, 94, 73]
        np.testing.assert_array_equal(y, y_expected)
        np.testing.assert_array_equal(x, x_expected)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
