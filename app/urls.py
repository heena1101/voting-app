from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('', views.landing, name="landing"),
    path('index',views.index,name="index"),
    path('selected/<int:choice_id>',views.selected,name="selected"),
    path('login',views.login_page,name='login_page'),
    path('logout',views.logout_user,name='logout'),
    path('signup',views.signup,name='signup'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)