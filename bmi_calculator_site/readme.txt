BMI calculator site - README

This project is a web application developed using Flask. Below are the steps required to run the application.

Requirements:
To run this project, you will need the following software:
- Python 3.x (Python 3.6 or later is recommended)

Getting Started:

1. Download the Project
First, download or clone the project to your computer:
git clone <repository_url>

2. Set Up Virtual Environment
Navigate to the project directory and create a virtual environment:
cd bmi_calculator_site
python -m venv venv

3. Activate the Virtual Environment
You need to activate the virtual environment. Use the following commands:

- Windows:
  .\venv\Scripts\activate

- Mac/Linux:
  source venv/bin/activate

4. Install Required Dependencies
After activating the virtual environment, install the required dependencies for the project:
pip install -r requirements.txt

If you don't have a `requirements.txt` file, you can install Flask manually:
pip install flask

5. Run the Flask Application
Start the application by running the `app.py` file:
python app.py

6. View the Application in a Browser
Once the application starts, open the following address in your browser to view the application:
http://127.0.0.1:5000/

7. Project Structure

The project directory is structured as follows:
bmi_calculator_site/
│
├── app.py          # Flask application file
│
├── static/         # Static files like CSS, JavaScript, images, etc.
│   └── style.css   # Homepage style file
│   └── bmi.css     # BMI style file
│
├── templates/      # HTML template files
│   ├── index.html  # Homepage HTML file
│   └── bmi.html    # BMI calculation HTML file
│
└── venv/           # Virtual environment

Contributing to the Project:
If you would like to contribute to this project, follow these steps:

1. Clone this project to your computer.
2. Add new features or fix bugs.
3. Submit your changes as a pull request.