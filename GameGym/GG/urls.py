from django.urls import path, include
from . import views
# from .views import LoginUser

urlpatterns = [
    path('', views.index, name='home'),
    # path('bron/', views.BronPc.as_view(), name='bron'),
    path('map/', views.PCListView.as_view(), name = 'map'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('bron/', views.Bron.as_view(), name = 'bron'),
    path('info/', views.info, name = 'info'),
    #path('connect/', views.connect, name = 'connect'),
    path('connect/', views.back_connect.as_view(), name = 'connect'),
]
