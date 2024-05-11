from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="second_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["sensor"],
) as dag:
    
    runme = BashOperator(
        task_id="runme",
        bash_command="echo 'This is stupid RUNME task ((('",
    )

    runme
