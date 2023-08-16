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

## API Documentation



**Get authentication token:** To be able to access the API, user needs to get authenticated first. A registered user can obtain the authentication token from the following api-endpoint-
```
 /api/gettoken
```
Note: the user should make a POST request and provide the username and password in JSON format. For example:
```
 {
	 "username":<username>,
	 "password":<password>
 }
```
following successful request, the user will get an authentication token as a response like this-
```
{
	"token":  "c0eafasi4753f717d32a018abchdheua3ed1a2"
}
```
finally, user can consume the API.

### API endpoint:
- **Get All Input Values**

> Parameters: start_datetime, end_datetime, user_id

> Returns: All the Input Values the user ever entered within start_datetime(inclusive) and end_datetime (inclusive)

> Endpoint: 
```
 /api/getinputvalues
```
Example:

POST request:
```
api/getinputvalues?start_datetime=2023-08-16 07:51:06&end_datetime=2023-08-16 07:55:55&user_id=5
```
Response: 
```
{
	"status":  "success",
	"user_id":  "5",
	"payload":  [
		{
		"timestamp":  "2023-08-16T07:55:55Z",
		"input_values":  "110, 99, 77, 64, 45, 35, 23, 11, 8, 5, 2"
		}
	]
}
```
- **Note:** User must include the authorization token in the request header. The header key should be named as "Authorization". See the following example:
```
Authorization: token c0eafasi4753f717d32a018abchdheua3ed1a2
```