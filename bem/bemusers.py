from sql_tools.mysql import MYSQL
from .schema import drop_user_schema, make_user_schema
#from .math.decorator import raws_of_matrix



def create_user(user, make_schema=False):
    MYSQL.add_element('bem_db', 'bem_users', USER=user)
    if make_schema:
        make_user_schema(user)
        MYSQL.update_element('bem_db', 'bem_users',
                             sets="SATSC=1",
                             where="USER='{0}'".format(user))


def get_users():
    return MYSQL.table_content('bem_db', 'bem_users')


def drop_user(user, drop_schema=False):
    where="USER='{0}'".format(user)
    MYSQL.remove_elements('bem_db', 'bem_users', where=where)
    if drop_schema:
        drop_user_schema(user)


def register_purchase(user, purchase, value, _type):
    table = "{0}_purchases".format(user)
    MYSQL.add_element('bem_db', table, NAME=purchase, VALUE=value, TYPE=_type)


def drop_purchase(user, purchase_id=None):
    where = "ID={0}".format(purchase_id)
    table = "{0}_purchases".format(user)
    MYSQL.remove_elements('bem_db', table, where=where)


def get_purchases(user):
    return MYSQL.table_content('bem_db', '{0}_purchases'.format(user))


def register_iocome(user, iocome, value, _type, period, period_limit=None, date_limit=None):
    table = "{0}_iocome".format(user)
    MYSQL.add_element('bem_db', table, NAME=purchase, VALUE=value, TYPE=_type,
                      PERIOD=period, DATE_LIMIT=str(date_limit), PERIOD_LIMIT=str(period_limit))


def drop_iocome(user, iocome_id):
    where = "ID={0}".format(iocome_id)
    table = "{0}_iocome".format(user)
    MYSQL.remove_elements('bem_db', table, where=where)


def get_iocome(user):
    return MYSQL.table_content('bem_db', '{0}_iocome'.format(user))
