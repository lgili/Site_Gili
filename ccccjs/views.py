from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# from rest_framework import viewsets
# from .models import Language
# from .serializers import LanguageSerializer


# from django.contrib.auth.forms import UserCreationForm
# from django.views.generic.edit import CreateView

# from django.contrib.auth.models import User
from django.http import JsonResponse

from .buck import bode_planta_magnitude,bode_planta_fase, bode_controle_fase,bode_controle_magnitude,bode_malha_fechada_fase,bode_malha_fechada_magnitude,bode_malha_fechada_PI_fase,bode_malha_fechada_PI_magnitude
from .buck import Cal_PI,RZmap,goLGR_MF, goLGR_MA,step_MF,impulse_MF

# def validate_username(request):
	
# 	    username = request.GET.get('username', None)
# 	    data = {
# 	        'name' : username
# 	    }
# 	    return JsonResponse({"hello":"pythonist"})
            



# class SignUpView(CreateView):
#     template_name = 'signup.html'
#     form_class = UserCreationForm



# class LanguageView(viewsets.ModelViewSet):
# 	queryset = Language.objects.all()
# 	serializer_class = LanguageSerializer




def buck_new(request):
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


            planta_magnitude = bode_planta_magnitude(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            planta_fase = bode_planta_fase(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)

            #controle_magnitude = bode_controle_magnitude(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            #controle_fase = bode_controle_fase(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)

            if(PI_ON):
            	MF_magnitude = bode_malha_fechada_PI_magnitude(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            	MF_fase = bode_malha_fechada_PI_fase(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)

            else:
               	MF_magnitude = bode_malha_fechada_magnitude(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
               	MF_fase = bode_malha_fechada_fase(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)

            Step = step_MF(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            Impulse = impulse_MF(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            Polos = RZmap(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            LGR_MF = goLGR_MF(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            LGR_MA = goLGR_MA(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)
            

            Calcula_PI = Cal_PI(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz)  
            #Step =10
             	

  #           num = [k*ns3, k*ns2, k*ns1, k*ns0]
		# 	den = [ds3, ds2, ds1, ds0]
		# 	g = tf(num, den)

		# 	dado, t = impulse(g, Plot=False)
		# 	conteudo = []
		# 	dado = dado.tolist()
		# 	t = t.tolist()

		# for i in range(len(dado)):
		# 	conteudo.append({ 'x' : t[i], 'y': dado[i]})

		# return json.dumps(conteudo)




            dados ={"planta_magnitude" : planta_magnitude, "planta_fase":planta_fase, "Ro":Vi,"MF_magnitude":MF_magnitude,"MF_fase":MF_fase, "PI_ON":PI_ON,"Step":Step,"Polos":Polos,"LGR_MF":LGR_MF,"LGR_MA":LGR_MA,"Impulse":Impulse}
            #data = { "kp" : kp,  "kh" : kh, "nc2" : nc2, "nc1" : nc1, "nc0" : nc0,  "dc2" : dc2, "dc1" : dc1, "dc0" : dc0,  nh2 : nh2,
	        #"nh1" : nh1,  "nh0" : nh0,  "dh2" : dh2,  "dh1" : dh1,  "dh0" : dh0,   }
            #data = {"email":email , "password" : password}
            #Returning same data back to browser.It is not possible with Normal submit
            return JsonResponse(dados, safe=False)
    #Get goes here
    return render(request,'buck.html')  


# def base(request):
	
#     return render(
#         request,
#         'base1.html',
#         {
#             'title': 'x',
#             'message':'fafa',
           
#         }
#     )         

# def base(request):
#     if request.method == 'POST':
#         #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
#         if request.is_ajax():
#             #Always use get on request.POST. Correct way of querying a QueryDict.
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             data = {"email":email , "password" : password}
#             #Returning same data back to browser.It is not possible with Normal submit
#             return JsonResponse(data)
#     #Get goes here
#     return render(request,'base1.html')    