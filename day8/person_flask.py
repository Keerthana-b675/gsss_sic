from flask import Flask, jsonify, request
from db_operations import PersonOperations as PerOprs, Person

people = PerOprs()
people.create_database()
people.create_table()

app = Flask(__name__)

@app.route('/people',methods=['POST'])
def people_create():
    body = request.get_json()
    new_people = Person(body['id'],body['name'], body['gender'], body['age'], body['location'])
    print(new_people)
    id = people.insert_row(new_people)
    people = people.search_row(id)
    people_dict = {'id':people[0], 'name':people[1], 'gender':people[2], 'age':people_dict[3], 'location': people[4]}
    return jsonify(people_dict)

@app.route('/people/<id>',methods=['GET'])
def people_read_by_id(id):
    people = Person.search_row(id)
    if people == None:
        return jsonify("Person not found")
    people_dict = {'id':people[0], 'name':people[1], 'gender':people[2], 'age':people_dict[3], 'location': people[4]}
    return jsonify(people_dict)

@app.route('/people',methods=['GET'])
def people_read_all():
    people_list = people.list_all_rows()
    people_dict = []
    for people in people_list:
        people_dict.append({'id':people[0], 'name':people[1], 'gender':people[2], 'age':people_dict[3], 'location': people[4]})
    return jsonify(people_dict)

@app.route('/people/<id>',methods=['PUT'])
def people_update(id):
    body = request.get_json()
    old_people_obj = people.search_row(id)
    if not old_people_obj:
        return jsonify({'message': 'Employee not found'})
    old_people_obj = []
    old_people_obj.append(body['name'])
    old_people_obj.append(body['designation'])
    old_people_obj.append(body['phone_number'])
    old_people_obj.append(body['commission'])
    old_people_obj.append(body['salary'])
    old_people_obj.append(body['years_of_exp'])
    old_people_obj.append(body['location'])
    old_people_obj.append(id)
    old_people_obj = tuple(old_people_obj)
    people.update_row(old_people_obj)

    people = people.search_row(id)
    people_dict = ({'id':people[0], 'name':people[1], 'gender':people[2], 'age':people_dict[3], 'location': people[4]})
    return jsonify(people_dict)

@app.route('/people/<id>',methods=['DELETE'])
def people_delete(id):
    old_people_obj = people.search_row(id)
    if not old_people_obj:
        return jsonify({'message': 'Person not found', 'is_error': 1})
    people.delete_row(id)
    return jsonify({'message': 'Person is deleted', 'is_error': 0})

app.run(debug=True)