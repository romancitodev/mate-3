"""🧮 CLI Simple para Mate3"""

import subprocess
import sys
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console

app = typer.Typer(help="🧮 Mate3 - Simple CLI")
console = Console()


@app.command()
def test(clase: Optional[int] = None) -> None:
    """🧪 Run tests"""
    cmd = [sys.executable, "-m", "pytest", "-v"]

    if clase:
        cmd.append(f"tests/test_clase_{clase:02d}.py")

    subprocess.run(cmd)


@app.command()
def run(clase: int, ejercicio: Optional[int] = None) -> None:
    """🚀 Run a class"""
    module_name = f"src.clase_{clase:02d}.main"
    if ejercicio:
        cmd = [
            sys.executable,
            "-c",
            f"from {module_name} import ejercicio_{ejercicio}; from src.core.main import run_exercise; run_exercise(ejercicio_{ejercicio})",
        ]
    else:
        cmd = [sys.executable, "-c", f"from {module_name} import main; main()"]
    subprocess.run(cmd)


@app.command()
def new(numero: int) -> None:
    """📚 Create new class"""
    clase_dir = Path(f"src/clase_{numero:02d}")
    test_file = Path(f"tests/test_clase_{numero:02d}.py")

    # Create class directory
    clase_dir.mkdir(parents=True, exist_ok=True)

    # __init__.py
    init_content = f'"""Clase {numero:02d}"""\nfrom .main import *'
    (clase_dir / "__init__.py").write_text(init_content, encoding="utf-8")

    # main.py template
    main_template = f'''"""Clase {numero:02d}"""

import numpy as np
import inspect
from src.core.main import run_exercises_from_main

def ejercicio_1():
    """Ejercicio 1"""
    pass


def main():
    """Run all exercises"""
    module = inspect.currentframe()
    run_exercises_from_main(module)


if __name__ == "__main__":
    main()
'''
    (clase_dir / "main.py").write_text(main_template, encoding="utf-8")

    # test template
    test_template = f'''"""Tests for clase {numero:02d}"""

import pytest
from src.clase_{numero:02d} import *


def test_ejercicio_1():
    """Test ejercicio 1"""
    # Add your tests here
    assert True

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
'''
    test_file.write_text(test_template, encoding="utf-8")

    console.print(f"✅ Clase {numero:02d} created!", style="green")


if __name__ == "__main__":
    app()
