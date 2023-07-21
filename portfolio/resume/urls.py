from django.urls import path
from .views import home, portfolio_project

urlpatterns = [
    path("", home, name="home"),
    path("portfolio_project/<int:id>", portfolio_project, name="portfolio_project"),
]
