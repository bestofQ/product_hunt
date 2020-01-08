from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

# 授权
from django.contrib.auth.decorators import login_required
# 导入product
from .models import Product

from django.utils import timezone

# Create your views here.

def product_list(request):
	products = Product.objects
	return render(request, 'product_list.html', {"products": products})

def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'detail.html', {"product": product})


# 授权  装饰器
@login_required
def publish(request):
	if request.method == 'GET':
		return render(request, 'publish.html')
	elif request.method == 'POST':
		title = request.POST.get('app_title')
		intro = request.POST.get('app_intro')
		url   = request.POST.get('app_link')

		try:
			icon  = request.FILES.get('app_icon')
			image = request.FILES.get('app_image_icon')

			# icon  = request.FILES['APP图标']
			# image = request.FILES['大图']

			product = Product()
			product.title = title
			product.intro = intro
			product.url = url
			product.icon = icon
			product.image = image

			# product.pub_date = timezone.datetime.now()
			product.pub_date = timezone.now()
			product.hunter = request.user

			product.save()

			return redirect('主页')
		except Exception as err:
			return render(request, 'publish.html', {'错误':err})
			
		# try:
		# 	icon  = request.FILES.get('APP_icon')
		# 	image = request.FILES.get('app_image')

		# 	# icon  = request.FILES['APP图标']
		# 	# image = request.FILES['大图']

		# 	product = Product()
		# 	product.title = title
		# 	product.intro = intro
		# 	product.url = url
		# 	product.icon = icon
		# 	product.image = image

		# 	# product.pub_date = timezone.datetime.now()
		# 	product.pub_date = timezone.now()
		# 	product.hunter = request.user

		# 	product.save()

		# 	return render(request, 'publish.html', {'path1':icon, 'path2': image})
		# 	# return redirect('主页')

		# except Exception as err:
		# 	return render(request, 'publish.html', {'错误':err})