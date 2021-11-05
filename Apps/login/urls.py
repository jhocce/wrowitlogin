from django.conf.urls import url
from .views import loginface

urlpatterns = [
	url(r'^face/$', loginface.as_view(), name="loginface"),
	# url(r'^subir/$', CrearProducto1View.as_view(), name="subir"),
	# url(r'^ver/(?P<pk_publica>[^/]+)/$', DetallarProducto.as_view(), name="ver"),
	# url(r'^eliminar/$', CrearUserView.as_view(), name="eliminar"),

	
]