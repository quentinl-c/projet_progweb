
def formatData(l, minl, maxl, haveKey):
	if haveKey:
		if len(l) == 0:
			data = {'noTask' : True}
		else:
			data = {'noTask' : False, 'start' : minl, 'end' : maxl, 'tasks' : l}
	else:
		data = {'auth' : False}
	return data