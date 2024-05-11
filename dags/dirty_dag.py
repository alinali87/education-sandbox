from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


with DAG(
    dag_id="dirty_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    task_1 = BashOperator(
        task_id="task_1",
        bash_command="echo 'LAEDE: Today is a wonderful day!'",
    )

    task_1

