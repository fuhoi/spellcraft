import cgi
import datetime
import os
import urllib
import wsgiref.handlers

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

# Models    
# class type(db.model):
    # """models an individual type entity with a code and name"""
    # code = db.stringproperty(multiline=false)
    # name = db.stringproperty(multiline=false)

# class resource(db.model):
    # """models an individual resource entity with a code and name"""
    # code = db.stringproperty(multiline=false)
    # name = db.stringproperty(multiline=false)
    
# class spell(db.model):
    # """models an individual spell entity with a name, type, resource cost, summary, description"""
    # name = db.stringproperty(multiline=false)
    # type = db.referenceproperty(type)
    # summary = db.stringproperty(multiline=false)
    # description = db.stringproperty(multiline=true)
    
# class cost(db.model):
    # """models an individual cost entity with a spell, resource and quantity"""
    # spell = db.referenceproperty(spell)
    # resource = db.referenceproperty(resource)
    # quantity = db.integerproperty()

# Keys
# def type_key(type_name=none):
    # """constructs a datastore key for a type entity with a type"""
    # return db.key.from_path('type', type_name or 'default_type')

# def resource_key(resource_name=none):
    # """constructs a datastore key for a resource entity with a resource"""
    # return db.key.from_path('resource', resource_name or 'default_resource')
    
# def spell_key(spell_name=none):
    # """constructs a datastore key for a spell entity with a spell"""
    # return db.key.from_path('spell', spell_name or 'default_spell')
    
# def cost_key(cost_name=none):
    # """constructs a datastore key for a cost entity with a cost"""
    # return db.key.from_path('cost', cost_name or 'default_cost')

class MainPage(webapp.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(path, template_values))
        # # spells
        # spells_query = spell.all().ancestor(spell_key("spellcraft")).order('name')
        # spells = spells_query.fetch(10)
        # # types
        # types_query = type.all().ancestor(type_key("spellcraft")).order('name')
        # types = types_query.fetch(10)
        # # resources
        # resources_query = resource.all().ancestor(resource_key("spellcraft")).order('name')
        # resources = resources_query.fetch(10)
        # # links
        # if users.get_current_user():
            # url = users.create_logout_url(self.request.url)
            # url_linktext = 'logout'
        # else:
            # url = users.create_login_url(self.request.url)
            # url_linktext = 'login'
        # # template values    
        # template_values = {
            # 'spells': spells,
            # 'types': types,
            # 'resources': resources
        # }
        # Display
        #path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        #self.response.out.write(template.render(path, template_values))

# class types(webapp.requesthandler):
    # def get(self):
        # types_query = type.all().ancestor(type_key("spellcraft")).order('name')
        # types = types_query.fetch(10)
        
        # template_values = {
            # 'types': types
        # }
        
        # path = os.path.join(os.path.dirname(__file__), 'html/types.html')
        # self.response.out.write(template.render(path, template_values))

# class typecreate(webapp.requesthandler):
    # def post(self):
        # type_ancestor = type_key("spellcraft")
        # type_code = self.request.get('code')
        # type_name = self.request.get('name')
        # type = type(parent=type_ancestor,code=type_code,name=type_name)
        # type.put()
        # self.redirect('/types')
        
# class typedeleteall(webapp.requesthandler):
    # def get(self):
        # db.delete(type.all())
        # self.redirect('/types')

# class resources(webapp.requesthandler):
    # def get(self):
        # resources_query = resource.all().ancestor(resource_key("spellcraft")).order('name')
        # resources = resources_query.fetch(10)
        
        # template_values = {
            # 'resources': resources
        # }
        
        # path = os.path.join(os.path.dirname(__file__), 'html/resources.html')
        # self.response.out.write(template.render(path, template_values))

# class resourcecreate(webapp.requesthandler):
    # def post(self):
        # resource_ancestor = resource_key("spellcraft")
        # resource_code = self.request.get('code')
        # resource_name = self.request.get('name')
        # resource = resource(parent=resource_ancestor,code=resource_code,name=resource_name)
        # resource.put()
        # self.redirect('/resources')
        
