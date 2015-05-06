from string import letters

def as_dict(result):
	time_fmt = '%c'
	d = {
	'Title': result.title,
	'content': result.content,
	'Author': result.creatorLogin,
	'Date': result.date.strftime(time_fmt)}
	return d