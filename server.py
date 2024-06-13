from flask import Flask, request
from find_overlap import findCourseOverlap
from intervalUpdate import intervalUpdate
from multiprocessing import Process

app = Flask(__name__)

# badges is the only query string allowed
@app.route('/courses')

def get_courses():
    # get badges from query string
    badges = request.args.get('badges')
    badges = badges.split(',')

    # return findCourseOverlap([badge for badge in badges])
    # return every course in findCourseOverlap, starting with [, and ending with ], double quotes, commas separated
    # return str(findCourseOverlap([badge for badge in badges])) doesn't work because it gives single quotes
    formattedList = "["
    formattedListCall = sorted(findCourseOverlap([badge for badge in badges]))
    for course in formattedListCall:
        # if the course has double quotes, remove them
        if "\"" in course:
            course = course.replace("\"", "")

    # now that the course is formatted, add it to the formattedList
    for course in formattedListCall:
        formattedList += "\"" + course + "\", "

    if formattedList == "[": return "[]"

    # remove last comma and space
    formattedList = formattedList[:-2]
    formattedList += "]"
    return formattedList

@app.route('/update-date')
def get_update_date():
    # get the update date from the file lastScraped.txt
    # example date format 2023-08-30 16:02:55.051360
    with open("lastScraped.txt") as f:
        updateDate = f.read()
    return updateDate

if __name__ == '__main__':
    p = Process(target=intervalUpdate)
    p.start()
    app.run(debug=True)

# Path: find_overlap.py
