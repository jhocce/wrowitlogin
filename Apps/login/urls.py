from django.conf.urls import url
from .views import loginface, returnface

urlpatterns = [
	url(r'^face/$', loginface.as_view(), name="loginface"),
	url(r'^returnface/$', returnface.as_view(), name="returnface"),
	# url(r'^ver/(?P<pk_publica>[^/]+)/$', DetallarProducto.as_view(), name="ver"),
	# url(r'^eliminar/$', CrearUserView.as_view(), name="eliminar"),

	
]