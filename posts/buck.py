
import control
from control import *
from control.matlab import *
import numpy as np
import json
import math
import cmath
from sympy import Symbol, cos


def bode_planta_magnitude(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz):

  # Something
  		Ro = float(Ro)
  		Vi = float(Vi)
  		L = float(L)
  		C = float(C)
  		kp = float(kp)
  		nc2 = float(nc2)
  		nc1 = float(nc1)
  		nc0 = float(nc0)
  		dc2 = float(dc2)
  		dc1 = float(dc1)
  		dc0 = float (dc0)
  		kh = float(kh)
  		
  		

  		rC= 0
  		rL =0
  		num_p = [0,Vi*Ro*rC*C, Vi*Ro]
  		den_p = [L*C*(Ro+rC) ,  (L+rL*C*Ro+rL*C*rC+Ro*rC*C) ,   Ro+rL]
  		sys_p = tf(num_p, den_p)
  		
  		dado, x, t = bode(sys_p, Plot=False)
  		conteudo = []
  		dado = dado.tolist()
  		t = t.tolist()
  		for i in range(len(dado)):
  			conteudo.append({ 'x' : t[i], 'y': dado[i]})

  		
  		return json.dumps(conteudo)



def bode_controle_magnitude(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz):

  # Something
  		Ro = float(Ro)
  		Vi = float(Vi)
  		L = float(L)
  		C = float(C)
  		kp = float(kp)
  		nc2 = float(nc2)
  		nc1 = float(nc1)
  		nc0 = float(nc0)
  		dc2 = float(dc2)
  		dc1 = float(dc1)
  		dc0 = float (dc0)
  		kh = float(kh)
  		
  		

  		
  		num_c = [kp*nc2,kp*nc1,kp*nc0]
  		den_c = [dc2, dc1, dc0]
  		sys_c = tf(num_c,den_c)
  		
  		dado, x, t = bode(sys_c, Plot=False)
  		conteudo = []
  		dado = dado.tolist()
  		t = t.tolist()
  		for i in range(len(dado)):
  			conteudo.append({ 'x' : t[i], 'y': dado[i]})

  		
  		return json.dumps(conteudo)  		

# def bode_planta_fase(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz):

#   # Something
#   		Ro = float(Ro)
#   		Vi = float(Vi)
#   		L = float(L)
#   		C = float(C)
#   		kp = float(kp)
#   		nc2 = float(nc2)
#   		nc1 = float(nc1)
#   		nc0 = float(nc0)
#   		dc2 = float(dc2)
#   		dc1 = float(dc1)
#   		dc0 = float (dc0)
#   		kh = float(kh)
  		
  		

#   		rC= 0
#   		rL =0
#   		num_p = [Vi*Ro*rC*C, Vi*Ro]
#   		den_p = [L*C*(Ro+rC) ,  (L+rL*C*Ro+rL*C*rC+Ro*rC*C) ,   Ro+rL]
#   		sys_p = tf(num_p, den_p)
#       num_p1= [Vi, Vi*rC*C]
#       den_p1= [L*C, L*C*(1/(Ro*C)+rC+rL/(L)), 1]
#       sys_p1= tf[num_p1,den_p1]

#       x,dado, t = bode(sys_p1, Plot=False)
#   		conteudo = []
#   		dado = dado.tolist()
#   		t = t.tolist()
#   		for i in range(len(dado)):
#   			conteudo.append({ 'x' : t[i], 'y': dado[i]})

  		
#   		return json.dumps(conteudo)  

# def bode_controle_fase(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz):

#   # Something
#   		Ro = float(Ro)
#   		Vi = float(Vi)
#   		L = float(L)
#   		C = float(C)
#   		kp = float(kp)
#   		nc2 = float(nc2)
#   		nc1 = float(nc1)
#   		nc0 = float(nc0)
#   		dc2 = float(dc2)
#   		dc1 = float(dc1)
#   		dc0 = float (dc0)
#   		kh = float(kh)
  		
  		

#   		num_c = [kp*nc2,kp*nc1,kp*nc0]
#   		den_c = [dc2, dc1, dc0]
#   		sys_c = tf(num_c,den_c)
  		
#   		x,dado, t = bode(sys_c, Plot=False)
#   		conteudo = []
#   		dado = dado.tolist()
#   		t = t.tolist()
#   		for i in range(len(dado)):
#   			conteudo.append({ 'x' : t[i], 'y': dado[i]})

  		
#   		return json.dumps(conteudo)  				

