from django.urls import path
from .views import HomePageView,PyProgrammingView,PyDevelopmentView,MlView,DsView,PyProgrammingDetailView,PyDevelopmentDetailView,MlDetailView,DsDetailView

urlpatterns = [    
    path('',HomePageView.as_view(),name='home'),
    path('pyprogramming',PyProgrammingView.as_view(),name='pyprogramming'),
    path('pydevelopment',PyDevelopmentView.as_view(),name='pydevelopment'),
    path('ml',MlView.as_view(),name='ml'),
    path('datascience',DsView.as_view(),name='datascience'),
    path('pyprogramming/blogs/<int:pk>',PyProgrammingDetailView.as_view(),name='pyProgBlogDetail'),    
    path('pydevelopment/blogs/<int:pk>',PyDevelopmentDetailView.as_view(),name='pyDevBlogDetail'),    
    path('ml/blogs/<int:pk>',MlDetailView.as_view(),name='MlBlogDetail'),    
    path('datascience/blogs/<int:pk>',DsDetailView.as_view(),name='DsBlogDetail'),   
]
