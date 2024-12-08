from django.urls import path
from prime.views import series
app_name='prime'
urlpatterns=[
    path('series/',series,name='series'),
]