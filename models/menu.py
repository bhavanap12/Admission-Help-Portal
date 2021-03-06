# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('Admission_Portal'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index')),
    
    (T('Engineering'), False, URL('default', 'user'),[(T('Colleges'), False, URL('default', 'engineering_colleges')),(T('News and Articles'), False, URL('default', 'engineering_news_and_articles')),(T('Resources'), False, URL('default', 'engineering_resources'))]),
    (T('Architecture'), False, URL('default', 'user'),[(T('Colleges'), False, URL('default', 'architecture_colleges')),(T('News and Articles'), False, URL('default', 'architecture_news_and_articles')),(T('Resources'), False, URL('default', 'architecture_resources'))]),
    (T('Design'), False, URL('default', 'user'),[(T('Colleges'), False, URL('default', 'design_colleges')),(T('News and Articles'), False, URL('default', 'design_news_and_articles')),(T('Resources'), False, URL('default', 'design_resources'))]),
    (T('Follow'), False, URL('default', 'follow')),
    (T('Notifications'), False, URL('default', 'notify'))
]


if auth.has_membership('managers'):
    response.menu.append((T('Manage'),False,URL('default','manage_admin')),)

if auth.has_membership('experts'):
    response.menu.append((T('Propose'),False,URL('default','propose')),)
    
if auth.has_membership('content_manager'):
    response.menu.append((T('Proposals'),False,URL('default','proposals')))

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------



if "auth" in locals():
    auth.wikimenu()
