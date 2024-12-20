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

def Home(request):
    
   
    try:
        A={
                "a":'VegOFF'
            }
        pizzaType=request.POST.get('Veg')
                                    # print(pizzaType,'pizzaType')
        # product=request.POST['product']
        # print(product,'product')

                                    # Veg Non Veg Mix start
        if pizzaType==None:
            VegOFF=PizzaModel.objects.all()
            print(VegOFF,'noneveg')
            A={
                "a":VegOFF
            }
            # return render(request,'Home.html',A)
           
                                    # print(VegOFF,'VegOFF------------')
                                    # Veg Non Veg Mix End


        if request.method=='POST':

            pizzaType=request.POST['Veg']
            

            # product=request.POST['product']
            # print(product,'product POST')

                                                    # Only Veg start
            if pizzaType=='VEG_ON':
                

                Vegdata=PizzaModel.objects.filter(pizzaType='veg')
                                                    # print(Vegdata,'vegdata')
                A={
                    "a":Vegdata,
                    
                }

                # return render(request,'Home.html',A)


                # if Pizzas:
                #     return
                    
                # if Melts:
                #     return
                
                # if Pastas:
                #     return
                
                # if Desserts:
                #     return
                
                

               

            # Only Veg start
            
                

            
            # print(pizzaType,'pizzaType')
            pass
        
    except:
        pass
    return render(request,'Home.html',A)
    # return HttpResponse('Welcome')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home),

]
