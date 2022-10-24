from django.shortcuts import render
from . models import place
from . models import team


# Create your views here.
def demo(request):
    new=place.objects.all()
    new1=team.objects.all()
    return render(request, 'index.html',{'result':new,'result1':new1})
