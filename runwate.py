# Import the app object
import os
from wate import app
#from wate.db_ops import DB_USER_KEY, DB_PASS_KEY, DB_HOST_KEY


# Check for database variables
#assert DB_USER_KEY in os.environ, "Set the Database Username!"
#assert DB_PASS_KEY in os.environ, "Set the Database Password!"
#assert DB_HOST_KEY in os.environ, "Set the Database Host!"

# Run
app.run(host='0.0.0.0', debug = True)
