from airflow.decorators import task
from airflow import DAG


with DAG(
    dag_id="custom_sensor",
    start_date=datetime(2024, 1, 1),
    schedule=None,
) as dag: