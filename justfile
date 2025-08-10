set shell := ['nu', '-c']

test args="":
    uv run src/cli.py  test {{args}}

run args: 
    uv run src/cli.py run {{args}}

new args: 
    uv run src/cli.py new {{args}}