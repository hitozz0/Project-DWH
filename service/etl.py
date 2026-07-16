import pandas as pd
import sqlite3

def run_etl():
    fact_1()
    fact_2()
    fact_3()
    print("--- ETL SUCCESSFUL ---")

def fact_1():
    staging = './databases/data.db'
    warehouse = './databases/warehouse.db'

    try:
        conn_staging = sqlite3.connect(staging)
        df_staging = pd.read_sql("SELECT * FROM merged_data", conn_staging)
        conn_staging.close()

        total_penjualan_per_item = (
            df_staging.groupby(['nama_cabang', 'nama_obat'])['jumlah'].sum().reset_index(name='total_jumlah_terjual')
        )
        
        fact_product_terlaris =(
            total_penjualan_per_item
            .sort_values(by='total_jumlah_terjual', ascending=False)
            .drop_duplicates(subset=['nama_cabang'])
            .sort_values(by='nama_cabang')
            .reset_index(drop=True)
        )

        conn_warehouse = sqlite3.connect(warehouse)

        fact_product_terlaris.to_sql("fact_product_terlaris_per_cabang", conn_warehouse, if_exists="replace", index=False)

        conn_warehouse.close()
    except Exception as e:
        print(f"error : {e}")

def fact_2():
    staging = './databases/data.db'
    warehouse = './databases/warehouse.db'

    try:
        conn_staging = sqlite3.connect(staging)
        df_staging = pd.read_sql("SELECT * FROM merged_data", conn_staging)
        conn_staging.close()

        total_penjualan_per_kategori = (
            df_staging.groupby(['nama_cabang', 'kategori'])['jumlah'].sum().reset_index(name='total_jumlah_terjual')
        )
        
        fact_kategori_terlaris =(
            total_penjualan_per_kategori
            .sort_values(by='total_jumlah_terjual', ascending=False)
            .drop_duplicates(subset=['nama_cabang'])
            .sort_values(by='nama_cabang')
            .reset_index(drop=True)
        )

        conn_warehouse = sqlite3.connect(warehouse)

        fact_kategori_terlaris.to_sql("fact_kategori_terlaris_per_cabang", conn_warehouse, if_exists="replace", index=False)

        conn_warehouse.close()
    except Exception as e:
        print(f"error : {e}")

def fact_3():
    staging = './databases/data.db'
    warehouse = './databases/warehouse.db'

    try:
        conn_staging = sqlite3.connect(staging)
        df_staging = pd.read_sql("SELECT * FROM merged_data", conn_staging)
        conn_staging.close()

        total_penjualan_per_cabang = (
            df_staging.groupby(['nama_cabang'])['jumlah'].sum().reset_index(name='total_jumlah_terjual')
        )

        conn_warehouse = sqlite3.connect(warehouse)

        total_penjualan_per_cabang.to_sql("fact_total_penjualan_per_cabang", conn_warehouse, if_exists="replace", index=False)

        conn_warehouse.close()
    except Exception as e:
        print(f"error : {e}")