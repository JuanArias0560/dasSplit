from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="split"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("feed/",views.feed, name="feed"),
    path("pockets/",views.pocket, name="pocket"),
    path("payments/",views.payment, name="payment"),
    path("charges/",views.charge, name="charge"),
    path("register/",views.register_request, name="register"),
    path("login/",views.login_request, name="login"),
    path("logout/",views.logout_request, name="logout"),
    path("show_pocket/<pocket_id>",views.show_pocket, name='show-pocket'),    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
