# SimpleBlog-API
SimpleBlog API is a RESTful API built with Django and Django REST framework (DRF) that provides endpoints for managing a simple blogging application. The API includes token-based authentication for secure access to protected endpoints, as well as signup and signin functionality for user authentication. The API is also documented using Swagger and ReDoc for easy API exploration and testing.

## Live site
The live site is deployed at: https://danieladewole.pythonanywhere.com/

## Documentation
+ Swagger: The Swagger documentation can be accessed at https://danieladewole.pythonanywhere.com. This provides a comprehensive and interactive documentation for the API endpoints, including request and response formats.

+ The ReDoc documentation can be accessed at https://danieladewole.pythonanywhere.com/redoc/. This provides an alternative documentation view with a clean and user-friendly UI for exploring the API endpoints.


## Features
+ Token-based authentication for secure access to protected endpoints
+ User signup and signin functionality for user authentication
+ CRUD (Create, Read, Update, Delete) operations for managing blog posts
+ API endpoints for managing blog posts, including listing, creating, retrieving, updating, and deleting posts
+ Swagger and ReDoc documentation for easy API exploration and testing

## Installation
1. Clone the repository to your local machine
```
git clone https://github.com/DanAdewole/SimpleBlog-API.git
```

2. Change to the project directory
```
cd SimpleBlog-API
```

3. Create and activate a virtual environment (optional, but recommended)
```
python3 -m venv venv
source venv/bin/activate
```

4. Install the dependencies
```
pip install -r requirements.txt
```

5. Set up the database
```
python manage.py migrate
```
6. Create a superuser (optional, for accessing the domain site):
```
python manage.py createsuperuser
```

7. Start the development server
```
python manage.py runserver
```

## Usage
### Authentication
The API uses token-based authentication for secure access to protected endpoints. To authenticate, you can use the provided signup and signin endpoints to create a new user account or obtain a token for an existing user, respectively. Include the token in the Authorization header of your requests to protected endpoints, with the format: Bearer <TOKEN>. For example:
```
Authorization: Bearer <TOKEN>
```

### Endpoints
The API provides the following endpoints for managing blog posts:
+ **GET /posts/**: Retrieve a list of all blog posts
+ **POST /posts/**: Create a new blog post
+ **GET /posts/{id}/**: Retrieve a single blog post by ID
+ **PUT /posts/{id}/**: Update a blog post by ID
+ **DELETE /posts/{id}/**: Delete a blog post by ID

For detailed documentation on the API endpoints, including request and response formats, you can access the Swagger documentation at: http://127.0.0.1:8000 or the ReDoc documentation at: http://127.0.0.1:8000/redoc/


## Contributing
Contributions to the Simple Blog API project are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on GitHub.

## License
This project is licensed under the [MIT LICENSE](LICENSE)