# def bode_malha_fechada_magnitude(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz):

#   # Something
#   		Ro = float(Ro)
#   		Vi = float(Vi)
#   		L = float(L)
#   		C = float(C)
#   		kp = float(kp)
#   		nc2 = float(nc2)
#   		nc1 = float(nc1)
#   		nc0 = float(nc0)
#   		dc2 = float(dc2)
#   		dc1 = float(dc1)
#   		dc0 = float (dc0)
#   		kh = float(kh)
  		
  		

#   		rC= 0
#   		rL =0
#   		num_p = [Vi*Ro*rC*C, Vi*Ro]
#   		den_p = [L*C*(Ro+rC) ,  (L+rL*C*Ro+rL*C*rC+Ro*rC*C) ,   Ro+rL]
#   		sys_p = tf(num_p, den_p)

#   		num_c = [kp*nc2,kp*nc1,kp*nc0]
#   		den_c = [dc2, dc1, dc0]
#   		sys_c = tf(num_c,den_c)

#   		# num_h = [kh*nh2,kh*nh1,kp*nh0]
#   		# den_h = [dh2, dh1, dh0]
#   		# sys_h = tf(num_h,den_h)

#   		MF_sys = sys_p*sys_c
  		
#   		dado, x, t = bode(MF_sys, Plot=False)
#   		conteudo = []
#   		dado = dado.tolist()
#   		t = t.tolist()
#   		for i in range(len(dado)):
#   			conteudo.append({ 'x' : t[i], 'y': dado[i]})

  		
#   		return json.dumps(conteudo)

# def bode_malha_fechada_fase(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz):

#   # Something
#   		Ro = float(Ro)
#   		Vi = float(Vi)
#   		L = float(L)
#   		C = float(C)
#   		kp = float(kp)
#   		nc2 = float(nc2)
#   		nc1 = float(nc1)
#   		nc0 = float(nc0)
#   		dc2 = float(dc2)
#   		dc1 = float(dc1)
#   		dc0 = float (dc0)
#   		kh = float(kh)
  		
  		

#   		rC= 0
#   		rL =0
#   		num_p = [Vi*Ro*rC*C, Vi*Ro]
#   		den_p = [L*C*(Ro+rC) ,  (L+rL*C*Ro+rL*C*rC+Ro*rC*C) ,   Ro+rL]
#   		sys_p = tf(num_p, den_p)

#   		num_c = [kp*nc2,kp*nc1,kp*nc0]
#   		den_c = [dc2, dc1, dc0]
#   		sys_c = tf(num_c,den_c)

#   		# num_h = [kh*nh2,kh*nh1,kp*nh0]
#   		# den_h = [dh2, dh1, dh0]
#   		# sys_h = tf(num_h,den_h)

#   		MF_sys = sys_p
  		
#   		x, dado, t = bode(MF_sys, Plot=False)
#   		conteudo = []
#   		dado = dado.tolist()
#   		t = t.tolist()
#   		for i in range(len(dado)):
#   			conteudo.append({ 'x' : t[i], 'y': dado[i]})

  		
#   		return json.dumps(conteudo) 

# def bode_malha_fechada_PI_magnitude(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz):

#   # Something
#   		Ro = float(Ro)
#   		Vi = float(Vi)
#   		L = float(L)
#   		C = float(C)
#   		kp = float(kp)
#   		nc2 = float(nc2)
#   		nc1 = float(nc1)
#   		nc0 = float(nc0)
#   		dc2 = float(dc2)
#   		dc1 = float(dc1)
#   		dc0 = float (dc0)
#   		kh = float(kh)
#   		Phase_Mar = float(Phase_Mar)
#   		Freq_cruz = float(Freq_cruz)
  		
  		

#   		pi=3.14159265359
#   		rC= 0
#   		rL =0
#   		num_p = [Vi*Ro*rC*C, Vi*Ro]
#   		den_p = [L*C*(Ro+rC) ,  (L+rL*C*Ro+rL*C*rC+Ro*rC*C) ,   Ro+rL]
#   		sys_p = tf(num_p, den_p)

#   		MFRadTen = Phase_Mar*pi/180
#   		WcRadTen = [Freq_cruz*2*pi]

#   		FTLAncTen = kh*sys_p;


#   		mag, phase,x = freqresp(FTLAncTen, WcRadTen)
#   		#phase = np.array(phase).tolist()
#   		#phase = phase.tolist()
#   		#map(float, phase)
  		
