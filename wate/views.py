from wate import app
import db_ops
from flask import render_template, request, send_from_directory

@app.route('/')
def index():
    users  = db_ops.users_everything_get()
    header = db_ops.COMPLETE_USER_SCHEMA

    retval = tablemaker( header, users )

    return retval

@app.route('/login', methods=['GET', 'POST'])
def login():
    print "login"
    if request.method == 'GET':
        print "get"
        return app.send_static_file('login.html')
    else:
        return str(request.form)


@app.route('/user/<username>')
def user_data(username=None):
    if username is None:
        return "No such user!", 520

    mpts = db_ops.all_weights_and_dates_get(username)

    if len(mpts) == 0:
        return "Missing data!", 520

    retval  = "<title>{}</title>".format(username)
    retval  = "<h1>{}</h1>".format(username)
    retval += tablemaker(["weight", "date"], mpts)

    return retval

@app.route('/graph/<username>')
def user_graph(username=None):
    if username is None:
        return "No such user!", 520

    mpts = db_ops.all_weights_and_dates_get(username)

    if len(mpts) == 0:
        return "Missing data!", 520

    template_array = u""
    for pt in mpts:
        template_array += u"[new Date({}, {}, {}),{}],".format( pt.date.year,
                                                                pt.date.month-1,    # Google month items are zero indexed
                                                                pt.date.day,
                                                                pt.weight_lbs )
    # Remove the trailing comma from the loop
    template_array=template_array.rstrip(',')

    return render_template('usergraph.html', username=username, date_wgt_array=template_array)

def tablemaker(header_row, other_rows):
    retval = '<table border="1">'

    # First, print the header
    retval += '<tr>'
    for item in header_row:
        retval += "<th>{}</th>".format(item)
    retval += '</tr>'

    # Now print each row
    for row in other_rows:
        retval += "<tr>"
        for item in row:
            retval += "<td>{}</td>".format(item)
        retval += "</tr>"

    retval += "</table>"

    return retval
