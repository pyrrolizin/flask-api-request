.PHONY: doc

help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "To generate documentation type make doc"
	@echo "------------------------------------"

setup:
	@( virtualenv venv; . ./venv/bin/activate ; pip install -r requirements.txt )


doc:
	@( . ./venv/bin/activate; cd src; pdoc --html --force -c show_source_code=False webapp -o ../doc )

test:
	@( . ./venv/bin/activate; cd src; python -m pytest tests -v )

run:
	@( . ./venv/bin/activate; cd src; python app.py )
