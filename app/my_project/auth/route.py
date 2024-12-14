from flask import Blueprint, request, jsonify, current_app
from .controller import *


branch_bp = Blueprint('branch_bp', __name__, url_prefix='/api/branches')
user_bp = Blueprint('user_bp', __name__, url_prefix='/api/users')
select_bp = Blueprint('select_bp', __name__, url_prefix='/api/select')
api_bp = Blueprint('api_bp', __name__, url_prefix='/api/lab5')


# ---------- Branch Routes ----------
@branch_bp.route('/', methods=['GET'])
def get_all_branches():
    return BranchController.get_all_branches()

@branch_bp.route('/<int:branch_id>', methods=['GET'])
def get_branch(branch_id):
    return BranchController.get_branch(branch_id)

@branch_bp.route('/', methods=['POST'])
def add_branch():
    data = request.get_json()
    print(data)
    return BranchController.add_branch(data)

@branch_bp.route('/<int:branch_id>', methods=['PUT'])
def update_branch(branch_id):
    data = request.get_json()
    return BranchController.update_branch(branch_id, data)

@branch_bp.route('/<int:branch_id>', methods=['DELETE'])
def delete_branch(branch_id):
    return BranchController.delete_branch(branch_id)


# ---------- User Routes ----------
@user_bp.route('/', methods=['GET'])
def get_all_users():
    return UserController.get_all_users()

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return UserController.get_user(user_id)

@user_bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    return UserController.add_user(data)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return UserController.update_user(user_id, data)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return UserController.delete_user(user_id)



# ---------- Select Routes LAB4 ----------
@select_bp.route('/m_and_one', methods=['GET'])
def get_all_stories_with_tags():
    query = "SELECT Branch.city AS branch_city, Courier.full_name AS courier_name FROM Branch LEFT JOIN Courier ON Branch.id = Courier.branch_id ORDER BY Branch.city, Courier.full_name"

    connection = current_app.mysql.connection
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)

        if result:
            return jsonify(result), 200
        else:
            return jsonify({'message': 'No data found'}), 404
        
    except Exception as e:
        return jsonify({'error': f'Failed to retrieve stories with tags: {str(e)}'}), 500
    finally:
        cursor.close()

@select_bp.route('/m_and_m', methods=['GET'])
def get_all_users_with_stories():
    query = "SELECT Parcel.tracking_number AS parcel_tracking_number, Courier.full_name AS courier_name FROM ParcelMovement JOIN Parcel ON ParcelMovement.parcel_id = Parcel.id JOIN Courier ON ParcelMovement.courier_id = Courier.id ORDER BY Parcel.tracking_number, Courier.full_name"

    connection = current_app.mysql.connection
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)

        if result:
            return jsonify(result), 200
        else:
            return jsonify({'message': 'No data found'}), 404
        
    except Exception as e:
        return jsonify({'error': f'Failed to retrieve users with stories: {str(e)}'}), 500
    finally:
        cursor.close()





# ---------- LAB5 ----------

@api_bp.route('/branchReview', methods=['POST'])
def branchReview():
    data = request.json
    branch_code = data.get('branch_code')
    review_text = data.get('review_text')
    
    if not branch_code or not review_text:
        return jsonify({'error': 'Missing required fields'}), 400
    
    query = "INSERT INTO BranchReview (branch_code, review_text) VALUES (%s, %s);"

    connection = current_app.mysql.connection
    try:
        cursor = connection.cursor()
        cursor.execute(query, (branch_code, review_text))  
        connection.commit()

        return jsonify({'message': 'Review added successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'Failed to add review: {str(e)}'}), 500
    finally:
        cursor.close()

@api_bp.route('/insertIntoSpecifiedTable', methods=['POST'])
def insertIntoSpecifiedTable():
    data = request.json
    table_name = data.get('table_name')
    columns = data.get('columns')
    values = data.get('values')
    
    # Перевірка даних
    if not table_name or not isinstance(table_name, str):
        return jsonify({'error': 'Invalid or missing table_name'}), 400

    if not columns or not isinstance(columns, str):
        return jsonify({'error': 'Invalid or missing columns'}), 400

    if not values or not isinstance(values, str):
        return jsonify({'error': 'Invalid or missing values'}), 400
    
    # SQL-запит із параметрами
    query = "CALL InsertIntoSpecifiedTable(%s, %s, %s)"
    params = (table_name, columns, values)

    connection = current_app.mysql.connection
    
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()

        return jsonify({'message': 'Data added successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'Failed to add data: {str(e)}'}), 500
    finally:
        cursor.close()

@api_bp.route('/insertNonameRows', methods=['POST'])
def insertNonameRows():
    data = request.json
    table_name = data.get('table_name')
    column_name = data.get('column_name')
    rows_count = data.get('rows_count')
    
    if not table_name or not column_name or not rows_count:
        return jsonify({'error': 'Missing required fields'}), 400
    
    query = "CALL InsertNonameRows(%s, %s, %s);"
    select_query = f"SELECT * FROM {table_name};"

    connection = current_app.mysql.connection
    try:
        cursor = connection.cursor()
        cursor.execute(query, (table_name, column_name, rows_count))  
        connection.commit()

        cursor.execute(select_query)
        result = cursor.fetchall()

        if result:
            return jsonify(result), 200

        return jsonify({'message': 'Rows added successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'Failed to add rows: {str(e)}'}), 500
    finally:
        cursor.close()

@api_bp.route('/getAndPrintTotalRecords', methods=['GET'])
def getAndPrintTotalRecords():
    query = "CALL GetAndPrintTotalRecords();"
    
    connection = current_app.mysql.connection
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            return jsonify(result), 200
        else:
            return jsonify({'message': 'No data found'}), 404
        
    except Exception as e:
        return jsonify({'error': f'Failed to retrieve sum media id: {str(e)}'}), 500
    finally:
        cursor.close()


@api_bp.route('/createDynamicDatabases', methods=['POST'])
def createDynamicDatabases():
    query = "CALL CreateDynamicDatabases();"

    connection = current_app.mysql.connection
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

        return jsonify({'message': 'Databases created successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'Failed to create databases: {str(e)}'}), 500
    finally:
        cursor.close()
