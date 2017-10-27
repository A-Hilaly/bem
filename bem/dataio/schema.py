from sql_tools.mysql import (MYSQL,
                             INT,
                             VARCHAR,
                             TIMESTAMP,
                             ENUM,
                             BOOLEAN)

bem_schema = {
    "bem_db" : [
      {
          "name" : "bem_users",
          "fields" : {
              "USER" : VARCHAR(30),
              "SATSC" : BOOLEAN(default=0),
          },
          "extra" : {
                "primary_key" : "USER",
          },
          "auto_incr" : None,
      }
    ]
}

UPS = {
    "user_purchases" : {
        "name" : "{0}_purchases",
        "fields" : {
            "ID" : INT(10, True, auto_increment=True),
            "NAME" : VARCHAR(50),
            "VALUE" : VARCHAR(10),
            "DATE" : TIMESTAMP(default='NOW'),
            "TYPE" : VARCHAR(50, default="UNKNOWN"),
        },
        "extra" : {
              "primary_key" : "ID",
        },
        "auto_incr" : 0,
    }
}

UCS = {
    "user_charges" : {
        "name" : "{0}_iocome",
        "fields" : {
            "ID" : INT(10, True, auto_increment=True),
            "NAME" : VARCHAR(50),
            "VALUE" : VARCHAR(10),
            "DATE" : TIMESTAMP(default='NOW'),
            "TYPE" : VARCHAR(50, default="UNKNOWN"),
            "PERIOD" : VARCHAR(10, default="1M"),
            "DATE_LIMIT" : VARCHAR(30, default="NaN-NaN-NaN"),
            "PERIOD_LIMIT" : INT(4, default=0),
        },
        "extra" : {
              "primary_key" : "ID",
        },
        "auto_incr" : 0,
    }
}


def make_bem_schema():
    databases = [i for i in bem_schema.keys()]
    for database in databases:
        # databases
        MYSQL.make_database(database)
        tables = bem_schema[database]
        for table in tables:
            # tables
            MYSQL.make_table(database,
                             table["name"],
                             **table["fields"],
                             **table["extra"])
            if table["auto_incr"] != None:
                MYSQL.table_primary_start(database, table["name"],
                                          table["auto_incr"])


def check_bem_schema():
    check_db = 'bem_db' in MYSQL.databases()
    check_users = 'bem_users' in MYSQL.tables('bem_db')
    status = check_db and check_users
    if status:
        return 1
    elif check_db:
        return -1
    return -2


def drop_bem_schema():
    status = check_bem_schema()
    if status or status == -1:
        MYSQL.remove_database('bem_db')


def check_user_schema(user_name):
    exists_p = '{0}_purchases'.format(user_name) in MYSQL.tables('bem_db')
    exists_c = '{0}_iocome'.format(user_name) in MYSQL.tables('bem_db')
    if exists_p and exists_c:
        return True
    elif exists_p:
        return -1
    elif exists_c:
        return -2
    return -3


def _make_user_ups(user_name):
    ups = UPS['user_purchases']
    MYSQL.make_table('bem_db', ups['name'].format(user_name),
                     **ups['fields'], **ups['extra'])
    MYSQL.table_primary_start('bem_db', ups["name"].format(user_name),
                              ups["auto_incr"])


def _make_user_ucs(user_name):
    ucs = UCS['user_charges']
    MYSQL.make_table('bem_db', ucs['name'].format(user_name),
                     **ucs['fields'], **ucs['extra'])
    MYSQL.table_primary_start('bem_db', ucs["name"].format(user_name),
                              ucs["auto_incr"])


def make_user_schema(user_name):
    status = check_user_schema(user_name)
    if status == -1:
        _make_user_ups(user_name)
    elif status == -2:
        _make_user_ucs(user_name)
    elif status == -3:
        _make_user_ups(user_name)
        _make_user_ucs(user_name)


def drop_user_schema(user_name):
    status = check_user_schema(user_name)
    if status == -2:
        MYSQL.remove_table('bem_db', "{0}_iocome".format(user_name))
    elif status == -1:
        MYSQL.remove_table('bem_db', "{0}_purchases".format(user_name))
    elif status == -3:
        pass
    elif status:
        MYSQL.remove_table('bem_db', "{0}_iocome".format(user_name))
        MYSQL.remove_table('bem_db', "{0}_purchases".format(user_name))
