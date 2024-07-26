import json
import psycopg2 as ps
from psycopg2._psycopg import cursor

from Members import Member

def read_config(path: str = 'config.json'):
    try:
        with open(path, 'r') as f:
            config = json.loads(f.read())['config_db']
            return config
    except Exception as e:
        print(f"Error on reading config file! {e}")

def read_faculties(path: str = 'config.json'):
    try:
        with open(path, 'r') as f:
            faculties = json.loads(f.read())['faculties']
            return faculties
    except Exception as e:
        print(f"Error on reading from current file! {e}")



def execute_query(sql_query: str, config: dict, show: bool = True):
    try:
        with ps.connect(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql_query)
                if show:
                    return cursor.fetchall()
                else:
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


def show_dict_stylish(initial_dict: list, len_of_item: int = 2, printed: bool = True) -> dict:
    second_dict = {}
    if len_of_item == 2:
        for item in initial_dict:
            second_dict[item[len_of_item-2]] = item[len_of_item-1]
            if printed:
                print(f"{item[len_of_item-2]}.{item[len_of_item-1]}")
            else:
                pass
        return second_dict
    elif len_of_item == 3:
        for item in initial_dict:
            second_dict[item[0]] = item[len_of_item-1], item[len_of_item-2]
            if printed:
                print(f"{item[len_of_item-3]}.{item[len_of_item-2]} {item[len_of_item-1]}")
            else:
                pass
        return second_dict


def see_how_many_at_a_event():
    config = read_config()
    sql_query = ("select event_id, name from euroavia.events ")
    x = execute_query(sql_query,config)
    events_dict = show_dict_stylish(x)
    event_id = input('Dati un id:')
    while event_id.isdigit() == False or int(event_id) not in list(events_dict.keys()):
        event_id = input(f'Numar invalid ! Reintroduceti id-ul:')

    sql_query = (f"select count(member_id) from euroavia.events_members where event_id ={int(event_id)}")

    number_of_members = execute_query(sql_query,config)[0][0]
    print(f"La {events_dict[int(event_id)]} s-au inscris {number_of_members} euroavieni!")


def see_how_many_at_a_department():
    config = read_config()
    sql_query = ("select department_id, name from euroavia.departments ")
    x = execute_query(sql_query,config)
    deps_dict = show_dict_stylish(x)

    dep_id = input('Dati un id:')
    while dep_id.isdigit() == False or int(dep_id) not in list(deps_dict.keys()):
        dep_id = input(f'Numar invalid ! Reintroduceti id-ul:')

    sql_query = (f"select count(department_id) from euroavia.members where department_id ={int(dep_id)}")
    number_of_members = execute_query(sql_query,config)[0][0]
    print(f"In departamentul {deps_dict[int(dep_id)]} sunt {number_of_members} euroavieni!")


def see_events_for_member(path = 'config.json'):
    config = read_config()
    sql_query = ("select id, last_name, first_name from euroavia.members ")
    x = execute_query(sql_query,config)
    members_dict = show_dict_stylish(x ,len_of_item=3)

    member_id = input('Dati un id:')
    while member_id.isdigit() == False or int(member_id) not in list(members_dict.keys()):
        member_id = input(f'Numar invalid ! Reintroduceti id-ul:')

    sql_query = (f"select event_id from euroavia.events_members where member_id ={int(member_id)}")
    events = execute_query(sql_query,config)

    sql_query = (f"select event_id, name from euroavia.events ")
    y = execute_query(sql_query, config)
    events_dict = show_dict_stylish(y, printed=False)

    print(f"\n{members_dict[int(member_id)][0]} {members_dict[int(member_id)][1]} va participa la: ")
    id_and_events = {}
    event_list = []
    for item in events:
        event_list.append(str(item[0]))
        print(f"\t\t\t{item[0]}.{events_dict[item[0]]}")
    id_and_events[member_id] = event_list
    return id_and_events


def see_how_many_from_a_study_year(path: str = "config.json"):
    config = read_config()
    with open(path, 'r') as f:
        study_years = json.loads(f.read())['study_years']
    study_year = input("Introduceti un an de la 1 la 4: ")
    while study_year.isdigit() == False or study_year not in study_years.keys():
        study_year = input("An inexistent! Introduceti un an de la 1 la 4: ")

    sql_query = (
        f"select id, last_name, first_name from euroavia.members where study_year = '{study_years[study_year]}' ")
    members = execute_query(sql_query, config)
    print(f"\nStudentii care sunt in anul {study_years[study_year]}:  ")
    for member in members:
        print(f"\t{member[0]}. {member[1]} {member[2]}")



