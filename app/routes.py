from  app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User

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
"""
Аргумент methods в дизайнере маршрутов -
это сообщения для Flask, что эта функция просмотра принимает запросы GET и POST
"""

"""
Метод form.validate_on_submit() выполняет всю обработку формы.
Когда браузер отправляет запрос GET для получения веб-страницы с формой,
этот метод возвращает False. Когда браузер отправляет запрос POST в результате
нажатия пользователем кнопки submit, form.validate_on_submit() собирает все
данные, запускает все валидаторы, прикрепленные к полям, и если все в порядке,
вернет True.
"""

"""
Функция flash() — полезный способ показать сообщение пользователю.
"""

"""
Функция redirect() указывает веб-браузеру клиента автоматически перейти на
другую страницу, указанную в качестве аргумента.
"""

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username = form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember = form.remember_me.data)
		return redirect(url_for('index'))
	return render_template('login.html', title = 'Sign In', form = form)
'''
<html>
	<head>
		<title>My microblog</title>
	</head>
	<body>
		<h1>Hello,+ users['user'].title() +!</h1>
	</body>
</html>'''
