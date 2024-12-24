"""
URL configuration for pizzahut project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render,HttpResponse

from home.models import PizzaModel

# def header(check):
#     a={
#         'checkbox':check
#     }
#     return render('Header.html',a)

chk=''
def Home(request):
    HeaderName='deal'
    A={
        "b":HeaderName
    }

    return render(request,'Home.html',A)
    # return HttpResponse('Welcome')

HeaderName='Deal'
def Pizzas(request):
    
    HeaderName='Pizzas'
    try:
        pizzaType=request.POST.get('Veg')
        print(pizzaType)
        if pizzaType==None or pizzaType=='unchk':
            chk=''
            VegOFF=PizzaModel.objects.all()
            print(VegOFF,'noneveg')
            A={
                "a":VegOFF,
                "b":HeaderName
            }

        

        if request.method=='POST':

            if pizzaType=='VEG_ON':
                print('Veg only Working')
                chk='unchk'
                Vegdata=PizzaModel.objects.filter(pizzaType='veg')
                A={
                    "a":Vegdata,
                    'chk':chk
                    
                }
            pass
        
    except:
        pass
    return render(request,'Pizza.html',A)

def Melts(request):    
    HeaderName='Melts'
    A={
        "b":HeaderName
    }

    return render(request,'Melts.html',A)

def Pastas(request):    
    HeaderName='Pastas'
    A={
        "b":HeaderName
    }
    return render(request,'Pastas.html',A)

def Desserts(request):
    
    HeaderName='Desserts'
    A={
        "b":HeaderName
    }
    return render(request,'Desserts.html',A)


def Drinks(request):
    
    HeaderName='drinks'
    A={
        "b":HeaderName
    }
    return render(request,'Drinks.html',A)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',Pizzas),

    path('Deal',Home),
    
    path('Melts',Melts),
    
    path('Pastas',Pastas),
    
    path('Desserts',Desserts),

    path('Drinks',Drinks)

]
