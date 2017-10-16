from sql_tools.mysql import MYSQL
from .database.schema import drop_user_schema, make_user_schema


def create_user(user, make_schema=False):
    MYSQL.add_element('bem_db', 'bem_users', USER=user)
    if make_schema:
        make_user_schema(user)


def drop_user(user, drop_schema=False):
    where="USER='{0}'".format(user)
    MYSQL.remove_elements('bem_db', 'bem_users', where=where)
    if drop_schema:
        drop_user_schema(user)


def register_purcharse(user, purchase, value, _type):
    table = "{0}_purchases".format(user)
    MYSQL.add_element('bem_db', table, NAME=purchase, VALUE=value, TYPE=_type)


def drop_purchase(user, purchase_id=None):
    where = "ID={0}".format(purchase_id)
    table = "{0}_purchases".format(user)
    MYSQL.remove_elements('bem_db', table, where=where)


def register_iocome(user, iocome, value, _type):
    table = "{0}_iocome".format(user)
    MYSQL.add_element('bem_db', table, NAME=purchase, VALUE=value, TYPE=_type)


def drop_iocome(user, iocome_id):
    where = "ID={0}".format(iocome_id)
    table = "{0}_iocome".format(user)
    MYSQL.remove_elements('bem_db', table, where=where)
