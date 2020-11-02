build:
	docker build . -t cryptofield

pylint:
	docker run cryptofield pylint cryptofield

test:
	docker run cryptofield python -m unittest discover -s tests

check: build pylint test