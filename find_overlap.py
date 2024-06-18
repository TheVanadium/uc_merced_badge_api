import csv


def findCourseOverlap(badgeArray):
    courses = []
    with open("ucmerced.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row == []:
                continue
            if row[0] in badgeArray:
                courses.append(row[1].split(", "))

    for i in range(len(courses)):
        for j in range(len(courses[i])):
            courses[i][j] = courses[i][j].replace("[", "")
            courses[i][j] = courses[i][j].replace("]", "")
            courses[i][j] = courses[i][j].replace("'", "")

    overlap = []
    for courseList in courses:
        for course in courseList:
            if all(course in courseList for courseList in courses):
                if course in overlap:
                    continue
                overlap.append(course)

    for i in range(len(overlap)):
        overlap[i] = overlap[i].replace("[", "")
        overlap[i] = overlap[i].replace("]", "")
        overlap[i] = overlap[i].replace("'", "")
    overlap = sorted(overlap)

    overlap = [course.replace("|commaReplacement|", ",") for course in overlap]

    return overlap


if __name__ == "__main__":
    print(findCourseOverlap(["sustainability", "global-awareness"]))
