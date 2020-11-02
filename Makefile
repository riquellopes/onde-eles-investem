.SILENT:
PIP=.venv/bin/pip
PYTEST=.venv/bin/pytest
PYTHON=.venv/bin/python
COVERALLS=.venv/bin/coveralls
SCRAPY=.venv/bin/scrapy
STREAMLIT=.venv/bin/streamlit


venv:
	virtualenv .venv --python=python3

setup:venv
	${PIP} install -r requirements_dev.txt

clean:
	find . -name "*.pyc" -exec rm -rf {} \;

coveralls:
	${COVERALLS}

crawl:
	@docker-compose run --rm scrapper scrapy crawl candidatos

run:
	${STREAMLIT} run app.py
up:
	@docker-compose up -d