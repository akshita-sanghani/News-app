"""
URL configuration for wscubetech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from wscubetech import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aboutus/', views.aboutUs),
    path('course/<courseid>', views.courseId),
    path('', views.homePage, name='home'),
    path('about-us/', views.about, name='about-us'),
    path('post/', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('userform/', views.userForm, name='userform'),
    path('submitform/', views.submitForm, name='submitform'),
    path('calculator/', views.calculator),
    path('evenodd/', views.evenodd),
    path('marksheet/', views.marksheet),
    path('validation/', views.validation),
    path('newsDetails/<slug>',views.newsDetails),
    path('saveenquiry/',views.saveEnquiry, name='saveenquiry')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)