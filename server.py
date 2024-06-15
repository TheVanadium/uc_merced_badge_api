from flask import Flask, request
from find_overlap import findCourseOverlap
from intervalUpdate import intervalUpdate
from multiprocessing import Process

app = Flask(__name__)

@app.route('/courses')

def get_courses():
    badges = request.args.get('badges')
    badges = badges.split(',')

    formattedList = "["
    formattedListCall = sorted(findCourseOverlap([badge for badge in badges]))
    for course in formattedListCall:
        if "\"" in course:
            course = course.replace("\"", "")

    for course in formattedListCall:
        formattedList += "\"" + course + "\", "

    if formattedList == "[": return "[]"

    # remove last comma and space
    formattedList = formattedList[:-2]
    formattedList += "]"
    return formattedList

@app.route('/update-date')
def get_update_date():
    with open("lastScraped.txt") as f:
        updateDate = f.read()
    return updateDate

if __name__ == '__main__':
    p = Process(target=intervalUpdate)
    p.start()
    app.run(debug=True)
