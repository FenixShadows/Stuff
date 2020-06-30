# coding : utf-8
import cgi

print('Content-type:text/html;charset=utf-8\n') 

html = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"> 
        <title> Une page web avec python et html </title>
    </head>
    <body>
        Vous etes sur une page HTML
        <h1> Bienvenue sur mon site Web - Bien vouloir vous indentifier... </h1>
        <form method = 'post' action = 'result.py'>
            <p> <input type="text" name ='username'>
            <input type="submit" value="Envoyer"> </p> 
        </form>
    </body>

</html>
'''
print(html)