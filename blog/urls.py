from django.urls import path
from .views import IndexView,BlogDetailView,BlogCreateView,BlogUpdateView

app_name = 'blog'  #namespace dado en config.urls 

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('<int:pk>', BlogDetailView.as_view(), name='detail'),
    path("<int:pk>/update/", BlogUpdateView.as_view(), name='update'),
    path('create/', BlogCreateView.as_view(), name='create'),
]
