from django.contrib import admin
from django.urls import path
from Quiz.views import *
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home,name='home'),
    path('addQuestion/', addQuestion,name='addQuestion'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)