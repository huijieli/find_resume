#-*- coding: utf-8 -*-
'''
Created on 2012-12-20

@author: huijieli
'''
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import sqlite3

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

connectcount=0

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/find", FindHander),
            (r"/add", AddHander),
            (r"/delete", DelHander), 
            (r"/file/(.*)", tornado.web.StaticFileHandler, {"path": os.path.dirname(__file__)}),
            
            
        ]
        settings = dict(
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
            autoescape="xhtml_escape",
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render("index.html")


class FindHander(tornado.web.RequestHandler):
    def get(self):
        self.post()
    def post(self):
        
        
        conn=sqlite3.connect('resume3.db')
        curs=conn.cursor()
        query='select * from resume '
        curs.execute(query)
        name=[]
        for item in curs.fetchall():
            name.append(item[0])
        print name

#        print result
#        data={}
#        data['name']=  name
#        data['content']=file
        return self.render("add.html",name=name)

        


class AddHander(tornado.web.RequestHandler):
    def get(self):
        self.post()
    def post(self):
#        print self.request.files
#        print self.request.files['myfile'][0]['body']
        filename=self.request.files['myfile'][0]['filename']
#        fp = open(self.request.files['myfile'][0]['filename'],'wb')
        content=self.request.files['myfile'][0]['body']
        fp = open(filename,'wb')
        fp.write(content)
        fp.close()
        
        
        
        
        conn=sqlite3.connect('resume3.db')
        curs=conn.cursor()
        curs.execute('''
        CREATE TABLE if not exists resume(
        name TEXT PRIMARY KEY,
        content       BLOB
        
        )
        
        ''')
        query='INSERT INTO resume VALUES(?,?)'
        
        curs.execute(query,[filename,sqlite3.Binary(content)])
        
        conn.commit()
        self.redirect("/")
#
#    
#        fp.write (content)  
#        fp.close()
        
        

class DelHander(tornado.web.RequestHandler):
    def get(self):
        self.post()
    def post(self):
        print self.request.arguments



        
def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
#    conn=sqlite3.connect('resume3.db')
#    curs=conn.cursor()
#    query='select * from resume '
#    curs.execute(query)
#    name,file=curs.fetchone()
#    
#    fp = open(name,'wb')
#    fp.write(file)
#    fp.close()
    
#    main()



