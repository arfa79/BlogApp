# BlogApp

This is a Dockerized Django application for managing blog posts, integrating Celery for asynchronous task execution, and utilizing Django Ninja for API development.

## Table of Contents
- [Project Purpose](#project-purpose)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Purpose

BlogApp aims to provide a platform for viewing, creating, and updating blog posts. It utilizes Django and Celery to handle backend logic, Django Ninja for API development, and integrates with PostgreSQL and Redis for data storage and caching.
## Dependencies

BlogApp has the following dependencies:
- Docker
- Python
- Django
- Git
- Redis
- Celery
- PostgreSQL
- Linux
- pytest

To install the Python dependencies, activate the virtual environment and run:

    pip install -r requirements.txt

## Configuration

The project includes a settings.py file for Django configuration. Key configurations include database settings, authentication settings, Redis configurations, and Celery configuration.

## Deployment

To deploy BlogApp, follow these steps:

Clone the project repository.

    git clone https://github.com/arfa79/BlogApp.git

Set up the environment and activate it:

    source <path_to_virtual_environment>/bin/activate

Navigate to the project directory and run:

    docker-compose up

In another terminal with the environment activated and in the project directory, run:

    sh postgre.sh

This migrates the database and creates a superuser.
Access the server at http://localhost:8000.
To shut down the server and clean up, use:

    sh end.sh

## Testing

To run tests, execute the following command:

    python manage.py pytest tests

This will run tests.

## Contributing

Contributions to BlogApp are welcome! If you'd like to contribute, please follow these guidelines:

    Fork the repository and create a new branch for your feature or fix.
    Ensure your code follows the project's coding standards.
    Submit a pull request with a clear description of the changes.

## License

BlogApp is licensed under the GNU General Public License v3.0 (GPL-3.0).

## Contact

For any questions or feedback, feel free to reach out to the project maintainer(s) at arfa79lg@lg.com

