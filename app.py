# save this as app.py
from flask import Flask


app = Flask(__name__)

# sql ile connection yaradir
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test:123@127.0.0.1:3307/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'my_project'


#controller file dan route lari gormek ucun
#db ile connection yaradiriq
from controllers import *
from extensions import *
from models import *



# daha flask run yox, python app.py ile run edirik apini
if __name__ == '__main__':
    # app.init_app(db)
    # app.init_app(migrate)
    app.run(port=5000,debug=True)