"""My Server"""
import http.server
import socketserver

PORT = 8000

class TestMe():
    """Class for tests"""
    def take_five(self):
        """returns 5"""
        return 5
    def port(self):
        """returns port"""
        return PORT

if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
