import time
import logging
from datetime import datetime, timedelta

dag_timeout = 60 

# Logging Configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("dag_timeout")

def log_alert(text):
    logger.warning(text)

def check_dag_run_duration(execution_date):
    now = time.time()

    if (now - execution_date.timestamp()) > timedelta(hours=1).total_seconds():
        log_alert(f"DAG Runtime Alert - SMS")
    else:
        log_alert(f"Succuss: DAG Run within accepable timeframe")

def main():
    # Simulates a DAG
    execution_date = datetime.now() - timedelta(hours=0.5) ## set execution_date to datetime of run start
    check_dag_run_duration(execution_date)

main()


# current_time = datetime.now().strftime('%H:%M:%S')
# print(current_time)