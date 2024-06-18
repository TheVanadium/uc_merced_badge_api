# scrape the website every 10 minutes, write the data to a csv file
import csv
import time
import datetime
from courseScraper import getUCMercedCourses

BADGES: set[str] = [
    "diversity-and-identity",
    "ethics",
    "global-awareness",
    "literary-and-textual-analysis",
    "media-and-visual-analysis",
    "scientific-method",
    "societies-and-cultures-past",
    "sustainability",
]


# function that runs getUCMercedCourses and writes the data to a csv file
def writeUCMercedCourses():
    with open("ucmerced.csv", "w") as f:
        writer = csv.writer(f)
        # header
        writer.writerow(["badge", "courses"])
        for badge in BADGES:
            courses = getUCMercedCourses(badge)
            # replace all commas in the course names with "|commaReplacement|"
            # so that the csv file doesn't get messed up
            courses = [course.replace(",", "|commaReplacement|") for course in courses]
            writer.writerow([badge, courses])


def writeLastScraped():
    with open("lastScraped.txt", "w") as f:
        f.write(str(datetime.datetime.now()))


# function to run every 10 minutes
def intervalUpdate():
    while True:
        writeUCMercedCourses()
        print("Scraped at", datetime.datetime.now())
        writeLastScraped()
        print("Wrote to file at", datetime.datetime.now())
        # scrape every 10 minutes
        time.sleep(6000)


if __name__ == "__main__":
    intervalUpdate()
