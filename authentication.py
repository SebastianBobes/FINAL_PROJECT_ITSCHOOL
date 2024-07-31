import json

import euroavia_db

def read_users_from_db(source: str = 'local_board') -> dict:
    config = euroavia_db.read_config()
    if source == 'local_board':
        sql_query = (f"select id,email_address, position from euroavia.{source}")
    elif source == 'heads':
        sql_query = (f"select id,email_address,department_head_of  from euroavia.{source}")
    x = euroavia_db.execute_query(sql_query,config)
    my_dict = euroavia_db.show_dict_stylish(x, len_of_item=3, printed=False)
    str = ''
    new_dict={}
    for id in my_dict:
        for char in my_dict[id][1]:
            if  char !='@':
                str = str+char
            else:
                my_list  = list(my_dict[id])
                my_list.remove(my_dict[id][1])
                my_list.append(str)
                new_dict.update({id:my_list})
                my_list = []
                str= ''
                break
    return new_dict

def read_dep(dep_id: int, path:str='config.json'):
    with open(path, 'r') as f:
        dep = json.loads(f.read())['departments_id']
        dep_swap={v:k for k,v  in dep.items()}
    return dep_swap[dep_id]

def create_auth_dict(users: dict, source:str = "local_board") -> dict:
    auth_dict = {}
    auth_dict[f'{source}'] = []
    for id in users:
        if source=='local_board':
            auth_dict[f'{source}'].append({"id": id, "user": users[id][1], "position": users[id][0]})
        elif source == 'heads':
            auth_dict[f'{source}'].append({"id": id, "user": users[id][1], "dep_head_of:": read_dep(users[id][0])})

    return auth_dict




def write_and_read_credentials(path: str = "auth.json"):
    users = read_users_from_db(source='heads')
    auth_dict = create_auth_dict(users, 'heads')
    users = read_users_from_db()
    auth_dict.update(create_auth_dict(users, 'local_board'))
    with open(path, 'r') as f:
        initial_dict = json.loads(f.read())
        for i in initial_dict:
            for index,member_dict in enumerate(initial_dict[i]):
                auth_dict[i][index]['password']  = member_dict['password']
    with open(path, 'w') as f:
        f.seek(0)
        f.write(json.dumps((auth_dict), indent = 4))

    return auth_dict

def read_function_from_file(user,path: str = 'auth.json'):
    with open(path, 'r') as f:
        credentials = json.loads(f.read())
        for item in credentials.keys():
            for my_dict in credentials[item]:
                if user == my_dict['user']:
                    if item == 'heads':
                        return my_dict['dep_head_of:']
                    elif item == 'local_board':
                        return my_dict['position']

# def change_password(user, password, path: str = 'auth.json'):
#     with open(path, 'w'):












