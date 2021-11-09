import requests
from urllib.parse import urlencode

from collections import deque

from django.shortcuts import render
from django.views.generic import ListView, View, RedirectView
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleads import oauth2

# from .models import PermisosF



class googlev(View):
	""" Esta vista solo sirve para la comprobacion del servidor 
	algo que no se si esta relacionado al nombre del servidor o solo
	es un archivo de comprobacion generico pendiente de la ubicacion 
	de este archivo en los template, no se como manejan ustedes esa parte """
	template_name = 'googlee41be98abcadb5cd.html'


	def dispatch(self, request, *args, **kwargs):
		
		return super(googlev, self).dispatch(request,*args, **kwargs )
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name ,{})

class goo(View):
	""" Con esta vista inicia el proceso de autenticacion 
	como vez no necesita template porque solo esta para pasar un 
	HttpResponseRedirect si quieres la modificas para que admit la 
	vista generica RedirectView """

	template_name = ''


	def dispatch(self, request, *args, **kwargs):
		
		return super(goo, self).dispatch(request,*args, **kwargs )
	def get(self, request, *args, **kwargs):
		""" ubicar el archivo client_secret.json en el directorio raiz del 
		proyecto alli se almacenan las credenciales  """
		flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
		   client_secrets_file='client_secret.json',
		    scopes = ('https://www.googleapis.com/auth/adwords', 'https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email', 'openid')
		     )
		flow.redirect_uri = 'https://wrowit.herokuapp.com/google/redirect/'
		authorization_url, state = flow.authorization_url(
		access_type='offline',
		include_granted_scopes='true')
		return HttpResponseRedirect(authorization_url)



class redirectgo(View):
	""" Esta vista solo nos sirve para recibir los parametros por url 
	para poder pedir el refresh token y consumir el API """

	template_name = ''

	def dispatch(self, request, *args, **kwargs):
		
		return super(redirectgo, self).dispatch(request,*args, **kwargs )


	def GetRefreshToken(self, code, obj):
		""" no sirve esta es la que falta por arreglar!. """

		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

		url = 'https://oauth2.googleapis.com/token'
		token = obj.token
		client_secret = obj.client_secret
		client_id = obj.client_id
		redirect_uri = 'https://wrowit.herokuapp.com/google/redirect/'
		data = { 
			'code' : code,
			'client_id' : client_id,
			'client_secret' : client_secret,
			'redirect_uri' : redirect_uri,
			'grant_type' : 'authorization_code'
			}
		res = requests.post(url=url, data=data, headers = headers)
		return res


	def GetUser(self, token):
		""" Con esta función se obtienen los datos del usuario 
			que a iniciado sesion """
		try:
			resp = requests.get('https://www.googleapis.com/oauth2/v1/userinfo?access_token={0}'.format(token))
			print(resp.content )
		except Exception as e:
			raise e
		return resp.content

	def get(self, request, *args, **kwargs):

		code = self.request.GET.get('code')
		state = self.request.GET.get('state')
		scope = self.request.GET.get('scope')

		flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
		   client_secrets_file='client_secret.json',
		   scopes = ('https://www.googleapis.com/auth/adwords', 'https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email', 'openid')
		     )
		flow.redirect_uri = 'https://wrowit.herokuapp.com/google/redirect/'
		flow.fetch_token(code=code)
		credentialsa = flow.credentials

		# deprecada
		# print(self.GetRefreshToken(code=code, obj=credentialsa ) )

		""" aca se procede a guardar y procesar las credenciales pero como
		la funcion self.GetRefreshToken() no esta completa no se implementa

		pero una ves terminada lo ideal seria guardar el token_access y proceder
		 a pedir los datos del usuario que en este caso se hace con la funcion 
		 self.GetUser() 

		 como proceder aca? puede ser redirigir al usuario a una pantalla que diga 
		 que esta registrado con google y que proceda con determinar la contraseña 
		 en wrowit, de momento en las lineas que sigue solo renderiza la respuesta 
		 en el navegador """

		

		json_dat = self.GetUser(token=credentialsa.token )

		return HttpResponse("---->> {0} ".format(json_dat) )



