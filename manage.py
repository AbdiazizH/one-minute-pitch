# Import db from app factory
from app import create_app,db
from flask_script import Manager,Server
from app.models import *
# Set up migrations
from flask_migrate import Migrate




# Creating app instance
app = create_app('test')
app = create_app('development')
app = create_app('production')
app.config['SECRET_KEY']='oszvcfcdlkrk:9d454a4207418f7d6084c0af1fa0c93a32656ec9783bef5ec6c86212ba57'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://moringa:123456#$@localhost/abdiaziz3'
# Create manager instance 
manager = Manager(app)



# Create migrate instance
migrate = Migrate(app,db)

manager.add_command('server',Server)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@manager.command
def test():
    '''
    Run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict( app=app, db=db, User=User, Pitch = Pitch, Comment=Comment)


if __name__ == '__main__':
    manager.run()