import json
import psycopg2 as ps
from psycopg2._psycopg import cursor

from Members import Member

#membru din lb sa faca insert, update, select
#head poate sa faca select la orice dep
#dar doar la dep lui poate sa faca insert, update
#doar supervizorul departamentului poate face delete

#sa vezi cati s au inscris la un eveniment----
#sa vezi cati oameni sunt la un anumit departament----
#sa vezi la ce evenimente a participat un anumit membru----
#sa dai un an de la 1 la 4 sa vezi cati membrii sunt de la anul citit de la tast---


#sa stergi un eveniment la care un membru nu mai vine
#sa adaugi un eveniment la care un membru sa vina


#sa stergi un membru - doar supervizorul departamentului

def read_config(path: str = 'config.json'):
    try:
        with open(path, 'r') as f:
            config = json.loads(f.read())['config_db']
            return config
    except Exception as e:
        print(f"Error on reading config file! {e}")


def execute_query(sql_query: str, config: dict):
    try:
        with ps.connect(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql_query)
                return cursor
    except Exception as e:
        print(f"Failure on reading from database. Error: {e}")
        return False

def insert_member_into_db(member: Member) -> bool:
    config = read_config()
    sql_query = ("INSERT into euroavia.members (last_name, first_name, middle_name,telephone_number,study_year,college,department_id,email_address)"
                f"values('{member.last_name}','{member.first_name}','{member.middle_name}','{member.telephone_number}','{member.study_year}', '{member.college}',{member.department_id}, '{member.email}')")
    try:
        execute_query(sql_query,config)
    except Exception as e:
        print(f"Error on inserting member into DB! {e}")
        return False
    else:
        return True



def read_last_id() -> int:
    config = read_config()
    sql_query = ("SELECT id from euroavia.members")
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_query)
            list_of_members = []
            columns = [desc[0] for desc in cursor.description]
            for item in cursor.fetchall():
                list_of_members.append(dict(zip(columns, item)))
            return list_of_members[-1]['id']

def add_events_for_member(member:Member, events:list,  path: str = "config.json") -> bool:
    config = read_config()
    try:
        with ps.connect(**config) as conn:
            with conn.cursor() as cursor:
                with open(path, 'r') as f:
                    events_id = json.loads(f.read())['event_id']
                    for event in events:
                        sql_query = (f"INSERT into euroavia.events_members(event_id, member_id) values({events_id[event]},{read_last_id()})")
                        cursor.execute(sql_query)
    except Exception as e:
        print(f"Error on adding events in DB! {e}")
        return False
    else:
        return True


def unicity_checker(parameter: str, category: str) ->bool:
    config = read_config()
    try:
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
                    else:
                        return False
    except Exception as e:
        print(f"Something went wrong with checking unicity! {e}")
        return False




#cati s au inscris la un eveniment anume
def see_how_many_at_a_event():
    config = read_config()
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql_query = ("select event_id, name from euroavia.events ")
            cursor.execute(sql_query)
            x = cursor.fetchall()
            my_dict = {}
            for event in x:
                my_dict[event[0]] = event[1]
                print(f"{event[0]}.{event[1]}")

            event_id = input('Dati un id:')
            while event_id.isdigit() == False or int(event_id) not in list(my_dict.keys()):
                event_id = input(f'Numar invalid ! Reintroduceti id-ul:')
            sql_query = (f"select count(member_id) from euroavia.events_members where event_id ={int(event_id)}")
            cursor.execute(sql_query)
            number_of_members = cursor.fetchall()[0][0]
            print(f"La {my_dict[int(event_id)]} s-au inscris {number_of_members} euroavieni!")

def see_how_many_at_a_department():
    config = read_config()
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql_query = ("select department_id, name from euroavia.departments ")
            cursor.execute(sql_query)
            x = cursor.fetchall()
            my_dict = {}
            for dep in x:
                my_dict[dep[0]] = dep[1]
                print(f"{dep[0]}.{dep[1]}")

            dep_id = input('Dati un id:')
            while dep_id.isdigit() == False or int(dep_id) not in list(my_dict.keys()):
                dep_id = input(f'Numar invalid ! Reintroduceti id-ul:')
            sql_query = (f"select count(department_id) from euroavia.members where department_id ={int(dep_id)}")
            cursor.execute(sql_query)
            number_of_members = cursor.fetchall()[0][0]
            print(f"In departamentul {my_dict[int(dep_id)]} sunt {number_of_members} euroavieni!")

def see_events_for_member(path = 'config.json'):
    config = read_config()
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql_query = ("select id, last_name, first_name from euroavia.members ")
            cursor.execute(sql_query)
            x = cursor.fetchall()
            my_dict = {}
            for dep in x:
                my_dict[dep[0]] = dep[1],dep[2]
                print(f"{dep[0]}.{dep[1]} {dep[2]}")
            member_id  = input('Dati un id:')
            while member_id.isdigit() == False or int(member_id) not in list(my_dict.keys()):
                member_id = input(f'Numar invalid ! Reintroduceti id-ul:')
            sql_query = (f"select event_id from euroavia.events_members where member_id ={int(member_id)}")
            cursor.execute(sql_query)
            events = cursor.fetchall()
            try:
                with open(path, 'r') as f:
                    event_ids = json.loads(f.read())['event_id']
            except Exception as e:
                print(f"Failed reading event_ids from file! {e}")
            event_ids_swap = {v: k for k, v in event_ids.items()}
            print(f"\n{dep[1]} {dep[2]} a participat la: " )
            for item in events:
                    print(f"\t\t\t-{event_ids_swap[item[0]]}")

def see_how_many_from_a_study_year(path: str = "config.json"):
    config = read_config()
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            with open(path, 'r') as f:
                study_years = json.loads(f.read())['study_years']
            study_year = input("Introduceti un an de la 1 la 4: ")
            while study_year.isdigit() == False or study_year not in study_years.keys():
                study_year = input("An inexistent! Introduceti un an de la 1 la 4: ")

            sql_query = (f"select id, last_name, first_name from euroavia.members where study_year = '{study_years[study_year]}' ")
            cursor.execute(sql_query)
            members = cursor.fetchall()
            print(f"\nStudentii care sunt in anul {study_years[study_year]}:  ")
            for member in members:
                print(f"\t{member[0]}. {member[1]} {member[2]}")








if __name__ == '__main__':
    # see_how_many_at_a_event()
    # see_how_many_at_a_department()
    #see_events_for_member()
    see_how_many_from_a_study_year()





