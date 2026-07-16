import pandas as pd
import sqlite3

def show_analytic():
    warehouse = './databases/warehouse.db'
    conn = sqlite3.connect(warehouse)
    fact_1 = pd.read_sql("SELECT * FROM fact_product_terlaris_per_cabang", conn)
    fact_2 = pd.read_sql("SELECT * FROM fact_kategori_terlaris_per_cabang", conn)
    fact_3 = pd.read_sql("SELECT * FROM fact_total_penjualan_per_cabang", conn)

    print("")
    print("========== Analytic Data ==========")
    print("")
    print("========== Product terlaris per cabang ==========")
    print("")
    print(fact_1)
    print("")
    print("")
    print("========== kategori terlaris per cabang ==========")
    print("")
    print(fact_2)
    print("")
    print("")
    print("========== total penjualan per cabang ==========")
    print("")
    print(fact_3)
    print("")
    
    conn.close()