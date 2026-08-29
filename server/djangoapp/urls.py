from django.urls import path,re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
    path('register/', TemplateView.as_view(template_name="index.html")),

    # path for login
    path(route='login', view=views.login_user, name='login'),
    path('login/', TemplateView.as_view(template_name="index.html")),
    path('logout/', views.logout_request, name='logout'),
    
    # path for dealer reviews view

    # path for add a review view

    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
