from wate import app
import db_ops

@app.route('/')
def index():
    users  = db_ops.users_everything_get()
    header = db_ops.COMPLETE_USER_SCHEMA

    retval = '<table border="1">'


    # First, print the header
    retval += '<tr>'
    for item in header:
        retval += "<th>{}</th>".format(item)
    retval += '</tr>'

    # Now print each user
    for user in users:
        retval += "<tr>"
        for item in user:
            retval += "<td>{}</td>".format(item)
        retval += "</tr>"

    retval += "</table>"

    return retval


#@app.route('/user/<username>')
#def user_data(username=None):
