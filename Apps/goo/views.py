import requests
from urllib.parse import urlencode

from django.shortcuts import render
from django.views.generic import ListView, View, RedirectView
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleads import oauth2

# from .models import PermisosF



class googlev(View):

	template_name = 'googlee41be98abcadb5cd.html'


	def dispatch(self, request, *args, **kwargs):
		
		return super(googlev, self).dispatch(request,*args, **kwargs )
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name ,{})

class goo(View):

	template_name = ''


	def dispatch(self, request, *args, **kwargs):
		
		return super(goo, self).dispatch(request,*args, **kwargs )
	def get(self, request, *args, **kwargs):

		# https://wrowit.herokuapp.com/google/redirect/

		flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
		   client_secrets_file='client_secret.json',
		    scopes=[oauth2.GetAPIScope('adwords'), 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile'])
		flow.redirect_uri = 'https://wrowit.herokuapp.com/google/redirect/'
		authorization_url, state = flow.authorization_url(
		access_type='offline',
		include_granted_scopes='true')
		return HttpResponseRedirect(authorization_url)




class redirectgo(View):

	template_name = ''
	def dispatch(self, request, *args, **kwargs):
		
		return super(redirectgo, self).dispatch(request,*args, **kwargs )
	def get(self, request, *args, **kwargs):

		code = self.request.GET.get('code')
		state = self.request.GET.get('state')
		scope = self.request.GET.get('scope')

		# flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
		#    client_secrets_file='client_secret.json',
		#     scopes=[oauth2.GetAPIScope('adwords')])
		# go = flow.fetch_token(code=code)
		
		# credentials = go.credentials

		# try:
		# 	data = requests.post('https://www.googleapis.com/oauth2/v4/token',
		# 		{
		# 			'code' : code,
		# 			'client_id' : '558376713536-hehho8pmk7lcbn7vumtmstikpjat85s6.apps.googleusercontent.com',
		# 			'client_secret' : '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',
		# 			'redirect_uri' : 'https://wrowit.herokuapp.com/',
		# 			'grant_type' : 'authorization_code'
		# 		})
		# 	print("--------", data.json() )
		# except Exception as e:
		# 	data = e
		flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
		   client_secrets_file='client_secret.json',
		     # scopes=[oauth2.GetAPIScope('adwords'), 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
		     )
		flow.redirect_uri = 'https://wrowit.herokuapp.com/google/redirect/'

		p= flow.fetch_token(code=code)
		print('----->>>', p)
		credentials = flow.credentials

		return HttpResponse("---->> {0} ", credentials )




# implimentar multidioma 

# *** con migo **

# monto iniciar a subastar 100k

# corroborar la identidad del subastador antes de publicar su oferta


