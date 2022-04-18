start:
	uvicorn main:app --reload

pytest:
	pytest

diff:
	yapf -r . --diff

format:
	yapf -r . --in-place
