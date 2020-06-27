import requests
from django.shortcuts import render

def index(request):
    d = []
    if request.method == "POST":

        
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=kelvin&appid=45f24740bed69f5a5b4e3796d1bb8082'
        city = request.POST['city']
        # print(city)
        r = requests.get(url.format(city))
        result = r.json()
        if result['cod'] != "404":
            
            data = {
                'lon' : result['coord']['lon'],
                'lat' : result['coord']['lat'],
                'main' : result['weather'][0]['main'],
                'desc' : result['weather'][0]['description'],
                'temp' : int(result['main']['temp'] - 273.15),
                'name' : city
            }
            d.append(data)
        else:
            return render(request,'weather/index.html',{'error' : 'City not found'})
    context = {
        'd' : d
    }
    
    return render(request, 'weather/index.html' , context)
