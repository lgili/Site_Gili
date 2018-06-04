try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass
from crispy_forms.helper import FormHelper
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from datetime import datetime

from comments.forms import CommentForm
from comments.models import Comment
from .forms import PostForm , NameForm
from .models import Post
from .utils import get_read_time

from django.http import JsonResponse


from .buck import bode_planta_magnitude
#from .buck import bode_planta_magnitude,bode_planta_fase, bode_controle_fase,bode_controle_magnitude,bode_malha_fechada_fase,bode_malha_fechada_magnitude,bode_malha_fechada_PI_fase,bode_malha_fechada_PI_magnitude
#from .buck import Cal_PI,RZmap,goLGR_MF, goLGR_MA,step_MF,impulse_MF

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
		
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content)
	print(get_read_time(instance.content))
	initial_data = {
			"content_type": instance.get_content_type,
			"object_id": instance.id
	}
	form = CommentForm(request.POST or None, initial=initial_data)
	if form.is_valid() and request.user.is_authenticated():
		c_type = form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = form.cleaned_data.get('object_id')
		content_data = form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()


		new_comment, created = Comment.objects.get_or_create(
							user = request.user,
							content_type= content_type,
							object_id = obj_id,
							content = content_data,
							parent = parent_obj,
						)
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())


	comments = instance.comments
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
		"comments": comments,
		"comment_form":form,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active().order_by("timestamp")

	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()
	
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
               # Q(metatag__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"object_list": queryset, 
		"title": "List",
		"page_request_var": page_request_var,
		"today": today,
        
	}
	return render(request, "post_list.html", context)





def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "post_form.html", context)



def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")



def chat(request):
    """Renders the contact page."""
    
    return render(
        request,
        'thankyou.html',
        {
            'title':'Graficos Modbus e Scada',
            'message':'Em teste sempre',
            'year':datetime.now().year,
        }
    )

def about(request):

    return render(
        request,
        'about.html',
        {
            'title':'ha',
            'message':'fafa',
           'year':datetime.now().year,
        }
    )


# def buck(request):

#     return render(
#         request,
#         'buck.html',
#         {
#             'title':'buck',
            
#         }
#     )


def buck(request):
    if request.method == 'POST':
        #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        if request.is_ajax():
            #Always use get on request.POST. Correct way of querying a QueryDict.
            kp = request.POST.get('kp')
            kh = request.POST.get('kh')
            nc2 = request.POST.get('nc2')
            nc1 = request.POST.get('nc1')
            nc0 = request.POST.get('nc0')
            dc2 = request.POST.get('dc2')
            dc1 = request.POST.get('dc1')
            dc0 = request.POST.get('dc0')
            Phase_Mar = request.POST.get('Phase_Mar')
            Freq_cruz = request.POST.get('Freq_cruz')
            

            Ro = request.POST.get('Ro')
            L = request.POST.get('L')
            C = request.POST.get('C')
            Vi = request.POST.get('Vi')

            PI_ON = request.POST.get('PI_ON')


            # planta_magnitude = bode_planta_magnitude(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            # planta_fase = bode_planta_fase(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)

            

            # if(PI_ON):
            # 	MF_magnitude = bode_malha_fechada_PI_magnitude(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            # 	MF_fase = bode_malha_fechada_PI_fase(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)

            # else:
            #    	MF_magnitude = bode_malha_fechada_magnitude(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            #    	MF_fase = bode_malha_fechada_fase(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)

            # Step = step_MF(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            # Impulse = impulse_MF(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            # Polos = RZmap(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            # LGR_MF = goLGR_MF(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            # LGR_MA = goLGR_MA(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            

            # Calcula_PI = Cal_PI(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)  
            Step =10
            planta_magnitude=1
            planta_fase=2
            MF_magnitude=3
            MF_fase=4
            Impulse=6
            Polos=9
            LGR_MF=0
            LGR_MA=8
             	





            dados ={"planta_magnitude" : planta_magnitude, "planta_fase":planta_fase, "Ro":Vi,"MF_magnitude":MF_magnitude,"MF_fase":MF_fase, "PI_ON":PI_ON,"Step":Step,"Polos":Polos,"LGR_MF":LGR_MF,"LGR_MA":LGR_MA,"Impulse":Impulse}
            #data = { "kp" : kp,  "kh" : kh, "nc2" : nc2, "nc1" : nc1, "nc0" : nc0,  "dc2" : dc2, "dc1" : dc1, "dc0" : dc0,  nh2 : nh2,
	        #"nh1" : nh1,  "nh0" : nh0,  "dh2" : dh2,  "dh1" : dh1,  "dh0" : dh0,   }
            #data = {"email":email , "password" : password}
            #Returning same data back to browser.It is not possible with Normal submit
            return JsonResponse(dados, safe=False)
    #Get goes here
    return render(request,'buck.html')  

def boost(request):

    return render(
        request,
        'boost.html',
        {
            'title':'boost',
            
        }
    )

def buck_boost(request):

    return render(
        request,
        'buck_boost.html',
        {
            'title':'buck_boost',
            
        }
    )

def flyback(request):

    return render(
        request,
        'flyback.html',
        {
            'title':'flyback',
            
        }
    ) 

def forward(request):

    return render(
        request,
        'forward.html',
        {
            'title':'forward',
            
        }
    )        
  
def push_pull(request):

    return render(
        request,
        'push_pull.html',
        {
            'title':'push_pull',
            
        }
    ) 	

def half_bridge(request):

    return render(
        request,
        'half_bridge.html',
        {
            'title':'half_bridge',
            
        }
    )  

def full_bridge(request):

    return render(
        request,
        'full_bridge.html',
        {
            'title':'full_bridge',
            
        }
    )     