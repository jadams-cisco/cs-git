import web
import git

urls = ('/.*', 'hooks')

app = web.application(urls, globals())

class hooks:
    def POST(self):
        data = web.data()
        print 'DATA RECEIVED:'
        print data
        g = git.cmd.Git()
        g.pull()
        return 'OK'

if __name__ == '__main__':
    web.config.default_port = 8888
    app.run()