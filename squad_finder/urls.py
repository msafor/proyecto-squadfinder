"""
URL configuration for squad_finder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
from api import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", v.index, name="index"),
    path("login/", v.login, name= "login"),
    path("register/", v.register, name="register"),
    path("crear-squad/",v.crear_squad,name="crear-squad"),
    path("stats/", v.stats, name="stats"),
    path("games/", v.games, name="games"),
    path("api/auth/register/", v.RegisterView.as_view(),name="auth_register"),
    path("api/auth/login/",TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(),name="token_refresh"),
    path("api/games/", v.GameList.as_view(), name="game_list"),
    path("api/squads/", v.SquadList.as_view(), name="squad_list"),
    path("api/squads/<int:pk>/", v.SquadDetail.as_view(),name="squad_detail"),
    path("api/stats/", v.SquadStatsApiView.as_view(), name="api_stats")
]
