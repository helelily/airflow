from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {"owner":"admin",
   "depends_on_past":False,
   "start_date":datetime(2015,6,1),
   "retries":1,
   "retry_delay":timedelta(minutes=5)}

schedule_interval = "@once"

dag = DAG("hello_world", default_args=default_args, schedule_interval=schedule_interval)

t1 = BashOperator(task_id="hello",
	          bash_command= "echo \"Hello World\"",
                  dag=dag)
