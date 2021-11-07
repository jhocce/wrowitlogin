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

class goo(View):

	template_name = ''


	def dispatch(self, request, *args, **kwargs):
		
		return super(goo, self).dispatch(request,*args, **kwargs )
	def get(self, request, *args, **kwargs):

		# https://wrowit.herokuapp.com/google/redirect/

		flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
		   client_secrets_file='client_secret.json',
		    scopes=[oauth2.GetAPIScope('adwords')])
		flow.redirect_uri = 'https://wrowit.herokuapp.com/google/redirect/'
		authorization_url, state = flow.authorization_url(
		access_type='offline',
		include_granted_scopes='true')
		return HttpResponseRedirect(authorization_url)




class redirect(View):

	template_name = ''
	def dispatch(self, request, *args, **kwargs):
		
		return super(redirect, self).dispatch(request,*args, **kwargs )
	def get(self, request, *args, **kwargs):

		code = self.request.GET.get('code')
		state = self.request.GET.get('state')
		scope = self.request.GET.get('scope')


		return HttpResponse("{0} <br> {1} <br> {3}".format(code, state, scope) )