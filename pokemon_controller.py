from db import get_db
import json

def get_by_parameters(items):
    count = 0
    where = ""
    orderby = ""
    for key, value in items:
        if (key != 'orderby'):
            if (count == 0):
                where = " WHERE " + check_value_type(key, value)
            else:
                where = where + " AND " + check_value_type(key, value)
            count += 1
        else:
            orderby = value

    if (count == 0):
        return {'message': 'request has not filters'}

    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM tbl_pokemon" + where
    if orderby:
        statement = statement + " ORDER BY " +  orderby
    
    cursor.execute(statement)
    result = cursor.fetchall()
    return json.dumps( [dict(ix) for ix in result] )
   

def check_value_type(key, value):
    if type(value) == int or type(value) == float:
        return key + " = '" + value
    else:
        return "UPPER("  + key + ") = '" + value.upper() + "'"