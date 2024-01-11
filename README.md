# UC Merced Badge API
An API that gives you UC Merced courses with user-specified badges.

## Installation
The required packages are `flask` and `bs4`.

## Usage
To run the API, run `python server.py` in the root directory. This should execute intervalUpdate() which will update the database every 10 minutes. The database consists of 2 files: 
- `ucmerced.csv` which contains all the badges and the courses that have them
- `lastUpdate.txt` which contains the date the database was last updated

The main page of the opened flask app from the server should be blank; the main usage is in the querying. There are 2 valid API queries:
- `/courses?badges=""` where the badges string is a comma-seperated list (no spaces) of badges. For example, `/courses?badges=diversity-and-identity,ethics` will return all courses that have both the "Diversity and Identity" and "Ethics" badges (see the BADGES variable in intervalUpdate.py for a list of valid badges). Returns a list of courses in JSON format with all badges listed.
- `/update-date` returns the date the database was last updated, in the format `YYYY-MM-DD hh:mm:ss.ffffff`.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
