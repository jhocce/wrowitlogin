import requests

from django.shortcuts import render
from django.views.generic import ListView, View, RedirectView
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adrule import AdRule
from facebook_business.api import FacebookAdsApi




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
		
		# code = self.request.GET.get('code')

		# Copyright 2014 Facebook, Inc.

		
		
		# access_token = code
		client_id = '457901605665005'
		client_secret = 'f5f111abebde1a9a94ae282de45ce0ef'
		code = self.request.GET.get('code')
		redirect_uri = 'https://wrowit.herokuapp.com/login/returnface/'
		url_auth = 'https://graph.facebook.com/v12.0/oauth/access_token'
		# auth_data = {
		#  'client_id':client_id,
		#  'client_secret':client_secret,
		#  'code':code,
		#  'redirect_uri':redirect_uri
		#  }

		# se pide el access_token.
		resp = requests.get('{0}?client_id={1}&client_secret={2}&code={3}&redirect_uri={4}'.format(url_auth, client_id, client_secret, code, redirect_uri ) )

		try:
			print("Response---->>> ",resp.json())
			return HttpResponse(resp.json())
			# obj = Permisos(**resp.json())
			# obj.save()
			# access_token = resp.json()['access_token']
		except Exception as e:
			print(e)
			return HttpResponse(e)

		# First we try to get all pages from a user
		# fields = [
		#     'access_token',
		# ]
		# params = {
		# }
		# pages = User(<USER_ID>).get_accounts(
		#     fields=fields,
		#     params=params,
		# )
		# page_id = pages[0].get_id()
		# print(pages[0].get_id())

		# # Then we get first page's insight using page access token
		# FacebookAdsApi.init(<ACCESS_TOKEN>=pages[0]["access_token"])
		# fields = [
		# ]
		# params = {
		#     'metric': 'page_fan_adds',
		# }
		# insights = Page(page_id).get_insights(
		#     fields=fields,
		#     params=params,
		# )
		# FacebookAdsApi.init(<ACCESS_TOKEN>=access_token)


		# app_secret = 'f5f111abebde1a9a94ae282de45ce0ef'
		# ad_account_id = 'act_174036684896239'
		# schedule_interval = 'DAILY'
		# entity_type = 'CAMPAIGN'
		# notification_user_id = '4453085001435900'
		# filter_field = 'reach'
		# filter_value = '1'
		# filter_operator = 'GREATER_THAN'
		# app_id = '457901605665005'
		# FacebookAdsApi.init(access_token=access_token)

		# fields = [
		# ]
		# params = {
		#     'name': 'Sample SDK Rule',
		#     'schedule_spec': { 'schedule_type': schedule_interval },
		#     'evaluation_spec': { 'evaluation_type': 'SCHEDULE', 'filters': [ { 'field': filter_field, 'value': filter_value, 'operator': filter_operator }, { 'field': 'entity_type', 'value': entity_type, 'operator': 'EQUAL' }, { 'field': 'time_preset', 'value': 'LIFETIME', 'operator': 'EQUAL' } ] },
		#     'execution_spec': { 'execution_type': 'NOTIFICATION', 'execution_options': [ { 'field': 'user_ids', 'value': [notification_user_id], 'operator': 'EQUAL' } ] },
		# }
		# print( )


		# return HttpResponse("prueba->{0}".format(AdAccount(ad_account_id).create_ad_rules_library(
		#     fields=fields,
		#     params=params,
		# )))
