import requests

from django.shortcuts import render
from django.views.generic import ListView, View, RedirectView
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect



class loginface(View):

	""" Esto es solo una vista de redirecionamiento puedes usar la vista redirecwiew generica
		si lo deseas el resultado deberia ser lo mismo, no hay que modificar estos valores 
		pues representan las credenciales definidas en la aplicacion creada en el 
		servidor de aliexpress. """


	template_name = 'index.html'

	def dispatch(self, request, *args, **kwargs):
		
		return super(loginface, self).dispatch(request,*args, **kwargs )

	def get(self, request, *args, **kwargs):
		# https://www.facebook.com/v12.0/dialog/oauth?
		#   client_id={app-id}
		#   &redirect_uri={redirect-uri}
		#   &state={state-param}


		client_id = '457901605665005'
		secret = 'f5f111abebde1a9a94ae282de45ce0ef'
		url = ''
		
		url_autorizacion = 'https://www.facebook.com/v12.0/dialog/oauth'
		redirect_uri = 'https://wrowit.herokuapp.com/login/returnface/'
		return HttpResponseRedirect("{0}?response_type=code&client_id={1}&redirect_uri={2}&state=1212".format(url_autorizacion,client_id,redirect_uri ))




class returnface(View):
	""" Vista que recibe la peticion desde el servidor de amazon con los datos necesarios
	para generar el acces_token el cual debe ser guardado en la base de datos para futuras 
	peticiones.
	"""

	template_name = 'ali/index.html'
	
	def dispatch(self, request, *args, **kwargs):


		return super(returnface, self).dispatch(request,*args, **kwargs )
	def get(self, request,  *args, **kwargs):
		
		code = self.request.GET.get('code')
		return HttpResponse("prueba->", code)

		appkey = '32934847'
		secret = 'c394309ac3257ee7790787e19c6ca07d'
		url_auth = 'https://oauth.aliexpress.com/token';
		auth_data = {
		 'grant_type':'authorization_code',
		 'client_id':appkey,
		 'client_secret':secret,
		 'code':code,
		 'sp':'ae',
		 'redirect_uri':'redirect_uri'
		 }

		# se pide el access_token.
		resp = requests.post(url_auth, data=auth_data )

		try:
			print("Response---->>> ",resp.json())
			obj = Permisos(**resp.json())
			obj.save()
			access_token = resp.json()['access_token']
		except Exception as e:
			print(e)
			return HttpResponse("Ya no puedes iniciar sesion desde este enlace... ")





# code=AQAKsoeFqLl8uncyc3nHP7BO3yPOfoH-y9b6iLOj_4HZWObC4C1yZB-kShxGAXSorKJPF1ncvUseMcoDVRw2mkhUELFpS7rFcq4vh3n-6SbTkjo9d-NrkYyCZwcUJ8rpC8w5SBVYnLo1L5Kp_4_ZKpqtpMZEOmu1R36Kw7LoqIbcHVYUDmVDLc38dKuEzS9-Sq8Bhw7lYkNaDcdFayQPDxcP5fBLVLXSWn0yOeNd-8nYuMp9R3SfI1yW0AxxMPG6mPNJ-iYz5aV5rieXBWX0SzNfyhuM3d29i8Mq5GTmQcUa7bOGLtiSecGP3hM_i98aLANi8NLWCIw3OPKbd2at-6mWQcQzgHvamUnDxOILVMoWPWc6on8Z4ux9g6sNH5tpPn0
# &state=1212#_=_