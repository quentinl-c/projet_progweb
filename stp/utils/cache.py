from google.appengine.api import memcache
from TaskOffer import TaskOffer
import time

def frontTasks(update = False):
	key = 'top'
	tasks = memcache.get(key)
	if tasks is None or update:
		time.sleep(0.1)#synchro with DB
		tasks = TaskOffer.getPublishedTasks()
		tasks = list(tasks)
		memcache.set(key, tasks)

	return tasks
