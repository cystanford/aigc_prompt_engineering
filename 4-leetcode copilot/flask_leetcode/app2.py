from flask import Flask, jsonify, request
import json
import data_processing
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
conn, cursor = data_processing.get_db_session(db='chatgpt')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://用户名:密码@localhost/chatgpt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/get_problem', methods=['GET'])
def get_problem():
    problem_id = request.args.get('problem_id')
    # Assuming you have a database connection named `db` and problem_info table
    cursor = conn.cursor()
    query = "SELECT detail FROM problem_info WHERE problem_id=%s"
    cursor.execute(query, (problem_id,))
    result = cursor.fetchone()
    if not result:
        return jsonify({'error': 'Problem not found'}), 404
    problem_detail = result[0]
    #return jsonify({'problem_id': problem_id, 'detail': json.loads(problem_detail)})
    return jsonify({'problem_id': problem_id, 'detail': problem_detail})

class Problem(db.Model):
    __tablename__ = 'problem_list'
    problem_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    acceptance = db.Column(db.String(10), nullable=False)

@app.route('/get_problem_list', methods=['GET'])
def get_problem_list():
    problems = Problem.query.all()
    problem_list = []
    for problem in problems:
        problem_dict = {
            'id': problem.problem_id,
            'title': problem.title,
            'difficulty': problem.difficulty,
            'acceptance': problem.acceptance
        }
        problem_list.append(problem_dict)
    return jsonify({'problem_list': problem_list})

if __name__ == '__main__':
    app.run(debug=True)
