from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('teampsbox.urls')),
    path('psblog/', include('psblog.urls')),
    path('accounts/', include('accounts.urls')),

]
