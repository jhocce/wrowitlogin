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
		    scopes = ('https://www.googleapis.com/auth/adwords', 'https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email', 'openid')
		     )
		flow.redirect_uri = 'https://wrowit.herokuapp.com/google/redirect/'
		authorization_url, state = flow.authorization_url(
		access_type='offline',
		include_granted_scopes='true')
		return HttpResponseRedirect(authorization_url)

# email+profile+https://www.googleapis.com/auth/userinfo.email+https://www.googleapis.com/auth/adwords+https://www.googleapis.com/auth/userinfo.profile+openid




class redirectgo(View):

	template_name = ''

	def dispatch(self, request, *args, **kwargs):
		
		return super(redirectgo, self).dispatch(request,*args, **kwargs )


	def GetRefreshToken(self, code, obj):


		# flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
		# 		'client_secret.json',
		# 		scopes=['https://www.googleapis.com/auth/drive.metadata.readonly'],
		# 		state=state)
		# flow.redirect_uri = 'https://wrowit.herokuapp.com/google/redirect/'

		# authorization_response = self.request.url
		# flow.fetch_token(authorization_response=authorization_response)

		# credentials = flow.credentials
		# print("--------------> ", dir(credentials))
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
		# print(data)
		res = requests.post(url=url, data=data, headers = headers)
		return res


	def GetUser(self, token):
		try:
			print("llllllllllllllllllllllls")
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
		# print(dir(credentialsa))
		print("--------------------------------")
		print("--------------------------------")
		print("--------------------------------")
		print("--------------------------------")
		print(self.GetRefreshToken(code=code, obj=credentialsa ) )
		# print(credentialsa.token)

		# json_dat = credentialsa.to_json()
		json_dat = self.GetUser(token=credentialsa.token )

		return HttpResponse("---->> {0} ".format(json_dat) )
# refresh_token
# token
# scopes
# client_secret
# client_id
# expiry

# implimentar multidioma 

# *** con migo **

# monto iniciar a subastar 100k

# corroborar la identidad del subastador antes de publicar su oferta


