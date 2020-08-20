
# ----------------------------------------------------------------------------# 
# * Migration Imports
# ----------------------------------------------------------------------------# 
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from models import db

# ----------------------------------------------------------------------------# 
# * Manage Migration
# ----------------------------------------------------------------------------# 
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()





#  # ----------------------------------------------------------------------------# 
#  # * Migration Imports
#  # ----------------------------------------------------------------------------# 

#  from flask_script import Manager
#  from flask_migrate import Migrate, MigrateCommand


#  # ----------------------------------------------------------------------------# 
#  # * Manage Migration
#  # ----------------------------------------------------------------------------# 
#  def migration(app,db):
#      migrate = Migrate(app, db)
#      manager = Manager(app)
#      manager.add_command('db', MigrateCommand)

