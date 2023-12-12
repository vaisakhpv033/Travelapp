from django.shortcuts import render

from .models import guides, reviews


# Create your views here
def demo(request):
    obj = guides.objects.all()
    obj1 = reviews.objects.all()
    return render(request, 'index.html', {'result': obj, 'review': obj1})
