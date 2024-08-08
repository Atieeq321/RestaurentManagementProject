from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('', views.Home,  name="home"),
    path('order/<int:table_id>/<int:menu_item_id>/', views.Order, name='order'),
    path("base/", views.Base, name="base")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)