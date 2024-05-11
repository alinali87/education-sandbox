from airflow import DAG
from datetime import datetime, timedelta
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="first_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    tags=["sensor"],
    catchup=False,
) as dag:
    
    wait_for_files = FileSensor.partial(
        task_id="wait_for_files",
        fs_conn_id="fs_default",
    ).expand(
        filepath=["data_1.csv", "data_2.csv", "data_2.csv"]
    )

    process_files = BashOperator( # TODO
        task_id="process_files",
        bash_command="echo 'Processed the files!'",
    )

    wait_for_files >> process_files
