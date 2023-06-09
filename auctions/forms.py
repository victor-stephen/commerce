from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from auctions.models import Comment, Listing, Bid


class CreateListing(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'category', 'imageUrl', 'startPrice']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Title', 'autocomplete': 'off', 'class':'form-control w-50 mb-4'}),
            'category': forms.Select(attrs={'placeholder': 'Category', 'autocomplete': 'off', 'class': 'form-control w-50 mb-4'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description', 'autocomplete': 'off', 'class': 'form-control w-50 mb-4'}),
            'startPrice': forms.NumberInput(attrs={'class':'form-control w-auto mb-4'}),
            'imageUrl': forms.TextInput(attrs={'placeholder':'ImageUrl','class':'form-control w-50 mb-4'}),
        }
    
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder':'New Comment', 'autocomplete': 'off', 'class':'form-control h-25 my-4'})
        }

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bid']
        widgets = {
            'bid':forms.NumberInput(attrs={'placeholder':'Bid', 'autocomplete':'off', 'class':'form-control w-auto mb-4'})
        }

class BidFormAdmin(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['bidder', 'product', 'bid']

    def clean(self):
        bid = self.cleaned_data.get("bid")
        print(type(bid))
        currentPrice = self.cleaned_data.get("product").currentPrice
        print(type(currentPrice))
        if currentPrice > bid or currentPrice == bid:
            raise forms.ValidationError(f"Bid must be than current bid which is {currentPrice}")
        return self.cleaned_data