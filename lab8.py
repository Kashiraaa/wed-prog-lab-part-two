from flask import Blueprint, render_template, request, abort, jsonify
from datetime import datetime

lab8 = Blueprint('lab8',__name__)


@lab8.route('/lab8/')
def main():
    return render_template('lab8/index.html')

courses = [
    {"name": "c++", "videos": 3, "price": 3000, "created_date": datetime.now()},
    {"name": "basic", "videos": 30, "price": 450, "created_date": datetime.now()},
    {"name": "c#", "videos": 8, "created_date": datetime.now()}
]


@lab8.route('/lab8/api/courses/', methods=['GET']) 
def get_courses():
    return jsonify(courses)


@lab8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_course(course_num):
    if course_num < 0 or course_num >= len(courses):
        abort(404)  
    return courses[course_num]

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['DELETE'])
def del_course(course_num):
    if course_num < 0 or course_num >= len(courses):
        abort(404)  
    del courses[course_num]
    return '', 204