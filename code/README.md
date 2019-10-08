## Make python virtual env
```bash
$ virtualen env
```

## Flask project create endpoint articles
run it use
```bash
$ source env/bin/activate
```
use library
```bash
$ pip3 install flask flask-sqlalchemy
$ pip3 install flask_script
$ pip3 install pymysql
$ pip3 install pyjwt
$ pip3 install requests
```
[Read More](https://pyjwt.readthedocs.io/en/latest/)

use rqworker
```bash
$ rq worker --url redis://root:@7.7.7.4:6379/
```

## This Project Use
* Python 3.6.8
* Flask 1.1.1
* Werkzeug 0.16.0