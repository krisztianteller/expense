Harvard's CS50 Web Programming with Python and Javascript 2020<br>
Brian Yu
brian@cs.harvard.edu<br>
David J. Malan
malan@harvard.edu

---

## **_Capstone project by Krisztian Teller_**

Project Name: Capstone Expenses<br>
Project Completed on: 28/7/2021<br>

[GitHub](https://github.com/krisztianteller) <br>
[Video Demonstration of App](https://youtu.be/rUpbSuqpFT0) <br>
Email: krisztian.teller@gmail.com

### **About:**

The project I chose for the capstone project is tracking your expenses that allows users to log in and taking care about his expense. Users can create new Expenses or add Income and see his Summary.

### **Project distinctiveness and complexities:**

The project is distinct in many aspects. One of which is the real time adding, an upgraded web protocol. **Django Channels** package was used to make this possible. Django allows for a steady connection to be opened between the server and client to send and receive data without the need for HTTP requests.I believe the chat feature alone should satisfy the distinctiveness and complexity requirements.

The project's frontend is built using **Django** library and not Django's html templates. **Bootstrap** CSS library was also integrated to assist with styling.

Since the project departed from using Django's html templating, we needed an alternative solution for authentication, authorization, and CORS (Cross Origin Resource Sharing) that Django natively handled. Default authentication and authorization settings were switched to **Django REST framework** and **Django REST framework JWT** (Json Web Token) packages, a departure from the standard CSRF tokens. **CORS Headers** was used to take care of CORS error.

### **Why:**

CS50's projects were challenging to say the least.  I truly appreciate the spirit of pushing students to problem solve, instead of hand holding. This course has done more to help me as a developer because I was thrown into the deep end forced me to understand programming at a fundamental level.  I had no exposure to Python when I began the course, let alone the Django framework. I needed to learn a new language, a new framework, how databases worked, websockets, authentication.. etc. In essense, the reason for this project selection was to remain in a state of growth and discomfort.

### **Files:**

The following is the file structure of the project where I added or modified. Default project files are ommitted.

```
/ (folder)
-- (files)

├── Pipfile.lock
├── README.md
└── capstone
    ├── Pipfile
    ├── Pipfile.lock
    ├── Procfile
    ├── authentication
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-39.pyc
    │   │   ├── urls.cpython-39.pyc
    │   │   ├── utils.cpython-39.pyc
    │   │   └── views.cpython-39.pyc
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── utils.py
    │   └── views.py
    ├── currencies.json
    ├── db.sqlite3
    ├── expenses
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-39.pyc
    │   │   ├── admin.cpython-39.pyc
    │   │   ├── apps.cpython-39.pyc
    │   │   ├── models.cpython-39.pyc
    │   │   ├── urls.cpython-39.pyc
    │   │   └── views.cpython-39.pyc
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── 0001_initial.cpython-39.pyc
    │   │       └── __init__.cpython-39.pyc
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── expenseswebsite
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-39.pyc
    │   │   ├── settings.cpython-39.pyc
    │   │   ├── urls.cpython-39.pyc
    │   │   └── wsgi.cpython-39.pyc
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── static
    │   │   ├── css
    │   │   │   ├── adminstyle.css
    │   │   │   ├── bootstrap.min.css
    │   │   │   ├── dashboard.css
    │   │   │   └── main.css
    │   │   ├── img
    │   │   │   └── pngwing.com.png
    │   │   └── js
    │   │       ├── register.js
    │   │       ├── searchExpenses.js
    │   │       ├── searchIncome.js
    │   │       └── stats.js
    │   ├── urls.py
    │   └── wsgi.py
    ├── income
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-39.pyc
    │   │   ├── admin.cpython-39.pyc
    │   │   ├── apps.cpython-39.pyc
    │   │   ├── models.cpython-39.pyc
    │   │   ├── urls.cpython-39.pyc
    │   │   └── views.cpython-39.pyc
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── 0001_initial.cpython-39.pyc
    │   │       └── __init__.cpython-39.pyc
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    ├── requirements.txt
    ├── settings.py
    ├── templates
    │   ├── admin
    │   │   └── base_site.html
    │   ├── authentication
    │   │   ├── login.html
    │   │   ├── register.html
    │   │   ├── reset_password.html
    │   │   └── set-newpassword.html
    │   ├── base.html
    │   ├── base_auth.html
    │   ├── expenses
    │   │   ├── add_expense.html
    │   │   ├── edit-expense.html
    │   │   ├── index.html
    │   │   ├── pdf.html
    │   │   └── stats.html
    │   ├── income
    │   │   ├── add_income.html
    │   │   ├── edit_income.html
    │   │   └── index.html
    │   ├── partials
    │   │   ├── _messages.html
    │   │   └── _sidebar.html
    │   └── preferences
    │       └── index.html
    └── userpreferences
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-39.pyc
        │   ├── admin.cpython-39.pyc
        │   ├── apps.cpython-39.pyc
        │   ├── models.cpython-39.pyc
        │   ├── urls.cpython-39.pyc
        │   └── views.cpython-39.pyc
        ├── admin.py
        ├── apps.py
        ├── migrations
        │   ├── 0001_initial.py
        │   ├── __init__.py
        │   └── __pycache__
        │       ├── 0001_initial.cpython-39.pyc
        │       └── __init__.cpython-39.pyc
        ├── models.py
        ├── tests.py
        ├── urls.py
        └── views.py


```

---

<br>

### **How to run application:**

The project has separate frontend and backend so they need to be launched separately. <br><br>
**Django server and backend setup**

1. Navigate to the project folder /capstone.

```

```

2. Install all required packages.

```
```

3. Initialize the database with makemigrations, migrate.

```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
4. Launch the Django server. If set up correctly, server will launch on http://127.0.0.1:8000/.

```
py manage.py runserver
```


5. Login

    username: super
    pwd: 123
