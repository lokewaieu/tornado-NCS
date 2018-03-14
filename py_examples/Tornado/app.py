# imports
import tornado.ioloop
import tornado.web
import os.path
import tornado.autoreload
import os

# write to screen
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('static/index.html')
	

#This tells tornado where to find static file
settings = dict(
	template_path=os.path.join(os.path.dirname(__file__),"templates"),
	static_path=os.path.join(os.path.dirname(__file__),"Tornado/templates/static"),
	debug=True
)

# r"/" == root website address
application = tornado.web.Application([
	(r"/", MainHandler),
	(r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static/'})
],**settings, gzip=True)

# Start the server at port 7777
if __name__ == "__main__":
	PortNumber = str(7777)
	print(r'Server Running at http://localhost:' + PortNumber + r'/')
	print(r'To close press ctrl + c')
	application.listen(PortNumber)
	tornado.autoreload.start()
	for dir, _, files in os.walk('static'):
        	[tornado.autoreload.watch(dir + '/' + f) for f in files if not f.startswith('.')]
	tornado.ioloop.IOLoop.instance().start()
