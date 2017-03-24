# -*- coding: utf-8 -*-
db.define_table('institute_list',
              Field('institute_name','string'),
              Field('Ownership','string'),
               Field('Exam','string'),
               Field('votes','integer',default=0),
               Field('URL','string'),
                Field('Stream',requires=IS_IN_SET(['Engineering','Design','Architecture'])),
               auth.signature)
db.define_table('vote',
              Field('institute','reference institute_list'),
              Field('score','integer',default=+1),
              auth.signature)
