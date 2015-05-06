from TaskOffer import TaskOffer

def search(filter, query):
	if filter == "byname":
		print query
		tasks = TaskOffer.findByCreator(query)
	else:
		tasks = TaskOffer.findByTitle(query)
	return tasks
