import webapp2
import sys

sys.path.insert(0, 'controller')
sys.path.insert(1, 'utils')
sys.path.insert(2, 'model')

from handler import Handler
from front import Front
from register import Register
from login import Login
from logout import Logout
from profil import Profil
from userInfo import UserInfo
from addTask import AddTask
from taskDashboard import TaskDashboard
from taskPanel import TaskPanel
from registerForTask import RegisterForTask
from cancelTask import CancelTask
from acceptProvider import AcceptProvider
from validateTask import ValidateTask
from loginAdmin import LoginAdmin
from adminFront import AdminFront
from deleteUser import DeleteUser
from deleteTask import DeleteTask
from initAdmin import InitAdmin

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
	('/registerForTask/(\d+)', RegisterForTask),
	('/cancelTask/(\d+)', CancelTask),
	('/acceptProvider/(\d+)', AcceptProvider),
	('/validateTask/(\d+)', ValidateTask),
	('/admin/login', LoginAdmin),
	('/admin', AdminFront),
	('/admin/deleteTask/(\d+)', DeleteTask),
	('/admin/deleteUser/(\d+)', DeleteUser),
	('/admin/init', InitAdmin)
], debug=True)
