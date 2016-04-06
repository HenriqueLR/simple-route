clean:
	@find . -name "*.pyc" | xargs rm -f

database:
	app/manage.py migrate
	app/manage.py syncdb

run: clean
	app/manage.py runserver 0.0.0.0:7000 --settings=conf.settings

install:
	pip install -r requirements.txt
