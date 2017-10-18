from flask import Flask, jsonify, make_response, request, abort

from bem.bemusers import (
    create_user,
    get_users,
    drop_user,
    register_purchase,
    drop_purchase,
    get_purchases,
)

from bem.schema import (
    make_bem_schema,
    check_bem_schema,
    drop_bem_schema,
    check_user_schema,
    drop_user_schema,
)


app = Flask(__name__)

#############################

@app.errorhandler(404)
def not_found(error):
    """
    """
    return make_response(jsonify({'error': 'URL Not found'}), 404)

def bem_error(error, msg):
    return make_response(jsonify({'error' : msg, 'code': error}))

#############################
# General Schema #
#############################

@app.route('/bem/schema', methods=['GET'])
def check_bem():
    """
    """
    if not request.json:
        abort(400)
    check_bem_schema()


@app.route('/bem/test', methods=['GET'])
def test():
    """
    """
    return jsonify({'working': 'OK'})

@app.route('/bem/users', methods=['GET'])
def bem_users():
    """
    """
    data = get_users()
    return jsonify({'bem_users': data})

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
        return jsonify({'Created new user': user, 'schema': schema})
    except:
        return bem_error(300, 'Could not create user')

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
        return jsonify({'Dropped user': user, 'schema': schema})
    except:
        return bem_error(300, 'Could drop user')

if __name__ == '__main__':
    app.run(debug=True)
