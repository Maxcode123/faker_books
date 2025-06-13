format:
	ruff format

test:
	uv run python -m unittest -v src/faker_books/tests/test_provider.py

build:
	uv build

publish:
	uv publish

clean:
	rm -rf dist/ src/faker_books.egg-info
