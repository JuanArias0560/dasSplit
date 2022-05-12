from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="split"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("feed/",views.feed, name="feed"),
    path("cuentas/",views.cuentas, name="cuentas"),
    path("register/",views.register_request, name="register"),
    path("login/",views.login_request, name="login"),
    path("logout/",views.logout_request, name="logout"),
    path("cuentas/",views.cuentas, name="cuentas"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
