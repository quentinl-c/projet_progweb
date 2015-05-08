import logging
import jinja2
import os


template_dir = os.path.join(os.path.dirname(__file__), '../templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
							   autoescape = True)

def handler404(request, response, exception):
	params = dict( title = "Erreur 404", 
		content = "La page demandee n'est pas disponible...")
	logging.exception(exception)
	t = jinja_env.get_template("message.html")
	response.out.write(t.render(params)) 
	response.set_status(404)