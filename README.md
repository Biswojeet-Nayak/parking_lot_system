```markdown
# Django Parking System

A simple parking system built with Django and Django Rest Framework (DRF). This project allows you to manage vehicles in a parking lot, including their registration, parking slot assignment, and more via a REST API and user-friendly HTML pages.

## Features

- **Vehicle Registration**: Register vehicles with details such as vehicle number, type, and parking slot.
- **Parking Slot Assignment**: Automatically assigns parking slots to vehicles as they are added.
- **API**: Full CRUD operations for vehicle management via a RESTful API.
- **Admin Interface**: Manage vehicles through the Django Admin interface.

## Technologies Used

- **Django**: Web framework for building the application.
- **Django Rest Framework (DRF)**: For creating the API to manage vehicles.
- **HTML/CSS**: For creating user-friendly pages to add and update vehicle details.
- **SQLite**: Default database (can be switched to other databases if needed).

## Installation

### Prerequisites

- Python 3.12
- Django 5.1.5
- Django Rest Framework

   ```
Steps to Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/django-parking-system.git
   cd django-parking-system
   ```
   
2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser for the Django Admin**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

   Your project will be running at `http://127.0.0.1:8000/`.

## Usage

### Admin Interface

- Visit `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created.
- You will be able to manage the vehicles in the parking system.

### Web Pages

- **Home Page**: `http://127.0.0.1:8000/`
  - Displays the parking system's home page.
- **Add Vehicle**: `http://127.0.0.1:8000/add/`
  - A form to add a new vehicle to the system.
- **Update Vehicle**: `http://127.0.0.1:8000/update/<vehicle_id>/`
  - A form to update an existing vehicle's details (replace `<vehicle_id>` with the actual vehicle's ID).
