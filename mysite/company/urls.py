from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    re_path(r'^news/.+', views.news),
    path('activity/', views.activity, name='activity'),
    re_path(r'^activity/.+', views.activity),
    path('contacts/', views.contacts, name='contacts'),
    re_path(r'^contacts/.+', views.contacts),
    path('management/', views.management, name='management'),
    path('management/', include([
        path('gogol/', views.gogol, name='gogol'),
        path('stus/', views.stus, name='stus'),
        path('smith/', views.smith, name='smith'),
    ])),
    re_path(r'^management/.+', views.management),
]
