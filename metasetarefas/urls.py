"""metasetarefas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from metas.views import home, listagem, nova_tarefa, update, delete, lista_contatos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('listagem/', listagem, name='url_listagem'),
    path('nova_tarefa/', nova_tarefa, name='url_nova_tarefa'),
    path('update/<int:pk>/', update, name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete'),
    path('lista_contatos/', lista_contatos, name='url_lista_contatos'),
    path('accounts/', include('django.contrib.auth.urls')),
]
