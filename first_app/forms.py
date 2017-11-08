from django import forms
# from first_app.models import User
from django.contrib.auth.models import User
from first_app.models import UserProfileInfo

# ===============================================

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

# ===============================================

class NewUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'

# ===============================================

NAME_MIN = 3

def validate_min_length(value):
    if len(value) < NAME_MIN:
        raise forms.ValidationError('Name must have {} chars at least'.format(NAME_MIN))

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
        all_data = super(ContactForm, self).clean()
        name = all_data.get('name')
        email = all_data.get('email')
        message = all_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')

class MyForm(forms.Form):
    name = forms.CharField(
        label='姓名',
        validators=[validate_min_length])
    email = forms.EmailField()
    verify_email = forms.EmailField(
        label='Email 再輸入')
    text = forms.CharField(
        label='註記',
        widget=forms.Textarea)

    def clean(self):
        # all_data = super(MyForm, self).clean()
        all_data = super().clean()

        # email 輸入與驗證欄的輸入須一致
        email = all_data['email']
        vemail = all_data['verify_email']
        if email != vemail:
            raise forms.ValidationError('Make sure emails should match!')

        # 註記欄位輸入的文字不可少於5
        text = all_data['text']
        if len(text) <= 5:
            raise forms.ValidationError('Text must have 5 chars at least')