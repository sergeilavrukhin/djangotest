from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from . import views
from .components.accounts.views import accounts_list, account_one

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/list/', accounts_list, name='accounts_list'),
    path('accounts/one/<id>/', account_one, name='account_one'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)