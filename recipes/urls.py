from django.urls import path

from recipes.views import contato, home, musta, sobre

# HTTP REQUEST


urlpatterns = [

    path('', home),  # Home
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato),  # /contatp/
    path('musta/', musta),
]
