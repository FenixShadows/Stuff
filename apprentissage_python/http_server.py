
#### Demarrer un serveur http pour page statiques ####
'''
import http.server 
import socketserver

port    = 80 
adress  = ("",port)
handler = http.server.SimpleHTTPRequestHandler
httpd   = socketserver.TCPServer(adress,handler)

print(f'Demarrage du serveur au port {port}...')

httpd.serve_forever()
'''

#### Demarrer un serveur http pour page dynamique ###
import http.server

port = 80
adress = ('',port)
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ['/']

httpd = server(adress,handler)
print(f'Demarrage du serveur au port {port}...')

httpd.serve_forever()