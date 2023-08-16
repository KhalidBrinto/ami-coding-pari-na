# Ami Coding Pari Na - Django APP

Ami Coding Pari Na is a powerful and user-friendly web application built on the Django framework, designed to provide seamless user experiences across multiple sections. The application features three main sections:

**Section 1: User Authentication and Registration**

The User Authentication and Registration section ensures a secure and personalized experience for users. It offers a straightforward and standardized login and registration process, allowing users to create accounts and log in securely. The application employs token-based authentication for enhanced security.

**Section 2: Khoj the Search - An Intelligent Search**

This intelligent search section allows logged-in users to perform efficient searches using comma-separated integers. The application stores these input values in a sorted descending order, along with the user ID and timestamp, creating a historical record of searches. Users can instantly check if a search value exists within their input history, receiving real-time feedback on their queries.

**Section 3: API Access for Input History**

The API Access section offers a powerful API endpoint that provides users with access to their input history. Users can specify date ranges and user IDs to retrieve a comprehensive list of input values they've previously entered within the defined timeframe. The API employs token-based authentication to ensure data privacy and security.


## Installation


- Clone this repository:

```
git clone https://github.com/KhalidBrinto/ami-coding-pari-na.git
cd ./ami-coding-pari-na/
```

- Install Django and other dependencies from requirements:

```
$ pip install -r requirements.txt
```

- Install Docker 

## Run the Application

Open terminal in the cloned directory and run the command:

```
python manage.py runserver
```

This should start and run the application in local server.

If you wish to containerize the application with Docker, create a docker image and run the 'Dockerfile' in this directory.




