from django.urls import path
from .views import BbCreateView, PiopleCreateView

from .import views
app_name= 'bboard'
urlpatterns = [
    
    path('', PiopleCreateView.as_view(), name = 'first'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', views.by_rubric, name = 'by_rubric'),
    path('', views.index, name='index'),
]
