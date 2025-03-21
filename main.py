from etl import ETL
from datetime import date
from fetch_player_ids import get_all_player_ids
import concurrent.futures
from functools import partial


def create_etl_object_and_run(player_id, db_file_path, db_table_name):
    player_etl = ETL(player_id, db_file_path, db_table_name)
    player_etl.run_etl()


if __name__ == "__main__":
    db_file_path = 'unrivaled_stats.db'
    db_table_name= f'unrivaled_stats_{date.today()}'
    ids = get_all_player_ids()[:100]
    partial_etl_function = partial(create_etl_object_and_run, db_file_path=db_file_path, db_table_name=db_table_name)
    with concurrent.futures.ThreadPoolExecutor(10) as executor:
        executor.map(partial_etl_function, ids)