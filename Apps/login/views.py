import requests
from urllib.parse import urlencode

from django.shortcuts import render
from django.views.generic import ListView, View, RedirectView
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adrule import AdRule
from facebook_business.api import FacebookAdsApi

from .models import PermisosF


class loginface(View):

	""" vista que inicia el proceso de autenticacion por acceso a url """


	template_name = 'index.html'

	def dispatch(self, request, *args, **kwargs):
		
		return super(loginface, self).dispatch(request,*args, **kwargs )

	def get(self, request, *args, **kwargs):
		
		# datos de la app
		client_id = '457901605665005'
		secret = 'f5f111abebde1a9a94ae282de45ce0ef'
		url = ''
		
		url_autorizacion = 'https://www.facebook.com/v12.0/dialog/oauth'
		redirect_uri = 'https://wrowit.herokuapp.com/login/returnface/'
		return HttpResponseRedirect("{0}?response_type=code&client_id={1}&redirect_uri={2}&state=1212&scope=email".format(url_autorizacion,client_id,redirect_uri ))



class returnface(View):
	""" Esta vista solo nos sirve para recibir los parametros por url 
	para poder pedir el refresh token y consumir el API """

	template_name = 'ali/index.html'
	
	def dispatch(self, request, *args, **kwargs):


		return super(returnface, self).dispatch(request,*args, **kwargs )

	def GetUser(self, access_token):
		""" Funcion de obtiene los datos del usuario que nos dio autorizacion """
		# url de la peticion
		url = 'https://graph.facebook.com/me?'
		# campos que se esperan consultar
		campos = 'id,name,email,first_name,last_name,gender,languages'
		resp = requests.get("{0}fields={1}&access_token={2}".format(url, campos, access_token))
		return resp.json()
		# https://graph.facebook.com/4453085001435900?fields=email&access_token=EAAGgdYaMOO0BAOOY3wwxS4SWDx5pgUEWiZAqZAzyPYnuvmjthlOpF76QHnqqD2XPtBDjwfN3F2lXN5fWmLcFsmcSXgT4SzjxZChEjgH6nbZBhm7qvqaIdAsMmZBxEP2NTcrnfm38nbJY10lDsqkNalEmJ8jjHrgwDB77bZAeZClZCvBb0bQGVmm2okaZAWqe1v7K1TWZA23kmyygZDZD

	def get(self, request,  *args, **kwargs):
		# datos de la app otra vez...
		client_id = '457901605665005'
		client_secret = 'f5f111abebde1a9a94ae282de45ce0ef'
		# obtener codigo de autorizacion de la redireccion
		code = self.request.GET.get('code')
		# URL de redireccion
		redirect_uri = 'https://wrowit.herokuapp.com/login/returnface/'
		# Url de autorizacion
		url_auth = 'https://graph.facebook.com/v12.0/oauth/access_token'

		resp = requests.get('{0}?client_id={1}&client_secret={2}&code={3}&redirect_uri={4}'.format(url_auth, client_id, client_secret, code, redirect_uri ) )

		try:	
			# guardar los permisos
			obj = PermisosF(**resp.json())
			obj.save()

			# Este es el token de acceso para consumir el api mas delante cuando
			# entremos en fase 2
			access_token = resp.json()['access_token']

			# datos de usuario que nos dio permisos
			datos = self.GetUser(access_token=access_token)
			a = urlencode(datos)
			return HttpResponse(a)

		except Exception as e:
			print(e)
			return HttpResponse(e)





		# access_token = 'EAAGgdYaMOO0BAFz0I9ZA8TiN6xGCWmoMU1m5ZAeZAxoR6cOgbVkBmgqZB1ZBt0dcNmKpRrB8hIhNjeQUNkZCsQHH1mH22txCXdc7BE5ZApn1JZCdkSfIFM4AYSJuOq0yZAA4UshssNsZBcSKSvPZCLz0MKdZCWPwteUhCVvKHbzfZB4gl8FZBlTRaksPmBNYE8BpTMJXNaNxcPqUiPoeIdhEZAm3UNXp0fwbzOpM6BF3S491z5RwQZDZD'
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