#   		WzTen = float(WcRadTen[0])/(math.tan(MFRadTen - (pi/2) - phase[0] ))
#   		#WzTen = WcRadTen/(math.tan(MFRadTen - (pi/2) - 0))
#   		#KcTen = WcRadTen[0]/(math.sqrt(WcRadTen[0]^2 + WzTen[0]^2)*(mag[0]))
#   		raiz= math.sqrt(math.pow(WcRadTen[0],2 )+math.pow(WzTen,2 ))
#   		xx = float(raiz)*float(mag[0])
#   		KcTen = float(WcRadTen[0])/(xx)

#   		num_c = [KcTen, KcTen*WzTen] 
#   		den_c = [1,0]
#   		sys_c = tf(num_c,den_c)
		
#   		MF_sys = FTLAncTen*sys_c
  		
#   		dado, x, t = bode(MF_sys, Plot=False)
#   		conteudo = []
#   		dado = dado.tolist()
#   		t = t.tolist()
#   		for i in range(len(dado)):
#   			conteudo.append({ 'x' : t[i], 'y': dado[i]})

  		
#   		return json.dumps(conteudo)

# def bode_malha_fechada_PI_fase(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz):

#   # Something
#   		Ro = float(Ro)
#   		Vi = float(Vi)
#   		L = float(L)
#   		C = float(C)
#   		kp = float(kp)
#   		nc2 = float(nc2)
#   		nc1 = float(nc1)
#   		nc0 = float(nc0)
#   		dc2 = float(dc2)
#   		dc1 = float(dc1)
#   		dc0 = float (dc0)
#   		kh = float(kh)
#   		Phase_Mar = float(Phase_Mar)
#   		Freq_cruz = float(Freq_cruz)
  		
  		

#   		pi=3.14159265359
#   		rC= 0
#   		rL =0
#   		num_p = [Vi*Ro*rC*C, Vi*Ro]
#   		den_p = [L*C*(Ro+rC) ,  (L+rL*C*Ro+rL*C*rC+Ro*rC*C) ,   Ro+rL]
#   		sys_p = tf(num_p, den_p)

#   		MFRadTen = Phase_Mar*pi/180
#   		WcRadTen = [Freq_cruz*2*pi]

#   		FTLAncTen = kh*sys_p;


#   		mag, phase,x = freqresp(FTLAncTen, WcRadTen)
#   		#phase = np.array(phase).tolist()
#   		#phase = phase.tolist()
#   		#map(float, phase)
  		
#   		WzTen = float(WcRadTen[0])/(math.tan(MFRadTen - (pi/2) - phase[0] ))
#   		#WzTen = WcRadTen/(math.tan(MFRadTen - (pi/2) - 0))
#   		#KcTen = WcRadTen[0]/(math.sqrt(WcRadTen[0]^2 + WzTen[0]^2)*(mag[0]))
#   		raiz= math.sqrt(math.pow(WcRadTen[0],2 )+math.pow(WzTen,2 ))
#   		xx = float(raiz)*float(mag[0])
#   		KcTen = float(WcRadTen[0])/(xx)

#   		num_c = [KcTen, KcTen*WzTen] 
#   		den_c = [1,0]
#   		sys_c = tf(num_c,den_c)
		
#   		MF_sys = FTLAncTen*sys_c
  		
#   		x,dado,  t = bode(MF_sys, Plot=False)
#   		conteudo = []
#   		dado = dado.tolist()
#   		t = t.tolist()
#   		for i in range(len(dado)):
#   			conteudo.append({ 'x' : t[i], 'y': dado[i]})

  		
#   		return json.dumps(conteudo)  


# def goLGR_MF(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz):

#   # Something
#   		Ro = float(Ro)
#   		Vi = float(Vi)
#   		L = float(L)
#   		C = float(C)
#   		kp = float(kp)
#   		nc2 = float(nc2)
#   		nc1 = float(nc1)
#   		nc0 = float(nc0)
#   		dc2 = float(dc2)
#   		dc1 = float(dc1)
#   		dc0 = float (dc0)
#   		kh = float(kh)
#   		Phase_Mar = float(Phase_Mar)
#   		Freq_cruz = float(Freq_cruz)
  		
  		

#   		pi=3.14159265359
#   		rC= 0
#   		rL =0
#   		num_p = [Vi*Ro*rC*C, Vi*Ro]
#   		den_p = [L*C*(Ro+rC) ,  (L+rL*C*Ro+rL*C*rC+Ro*rC*C) ,   Ro+rL]
#   		sys_p = tf(num_p, den_p)

