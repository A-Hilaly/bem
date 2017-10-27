from sql_tools.mysql import MYSQL


def register_purchase(user, purchase, value, _type):
    table = "{0}_purchases".format(user)
    MYSQL.add_element('bem_db', table, NAME=purchase, VALUE=value, TYPE=_type)


def drop_purchase(user, purchase_id=None):
    where = "ID={0}".format(purchase_id)
    table = "{0}_purchases".format(user)
    MYSQL.remove_elements('bem_db', table, where=where)


def get_purchases(user, date_opt=None, sort_opt=None, after=True):
    if not date_opt:
        if sort_opt:
            sby, sens = sort_opt
            return MYSQL.select_optimized('bem_db', '{0}_purchases'.format(user),
                sorted_by=sby, kind=sens, where="1=1",
            )
        else:
            return MYSQL.table_content('bem_db', '{0}_purchases'.format(user))
    if len(date_opt) == 2:
        dstart, dend = date_opt
        w = "DATE BETWEEN '{0}' AND '{1}'".format(dstart, dend)
        if sort_opt:
            sby, sens = sort_opt
            return MYSQL.select_optimized('bem_db', '{0}_purchases'.format(user),
                sorted_by=sby, kind=sens, where=w
            )
        else:
            return MYSQL.select_elements('bem_db', '{0}_purchases'.format(user),
                where=w,
            )
    elif len(date_opt) == 1:
        date_opt = date_opt[0]
        comp = ">" if after else "<"
        w = "DATE {0} '{1}'".format(comp, date_opt)
        if sort_opt:
            sby, sens = sort_opt
            return MYSQL.select_optimized('bem_db', '{0}_purchases'.format(user),
                sorted_by=sby, kind=sens, where=w,
            )
        else:
            return MYSQL.select_elements('bem_db', '{0}_purchases'.format(user),
                where=w,
            )
