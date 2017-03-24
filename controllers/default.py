# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
def engg_colleges():
    rows=db(db.institute_list.Stream=='Engineering').select()
    response.view='default/colleges.html'
    return locals()
def design_colleges():
    rows=db(db.institute_list.Stream=='Design').select()
    response.view='default/colleges.html'
    return locals()
def arch_colleges():
    rows=db(db.institute_list.Stream=='Architecture').select()
    response.view='default/colleges.html'
    return locals()
def vote_callback():
    vars=request.get_vars
    if vars and auth.user:
        id=vars.id
        direction=+1 if vars.direction == 'up' else -1
        list_row=db.institute_list(id)
        if list_row:
            voted=db.vote(institute=id,created_by=auth.user.id)
            if not voted:
                list_row.update_record(votes=list_row.votes+direction)
                db.vote.insert(institute=id,score=direction)
            elif voted.score!=direction:
                list_row.update_record(votes=list_row.votes+direction*2)
                voted.update_record(score=direction)
            else:
                pass
    return str(list_row.votes)
