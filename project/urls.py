from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.http import HttpResponse

def health(request):
    return HttpResponse('health')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health, name="health"),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    # path('viewprofile/', views.viewprofile, name='viewprofiles'),
    path('viewprofile/', views.profile, name='profile'),
    path('deleteprofile/', views.deleteprofile, name='deleteprofiles'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('stock/',include('stocksearch.urls')),
    path('help/', views.help, name='help'),
]
