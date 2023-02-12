from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('ssession',views.setsession),
    # path('getsession',views.getsession)
    path('create/', views.create_session),
    path('access/', views.access_session)
]
