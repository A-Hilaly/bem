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
    if drop_schema:
        drop_user_schema(user)
    MYSQL.remove_elements('bem_db', 'bem_users', where=where)
