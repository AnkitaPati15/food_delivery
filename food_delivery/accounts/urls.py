from django.urls import include, path

urlpatterns = [

    path(
        "",
        include("accounts.frontend_urls"),
    ),

    path(
        "api/",
        include("accounts.api_urls"),
    ),

]