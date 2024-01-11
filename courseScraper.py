import requests
from bs4 import BeautifulSoup

# function that gets the courses from a url and prints array of courses
def getUCMercedCourses(badgeUrl):
    BASE_URL = "https://ge.ucmerced.edu/intellectual-experience-badges/"
    response = requests.get(BASE_URL + badgeUrl)

    soup = BeautifulSoup(response.text, "lxml")

    # course list items are in h2 Courses's next sibling div
    print(badgeUrl)

    courseListItems = soup.find("h2", text="Courses").find_next_sibling("div").find_all("li")

    # get the text of each course and remove the "Units: " + unit number ... part
    courses = [course.text for course in courseListItems]
    courses = [course.replace("’", "'") for course in courses]
    courses = [course.replace("“", "'") for course in courses]
    courses = [course.replace("”", "'") for course in courses]

    for i, course in enumerate(courses):
        courses[i] = course.replace("’", "'")
        courses[i] = course.replace("“", "'")
        courses[i] = course.replace("”", "'")
        courses[i] = course[:course.index("Units:")].strip()

    return courses

if __name__ == "__main__":
    getUCMercedCourses("sustainability")