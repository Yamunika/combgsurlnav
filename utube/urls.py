from django.urls import path
from utube.views import like
app_name='utube'
urlpatterns=[
    path('like/',like,name='like'),
]