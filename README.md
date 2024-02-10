# QR Code Maker
[![userinfobot](https://img.shields.io/badge/Requirements-See%20Here-green)](https://github.com/matinazhir/qr-maker/blob/master/requirements.txt)


Really simple app to create QR codes easily with one click.

Put the text that you want to convert into a QR into the field and click on "create" button, tadaaa!

You get your QR code instantly in the app and you can scan it with a scanner or phone or whatever.


![QR-Maker Screenshot](https://imgur.com/BNdYej4.png "Screenshot of QR-Maker App")


# How to Run

1. Install python3, pip3, virtualenv, in your system.
2. Clone the project ```git clone https://github.com/matinazhir/qr-maker.git && cd qr-maker```.
3. In the project folder create a virtual environment using:
4. 
on Linux ```python3 -m venv .YourEnvName```,

on Windows ```python -m venv .YourEnvName```

and ```virtualenv .YourEnvName```.
5. Connect to your virtual environment using:

on Linux ```source .YourEnvName/bin/activate```,

on Windows ```.YourEnvName\Scripts\Activate```.
6. From the project folder, install packages using ```pip install -r requirements.txt```.
7. Now environment is ready. Run it by ```python app/main.py```.
