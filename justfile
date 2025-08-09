set shell := ['nu', '-c']

test args:
    uv run mate3/cli.py  test {{args}}

run args: 
    uv run mate3/cli.py run {{args}}

new args: 
    uv run mate3/cli.py new {{args}}