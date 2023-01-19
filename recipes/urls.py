from django.urls import path

from recipes.views import contato, home, sobre  # ta importanto do recipes

urlpatterns = [
    #   path('admin/', admin.site.urls), aqui nao precisa
    path('', home),  # adiciona url
    path('sobre/', sobre),  # adiciona url
    path('contato/', contato),  # adiciona url

]
# aqui é o django importanto do url do python
