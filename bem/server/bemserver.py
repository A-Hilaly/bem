from flask import Flask, jsonify, make_response, request, abort

from bem.dataio import (
    create_user,
    get_users,
    drop_user,
    register_purchase,
    drop_purchase,
    get_purchases,
    register_iocome,
    drop_iocome,
    get_iocome,
)

from bem.schema import (
    check_bem_schema
)


app = Flask(__name__)

#############################

@app.errorhandler(404)
def not_found(error):
    """
    """
    return make_response(jsonify({'error': 'URL Not found'}), 404)

def bem_error(error, msg, exception=None):
    if exception:
        return make_response(jsonify({'error' : msg,
                                      'code' : error,
                                      'exception msg': exception}))
    return make_response(jsonify({'error' : msg, 'code': error}))


#############################
# General Schema #
#############################


@app.route('/bem/test', methods=['GET'])
def test():
    """
    """
    return jsonify({'working': 'OK'})


@app.route('/bem/schema', methods=['GET'])
def check_bem():
    """
    """
    a = check_bem_schema()
    return jsonify({'bem_schema_status': a})


@app.route('/bem/users', methods=['GET'])
def bem_users():
    """
    """
    data = get_users()
    return jsonify({'total_users': len(data),
                    'bem_users': data})


@app.route('/bem/user', methods=['POST'])
def bem_add_user():
    """
    """
    if not request.json:
        abort(400)
    user = request.json.get('user')
    schema = request.json.get('schema')
    try:
        create_user(user, schema)
        return jsonify({'created_user': user, 'schema': schema})
    except Exception as e:
        return bem_error(300, 'Could not create user', e.msg)


@app.route('/bem/user', methods=['DELETE'])
def bem_drop_user():
    """
    """
    if not request.json:
        abort(400)
    user = request.json.get('user')
    schema = request.json.get('schema')
    try:
        drop_user(user, schema)
        return jsonify({'dropped_user': user, 'schema': schema})
    except Exception as e:
        return bem_error(300, 'Could drop user', e.msg)


@app.route('/bem/user/data', methods=['GET'])
def user_data():
    """
    """
    if not request.json:
        abort(400)
    user = request.json.get('user')
    data_type = request.json.get('data_type')
    date_opt = request.json.get('date_opt') or None
    sort_opt = request.json.get('sort_opt') or None
    after = request.json.get('after') or False
    try:
        if data_type == 'purchases':
            data = get_purchases(user, date_opt=date_opt, sort_opt=sort_opt,
                                 after=after)
            return jsonify({'user': user,
                            'data_type': data_type,
                            'data': data})
        elif data_type == 'iocome':
            data = get_iocome(user)
            return jsonify({'user': user,
                            'data_type': data_type,
                            'data': data})
    except Exception as e:
        return bem_error(300, 'Could not get data', e.msg)


@app.route('/bem/user/data', methods=['POST'])
def append_user_data():
    """
    """
    if not request.json:
        abort(400)
    user = request.json.get('user')
    data_type = request.json.get('data_type')
    auto = request.json.get('auto')
    ruled = request.json.get('ruled')
    try:
        if data_type == 'purchases':
            register_purchase(user, *auto)
            return jsonify({"register_purchases" : "OK",
                            "buffed data" : str(auto)})
        elif data_type == 'iocome':
            register_iocome(user, *auto, **ruled)
            return jsonify({"register_iocome" : "OK",
                            "buffed data" : str(data) + str(list(auto.values()))})
    except Exception as e:
        return bem_error(300, 'Could not post data', e.msg)


if __name__ == '__main__':
    app.run(debug=True)
