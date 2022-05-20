from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name="split"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("feed/",views.feed, name="feed"),
    path("myprofile/",views.myprofile, name="profile"),
    path("pockets/",views.pocket, name="pocket"),
    path("payments/<pocket_id>",views.payment, name="payment"),
    path("charges/<pocket_id>",views.charge, name="charge"),
    path("register/",views.register_request, name="register"),
    path("login/",views.login_request, name="login"),
    path("logout/",views.logout_request, name="logout"),
    path("show_pocket/<pocket_id>",views.show_pocket, name='show-pocket'),  
    path("update_charge/<charge_id>/<pocket_id>",views.update_charge, name="update-charge"),
    path("delete_charge/<charge_id>/<pocket_id>",views.delete_charge, name="delete-charge"),
    path("update_pocket/<pocket_id>",views.update_pocket, name="update-pocket"),
    path("delete_pocket/<pocket_id>",views.delete_pocket, name="delete-pocket"), 
    path("update_payment/<payment_id>/<pocket_id>",views.update_payment, name="update-payment"),
    path("delete_payment/<payment_id>/<pocket_id>",views.delete_payment, name="delete-payment"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
