import requests
from bs4 import BeautifulSoup


# function that gets the courses from a url and prints array of courses
def getUCMercedCourses(badgeUrl):
    BASE_URL = "https://ge.ucmerced.edu/intellectual-experience-badges/"
    response = requests.get(BASE_URL + badgeUrl)

    soup = BeautifulSoup(response.text, "lxml")

    courseListItems = (
        soup.find("h2", text="Courses").find_next_sibling("div").find_all("li")
    )

    courses = [course.text for course in courseListItems]
    courses = [course.replace("’", "'") for course in courses]
    courses = [course.replace("“", "'") for course in courses]
    courses = [course.replace("”", "'") for course in courses]

    for i, course in enumerate(courses):
        courses[i] = course.replace("’", "'")
        courses[i] = course.replace("“", "'")
        courses[i] = course.replace("”", "'")
        courses[i] = course[: course.index("Units:")].strip()

    return courses


if __name__ == "__main__":
    getUCMercedCourses("sustainability")
