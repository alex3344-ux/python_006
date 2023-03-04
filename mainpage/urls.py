from django.urls import path
# from .views import show_mainpage, MainpageView
from .views import MainpageView
# from .views import show_mainpage

app_name = "mainpage"

urlpatterns = [
    path("", MainpageView.as_view(), name="mainpage"),
    # path("", show_mainpage, name="mainpage"),
]
