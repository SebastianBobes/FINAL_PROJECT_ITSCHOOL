import json
import psycopg2 as ps
from psycopg2._psycopg import cursor
import excel_writer
from members import Member

def read_config(path: str = 'config.json')->dict:
    """
    returns config data in order to connect to DB
    """
    try:
        with open(path, 'r') as f:
            config = json.loads(f.read())['config_db']
            return config
    except Exception as e:
        print(f"Error on reading config file! {e}")

def read_sduty_years_from_config(path: str= 'config.json'):
    """
    reads study years dict from config file
    """
    try:
        with open(path, 'r') as f:
            study_years = json.loads(f.read())['study_years']
    except Exception as e:
        print(f"Couldn't read study years from file {e}")
    else:
        return study_years


def execute_query(sql_query: str, config: dict, show: bool = True):
    """

    :param sql_query: the string query
    :param config: config file to connect with db
    :param show: True if the result must be shown
    :return: returns data if exists, else cursor
    """
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

def read_parameter_from_db(table_name: str,id_name: str = 'event_id', name: str= 'name', name_2:str='') ->dict:
    """

    :param table_name: the table where you want to read informations
    :param id_name: the name of the id in the  table
    :param name: variable 1 you want to read
    :param name_2: variable 2 you want to read
    :return: a dictionary with the info
    """
    config  = read_config()
    if name_2 == '':
        sql_qury = (f"select {id_name},{name} from euroavia.{table_name}")
        x = execute_query(sql_query=sql_qury, config=config, show=True)
        return show_dict_stylish(x, printed=False)
    else:
        sql_qury = (f"select {id_name},{name}, {name_2} from euroavia.{table_name}")
        x = execute_query(sql_query=sql_qury, config=config, show=True)
        return show_dict_stylish(x, len_of_item = 3, printed=False)




def insert_member_into_db(member: Member) -> bool:
    """

    :param member: the member instance you want to insert in db
    :return: True if succeed, else False
    """
    config = read_config()
    sql_query = ("INSERT into euroavia.members (last_name, first_name, middle_name,telephone_number,study_year,college,department_id,email_address)"
                f"values('{member.last_name}','{member.first_name}','{member.middle_name}','{member.telephone_number}','{member.study_year}', '{member.college}',{member.department_id}, '{member.email}')")
    try:
        execute_query(sql_query,config, show=False)
    except Exception as e:
        print(f"Error on inserting member into DB! {e}")
        return False
    else:
        return True



def read_last_id() -> int:
    """
    reads the last id from current db
    :return: the id
    """
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

def add_events_for_member(events:list,  path: str = "config.json") -> bool:
    """

    :param events: list of envent to be added
    :param path: path of the config file
    :return: True if succeed, else False
    """
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

def add_events_for_member_from_form(events:list,  path: str = "config.json"):
    """
    function created to add events from a member chosen in form
    :param events: list of events to be added
    :param path: path of the config file
    :return:
    """
    config = read_config()
    with open(path, 'r') as f:
        events_id = json.loads(f.read())['event_id']
    for event in events:
        sql_query = (f"INSERT into euroavia.events_members(event_id, member_id) values({events_id[event]},{read_last_id()})")
        execute_query(sql_query, config, show=False)


def unicity_checker(parameter: str, category: str) ->bool:
    """
    it checks the unicity of a parameter in a table
    :param parameter: the varibale you want to check
    :param category: the category where to find the same variable
    :return:
    """
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


def show_dict_stylish(initial_dict: list, len_of_item: int = 2, printed: bool = True) -> dict | list:
    """
    function created to show the result of a execution of a query in an elegant way
    :param initial_dict: the dict you want to transform
    :param len_of_item: the len of the tuple inside the dict
    :param printed: True if you want to be printed, else False
    :return:
    """
    second_dict = {}
    if len_of_item == 1:
        second_list = []
        for item in initial_dict:
            second_list.append(item[0])
        return second_list

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


def see_how_many_at_a_event(event_id: int, excel: bool = False):
    """
    function created to see how many persons joined the event id given
    :param event_id: id of the event
    :param excel: True if data to be writen in excel, else False
    :return: data(list of every id and number of persons) for the excel or just the number of persons
    """
    config = read_config()
    data =[]
    if excel:
        sql_query = ("select event_id, name from euroavia.events ")
        x = execute_query(sql_query, config)
        events_dict = show_dict_stylish(x, printed=False)
        for event_id in events_dict.keys():
            sql_query = (f"select count(member_id) from euroavia.events_members where event_id ={event_id}")
            number_of_members = execute_query(sql_query, config)[0][0]
            data.append([events_dict[event_id],number_of_members])
        return data
    else:
        sql_query = (f"select count(member_id) from euroavia.events_members where event_id ={event_id}")
        number_of_members = execute_query(sql_query, config)[0][0]
        return number_of_members





def see_how_many_at_a_department(dep_id,excel: bool = False) ->list|int:
    """

    :param dep_id: the id of the department
    :param excel: True if the data to be writen in excel, else, False
    :return: data(list of every id and number of persons) for the excel or just the number of persons
    """
    config = read_config()
    data = []
    if excel:
        sql_query = ("select department_id, name from euroavia.departments ")
        x = execute_query(sql_query, config)
        deps_dict = show_dict_stylish(x, printed=False)
        for dep_id in (deps_dict.keys()):
            sql_query = (f"select count(id) from euroavia.members where department_id ={dep_id}")
            number_of_members = execute_query(sql_query, config)[0][0]
            data.append([deps_dict[dep_id], number_of_members])
        return data
    else:
        sql_query = (f"select count(id) from euroavia.members where department_id ={dep_id}")
        number_of_members = execute_query(sql_query, config)[0][0]
        return number_of_members




