import json
import psycopg2 as ps
from Members import Member


def execute_query(sql_query: str, config: dict):
    try:
        with ps.connect(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql_query)
                return cursor.statusmessage
    except Exception as e:
        print(f"Failure on reading from database. Error: {e}")
        return False

def insert_into_db(member:Member,path: str = "config.json"):
    with open(path, "r") as f:
        config = json.loads(f.read())['config_db']
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql_query = ("INSERT into euroavia.members (last_name, first_name, middle_name,telephone_number,study_year,college,department_id,email_address)"
                         f"values('{member.last_name}','{member.first_name}','{member.middle_name}','{member.telephone_number}','{member.study_year}', '{member.college}',{member.department_id}, '{member.email}')")
            cursor.execute(sql_query)



# def read_from_database(sql_query: str,config: dict):
#     try:
#         with ps.connect(**config) as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute(sql_query)
#                 response = cursor.fetchall()
#                 columns = [item.name for item in cursor.description]
#                 new_data = []
#                 for employee in response:
#                     new_data.append(dict(zip(columns, employee)))
#                 return new_data
#     except Exception as e:
#         print(f"Failure on reading from database. Error: {e}")


if __name__ == '__main__':
    pass



