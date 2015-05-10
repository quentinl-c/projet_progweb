from TaskOffer import TaskOffer

def search(filter, query):
	l = []
	if filter == "byname":
		tasks = TaskOffer.findByAuthor(query)
	else:
		tasks = TaskOffer.findByTitle(query)
	for task in tasks:
		if not task.private:
			l.append(task)
	return l
