from sql_tools.mysql import (MYSQL,
                             INT,
                             VARCHAR,
                             TIMESTAMP,
                             ENUM)

bem_schema = {
    "bem_db" : [
      {
          "name" : "bem_users",
          "fields" : {
              "ID" : INT(10, True, auto_increment=True),
              "USER" : VARCHAR(30),
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
        "name" : "{0}_purcharses",
        "fields" : {
            "ID" : INT(10, True, auto_increment=True),
            "NAME" : VARCHAR(30),
            "VALUE" : VARCHAR(10),
            "DATE" : TIMESTAMP(default='NOW'),
            "TYPE" : VARCHAR(30, default="UNKNOWN"),
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
            "NAME" : VARCHAR(30),
            "VALUE" : VARCHAR(10),
            "DATE" : TIMESTAMP(default='NOW'),
            "TYPE" : VARCHAR(30, default"UNKNOWN"),
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
    pass

def drop_bem_schema():
    pass

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
    pass


def drop_user_schema(user_name):
    pass