def see_events_for_member(member_id: int,delete: bool =False) -> dict|list:
    """
    function created to see the events joined by a member
    :param member_id: id of the member
    :param delete: True if you want to save a dictionary with the id of member and if of events joined bu that member
    :return: list with events ids or a dict with the id of member and events
    """
    config = read_config()

    sql_query = (f"select event_id from euroavia.events_members where member_id ={int(member_id)}")
    events = execute_query(sql_query,config)

    sql_query = (f"select event_id, name from euroavia.events ")
    y = execute_query(sql_query, config)
    events_dict = show_dict_stylish(y, printed=False)
    if delete ==  False:
        my_list = []
        for item in events:
            my_list.append(f"{item[0]}.{events_dict[item[0]]}")
        return my_list
    else:
        my_list =[]
        id_and_events = {}
        event_list = []
        for item in events:
            event_list.append(int(item[0]))
            my_list.append(f"{item[0]}.{events_dict[item[0]]}")
        id_and_events[member_id] = event_list
        return id_and_events




def see_how_many_from_a_study_year(study_year: str, excel: bool = False) -> list|int:
    """

    :param study_year: the study year you want to check
    :param excel: True if data to be writen in excel, else False
    :return: data for the excel or number of members from that study year
    """
    config = read_config()
    if excel:
        sql_query = (f"select id, last_name, first_name from euroavia.members where study_year = '{study_year}' ")
        members = execute_query(sql_query, config, show=True)
        list = []
        for member in members:
            list.append([study_year,member[1],member[2]])
        return list
    else:
        sql_query = (f"select count(id) from euroavia.members where study_year = '{study_year}' ")
        members = execute_query(sql_query, config, show=True)
        return members[0][0]






def delete_event_for_member(member_id: int,event_id : int):
    """
    delete the events the member is not joining anymore
    :param member_id: id of the member
    :param event_id: the id of the event you want to delete from db
    :return: True if succeed, else False
    """
    events = see_events_for_member(member_id,True)[member_id]
    if event_id not in events:
        return False
    try:
        config = read_config()
        sql_query = (f"delete from euroavia.events_members where (event_id = {event_id} and member_id={member_id})")
        execute_query(sql_query,config, show=False)
    except Exception as e:
        print(f"Eroare! Stergerea nu a fost realizata ! {e}")
    else:
        print("Stergerea a fost realizata cu succes!")
        return True


def add_event_for_member(member_id: int, event_id: int) -> bool:
    """
    add event for a member to join
    :param member_id:id of the member
    :param event_id: the id of the event member is joining
    :return: True if succed, else False
    """
    config = read_config()
    id_and_events = see_events_for_member(member_id)
    events = see_events_for_member(member_id,True)[member_id]

    if event_id in events:
        return False
    else:
        sql_query = (f"insert into euroavia.events_members (event_id,member_id) values({event_id}, {member_id}) ")
        try:
            execute_query(sql_query, config, False)
        except Exception as e:
            print(f"Failed on adding event for member! {e} ")
        else:
            print("Eveniment adaugat!")
            return True




def delete_member(member_id: int) -> bool:
    """
    delete member from db
    :param member_id: id of the member to be deleted
    :return: True if succed, else False
    """
    config = read_config()
    sql_query = (f"delete from euroavia.members where id = {member_id}")
    try:
        execute_query(sql_query, config, False)
    except Exception as e:
        print(f"Error on deleting member! {e}")
        return False
    else:
        print("Membrul a fost sters!")
        return True



def replace_member_to_another_dep(member_id: int, dep_id: int) -> bool:

    """
    update the department of a member
    :param member_id: id of the member
    :param dep_id: id of the department
    :return: True if succed, else False
    """

    config = read_config()
    sql_query = (f"select department_id from euroavia.members where id={member_id} ")
    x = execute_query(sql_query, config)
    if dep_id ==x[0][0]:
        return False
    else:
        sql_query = (f"update euroavia.members set department_id = {dep_id} where id ={member_id}")
        try:
            execute_query(sql_query,config, False)
        except Exception as e:
            print(f"Error on switching dep for member {e}")
            return False
        else:
            print("Ati schimbat departamentul membrului!")
            return True



def how_many_from_a_faculty(id: int, excel: bool = False):
    """
    function created to see the number of members from a specific faculty, or from all of them
    :param id: the id of the faculty
    :param excel: True if you want all the data to be wirten in excel, else False
    :return: integer(number of members) or a list with faculties and number of members for each faculty
    """
    config = read_config()
    faculties = read_parameter_from_db('faculties', 'id', 'name')
    if excel == False:
        for key in faculties.keys():
            if id  == key:
                break
        sql_query = (f"select count(id) from euroavia.members where college = {key} ")
        x = execute_query(sql_query, config)
        return x[0][0]
    else:
        my_list =[]
        for key in faculties.keys():
            sql_query = (f"select count(id) from euroavia.members where college = {key} ")
            x = execute_query(sql_query,config)
            my_list.append([faculties[key],x[0][0]])
        return my_list








