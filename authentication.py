import euroavia_db

def read_users_from_db(path: str = 'auth.json'):
    config = euroavia_db.read_config()
    sql_query = ("select email_address from euroavia.local_board")
    x = euroavia_db.execute_query(sql_query,config)
    lb_users = euroavia_db.show_dict_stylish(x,len_of_item=1)
    print()

if __name__ == '__main__':
    read_users_from_db()