def delete_event_for_member():
    id_and_events = see_events_for_member()
    member_id = list(id_and_events.keys())[0]
    events = list(id_and_events.values())[0]

    id_to_del =input("Dati id-ul evenimentului la care membrul nu va mai participa: ")
    while id_to_del not in events:
        id_to_del = input("Id invalid! Dati id-ul: ")

    try:
        config = read_config()
        sql_query = (f"delete from euroavia.events_members where (event_id = {id_to_del} and member_id={member_id})")
        execute_query(sql_query,config, show=False)
    except Exception as e:
        print(f"Eroare! Stergerea nu a fost realizata ! {e}")
    else:
        print("Stergerea a fost realizata cu succes!")

def add_event_for_member():

    id_and_events = see_events_for_member()
    events = list(id_and_events.values())[0]
    member_id = list(id_and_events.keys())[0]
    config = read_config()
    sql_query = ("select event_id, name from euroavia.events ")
    x = execute_query(sql_query, config)
    for event_id in events:
        [x.remove(item) for item in x if event_id == str(item[0])]

    print("Evenimentele la care membrul nu participa sunt: ")
    my_dict = show_dict_stylish(x)
    list_of_available_ids = list(my_dict.keys())
    list_of_available_ids = [str(item) for item in list_of_available_ids]
    if len(list_of_available_ids) == 0:
        print("Membrul participa deja la toate evenimentele!")
        exit()
    user_pick = input("Dati id-ul evenimentului la care va participa membrul: ")
    while user_pick not in list_of_available_ids:
        user_pick = input("Id invalid! Dati id-ul: ")

    sql_query = (f"insert into euroavia.events_members (event_id,member_id) values({int(user_pick)}, {member_id}) ")
    try:
        execute_query(sql_query, config, False)
    except Exception as e:
        print(f"Failed on adding event for member! {e} ")
    else:
        print("Eveniment adaugat!")



def delete_member():
    config = read_config()
    sql_query = ("select id, last_name, first_name from euroavia.members ")
    x =execute_query(sql_query, config)
    member_dict = show_dict_stylish(x)
    member_id = input('Dati un id:')
    while member_id.isdigit() == False or int(member_id) not in list(member_dict.keys()):
        member_id = input(f'Numar invalid ! Reintroduceti id-ul:')

    sql_query = (f"delete from euroavia.members where id = {member_id}")
    try:
        execute_query(sql_query, config, False)
    except Exception as e:
        print(f"Error on deleting member! {e}")
    else:
        print("Membrul a fost sters!")


def replace_member_to_another_dep():
    config = read_config()
    sql_query = ("select id, last_name, first_name from euroavia.members ")
    x = execute_query(sql_query, config)
    member_dict = show_dict_stylish(x,3)

    sql_query = ("select id, department_id from euroavia.members ")
    y = execute_query(sql_query, config)
    dep_dict = show_dict_stylish(y, printed = False)

    member_id = input('Dati un id:')
    while member_id.isdigit() == False or int(member_id) not in list(member_dict.keys()):
        member_id = input(f'Numar invalid ! Reintroduceti id-ul:')
    initial_dep_id = dep_dict[int(member_id)]

    sql_query = ("select department_id, name from euroavia.departments ")
    x = execute_query(sql_query,config)
    event_dict = show_dict_stylish(x)
    dep_id = input('Dati un id:')
    while dep_id.isdigit() == False or int(dep_id) not in list(event_dict.keys()) or dep_id == str(initial_dep_id):
        dep_id = input(f'Numar invalid ! Reintroduceti id-ul:')

    sql_query = (f"update euroavia.members set department_id = {dep_id} where id ={member_id}")
    try:
        execute_query(sql_query,config, False)
    except Exception as e:
        print(f"Error on switching dep for member {e}")
    else:
        print("Ati schimbat departamentul membrului!")


def how_many_from_a_faculty():
    config = read_config()
    faculties = read_faculties()
    for key in faculties.keys():
        sql_query = (f"select count(id) from euroavia.members where college = {key} ")
        x = execute_query(sql_query,config)
        print(f"{faculties[key]} ---> {x[0][0]} membrii inscrisi!")












if __name__ == '__main__':
    # see_how_many_at_a_event()
    # see_how_many_at_a_department()
    #see_events_for_member()
    # see_how_many_from_a_study_year()
    # delete_event_for_member()
    # add_event_for_member()
    # delete_member()
    # replace_member_to_another_dep()
     #how_many_from_a_faculty()
    # see_how_many_at_a_department()
    # see_events_for_member()
    # delete_event_for_member()

    how_many_from_a_faculty()





