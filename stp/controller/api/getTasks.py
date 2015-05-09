from handler import Handler
from TaskOffer import TaskOffer
from jsonRender import as_dict
from search import search
from api import Api
from jsonData import formatData
from google.appengine.api import memcache

DEFAULT_VALUE = 10

class GetTasks(Handler):
	def get(self):
		l = []
		searchMode = False

		key    = self.request.get("key")
		limit  = self.request.get("limit")
		filter = self.request.get("filter")
		query  = self.request.get("search")
		start = self.request.get("start")
		end = self.request.get("end")

		minl = 0
		maxl = DEFAULT_VALUE

		if start and end and not limit:
			try:
				minl = int(start)
				maxl = int(end)
				if maxl <= minl :
					minl = 0
					maxl = DEFAULT_VALUE
			except Exception, e:
				minl = 0
				maxl = DEFAULT_VALUE

		if limit:
			try:
				maxl = int(limit)
			except Exception, e:
				maxl = DEFAULT_VALUE

		if filter and query:
			if filter == "byname" or filter == "bytitle":
				searchMode = True

		if key :
			if Api.findByKey(key) :
				haveKey = True
				if searchMode:
					tasks = search(filter, query)
				else:
					tasks = TaskOffer.all()
				tasks = list(tasks)
				cmp = 0
				last = min(maxl, len(tasks) - 1)
				for i in range(minl, last + 1):
					l.append(as_dict(tasks[i]))
			else:
				haveKey = False
		else:
			haveKey = False
		data = formatData(l, minl, last, haveKey)
		self.render_json(data)