#   		MFRadTen = Phase_Mar*pi/180
#   		WcRadTen = [Freq_cruz*2*pi]

#   		FTLAncTen = kh*sys_p;


#   		mag, phase,x = freqresp(FTLAncTen, WcRadTen)
#   		#phase = np.array(phase).tolist()
#   		#phase = phase.tolist()
#   		#map(float, phase)
  		
#   		WzTen = float(WcRadTen[0])/(math.tan(MFRadTen - (pi/2) - phase[0] ))
#   		#WzTen = WcRadTen/(math.tan(MFRadTen - (pi/2) - 0))
#   		#KcTen = WcRadTen[0]/(math.sqrt(WcRadTen[0]^2 + WzTen[0]^2)*(mag[0]))
#   		raiz= math.sqrt(math.pow(WcRadTen[0],2 )+math.pow(WzTen,2 ))
#   		xx = float(raiz)*float(mag[0])
#   		KcTen = float(WcRadTen[0])/(xx)

#   		num_c = [KcTen, KcTen*WzTen] 
#   		den_c = [1,0]
#   		sys_c = tf(num_c,den_c)
		
#   		MF_sys = FTLAncTen*sys_c
#   		g=sys_p*sys_c
#   		h =tf(kh,1)
  		
#   		gc = feedback(g, h, sign=-1)
#   		a, b = root_locus(gc, kvect=np.arange(0,1000,0.5), Plot=False)
#   		conteudo = []
#   		conteudo2 = []
#   		conteudo3 = []
#   		conteudo4 = []
#   		conteudo5 = []

#   		banda = pole(gc)

#   		if ((len(banda)) == 1):
#   			for i in range(len(a)):
#   				conteudo.append({ 'x' : a[i][0].real, 'y': a[i][0].imag})

#   			return json.dumps([conteudo])

#   		elif (((len(banda))) == 2):
#   			for i in range(len(a)):
#   				conteudo.append({ 'x' : a[i][0].real, 'y': a[i][0].imag})
#   				conteudo2.append({ 'x' : a[i][1].real, 'y': a[i][1].imag})

#   			return json.dumps([conteudo, conteudo2])

#   		elif (((len(banda))) == 3):
#   			for i in range(len(a)):
#   				conteudo.append({ 'x' : a[i][0].real, 'y': a[i][0].imag})
#   				conteudo2.append({ 'x' : a[i][1].real, 'y': a[i][1].imag})
#   				conteudo3.append({ 'x' : a[i][2].real, 'y': a[i][2].imag})
#   			return json.dumps([conteudo, conteudo2, conteudo3])

#   		elif (((len(banda))) == 4):
#   			for i in range(len(a)):
#   				conteudo.append({ 'x' : a[i][0].real, 'y': a[i][0].imag})
#   				conteudo2.append({ 'x' : a[i][1].real, 'y': a[i][1].imag})
#   				conteudo3.append({ 'x' : a[i][2].real, 'y': a[i][2].imag})
#   				conteudo4.append({ 'x' : a[i][3].real, 'y': a[i][3].imag})
#   			return json.dumps([conteudo, conteudo2, conteudo3, conteudo4])

#   		else:
#   			for i in range(len(a)):
#   				conteudo.append({ 'x' : a[i][0].real, 'y': a[i][0].imag})
#   				conteudo2.append({ 'x' : a[i][1].real, 'y': a[i][1].imag})
#   				conteudo3.append({ 'x' : a[i][2].real, 'y': a[i][2].imag})
#   				conteudo4.append({ 'x' : a[i][3].real, 'y': a[i][3].imag})
#   				conteudo5.append({ 'x' : a[i][4].real, 'y': a[i][4].imag})
#   			return json.dumps([conteudo, conteudo2, conteudo3, conteudo4, conteudo5])

# def goLGR_MA(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz):

#   # Something
#   		Ro = float(Ro)
#   		Vi = float(Vi)
#   		L = float(L)
#   		C = float(C)
#   		kp = float(kp)
#   		nc2 = float(nc2)
#   		nc1 = float(nc1)
#   		nc0 = float(nc0)
#   		dc2 = float(dc2)
#   		dc1 = float(dc1)
#   		dc0 = float (dc0)
#   		kh = float(kh)
#   		Phase_Mar = float(Phase_Mar)
#   		Freq_cruz = float(Freq_cruz)
  		
  		

