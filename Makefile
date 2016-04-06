all: test

clean:
	@find . -name "*.pyc" | xargs rm -f

database:
	app/manage.py migrate
	app/manage.py syncdb

migrate:
	app/manage.py makemigrations
	app/manage.py migrate

run: clean
	app/manage.py runserver 0.0.0.0:7000 --settings=conf.settings

install:
	pip install -r requirements.txt

test: clean
	./runtests	
