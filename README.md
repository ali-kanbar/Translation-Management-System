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

### Adding a New Translation


![Screenshot 2024-07-23 190303](https://github.com/user-attachments/assets/17515895-4b5b-43b9-a5aa-66db6909bea1)
![Screenshot 2024-07-23 190354](https://github.com/user-attachments/assets/e633f6b7-af3b-48a9-bac2-1a10cc67547b)


### Translating a Word

- **Input**: Word: "hello"
- **Output**: "Translation: hola"

### Updating a Translation

- **Input**: Word: "hello", Updated Translation: "bonjour"
- **Output**: "Translation updated successfully"

### Deleting a Word

- **Input**: Word: "hello"
- **Output**: "Word deleted successfully"

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


  
