from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('shop.urls', namespace='shop')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':
    settings.MEDIA_ROOT}), #serve media files when deployed
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':
    settings.STATIC_ROOT}), #serve static files when deployed


    path('', include('register.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
