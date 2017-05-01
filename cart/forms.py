from django import forms


PRODUCT_QUANTITY_CHOICES  = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    """Adds items to cart or updates quantity"""
    # quantity between 1-20, coerce=int converts input into an integer
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
