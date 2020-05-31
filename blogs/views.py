from django.shortcuts import render
from django.views.generic import TemplateView, ListView,DetailView
from .models import ProgrammingModel,DevelopmentModel,MlModel,DataScienceModel


class HomePageView(TemplateView):
    template_name = 'home.html'


class PyProgrammingView(ListView):
    model = ProgrammingModel
    context_object_name = 'blogs'
    fields = '__all__'
    template_name = 'pyProgramming.html'


class PyDevelopmentView(ListView):
    model = DevelopmentModel
    context_object_name = 'blogs'
    fields = '__all__'
    template_name = 'pyDevelopment.html'
    
class MlView(ListView):
    model = MlModel
    context_object_name = 'blogs'
    fields = '__all__'
    template_name = 'ml.html'
    
class DsView(ListView):
    model = DataScienceModel
    context_object_name = 'blogs'
    fields = '__all__'
    template_name = 'dataScience.html'

class PyProgrammingDetailView(DetailView):
    model = ProgrammingModel
    template_name = 'pyProgBlogDetail.html'
    fields = '__all__'
    
class PyDevelopmentDetailView(DetailView):
    model = DevelopmentModel
    template_name = 'pyDevBlogDetail.html'
    fields = '__all__'
    
class MlDetailView(DetailView):
    model = MlModel
    template_name = 'mlBlogDetail.html'
    fields = '__all__'
    
class DsDetailView(DetailView):
    model = DataScienceModel
    template_name = 'dsBlogDetail.html'
    fields = '__all__'
    
    
# def handle404(request):
#     return render(request,'404.html',status=404)    
# Create your views here.
