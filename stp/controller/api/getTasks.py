from handler import Handler
from TaskOffer import TaskOffer
from jsonRender import as_dict
from search import search
from api import Api

DEFAULT_VALUE = 10

class GetTasks(Handler):
	def get(self):
		l = []
		searchMode = False

		key    = self.request.get("key")
		limit  = self.request.get("limit")
		filter = self.request.get("filter")
		query  = self.request.get("search")

		if limit:
			try:
				maxl = int(limit)
			except Exception, e:
				maxl = DEFAULT_VALUE
		else:
			maxl = DEFAULT_VALUE

		if filter and query:
			if filter == "byname" or filter == "bytitle":
				searchMode = True

		if key :
			if Api.findByKey(key) :
				if searchMode:
					tasks = search(filter, query)
				else:
					tasks = TaskOffer.all()
				for t in tasks:
					if len(l) < maxl:
						l.append(as_dict(t))
					else:
						break
				if len(l) == 0:
					l = {'NoTask' : True}
			else:
				l = {'Auth' : False}
		else:
			l = {'key' : None}
		self.render_json(l)
