from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import TemplateView
from project.todo import urls

urlpatterns = (
    [
        path("", TemplateView.as_view(template_name="home.html"), name="home"),
        path("login", auth_views.LoginView.as_view(), name="login"),
        path("logout", auth_views.LogoutView.as_view(), name="logout"),
        path("gtdadmin/", admin.site.urls),
        path("todo/", include(urls, namespace="todo")),
        path("403/", TemplateView.as_view(template_name="403.html"), name="403"),
        path("404/", TemplateView.as_view(template_name="404.html"), name="404"),
        path("500/", TemplateView.as_view(template_name="500.html"), name="500"),
    ]
    # Static media in DEBUG mode:
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

