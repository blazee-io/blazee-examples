jupyter:
	env $(cat .env | xargs) pipenv run jupyter notebook .
