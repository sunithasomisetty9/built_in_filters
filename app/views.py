from django.shortcuts import render
import datetime
# Create your views here.
def built_in_filters(request):
    dt=datetime.datetime.now()
    d={'data':'toDay is WeekEnd','count':1,'dt':dt}
    return render(request,'built_in_filters.html',d)