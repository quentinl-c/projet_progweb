import webapp2
import sys

sys.path.insert(0, 'controller')
sys.path.insert(1, 'utils')
sys.path.insert(2, 'model')
sys.path.insert(3, 'controller/api')

from handler import Handler
from front import Front
from register import Register
from login import Login
from logout import Logout
from profil import Profil
from userInfo import UserInfo
from addTask import AddTask
from taskDashboard import TaskDashboard, DeleteTaskOffer
from taskPanel import TaskPanel
from devRegister import DevRegister
from devPanel import DevPanel
from devLogin import DevLogin
from devLogout import DevLogout
from getTasks import GetTasks
from auth import Auth
from error404 import handler404
from apiTest import ApiTest
from apiFront import ApiFront
from registerForTask import RegisterForTask
from cancelTask import CancelTask
from acceptProvider import AcceptProvider
from validateTask import ValidateTask
from displayProfil import DisplayProfil
from loginAdmin import LoginAdmin
from adminFront import AdminFront
from deleteUser import DeleteUser
from deleteTask import DeleteTask
from initAdmin import InitAdmin
from aboutUs import AboutUs



app = webapp2.WSGIApplication([
	('/', Front),
	('/signup', Register),
	('/login', Login),
	('/logout', Logout),
	('/profil', Profil),
	('/userInfo', UserInfo),
	('/addTask', AddTask),
	('/taskDashboard/(\d+)', TaskDashboard),
	('/deleteTaskOffer/(\d+)', DeleteTaskOffer),
	('/aboutus', AboutUs),
	('/task/(\d+)', TaskPanel),
	('/displayProfil/(\d+)', DisplayProfil),
	('/api/register', DevRegister),
	('/api/devPanel', DevPanel),
	('/api/devLogin', DevLogin),
	('/api/devLogout', DevLogout),
	('/api/tasks', GetTasks),
	('/api/auth', Auth),
	('/api/test', ApiTest),
	('/api/front', ApiFront),
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
app.error_handlers[404] = handler404