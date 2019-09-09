# Currency Rates

App to calculate currencies exchange rates.<br>
Data fetched from European Central Bank.<br>

### Get the app running
Python 3.6.3<br>
Set up virtualenv and install packages with:<br>
pip install -r requirements.txt<br>
Migrate and run:<br>
python manage.py migrate<br>
python manage.py runserver<br>
To run test enter the command:<br>
pytest<br>
<br>
Local API usage:<br>
http://127.0.0.1:8000/api/currencies/exchange/?currency1=USD&currency2=PLN&amount=100<br>
You can use post /api/report/scrap to scrap page and create CurrencyRate objects.<br>
It takes some time to scrap pages.<br>
It can be updated with celery tasks to scrap page asynchronously after post request.<br>

### Deplyment
Create your .env file in currencies module directory and enter SECRET_KEY, set DEBUG to False, anything more you want to override.<br>
Run:<br>
export PRODUCTION=True<br>
python manage.py runserver

### Preview
CurrencyRate objects have unique date and currency, based on received from ECB data (daily rates).<br>
Tests are placed in tests directory with all the tests configuration files.<br>
I found that sometimes is better to have all the pytest fixtures and apps tests in other directory than app directories, so I tried this setup and it seems clear.
