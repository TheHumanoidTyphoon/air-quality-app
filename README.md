# Air Quality App

The Air Quality App is a simple GUI-based application that displays air quality data for a given city. It uses the [World Air Quality Index (AQI)](https://waqi.info/) API to retrieve the air quality data for the selected city.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

To run the Air Quality App, you'll need to have Python 3 installed on your machine. You can download it [here](https://www.python.org/downloads/).

### Installing

1. Clone the repository:

   ```
   $ git clone https://github.com/TheHumanoidTyphoon/air-quality-app.git
   ```

2. Navigate into the project directory:

   ```
   $ cd air-quality-app
   ```

3. Install the required packages:

   ```
   $ pip install -r requirements.txt
   ```

### Usage

1. Run the following command to start the app:

   ```
   $ python airquality_app.py
   ```

2. Enter the name of a city in the "City Name" field and select an air quality measurement option from the dropdown menu.

3. Click the "Lookup A Place" button to retrieve the air quality data for the selected city.

4. The air quality data will be displayed in the label below the button.

## Built With

* [Python](https://www.python.org/) - The programming language used
* [Tkinter](https://docs.python.org/3/library/tkinter.html) - The standard Python interface to the Tk GUI toolkit
* [Pillow](https://pillow.readthedocs.io/en/stable/) - The Python Imaging Library
* [Requests](https://docs.python-requests.org/en/latest/) - The HTTP library for Python

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/TheHumanoidTyphoon/air-quality-app/blob/master/LICENSE) file for details. 
