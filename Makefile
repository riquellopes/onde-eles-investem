.SILENT:
PIP=.venv/bin/pip
PYTEST=.venv/bin/pytest
PYTHON=.venv/bin/python
COVERALLS=.venv/bin/coveralls


venv:
	virtualenv .venv

setup:venv
	${PIP} install -U pip
	${PIP} install -r requirements_dev.txt

clean:
	find . -name "*.pyc" -exec rm -rf {} \;

coveralls:
	${COVERALLS}

crawl:
	@scrapy crawl candidatos

run:
	@streamlit run app.py