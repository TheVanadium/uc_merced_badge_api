from flask import Flask, request
from find_overlap import findCourseOverlap, coursesWithSubject

badgeList = [
  "Ethics",
  "Diversity and Identity",
  "Global Awareness",
  "Literary and Textual Analysis", 
  "Media and Visual Analysis", 
  "Scientific Method", 
  "Societies and Cultures of the Past",
  "Sustainability",
]

# lower case all the badges, replace spaces with - and remove "the" and "of"
for i in range(len(badgeList)):
    badgeList[i] = badgeList[i].lower().replace(" ", "-").replace("the-", "").replace("of-", "")


app = Flask(__name__)

# badges is the only query string allowed
@app.route('/courses')

def get_courses():
    badges = badgeList.copy() # default to all badges
    
    if request.args.get('badges'):
        badges = request.args.get('badges')
        badges = badges.split(',')

    if request.args.get('subject') and request.args.get('badges'):
        courseList = []
        for badge in badges:
            courseList.append(findCourseOverlap([badge]))
        courseList = list(dict.fromkeys(courseList))
        return coursesWithSubject(request.args.get('subject'), courseList)

    return findCourseOverlap([badge for badge in badges])


if __name__ == '__main__':
    app.run(debug=True)
