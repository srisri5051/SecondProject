from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import User, Product, Wishlist, Category
from .models import UserProfile

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    is_dealer = forms.BooleanField(label='Are you a dealer?', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_dealer', 'dealer_details']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
            'dealer_details': 'Dealer Details (if applicable)',
        }

    def clean(self):
        cleaned_data = super().clean()
        is_dealer = cleaned_data.get('is_dealer')
        dealer_details = cleaned_data.get('dealer_details')

        if is_dealer and not dealer_details:
            raise forms.ValidationError('Dealer details are required for dealer registration')

        return cleaned_data

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'country', 'quantity', 'price', 'image', 'category']
        labels = {
            'name': 'Name',
            'country': 'Country',
            'quantity': 'Quantity',
            'price': 'Price',
            'image': 'Image',
            'category':'category',
            
        }
        

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = []

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True 

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Old Password'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm New Password'})

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
        labels = {
            'name': 'Category Name',
            
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'mobile_number', 'current_location']

class MyForm(forms.Form):
    OPTIONS = [(i, str(i)) for i in range(1, 11)]  
    select_option = forms.ChoiceField(choices=OPTIONS)        
        












# from .models import Product, Wishlist, Category
# from django import forms
# from .models import User
# from django.contrib.auth.forms import PasswordChangeForm


# class RegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     is_dealer = forms.BooleanField(label='Are you a dealer?', required=False)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'is_dealer', 'dealer_details']
#         labels = {
#             'username': 'Username',
#             'email': 'Email',
#             'password': 'Password',
#             'dealer_details': 'Dealer Details (if applicable)',
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         is_dealer = cleaned_data.get('is_dealer')
#         dealer_details = cleaned_data.get('dealer_details')

#         if is_dealer and not dealer_details:
#             raise forms.ValidationError('Dealer details are required for dealer registration')

#         return cleaned_data
    

# ################################################################################################


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'quantity', 'price', 'image', 'category']
#         labels = {
#             'name': 'Name',
#             'quantity': 'Quantity',
#             'price': 'Price',
#             'image': 'Image',
#             'category': 'category'
            
#         }

#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     self.fields['image'].widget = forms.FileInput(attrs={'accept': 'image/jpeg,image/jpg'})



# ###############################################################################################
    
    
# # class ProductForm(forms.ModelForm):
# #     class Meta:
# #         model = Product
# #         fields = ['name', 'quantity','price', 'image']
# #         labels = {
# #             'name': 'Name',
# #             'quantity': 'Quantity',
# #             'price': 'Price',
# #             'image': 'Image',
# #         }



# class WishlistForm(forms.ModelForm):
#     class Meta:
#         model = Wishlist
#         fields = []












# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name']

#     def __init__(self, *args, **kwargs):
#         super(UserProfileForm, self).__init__(*args, **kwargs)
#         self.fields['username'].disabled = True






# class CustomPasswordChangeForm(PasswordChangeForm):
#     def _init_(self, *args, **kwargs):
#         super()._init_(*args, **kwargs)
#         self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Old Password'})
#         self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New Password'})
#         self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'ConfirmNewPassword'})



# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name',]
#         labels = {
#             'name': 'Category Name',
#         }




# class AddToCartForm(forms.Form):
#     quantity = forms.IntegerField(min_value=1, label='Quantity')
