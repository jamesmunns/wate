from wate import db
import bcrypt

class User(db.Model):
    # Schema definition
    username = db.Column(db.Text, primary_key=True)
    email    = db.Column(db.Text)
    passhash = db.Column(db.Text, nullable=False)
#    disp_units = db.Column(db.Enum( 'pounds',
#                                    'kilos',
#                                    'stones',
#                                    name = 'unit_types' ),
#                           nullable=False)
#    periodic_emails = db.Column(db.Boolean, nullable=False)
#    dirty = db.Column(db.Boolean, nullable=False)
#    join_date = db.Column(db.DateTime, nullable=False)
#    gender    = db.Column(db.Enum( 'male',
#                                   'female',
#                                   name = 'gender_types' ) )
#    birthday  = db.Column(db.Date)
#    height_cm = db.Column(db.Integer)

    def __init__(self, username, password, email=None
                #       disp_units, periodic_emails
                ):
        self.username = username
        self.email    = email
        self.passhash = self.hash_password(password)

    @staticmethod
    def hash_password( password ):
        return bcrypt.hashpw(password, bcrypt.gensalt())

    def __repr__(self):
        return '<User %r>'.format(self.username)
