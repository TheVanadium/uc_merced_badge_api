# UC Merced Badge API
An API that gives you UC Merced courses with user-specified badges.

## Installation
The required packages are `flask` and `bs4`.

## Usage
This project is yet to be hosted. To run it locally, install and run `python server.py` in the project directory. Using a browser, go to the local computer IP at the port it's running on (in the case below, it's port 5000).

![image](https://user-images.githubusercontent.com/53013571/211162475-fa27a16f-a68d-477c-baf8-b3f2414e6add.png)

The page you go to should be blank. The main usage is in the querying. The API is accessed via `/courses?badges=""` where the badges string is a comma-seperated list (no spaces) of badges.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
