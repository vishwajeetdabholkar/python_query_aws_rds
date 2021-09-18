import psycopg2
import pandas as pd
# code to query rds from python 
def rds_query_executor(query):
        ENDPOINT = "rds_endpoint"
        PORT = "5432"
        USR = "postgres"
        REGION = "aws_region"
        DBNAME = "rds_db_name"
        token = ""
        
        with psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password=token, ) as conn:
             with conn.cursor() as cur:
                 for query in queries_list:
                    query = ''' select * from db_name.table_name '''
             
                    cur.execute(query)
                    query_results = cur.fetchall()
                    colnames = [desc[0] for desc in cur.description]
                    df = pd.DataFrame(query_results, columns=colnames)
                    res.append(list(df.T.to_dict().values()))
