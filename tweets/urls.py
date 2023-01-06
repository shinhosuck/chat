from django.urls import path 
from .views import(
    home_view,
    tweet_list_view,
    tweet_create_view,
)

app_name = 'tweets'


urlpatterns = [
    path('', home_view, name='home'),
    path('tweets', tweet_list_view, name='tweets'),
    path('new/tweet', tweet_create_view, name='new-tweet'),
]