# SweetMarketplace

SweetMarketplace is an online marketplace specialized in confectionery products, developed using the Django framework.

## Table of Contents

1. [Description](#1-description)
2. [Screenshots & Video Sweet MarketPlace](#2-Screenshots-&-Video-Sweet-MarketPlace)
3. [Installation Instructions](#3-installation-instructions)
4. [Configuration](#4-configuration)
5. [Usage](#5-usage)


## 1. Description

SweetMarketplace provides an online platform where confectionery enthusiasts can purchase delicious products. Users can browse through categories, add products to their shopping cart, and place orders easily and quickly.


## 2. Screenshots & Video Sweet MarketPlace
![Alt Text](/Users/balanicacristina/Documents/GitHub/1.PythonProjects/sweet_market_place/photo_app/sweet_market_place.png)
- [Watch presentation video](https://youtu.be/WiQzqCyintI)

## 3. Installation Instructions

### 3.1 Prerequisites

Make sure you have the following installed on your system

- Python (versiunea 3.11)
- Django (versiunea 5.0.1)
- [Alte dependențe...]

### 3.2 Download and Installation

Clone this repository to your local machine:

``
git clone https://github.com/BDCristina/Sweets_Market_Place.git``

To install dependencies, run:

``
pip install -r requirements.txt``

### 3.3 Database Configuration

Apply migrations to configure the database:

``
python manage.py migrate ``
## 4. Configuration

### 4.1 Environment Settings
Copy the .env.example file to a new .env file and fill in the required environment variables.

Example of .env:
``
SECRET_KEY=mysecretkey
DEBUG=True
DATABASE_URL=sqlite:///:memory:
[... alte variabile ...] ``

### 4.2 Authentication Settings

Configure authentication settings in settings.py:
``
AUTHENTICATION_BACKENDS = [
    'path.to.CustomAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]``
## 5. Usage

Start the development server using:

``
python manage.py runserver ``

Access the application in a browser at http://localhost:8000.

If you have any questions or need further assistance, feel free to ask!

