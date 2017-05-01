from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
	"""Form the used fills out during the checkout"""
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'email', 'address',
					'postal_code', 'city']
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'address': forms.TextInput(attrs={'class': 'form-control'}),
			'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
			'city': forms.TextInput(attrs={'class': 'form-control'}),
		}

					
