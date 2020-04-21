# horcrux
Django project for Organisational account management

### Usage help
  * To install the dependencies, run, the command below  
    ```
	pip install -r requirements.txt
	```
	
  * To migrate the models and create superuser  
    ```
	python manage.py first_run
	```

  * To run the server  
    ```
	python manage.py runserver  
	```

  * Then go to localhost:8000/ url in the browser

### Some Important files which should not be removed
	db.sqlite3  
	files in "migrations" folder  
	secret_key.py  
	All of these files will be created automatically when the first_run command is run. Do NOT delete them as it will lead to data loss.
