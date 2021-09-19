from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from . import views
from .components.accounts.views import accounts_list, account_detail, account_send, account_movements, AccountListDRF

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/list/', accounts_list, name='accounts_list'),
    path('accounts/detail/<id>/', account_detail, name='account_detail'),
    path('accounts/send/', account_send, name='account_send'),
    path('accounts/movements/', account_movements, name='account_movements'),
    path('accounts/listdrf/', AccountListDRF.as_view(), name='account_list_drf'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)