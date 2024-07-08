/gym
    /app
        __init__.py                 # Initializes your application and brings together all components
        /models
            __init__.py             # Makes models a Python package
            models.py               # Contains all SQLAlchemy models
        /routes
            __init__.py             # Registers all Blueprints
            views.py                # Contains routes for general views
            user_routes.py          # Routes specific to user operations
            program_routes.py       # Routes specific to program operations
        /services
            __init__.py             # Makes services a Python package, could also import all services for easy access
            data_access.py          # General database access functions that don't fit into other services
            exercise_service.py     # Services related to exercise operations
            program_service.py      # Services related to program operations
        /static
            /css
            /js
            /images
        /templates
        
            layout.html             # Base layout for my templates
            home.html              # Home page template
            all_exercises.html
            register.html
        /utilities
            __init__.py             # Makes utilities a Python package
            helpers.py              # Utility functions to assist across the application
            validation_helpers.py   # Specific helper functions for validating data
    /instance
        config.py                   # Contains configuration variables that shouldn't be in version control
    /tests
        __init__.py                 # Makes tests a Python package
        test_basic.py               # Basic unit tests for your application
    requirements.txt               # Python requirements modules
    run.py                         # Entry point to start your Flask application
