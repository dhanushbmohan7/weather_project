from django.shortcuts import render
from django.http import HttpResponse
import urllib
import json
# Create your views here.
def index(request):
    if request.method ==  'POST':
        city=request.POST['city']
        
        
        source=urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=821471311c49935135cb96dbb8de5193')
        data_list=json.load(source)
        data={
            "country_code":str(data_list['sys']['country']),
            "temp":str(data_list['main']['temp'])+'°C',
            "feels":str(data_list['main']['feels_like'])+'°C',
            "place":str(data_list['name']),
            "image":data_list['weather'][0]['icon'],
            "description":str(data_list['weather'][0]['description'],)

        }
        print(data)
    else:
        data={}    
    return render(request,'theme.html',data)
