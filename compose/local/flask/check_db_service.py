"""Check if `palta-weather_db` service is ready"""

import os
import sys
from urllib import parse
import psycopg2

url = parse.urlparse(os.environ["DATABASE_URL"])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

try:
    psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
except psycopg2.OperationalError:  # noqa
    sys.exit(-1)

sys.exit(0)
