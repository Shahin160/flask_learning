# save this as app.py
from flask import Flask

app = Flask(__name__)

# sql ile connection yaradir
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3307/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#controller file dan route lari gormek ucun
from controllers import *

#db ile connection yaradiriq
from extensions import *


# daha flask run yox, python app.py ile run edirik apini
if __name__ == '__main__':
    app.run(port=5000,debug=True)