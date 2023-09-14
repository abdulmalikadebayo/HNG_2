# HNG_2

# API Documentation

## Overview

This document provides documentation for the HNG__2 REST API. It outlines the available endpoints, request/response formats, sample usage, limitations, and setup instructions.

## Base URL

The base URL for this API is `https://stage2-cg8i.onrender.com`. Replace it with the actual base URL where your API is hosted.


## Endpoints

### Create a New Person

- **URL:** `/api/`
- **HTTP Method:** `POST`
- **Request Body:**
  ```json
  {
    "name": "Abdul-Malik",
    "email": "abdulmalikadebayo1@gmail.com"
  }
  ```
- **Response:**
  - Status Code: `201 Created`
  - Body:
    ```json
    {
      "id": 1,
     "name": "Abdul-Malik",
     "email": "abdulmalikadebayo1@gmail.com"
    }
    ```

### Fetch Details of a Person

- **URL:** `/api/<user_id>/`
- **HTTP Method:** `GET`
- **Response:**
  - Status Code: `200 OK`
  - Body:
    ```json
    {
      "id": 1,
      "name": "Abdul-Malik",
      "email": "abdulmalikadebayo1@gmail.com"
    }
    ```

### Modify the Details of an Existing Person

- **URL:** `/api/<user_id>/`
- **HTTP Method:** `PUT` or `PATCH`
- **Request Body:**
  ```json
  {
    "name": "Updated Name",
    "email": "updated@example.com"
  }
  ```
- **Response:**
  - Status Code: `200 OK`
  - Body:
    ```json
    {
      "id": 1,
      "name": "Updated Name",
      "email": "updated@example.com"
    }
    ```

### Remove a Person

- **URL:** `/api/<user_id>/`
- **HTTP Method:** `DELETE`
- **Response:**
  - Status Code: `204 No Content`


## Setting Up and Deploying the API

Follow these steps to set up and deploy the API locally or on a server:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/abdulmalikadebayo/HNG_2-repo.git
   cd your-HNG_2-repo
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Migration:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the API:**
   The API will be available at `https://stage2-cg8i.onrender.com`. Replace the base URL with your server's URL if deployed elsewhere.

## Sample Usage

Provide examples of how to use the API using sample requests and expected responses for each endpoint. Use actual requests and responses as demonstrated earlier in this document.

```bash
# Create a new person
curl -X POST -H "Content-Type: application/json" -d '{"name": "adebayo", "email": "adebayo@example.com"}' https://stage2-cg8i.onrender.com/api/

# Fetch details of a person
curl https://stage2-cg8i.onrender.com/api/1/

# Modify the details of an existing person
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name", "email": "updated@example.com"}' https://stage2-cg8i.onrender.com/api/1/

# Remove a person
curl -X DELETE https://stage2-cg8i.onrender.com/api/1/
```

## Conclusion

This document provides essential information for developers and users to interact with and understand the HNG_2 REST API. If you have any questions or encounter issues, please refer to the documentation or contact our support team for assistance.
