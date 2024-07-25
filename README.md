# Simple E-commerce API

This project is a simple e-commerce API built using Django Rest Framework. It includes user authentication with JWT, CRUD operations for products and categories, product search functionality, and storing and retrieving recent search history.

## Features

- User Registration and Login with JWT Authentication
- Category Management: Create, Retrieve, Update, and Delete Categories
- Product Management: Create, Retrieve, Update, and Delete Products
- Search Products by Name
- Store and Retrieve User's Recent Search History
- User Logout by Blacklisting JWT Refresh Tokens

## Requirements

- Python 3.11.9+
- Django 4.2.6+
- Django Rest Framework
- djangorestframework-simplejwt

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/simple-e-commerce-api.git
    cd simple-e-commerce-api
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the database migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```sh
    python manage.py runserver
    ```

## API Endpoints

### User Authentication

- **Register**: `POST /api/register/`
- **Login**: `POST /api/login/`
- **Token Refresh**: `POST /api/token/refresh/`
- **Logout**: `POST /api/logout/`

### Categories

- **List and Create Categories**: `GET/POST /api/categories/`
- **Retrieve, Update, and Delete Category**: `GET/PUT/DELETE /api/categories/<int:pk>/`

### Products

- **List and Create Products**: `GET/POST /api/products/`
- **Retrieve, Update, and Delete Product**: `GET/PUT/DELETE /api/products/<int:pk>/`
- **Search Products**: `GET /api/products/search/?query=<search_term>`

### Search History

- **List User's Search History**: `GET /api/search-history/`

## Testing the API

You can use tools like Postman or curl to test the API endpoints.

### Example: Register a User

```sh
curl -X POST "http://localhost:8000/api/register/" -H "Content-Type: application/json" -d '{
  "username": "testuser",
  "password": "testpassword"
}'
