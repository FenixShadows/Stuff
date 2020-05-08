import cgitb
import cgi

# Ne pas la mettre quand le site est en production 

cgitb.enable()

form = cgi.FieldStorage()

if form.getvalue('username') :
    username = form.getvalue('username')
else :
    raise Exception('Pas de nom utilisateur...')

print('Content-type:text/html;charset=utf-8\n') 

html = f'''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"> 
        <title> Une page web avec python et html </title>
    </head>
    <body>
        Vous etes sur une page HTML {username}
    </body>

</html>
'''
print(html)