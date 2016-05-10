import web
import git

urls = ('/.*', 'hooks')

app = web.application(urls, globals())

class hooks:
    def POST(self):
        data = web.data()
        f = open('output.txt', 'w')
        f.write('response = ' + data)
        f.close()
        print 'DATA RECEIVED:'
        print data
        g = git.cmd.Git()
        g.pull()
        return 'OK'

if __name__ == '__main__':
    app.run()