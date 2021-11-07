from django.conf.urls import url
from .views import loginface, returnface

urlpatterns = [
	url(r'^face/$', loginface.as_view(), name="loginface"),
	url(r'^returnface/$', returnface.as_view(), name="returnface"),	
]