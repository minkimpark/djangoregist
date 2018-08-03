from django.urls import path
from django.conf.urls import url

from .djangoapps.registview import views as RegistViews
from .djangoapps.registok import views as RegistOk

urlpatterns =[
    url('registview$',RegistViews.registview, name='registview'),
    url('api_regist_create$',RegistOk.registok, name='registok'),

    url('login$',RegistViews.login, name='login')
]
