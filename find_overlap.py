from courseScraper import getUCMercedCourses

def findCourseOverlap(badgeArray):
    # get the courses for each badge
    courses = [getUCMercedCourses(badge) for badge in badgeArray]

    # find the intersection of the courses
    overlap = set(courses[0]).intersection(*courses[1:])

    overlap = sorted(overlap)

    return overlap

def coursesWithSubject(subject, courseList):
    subject = subject.upper()
    coursesWithSubject = []
    
    for course in courseList:
        if course.split(" ", 1)[0] == subject:
            coursesWithSubject.append(course)
    
    return coursesWithSubject

if __name__ == "__main__":
    print(coursesWithSubject("BIO", findCourseOverlap(["sustainability"])))
