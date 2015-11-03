Docker setup should be:
* NGiNX docker image
    * Handles the HTTP and HTTPS connections, as well as load balancing and static serving (eventually, maybe)
* Flask and Gunicorn
    * The app is written in Flask, Gunicorn is the server serving N instances of the Flask app
* PostgreSQL
    * Postgres is the database

