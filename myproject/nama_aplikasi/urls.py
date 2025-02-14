from django.urls import path
from . import views
from .views import github_contributions

urlpatterns = [
    path('', views.index_view, name='index'),  # Homepage
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('github-contributions/', github_contributions, name='github_contributions'),
]