#   		pi=3.14159265359
#   		rC= 0
#   		rL =0
#   		num_p = [Vi*Ro*rC*C, Vi*Ro]
#   		den_p = [L*C*(Ro+rC) ,  (L+rL*C*Ro+rL*C*rC+Ro*rC*C) ,   Ro+rL]
#   		sys_p = tf(num_p, den_p)

#   		MFRadTen = Phase_Mar*pi/180
#   		WcRadTen = [Freq_cruz*2*pi]

#   		FTLAncTen = kh*sys_p;


#   		mag, phase,x = freqresp(FTLAncTen, WcRadTen)
#   		#phase = np.array(phase).tolist()
#   		#phase = phase.tolist()
#   		#map(float, phase)
  		
#   		WzTen = float(WcRadTen[0])/(math.tan(MFRadTen - (pi/2) - phase[0] ))
#   		#WzTen = WcRadTen/(math.tan(MFRadTen - (pi/2) - 0))
#   		#KcTen = WcRadTen[0]/(math.sqrt(WcRadTen[0]^2 + WzTen[0]^2)*(mag[0]))
#   		raiz= math.sqrt(math.pow(WcRadTen[0],2 )+math.pow(WzTen,2 ))
#   		xx = float(raiz)*float(mag[0])
#   		KcTen = float(WcRadTen[0])/(xx)

#   		num_c = [KcTen, KcTen*WzTen] 
#   		den_c = [1,0]
#   		sys_c = tf(num_c,den_c)
		
#   		MF_sys = FTLAncTen*sys_c
#   		g=sys_p
#   		h =tf(kh,1)
  		
#   		gc = feedback(g, h, sign=-1)
#   		a, b = root_locus(gc, kvect=np.arange(0,1000,0.5), Plot=False)
#   		conteudo = []
#   		conteudo2 = []
#   		conteudo3 = []
#   		conteudo4 = []
#   		conteudo5 = []

#   		banda = pole(gc)

#   		if ((len(banda)) == 1):
#   			for i in range(len(a)):
#   				conteudo.append({ 'x' : a[i][0].real, 'y': a[i][0].imag})

#   			return json.dumps([conteudo])

#   		elif (((len(banda))) == 2):
#   			for i in range(len(a)):
#   				conteudo.append({ 'x' : a[i][0].real, 'y': a[i][0].imag})
#   				conteudo2.append({ 'x' : a[i][1].real, 'y': a[i][1].imag})

#   			return json.dumps([conteudo, conteudo2])

#   		elif (((len(banda))) == 3):
#   			for i in range(len(a)):
#   				conteudo.append({ 'x' : a[i][0].real, 'y': a[i][0].imag})
#   				conteudo2.append({ 'x' : a[i][1].real, 'y': a[i][1].imag})
#   				conteudo3.append({ 'x' : a[i][2].real, 'y': a[i][2].imag})
#   			return json.dumps([conteudo, conteudo2, conteudo3])

#   		elif (((len(banda))) == 4):
#   			for i in range(len(a)):
#   				conteudo.append({ 'x' : a[i][0].real, 'y': a[i][0].imag})
#   				conteudo2.append({ 'x' : a[i][1].real, 'y': a[i][1].imag})
#   				conteudo3.append({ 'x' : a[i][2].real, 'y': a[i][2].imag})
#   				conteudo4.append({ 'x' : a[i][3].real, 'y': a[i][3].imag})
#   			return json.dumps([conteudo, conteudo2, conteudo3, conteudo4])

#   		else:
#   			for i in range(len(a)):
#   				conteudo.append({ 'x' : a[i][0].real, 'y': a[i][0].imag})
#   				conteudo2.append({ 'x' : a[i][1].real, 'y': a[i][1].imag})
#   				conteudo3.append({ 'x' : a[i][2].real, 'y': a[i][2].imag})
#   				conteudo4.append({ 'x' : a[i][3].real, 'y': a[i][3].imag})
#   				conteudo5.append({ 'x' : a[i][4].real, 'y': a[i][4].imag})
#   			return json.dumps([conteudo, conteudo2, conteudo3, conteudo4, conteudo5])  			  		



# def RZmap(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz):

