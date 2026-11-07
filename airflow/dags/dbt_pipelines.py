from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    "dbt_household_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    dbt_staging = BashOperator(
        task_id="dbt_staging",
        bash_command="""
        cd /opt/dbt &&
        dbt run --select staging --no-partial-parse
        """
    )

    dbt_marts = BashOperator(
        task_id="dbt_marts",
        bash_command="""
        cd /opt/dbt &&
        dbt run --select marts --no-partial-parse
        """
    )

    dbt_tests = BashOperator(
        task_id="dbt_tests",
        bash_command="""
        cd /opt/dbt &&
        dbt test
        """
    )

    dbt_staging >> dbt_marts >> dbt_tests
