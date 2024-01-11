import csv

def findCourseOverlap(badgeArray):
    # get the courses for each badge from ucmerced.csv
    courses = []
    with open("ucmerced.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            # skip row if it's a blank row
            if row == []:
                continue
            if row[0] in badgeArray:
                courses.append(row[1].split(", "))

    # print courses fstring format
    print(f"courses: {courses}")

    # remove all the brackets and quotes from courses
    for i in range(len(courses)):
        for j in range(len(courses[i])):
            courses[i][j] = courses[i][j].replace("[", "")
            courses[i][j] = courses[i][j].replace("]", "")
            courses[i][j] = courses[i][j].replace("'", "")

    # find the overlap
    overlap = []
    for courseList in courses:
        for course in courseList:
            # if the course is in every courseList, add it to overlap
            if all(course in courseList for courseList in courses):
                # don't if it's already in overlap
                if course in overlap: continue
                overlap.append(course)

    # remove brackets and quotes
    for i in range(len(overlap)):
        overlap[i] = overlap[i].replace("[", "")
        overlap[i] = overlap[i].replace("]", "")
        overlap[i] = overlap[i].replace("'", "")
    overlap = sorted(overlap)


    # replace "|commaReplacement|" with commas
    overlap = [course.replace("|commaReplacement|", ",") for course in overlap]

    return overlap

if __name__ == "__main__":
    print(findCourseOverlap(["sustainability", "global-awareness"]))