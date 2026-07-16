import pandas as pd
import glob
import sqlite3

def merge_data():
    db_file = './databases/data.db'
    table = 'merged_data'
    data_file = glob.glob('./datasets/*.csv')

    conn = sqlite3.connect(db_file)

    for file in data_file:
        df = pd.read_csv(file)
        try:
            df = df.dropna(subset=['total_bayar'])
            df['harga_satuan'] = (
                df['harga_satuan']
                .astype(str)
                .str.replace(r'[Rrp\.\s,]', '', regex=True)
            )
            df['total_bayar'] = (
                df['total_bayar']
                .astype(str)
                .str.replace(r'[Rrp\.\s,]', '', regex=True)
            )

            df['harga_satuan'] = df['harga_satuan'].replace(['nan', ''], '0')

            df['harga_satuan'] = df['harga_satuan'].astype(int)
            df['total_bayar'] = df['total_bayar'].astype(int)

            df.to_sql(table, conn, if_exists="replace", index=False)
            print(f"Successfully appended {file} to {table}")
        except Exception as e:
            print(f"error : {e}")

    conn.close()
    print("Merging complete!")
