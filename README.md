# Translation Management System (TMS)

## Project Overview

The Translation Management System (TMS) is a web application built using Flask and SQLAlchemy that allows users to manage translations of words.
Users can add new words with their translations, look up translations of existing words, update translations, and delete words.
This project serves as a basic example of a CRUD (Create, Read, Update, Delete) application using Python and SQLite.

## Features

- **Add New Translations**: Users can add a new word and its translation to the database.
- **Translate Words**: Users can look up the translation of a word.
- **Update Translations**: Users can update the translation of an existing word.
- **Delete Words**: Users can delete a word and its translation from the database.
- **Session Management**: Uses Flask session to handle temporary data and ensure a smooth user experience.

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/tms.git
    cd tms
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set environment variables:**

    On Linux/macOS:

    ```bash
    export SECRET_KEY="8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
    export SQLALCHEMY_DATABASE_URI="sqlite:///Translation_Database.db"
    ```

    On Windows:

    ```powershell
    setx SECRET_KEY "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
    setx SQLALCHEMY_DATABASE_URI "sqlite:///Translation_Database.db"
    ```

5. **Run the application:**

    ```bash
    flask run
    ```

6. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. **Home Page**: Redirects to the main home page.
2. **Add Translation**: Navigate to `/add` to add a new word and its translation.
3. **Translate Word**: Navigate to `/translate` to look up the translation of a word.
4. **Update Translation**: Navigate to `/update` to update an existing word's translation.
5. **Delete Word**: Navigate to `/delete` to delete a word and its translation from the database.

## Example Inputs/Outputs

### Add Translation

#### Adding a New Translation to the Database

![Screenshot 2024-07-23 190303](https://github.com/user-attachments/assets/17515895-4b5b-43b9-a5aa-66db6909bea1) 
![Screenshot 2024-07-23 190354](https://github.com/user-attachments/assets/e633f6b7-af3b-48a9-bac2-1a10cc67547b)


#### Trying to add a word that already exists in the DataBase

![Screenshot 2024-07-23 190424](https://github.com/user-attachments/assets/793b6e8f-8b64-4d08-8f97-b7a905d90beb)
![Screenshot 2024-07-23 190433](https://github.com/user-attachments/assets/d6d95a33-ea72-4278-9664-96f72078628f)


#### Leaving one or both input fields empty

![Screenshot 2024-07-23 191512](https://github.com/user-attachments/assets/b9521670-ff07-4ccc-b80d-d6a2330ca8e5)
![Screenshot 2024-07-23 191520](https://github.com/user-attachments/assets/96aa933d-abfd-4eaa-8491-48f6059c5671)


#### What our DataBase looks like after adding some words and their translations

![image](https://github.com/user-attachments/assets/a621157f-e3ea-43d9-83a6-132b8e3cb056)


### Translating a Word

#### Translating a word that exists in the DataBase

![image](https://github.com/user-attachments/assets/f878d5ce-f34d-4cb4-bf60-433294f9432b)
![image](https://github.com/user-attachments/assets/1450fd19-9160-448b-88fb-4ff23c604034)

#### Trying to Translate a word that doesn't exists in the DataBase

![Screenshot 2024-07-23 191935](https://github.com/user-attachments/assets/be58b5fd-80ed-4220-8937-e24300ae954b)
![Screenshot 2024-07-23 191923](https://github.com/user-attachments/assets/8bbc7545-ea65-4234-a40a-f15d27510366)


#### Leaving the Word Field empty

![image](https://github.com/user-attachments/assets/c0917589-8210-460f-99a9-943feb9f0479)


### Updating a Translation

#### Updating the Translation of a word that exists inside the Database

![Screenshot 2024-07-23 192147](https://github.com/user-attachments/assets/a07a3b3a-fd73-4294-8846-d220409eec95)
![Screenshot 2024-07-23 192154](https://github.com/user-attachments/assets/2763c3f6-1e5b-462c-b919-5116c120f74d)


#### Trying to Update the Translation of a word that exists inside the Database

![Screenshot 2024-07-23 192324](https://github.com/user-attachments/assets/44ef4401-e056-425f-b317-82df88517906)
![Screenshot 2024-07-23 192335](https://github.com/user-attachments/assets/7ed71ffa-e662-4d4d-86b0-2e225ea42269)


#### Leaving one or both input fields empty

![Screenshot 2024-07-23 192435](https://github.com/user-attachments/assets/913512b2-ddb5-4218-aa67-96677b2f7fde)


#### What our DataBase looks like after adding some words and their translations

![Screenshot 2024-07-23 192618](https://github.com/user-attachments/assets/ada61d99-87b9-444d-8e91-6bf120350920)


### Deleting a Word

#### Deleting a word that exists in the DataBase

![image](https://github.com/user-attachments/assets/20890d9b-50f5-4eb4-8466-52a31f5e9810)
![image](https://github.com/user-attachments/assets/1d959f41-8883-4b65-8357-e17d32ccea9d)


#### Trying to delete a word that doesn't exists in the DataBase

![image](https://github.com/user-attachments/assets/f1e8e079-6b47-4e83-bf76-0cb3a080c636)
![image](https://github.com/user-attachments/assets/27a0ef09-d314-467f-82af-365579e8b5a8)


#### Leaving the word field empty

![image](https://github.com/user-attachments/assets/cbb76b62-547b-461c-9f7c-ee1aeec9bc9c)


#### What our DataBase looks like after adding some words and their translations

![image](https://github.com/user-attachments/assets/4ca9e1a3-38e0-490b-9b9b-d32b343ae7c3)


## Approach and Assumptions

### Approach

- The project follows a CRUD approach using Flask as the web framework and SQLAlchemy as the ORM.
- Flask session management is used to handle temporary data between requests.
- Environment variables are used to securely store sensitive information.

### Assumptions

- The application is designed for single-user usage without authentication.
- SQLite is used as the database for simplicity and ease of setup.
- The application runs on a local server for development and testing purposes.

## Technologies Used

- **Python**: The core programming language used.
- **Flask**: A lightweight WSGI web application framework.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **SQLite**: A lightweight disk-based database.
- **Flask-Session**: For session management in Flask.
- **HTML**: Used to structure the web pages.
- **CSS**: Used to style the web pages
- **Jinja2**: A templating engine for Python used with Flask to render dynamic web pages.


  
