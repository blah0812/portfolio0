from django.shortcuts import render
from product.models import Product
from product.form import ProductForm, RawProductionForm
# Create your views here.
def product_detail_view(request):
	obj = Product.objects.get(id=1)
	context = {
	#	'title': obj.title,
	'object': obj 
	#	'decription': obj.description
	}
	return render(request, "product/detail.html",context)


def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context = {
	#	'title': obj.title,
		'form': form 
	#	'decription': obj.description
	}
	return render(request, "product/product_create.html",context)

#def product_create_view(request):
	#print(request.GET)
	#print(request.POST)
#	if request.method == "POST":
#		my_new_title = request.POST.get('title')
#		print(my_new_title) 
#	context = {}

#	return render(request, "product/product_create.html",context)
# def product_create_view(request):
# 	my_form = RawProductionForm()
# 	if request.method == 'POST':
# 		my_form = RawProductionForm(request.POST)
# 		if my_form.is_valid():
# 			print(my_form.cleaned_data)
# 			Product.objects.create(**my_form.cleaned_data)
# 		else:
# 			print(my_form.errors)

# 	context = {
# 		"form" : my_form
# 	}

# 	return render(request, "product/product_create.html",context)



