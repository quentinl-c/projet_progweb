import webapp2
import sys

sys.path.insert(0, 'controller')
sys.path.insert(1, 'utils')
sys.path.insert(2, 'model')

from handler import Handler
from register import Register
from login import Login
from logout import Logout
from front import Front
from profil import Profil
from userInfo import UserInfo
from addTask import AddTask
from taskDashboard import TaskDashboard
from taskPanel import TaskPanel
from acceptTask import AcceptTask

app = webapp2.WSGIApplication([
	('/', Front),
	('/signup', Register),
	('/login', Login),
	('/logout', Logout),
	('/profil', Profil),
	('/userInfo', UserInfo),
	('/addTask', AddTask),
	('/taskDashboard/(\d+)', TaskDashboard),
	('/task/(\d+)', TaskPanel),
	('/acceptTask/(\d+)', AcceptTask)
], debug=True)
