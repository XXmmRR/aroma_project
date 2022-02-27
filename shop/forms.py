from django import forms
from .models import Review, RATE_CHOICES


class RateForm(forms.ModelForm):
	text = forms.CharField(widget=forms.Textarea, required=False, label='text')
	rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True, label='Please select a mark')

	class Meta:
		model = Review
		fields = ('name', 'body', 'rate', 'email')
		widgets = {
			'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
			'email': forms.TextInput(attrs={'placeholder': 'email', 'class': 'form-control'}),
			'body': forms.Textarea(attrs={'placeholder': 'body', 'class': 'form-control'}),
			'rate': forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
										choices=(RATE_CHOICES),)
		}
