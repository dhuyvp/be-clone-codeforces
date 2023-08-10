import os
import logging
import psycopg2
from time import time, sleep
from urllib.parse import urlparse

check_timeout = os.getenv("CHECK_TIMEOUT", 30)
check_interval = os.getenv("CHECK_INTERVAL", 1)
interval_unit = "second" if check_interval == 1 else "seconds"
start_time = time()
logger = logging.getLogger()

def pg_isready():
    while time() - start_time < float(check_timeout):
        try:
            result = urlparse(os.getenv("DATABASE_URL"))
            username = result.username
            password = result.password
            database = result.path[1:]
            hostname = result.hostname
            port = result.port
            conn = psycopg2.connect(
                host=hostname,
                port=port,
                user=username,
                password=password,
                database=database)
            logger.info("Postgres is ready! ✨ 💅")
            try:
                cur = conn.cursor()
                cur.execute('SELECT 1')
            except psycopg2.OperationalError:
                pass
            conn.close()
            return True
        except psycopg2.OperationalError:
            logger.info(f"Postgres isn't ready 😫😫. Waiting for {check_interval} {interval_unit}...")
            sleep(check_interval)

        logger.error(f"We could not connect to Postgres within {check_timeout} seconds.😫😫")
        return False
