# **Test graphene project**

##### To run project, please do the following:
* Run `pip3 install -r requirements.txt`
* In base directory create .env.py file and setup *SECRET_KEY* variable using the following with command line:
```
from django.core.management.utils import get_random_secret_key  
    
get_random_secret_key()
```
* Run `python3 manage.py migrate`
* Run `python3 manage.py loaddata business.json`
* Run `python3 manage.py runserver`
* Open server and visit `/business/` endpoint

##### To run tests, just execute 'tests.py' in business_app directory
