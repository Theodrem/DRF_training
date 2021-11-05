from .views import PostHeroView, GetHeroView, UpdateHeroView
from django.urls import path

urlpatterns = [
    path('post_hero/', PostHeroView.as_view(), name='post_hero'),
    path('get_hero/', GetHeroView.as_view(), name='get_hero'),
    path('update_hero/<int:pk>/', UpdateHeroView.as_view(), name='update_hero')
]