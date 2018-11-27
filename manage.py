from flask_script import Manager,Server
from app import create_app,db
from  flask_migrate import Migrate, MigrateCommand
from app.models import User,Role,Post, Comment, Image, PhotoProfile
from flask_login import LoginManager

# app = create_app('production')
app= create_app('production')

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
manager = Manager(app)

migrate = Migrate(app,db)
manager.add_command('server', Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Role = Role, Comment = Comment, Image = Image, PhotoProfile = PhotoProfile )
if __name__ == '__main__':
    manager.run()

