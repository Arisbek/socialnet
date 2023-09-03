"""
URL configuration for socialnet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from core.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('home/', homepage),
    path('shop/contacts/', contacts),
    path('shop/about_us/', about_us),
    path('short/<int:id>/',short_info,name='short'),
    path('shorts/',shorts,name='shorts'),
    path('category/<int:id>/',Category_info,name='category'),
    path('categories/',Categories,name='categories'),
    path('post/<int:id>/',post_info,name='post'),
    path('posts/', posts, name='posts'),
    path('saved_posts/',savedposts,name='saved-posts'),
    path('comments/', comment),
    path('profile/<int:id>/', profile, name='profile'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)