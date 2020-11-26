"""CBVbookpro URL Configuration

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
from django.urls import path
from books.views import ListBook,CreateBook,ViewDetails,UpdateBook,DeleteBook
urlpatterns = [
    path('admin/', admin.site.urls),
    path('listbook/',ListBook.as_view(),name="list"),
    path('createbook/',CreateBook.as_view(),name="create"),
    path('update/<int:pk>',UpdateBook.as_view(),name="update"),
    path('deatils/<int:pk>',ViewDetails.as_view(),name="view"),
    path('delete/<int:pk>',DeleteBook.as_view(),name="delete")

]
