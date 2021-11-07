from django.conf.urls import url
from .views import loginface, returnface, googlev, goo

urlpatterns = [
	url(r'^face/$', loginface.as_view(), name="loginface"),
	url(r'^returnface/$', returnface.as_view(), name="returnface"),
	url(r'^googlee41be98abcadb5cd.html$', googlev.as_view(), name="googlev"),


	# url(r'^ver/(?P<pk_publica>[^/]+)/$', DetallarProducto.as_view(), name="ver"),
	# url(r'^eliminar/$', CrearUserView.as_view(), name="eliminar"),

	
]