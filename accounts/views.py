from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegisterForm, form_senderror, EmailForm
from django.core.mail import send_mail, BadHeaderError,EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context


##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "form_login.html", {"form":form, "title": title})


def register_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        mail_subject = 'Your blog account is Activate .'
        to_email = form.cleaned_data.get('email')
        from_email = 'luizcarlosgili@gmail.com'
       # message = 'deu certo'
        #template = get_template('regiter_email.html')
        #context = Context({'user': user, 'other_info': info})
        #html_content = ''
        #send_mail(mail_subject, message, 'luizcarlosgili@gmail.com', [to_email])


        ctx = {
        'user': user,
        'purchase': 'Books'
    }

        html_content = get_template('register_mail.html').render(Context(ctx))
        msg = EmailMessage(mail_subject, html_content, from_email, [to_email])
        msg.content_subtype = "html"  # Main content is now text/html
        
        #email = EmailMessage(mail_subject, message, to=[to_email])
        #email.send()
        try:
                msg.send()
        except BadHeaderError:
                return HttpResponse("Invalid header found.")
            
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
            
        return redirect("/")    


    context = {
        "form": form,
        "title": title
    }
    return render(request, "form_register.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")






def sendERROR_view(request):
    if request.method == 'GET':
        form = form_senderror()
    else:
        form = form_senderror(request.POST)
        if form.is_valid():
            
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['luizcarlosgili@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("/thankyou/")
    return render(request, "form_send_error.html", {"form": form})




def thankyou_view(request): 
        return render( request,"thankyou.html",{   
        }
    )


def password_reset_view(request): 
        return render( request,"registration/password_reset_from.html",{   
        }
    )
