# Gym Project

## Project Description
-------------------
This project is a comprehensive web application designed for managing gym activities. Built with Flask, it handles user registration, program management, and exercise tracking. The application employs SQLAlchemy for database interactions and organizes its functionality through well-defined services and routes.

## Project Structure


- `app`
    __init__.py                 # Initializes the application and brings together all components
    __pycache__                 # Cache files generated by Python
  - `models`
        __init__.py             # Makes models a Python package
        __pycache__             # Cache files for models
        models.py               # Contains all SQLAlchemy models
    routes
        __pycache__             # Cache files for routes
        program_routes.py       # Routes specific to program operations
        user_routes.py          # Routes specific to user operations
        views.py                # Contains routes for general views
    services
        __pycache__             # Cache files for services
        data_access.cpython-311.pyc    # Compiled bytecode for data access
        data_access.cpython-312.pyc    # Compiled bytecode for data access
        data_population.cpython-312.pyc # Compiled bytecode for data population
        exercise_service.cpython-311.pyc # Compiled bytecode for exercise service
        exercise_service.cpython-312.pyc # Compiled bytecode for exercise service
        user_service.cpython-311.pyc    # Compiled bytecode for user service
        user_service.cpython-312.pyc    # Compiled bytecode for user service
        data_access.py          # General database access functions that don't fit into other services
        data_population.py      # Script for populating the database with initial data
        exercise_service.py     # Services related to exercise operations
        program_service.py      # Services related to program operations
        trainer_service.py      # Services related to trainer operations
        user_service.py         # Services related to user operations
        weight_service.py       # Services related to weight tracking
        workon_service.py       # Services related to workout operations
    static
        css                     # CSS files for styling
        images                  # Image files used in the application
        js                      # JavaScript files for front-end functionality
    templates
        all_exercises.html      # Template for displaying all exercises
        all_trainers.html       # Template for displaying all trainers
        change_trainer.html     # Template for changing trainer information
        home.html               # Home page template
        login.html              # User login template
        manager_dashboard.html  # Dashboard for managers
        messages.html           # Messages template
        presence.html           # Template for tracking presence
        profile.html            # User profile template
        register.html           # User registration template
        training_program.html   # Training program template
        user_dashboard.html     # Dashboard for users
        users.html              # Template for displaying users

instance
    config.py                   # Contains configuration variables that shouldn't be in version control
tests
    __init__.py                 # Makes tests a Python package
    test_basic.py               # Basic unit tests for the application
requirements.txt                # Python requirements modules
run.py                          # Entry point to start the Flask application 
