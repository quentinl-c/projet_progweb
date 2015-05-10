from string import letters

def as_dict(result):
	time_fmt = '%c'
	d = {
	'title': result.title,
	'id' : result.key().id(),
	'content': result.content,
	'author': result.creatorLogin,
	'date': str(result.date)}
	return d