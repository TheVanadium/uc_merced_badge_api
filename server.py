from flask import Flask, request
from find_overlap import findCourseOverlap


app = Flask(__name__)

# badges is the only query string allowed
@app.route('/courses')

def get_courses():
    # get badges from query string
    badges = request.args.get('badges')
    badges = badges.split(',')

    return findCourseOverlap([badge for badge in badges])


if __name__ == '__main__':
    app.run(debug=True)
