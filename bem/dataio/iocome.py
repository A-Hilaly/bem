from sql_tools.mysql import MYSQL


def register_iocome(user, iocome, value, _type, period, period_limit=None, date_limit=None):
    table = "{0}_iocome".format(user)
    MYSQL.add_element('bem_db', table, NAME=iocome, VALUE=value, TYPE=_type,
                      PERIOD=period, DATE_LIMIT=str(date_limit), PERIOD_LIMIT=str(period_limit))


def drop_iocome(user, iocome_id):
    where = "ID={0}".format(iocome_id)
    table = "{0}_iocome".format(user)
    MYSQL.remove_elements('bem_db', table, where=where)


def get_iocome(user):
    return MYSQL.table_content('bem_db', '{0}_iocome'.format(user))
