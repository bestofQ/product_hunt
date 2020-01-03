from django.shortcuts import render, redirect
# 注册导入的库
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
	# 判断method是 post 还是 get
	# post == 注册 
	if request.method == 'GET':
		return render(request, 'signup.html')
	elif request.method == 'POST':
		user = request.POST['user']	
		password = request.POST['password']	
		password1 = request.POST['password1']	
		# 判断user是否在数据库中
		# 如果获取不到 会报错
		try:
			# username == [keyprimary]
			User.objects.get(username=user)
			return render(request, 'signup.html', {'用户名错误': '该用户名已存在'})
		except User.DoesNotExist:
			if password == password1:
				User.objects.create(username=user, password=password)
				return redirect('主页')
			else:
				return render(request, 'signup.html', {'密码错误': '两次输入的密码不一致'})




