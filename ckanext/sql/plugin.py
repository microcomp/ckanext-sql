import logging
import ckan.plugins as p

log = logging.getLogger(__name__)

class SqlPlugin(p.SingletonPlugin):

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IConfigurable)
    p.implements(p.IRoutes, inherit=True)

    def configure(self, config):
        log.info('Plugin ckanext-sql loaded')

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_public_directory(config, 'public')

    def before_map(self, map):
        sql_controller = 'ckanext.sql.controller:SqlController'
        map.connect('sql', '/sql', controller=sql_controller, action='index')

        return map
