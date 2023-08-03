from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('<operação>/<int:n1>/<int:n2>', views.operação),
]
