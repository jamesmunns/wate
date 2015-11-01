from wate import app
import os
from collections import namedtuple
import psycopg2 as pg

DB_USER_KEY = "WATEDBUSER"
DB_PASS_KEY = "WATEDBPASS"

dbname   = "wate"
username = os.environ[DB_USER_KEY]
password = os.environ[DB_PASS_KEY]

COMPLETE_USER_SCHEMA = [ "id",
                         "name",
                         "username",
                         "email",
                         "joindate",
                         "passhash",
                         "use_metric_units",
                         "emails_disabled" ]

COMPLETE_WEIGHT_SCHEMA = [ "user_id",
                           "weight_lbs",
                           "measure_date",
                           "measure_time" ]

### Datatypes
User        = namedtuple("User",        COMPLETE_USER_SCHEMA )
Measurement = namedtuple("Measurement", [ "weight_lbs",
                                          "date" ] )

### Database operations
def users_everything_get():
    get_users = """
      SELECT * from users;
      """

    users = []

    with get_db().cursor() as cur:
        cur.execute(get_users)

        # Create a User object for each item from the db
        for user in cur.fetchall():

            # User layout matches Schema. Convert from list to *args
            users.append(User(*user))

    return users

def all_weights_and_dates_get(username):
    get_all_wgt = """
      SELECT weights.weight_lbs,weights.measure_date
        FROM users,weights
        WHERE weights.user_id = users.id
          and users.username = %s;
      """

    measure_pts = []

    with get_db().cursor() as cur:
        cur.execute(get_all_wgt)

        for mpt in cur.fetchall():
            measure_pts.append(Measurement(*mpt))

    return measure_pts

### Setup and teardown helpers
def get_db():
    db = getattr(g, '_dbc', None)
    if db is None:
        db = g._dbc = pg.connect(dbname=dbname, user=username, password=password)
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_dbc', None)
    if db is not None:
        db.close()
