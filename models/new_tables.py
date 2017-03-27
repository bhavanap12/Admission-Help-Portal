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


db.define_table('content_proposed',
                Field('branch','string'),
               Field('specialization','string'),
                Field('type_section',requires=IS_IN_SET(['News and Articles','Resources'])),
               Field('title','string'),
               Field('body','text'),
               Field('key_word1','string',),
               Field('key_word2','string',),
               Field('key_word3','string',),
               Field('time_stamp','datetime',readable=False,writable=False),
               Field('author','string',readable=False,writable=False),
              )
                
db.define_table('news_and_articles',
                Field('title','string'),
                Field('body','text'),
                Field('time_stamp','datetime'),
                Field('author','string'),
                Field('branch',readable=False,writable=False),
                Field('specialization',readable=False,writable=False)
               )
db.define_table('follow',
               Field('branch','string'),
               Field('specialization','string'),
               Field('subscribers','integer',default=0)
               )
db.define_table('notifications',
               Field('userId'),
               Field('branchy'),
               Field('specializationy'),
               Field('body','string'))

db.define_table('subscribe',
               Field('userId'),
               Field('branchy'),
               Field('specializationy'),
               Field('body','string'))

db.define_table('study_material',
                Field('title','string'),
                Field('Exam','string'),
                Field('path_of_resource','string'),
               )
