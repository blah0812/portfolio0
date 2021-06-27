from django.forms  import ModelForm	
from django import forms
from .models import Product

class ProductForm(ModelForm):
	title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
	description = forms.CharField(
						required=False, 
						widget=forms.Textarea(
							attrs={
								"placeholder": "Your Description",
								"id": "my-id-for-textarea",
								"class": "new-class-name two",
								"row": 20,
								"cols": 120
								}
							)
						)
	
	class Meta:
		model = Product
		#$exclude = ['featured']
		fields = ['title', 'description', 'price']

class RawProductionForm(forms.Form):
	title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
	description = forms.CharField(
						required=False, 
						widget=forms.Textarea(
							attrs={
								"placeholder": "Your Description",
								"id": "my-id-for-textarea",
								"class": "new-class-name two",
								"row": 20,
								"cols": 120
								}
							)
						)
	price = forms.DecimalField(initial=199.99)
