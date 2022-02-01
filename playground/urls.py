from django.urls import path
from . import views

# URLConf
# Since in the main URLs.py file we catered for all routes to playground
# We can leave only "hello/" since the playground will ne catered for
urlpatterns = [
    path('hello/', views.say_hello)
]