#   # Something
#   		Ro = float(Ro)
#   		Vi = float(Vi)
#   		L = float(L)
#   		C = float(C)
#   		kp = float(kp)
#   		nc2 = float(nc2)
#   		nc1 = float(nc1)
#   		nc0 = float(nc0)
#   		dc2 = float(dc2)
#   		dc1 = float(dc1)
#   		dc0 = float (dc0)
#   		kh = float(kh)
  		
  		

#   		rC= 0
#   		rL =0
#   		num_p = [0,Vi*Ro*rC*C, Vi*Ro]
#   		den_p = [L*C*(Ro+rC) ,  (L+rL*C*Ro+rL*C*rC+Ro*rC*C) ,   Ro+rL]
#   		sys_p = tf(num_p, den_p)
  		
#   		polos, zeros = pzmap(sys_p, Plot=False)
#   		conteudo = []
#   		conteudo2 = []

#   		polos = polos.tolist()
#   		zeros = zeros.tolist()
  		

#   		for i in range(len(polos)):
#   			conteudo.append({ 'x' : polos[i].real, 'y': polos[i].imag})

#   		for i in range(len(zeros)):
#   			conteudo2.append({ 'x' : zeros[i].real, 'y': zeros[i].imag})

#   		return json.dumps([conteudo,conteudo2])

# # 
# # 

# def step_MF():

#   # Something

#   		Ro = 1.52
#   		Vi = 160
#   		L = 0.000336
#   		C = 0.0000066
  		  		
  		
  		
#   		pi=3.14159265359
#   		rC= 0
#   		rL =0
#   		num_p = [Vi*Ro*rC*C, Vi*Ro]
#   		den_p = [L*C*(Ro+rC) ,  (L+rL*C*Ro+rL*C*rC+Ro*rC*C) ,   Ro+rL]
#   		sys_p = tf(num_p, den_p)

  		
  		

#   		dado, t = step(sys_p, Plot=False)
#   		conteudo = []
#   		dado = dado.tolist()
#   		t = t.tolist()

  		

#   		for i in range(len(dado)):
#   			conteudo.append({ 'x' : t[i], 'y': dado[i]})

  		
#   		return json.dumps(conteudo)


# def Cal_PI(Vi,Ro,L,C,kp,kh,nc2,nc1,nc0,dc2,dc1,dc0,Phase_Mar,Freq_cruz):

#   # Something
#   		Ro = float(Ro)
#   		Vi = float(Vi)
#   		L = float(L)
#   		C = float(C)
#   		kp = float(kp)
#   		nc2 = float(nc2)
#   		nc1 = float(nc1)
#   		nc0 = float(nc0)
#   		dc2 = float(dc2)
#   		dc1 = float(dc1)
#   		dc0 = float (dc0)
#   		kh = float(kh)
#   		Phase_Mar = float(Phase_Mar)
#   		Freq_cruz = float(Freq_cruz)
  		
  		
#   		dt = 1/5000
#   		pi=3.14159265359
#   		rC= 0
#   		rL =0
#   		num_p = [Vi*Ro*rC*C, Vi*Ro]
#   		den_p = [L*C*(Ro+rC) ,  (L+rL*C*Ro+rL*C*rC+Ro*rC*C) ,   Ro+rL]
#   		sys_p = tf(num_p, den_p,dt)

#   		MFRadTen = Phase_Mar*pi/180
#   		WcRadTen = [Freq_cruz*2*pi]

#   		FTLAncTen = kh*sys_p;


#   		mag, phase,x = freqresp(FTLAncTen, WcRadTen)
#   		#phase = np.array(phase).tolist()
#   		#phase = phase.tolist()
#   		#map(float, phase)
  		
#   		WzTen = float(WcRadTen[0])/(math.tan(MFRadTen - (pi/2) - phase[0] ))
#   		#WzTen = WcRadTen/(math.tan(MFRadTen - (pi/2) - 0))
#   		#KcTen = WcRadTen[0]/(math.sqrt(WcRadTen[0]^2 + WzTen[0]^2)*(mag[0]))
#   		raiz= math.sqrt(math.pow(WcRadTen[0],2 )+math.pow(WzTen,2 ))
#   		xx = float(raiz)*float(mag[0])
#   		KcTen = float(WcRadTen[0])/(xx)

#   		num_c = [KcTen, KcTen*WzTen] 

#   		s = Symbol("x")
#   		#FTControleTen = KcTen * (s+WzTen)/s;
#   		PI = KcTen *(s+WzTen)/s 
#   		#PI_eq = latex(PI)
  		

  		

  		

  		
#   		return json.dumps(num_c)  		 
