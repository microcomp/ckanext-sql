import ckan.plugins as p
from ckan.lib.base import BaseController, response

c = p.toolkit.c
render = p.toolkit.render

class SqlController(BaseController):
    def index(self):
        return render('sql/base.html')