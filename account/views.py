from django.shortcuts import render, redirect
# 注册导入的库
from django.contrib.auth.models import User
# 登录
from django.contrib import auth

# Create your views here.

def signup(request):
	# 判断method是 post 还是 get
	# post == 注册 
	if request.method == 'GET':
		return render(request, 'signup.html')
	elif request.method == 'POST':
		user = request.POST['user']	
		pwd = request.POST['pwd']	
		pwd1 = request.POST['pwd1']	
		# 判断user是否在数据库中
		# 如果获取不到 会报错
		try:
			# username == [keyprimary]
			User.objects.get(username=user)
			return render(request, 'signup.html', {'用户名错误': '该用户名已存在'})
		except User.DoesNotExist:
			if pwd == pwd1:
				User.objects.create_user(username=user, password=pwd)
				return redirect('主页')
			else:
				return render(request, 'signup.html', {'密码错误': '两次输入的密码不一致'})


def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	elif request.method == 'POST':
		user = request.POST['user']	
		pwd = request.POST['pwd']	
		user = auth.authenticate(username=user, password=pwd)
		if user is None:
			return render(request, 'login.html', {'错误': '用户名或密码错误'})
		else:
			auth.login(request, user)
			return redirect('主页')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('主页')


