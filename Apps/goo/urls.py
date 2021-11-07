
from django.conf.urls import url
from .views import goo, googlev, redirectgo

urlpatterns = [

	url(r'^goo/$', goo.as_view(), name="goo"),
	url(r'^redirect/$', redirectgo.as_view(), name="redirectgo"),
	url(r'^googlee41be98abcadb5cd.html$', googlev.as_view(), name="googlev"),
	# url(r'^face/$', loginface.as_view(), name="loginface"),
	# url(r'^returnface/$', returnface.as_view(), name="returnface"),
	# url(r'^googlee41be98abcadb5cd.html$', googlev.as_view(), name="googlev"),


	# url(r'^ver/(?P<pk_publica>[^/]+)/$', DetallarProducto.as_view(), name="ver"),
	# url(r'^eliminar/$', CrearUserView.as_view(), name="eliminar"),

	
]

	

