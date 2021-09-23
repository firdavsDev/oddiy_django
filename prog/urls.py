from django.urls import path
from .views import HomePageView,OnlineQabulView,YangliklarView,BizHaqimizdaView

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('qabul/',OnlineQabulView.as_view(),name='qabul'),
    path('news/',YangliklarView.as_view(),name='news'),
    path('haqimizda',BizHaqimizdaView.as_view(),name='haqida')
]

