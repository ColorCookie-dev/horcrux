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

  * To run the server (The site supports only ssl, so setup the project run the server accordingly)  
    ```
	python manage.py runserver  
	```

  * Now the server should be running visit the site from a browser  
  * Don't forget to append the name of the website in the horcrux/settings.py file in the variable ```ALLOWED_HOSTS```

#### Running the developmental sslserver for django
  * To install the dependencies,  
    ```
	pip install -r dev-requirements.txt
	```

  * To migrate the models and create superuser  
    ```
	python manage.py first_run
	```
  
  * Some necessary setup
    * Open the settings.py located under horcrux folder
	* Change the value of ```test_ssl_serv``` from ```False``` to ```True```

  * Run the experimental ssl server  
    ```
	python manage.py runsslserver
	```
  
  * Go to the site with a modern browser, and don't forget to add the name of the site to the list variable ```ALLOWED_HOSTS``` in the settings.py file. (```localhost``` and ```127.0.0.1``` is already present)

### Some Important files which should not be removed
	db.sqlite3  
	files in "migrations" folder  
	secret_key.py  
	All of these files will be created automatically when the ```first_run``` command is run. Do NOT delete them as it will lead to data loss.
