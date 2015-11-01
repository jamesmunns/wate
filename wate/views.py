from wate import app
import db_ops

@app.route('/')
def index():
    users = users_everything_get()
    header = db_ops.COMPLETE_USER_SCHEMA

    retval = ""

    # First, print the header
    for item in header:
        retval += ( item + ", " )
    retval += ( "<br>"*2 )

    # Now print each user
    for user in users:
        retval += ( str(user) + "<br>" )

    return retval


#@app.route('/user/<username>')
#def user_data(username=None):
