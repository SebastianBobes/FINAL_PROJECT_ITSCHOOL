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

def insert_member_into_db(member:Member, path: str = "config.json"):
    with open(path, "r") as f:
        config = json.loads(f.read())['config_db']
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql_query = ("INSERT into euroavia.members (last_name, first_name, middle_name,telephone_number,study_year,college,department_id,email_address)"
                         f"values('{member.last_name}','{member.first_name}','{member.middle_name}','{member.telephone_number}','{member.study_year}', '{member.college}',{member.department_id}, '{member.email}')")
            cursor.execute(sql_query)


def read_last_id(member: Member, path: str = "config.json"):
    with open(path, "r") as f:
        config = json.loads(f.read())['config_db']
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql_query = ("SELECT id from euroavia.members")
            cursor.execute(sql_query)
            list_of_members = []
            columns = [desc[0] for desc in cursor.description]
            for item in cursor.fetchall():
                list_of_members.append(dict(zip(columns, item)))
            return list_of_members[-1]['id']

def add_events_for_member(member:Member,events:list,  path: str = "config.json"):
    with open(path, "r") as f:
        config = json.loads(f.read())['config_db']
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            with open(path, 'r') as f:
                events_id = json.loads(f.read())['event_id']
                for event in events:
                    sql_query = (f"INSERT into euroavia.events_members(event_id, member_id) values({events_id[event]},{read_last_id(member)})")
                    cursor.execute(sql_query)





def unicity_checker(parameter, category: str, path:str = 'config.json'):
    with open(path, "r") as f:
        config = json.loads(f.read())['config_db']
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql_query = ("SELECT * from euroavia.members")
            cursor.execute(sql_query)
            list_of_members=[]
            columns = [desc[0] for desc in cursor.description]
            for item in cursor.fetchall():
                list_of_members.append(dict(zip(columns, item)))
            for member_info in list_of_members:
                if parameter in member_info[f'{category}']:
                    return True








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
    unicity_checker()



