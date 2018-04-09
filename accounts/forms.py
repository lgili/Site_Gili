from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )


User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
	attrs={
		'class': 'form-control',
		'placeholder': 'Username',
		'id' : 'Username'	,
		'label':'Username',
		#'style': 'height:35px;' ,	
	}
	))
    password = forms.CharField(widget=forms.PasswordInput(
	attrs={
		'class': 'form-control',
		'placeholder': 'Password',
		'id' : 'Password'	,
		'label':'Password',	
	}
	))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
       
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist or Incorrect passsword")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
	attrs={
		'class': 'form-control',
		'placeholder': 'Username',
		'id' : 'Username'	,
		'label':'Username1',	
	}
	))



    email = forms.EmailField(widget=forms.EmailInput(
	attrs={
		'class': 'form-control',
		'placeholder': 'Email address',
		'id' : 'Email address'	,
		'label':'Email address',	
	}
	))
    email2 = forms.EmailField(widget=forms.EmailInput(
	attrs={
		'class': 'form-control',
		'placeholder': 'Confirm Email',
		'id' : 'Confirm Email'	,
		'label':'Confirm Email',	
	}
	))
    password = forms.CharField(widget=forms.PasswordInput(
	attrs={
		'class': 'form-control',
		'placeholder': 'Password',
		'id' : 'Password'	,
		'label':'Password',	
	}
	))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    # def clean(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     email2 = self.cleaned_data.get('email2')
    #     if email != email2:
    #         raise forms.ValidationError("Emails must match")
    #     email_qs = User.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError("This email has already been registered")

    #     return super(UserRegisterForm,self).clean(*args, **kwargs)

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email




class form_senderror(forms.Form):
   from_email = forms.EmailField(widget=forms.EmailInput(
     attrs={
         'class': 'form-control',
         'placeholder': 'Email address',
         'id' : 'Email address'  ,
         'label':'Email address',
          
     }
     ))
   name = forms.CharField(widget=forms.TextInput(
     attrs={
         'class': 'form-control',
         'placeholder': 'Name',
         'id' : 'Name'   ,
         'label':'Name',
          }
     ))
   subject = forms.CharField(widget=forms.TextInput(
     attrs={
         'class': 'form-control',
         'placeholder': 'Subject',
         'id' : 'Subject'   ,
         'label':'subject',
          }
     ))
   message = forms.CharField(widget=forms.Textarea(
     attrs={
         'class': 'form-control',
         'placeholder': 'messagem',
         'id' : 'Message'   ,
         'label':'message',
         'rows' : '7',
          }
     ))
   #from_email = forms.EmailField(required=True)
   #name = forms.CharField(required=True)
   #subject = forms.CharField(required=True)
   #message = forms.CharField(widget=forms.Textarea, required=True)



class EmailForm(forms.Form):
      firstname = forms.CharField(max_length=255)
      lastname = forms.CharField(max_length=255)
      email = forms.EmailField()
      subject = forms.CharField(max_length=255)
      botcheck = forms.CharField(max_length=5)
      message = forms.CharField()




