build:
	docker build . -t cryptofield

pylint:
	docker run cryptofield pylint cryptofield

pytype:
	docker run cryptofield pytype cryptofield

test:
	docker run cryptofield python -m unittest discover -s tests

check: build pylint pytype test