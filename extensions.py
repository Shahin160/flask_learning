#proektimizde qurdugumuz elave modullar, for ex. sql-alchemy ve s.
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

#app ile connection yaradilir
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#after run flask db init and generate migrations folder
# flask db migrate -m "Initial migration."


#mysqlclient problem:
# brew-sql-problem.txt