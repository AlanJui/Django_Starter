from django import forms
from django.core import validators

def validate_min_length(value):
    if len(value) <= 5:
        raise forms.ValidationError('must have 5 chars at least')

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name needs to start with Z')

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')

class MyForm(forms.Form):
    name = forms.CharField(validators=[validate_min_length])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[
            validators.MaxLengthValidator(0)
        ]
    )

    def clean_text(self):
        data = self.cleaned_data['text']
        if len(data) <= 5:
            raise forms.ValidationError('Text must have 5 chars at least')
        return data

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('Got a Bot')
        return botcatcher