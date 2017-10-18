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
              "ID" : INT(10, True, auto_increment=True),
              "USER" : VARCHAR(30),
              "SATSC" : BOOLEAN(default=0),
          },
          "extra" : {
                "primary_key" : "ID",
          },
          "auto_incr" : 0,
      }
    ]
}

user_schema = {
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
    },
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
            "PERIOD_LIMIT" : INT(4, default=12),
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
    return check_db and check_users


def drop_bem_schema():
    MYSQL.remove_database('bem_db')


def make_user_schema(user_name):
    for table in user_schema.values():
        MYSQL.make_table('bem_db',
                         table["name"].format(user_name),
                         **table["fields"],
                         **table["extra"])
        if table["auto_incr"] != None:
            MYSQL.table_primary_start('bem_db', table["name"].format(user_name),
                                      table["auto_incr"])


def check_user_schema(user_name):
    exists_p = '{0}_purchases'.format(user_name) in MYSQL.tables('bem_db')
    exists_c = '{0}_iocome'.format(user_name) in MYSQL.tables('bem_db')
    return exists_c and exists_p


def drop_user_schema(user_name):
    MYSQL.remove_table('bem_db', "{0}_purchases".format(user_name))
    MYSQL.remove_table('bem_db', "{0}_iocome".format(user_name))