# class resourcedeleteall(webapp.requesthandler):
    # def get(self):
        # db.delete(resource.all())
        # self.redirect('/resources')
        
# class spells(webapp.requesthandler):
    # def get(self):
        # spells_query = spell.all().ancestor(spell_key("spellcraft")).order('name')
        # spells = spells_query.fetch(10)
        # types_query = type.all().ancestor(type_key("spellcraft")).order('name')
        # types = types_query.fetch(10)
        # resources_query = resource.all().ancestor(resource_key("spellcraft")).order('name')
        # resources = resources_query.fetch(10)
        
        # template_values = {
            # 'spells': spells,
            # 'types': types,
            # 'resources': resources
        # }
        
        # path = os.path.join(os.path.dirname(__file__), 'html/spells.html')
        # self.response.out.write(template.render(path, template_values))

# class spellcreate(webapp.requesthandler):
    # def post(self):
        # spell_ancestor = spell_key("spellcraft")
        
        # spell_name = self.request.get('name')
        # spell_type = self.request.get('type')
        # spell_summary = self.request.get('summary')
        # spell_description = self.request.get('desciption')
        
        # spell = spell(parent=spell_ancestor,name=spell_name,type=spell_type,summary=spell_summary,description=spell_description)
        # spell.put()
        
        # spell_resource_cost_chaos = self.request.get('resource_c')
        # spell_resource_cost_dark = self.request.get('resource_d')
        # spell_resource_cost_earth = self.request.get('resource_e')
        # spell_resource_cost_energy = self.request.get('resource_y')
        # spell_resource_cost_fire = self.request.get('resource_cost_f')
        # spell_resource_cost_light = self.request.get('resource_cost_l')
        # spell_resource_cost_storm = self.request.get('resource_cost_s')
        # spell_resource_cost_water = self.request.get('resource_cost_w')
        
        # q = db.gqlquery("select * from resource where name = :resource_name", "c")
        # resource = q.get()
        # cost = cost(parent=cost_key("spellcraft"),spell=spell,resource=resource,quantity=spell_resource_cost_chaos)
        
        # q = db.gqlquery("select * from resource where name = :resource_name", "d")
        # resource = q.get()
        # cost = cost(parent=cost_key("spellcraft"),spell=spell,resource=resource,quantity=spell_resource_cost_dark)
        
        # q = db.gqlquery("select * from resource where name = :resource_name", "e")
        # resource = q.get()
        # cost = cost(parent=cost_key("spellcraft"),spell=spell,resource=resource,quantity=spell_resource_cost_earth)
        
        # q = db.gqlquery("select * from resource where name = :resource_name", "y")
        # resource = q.get()
        # cost = cost(parent=cost_key("spellcraft"),spell=spell,resource=resource,quantity=spell_resource_cost_energy)
        
        # q = db.gqlquery("select * from resource where name = :resource_name", "f")
        # resource = q.get()
        # cost = cost(parent=cost_key("spellcraft"),spell=spell,resource=resource,quantity=spell_resource_cost_fire)
        
        # q = db.gqlquery("select * from resource where name = :resource_name", "l")
        # resource = q.get()
        # cost = cost(parent=cost_key("spellcraft"),spell=spell,resource=resource,quantity=spell_resource_cost_light)
        
        # q = db.gqlquery("select * from resource where name = :resource_name", "s")
        # resource = q.get()
        # cost = cost(parent=cost_key("spellcraft"),spell=spell,resource=resource,quantity=spell_resource_cost_storm)
        
        # q = db.gqlquery("select * from resource where name = :resource_name", "w")
        # resource = q.get()
        # cost = cost(parent=cost_key("spellcraft"),spell=spell,resource=resource,quantity=spell_resource_cost_water)
        
        # self.redirect('/spells')
        
# class spelldeleteall(webapp.requesthandler):
    # def get(self):
        # db.delete(spell.all())
        # self.redirect('/spells')
        
application = webapp.WSGIApplication([('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()