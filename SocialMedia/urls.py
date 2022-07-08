from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage.as_view(),name='home'),
    path('user_app/',include('user_app.urls',namespace='user_app')),
    path('user_app/',include('django.contrib.auth.urls')),
    path('test/',views.TestPage.as_view(),name='test'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),
    path('posts/', include("posts.urls", namespace="posts")),
    path('groups/',include("groups.urls", namespace="groups")),
]
