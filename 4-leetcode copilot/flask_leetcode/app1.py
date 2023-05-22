from flask import Flask, jsonify, request
import json
import data_processing

app = Flask(__name__)
db, cursor = data_processing.get_db_session(db='chatgpt')

@app.route('/get_problem', methods=['GET'])
def get_problem():
    problem_id = request.args.get('problem_id')
    # Assuming you have a database connection named `db` and problem_info table
    cursor = db.cursor()
    query = "SELECT detail FROM problem_info WHERE problem_id=%s"
    cursor.execute(query, (problem_id,))
    result = cursor.fetchone()
    if not result:
        return jsonify({'error': 'Problem not found'}), 404
    problem_detail = result[0]
    #return jsonify({'problem_id': problem_id, 'detail': json.loads(problem_detail)})
    return jsonify({'problem_id': problem_id, 'detail': problem_detail})

if __name__ == '__main__':
    app.run(debug=True)
