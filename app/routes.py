from  app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
	users = {'username': 'владимир'}
	posts = [
	{
	'author':{'username':'Fedja'},
	'body':'Все путем!'
	},
	{
	'author': {'username':'Lavnikevich'},
	'body': 'Копипастинг'
	},
	{
	'author': {'username':'Andruha'},
	'body': 'Автоматизация в массы!'
	}
	]
	return render_template('index.html', \
		title= 'My',users = users, posts = posts)
'''
<html>
	<head>
		<title>My microblog</title>
	</head>
	<body>
		<h1>Hello,+ users['user'].title() +!</h1>
	</body>
</html>'''
