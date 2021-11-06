from django.conf.urls import url
from .views import loginface, returnface, googlev

urlpatterns = [
	url(r'^face/$', loginface.as_view(), name="loginface"),
	url(r'^returnface/$', returnface.as_view(), name="returnface"),
	url(r'^$', googlev.as_view(), name="googlev"),

	# url(r'^ver/(?P<pk_publica>[^/]+)/$', DetallarProducto.as_view(), name="ver"),
	# url(r'^eliminar/$', CrearUserView.as_view(), name="eliminar"),

	
]