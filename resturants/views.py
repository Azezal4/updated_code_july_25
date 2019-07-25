from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,ListView

from .models import ResturantLocation

# Create your views here.
def resturant_list(request):
    template_name = "resturants/resturants_list.html"
    query_set = ResturantLocation.objects.all() #have all the objects from the function ResturantLocation
    context = {"object_list": query_set}    #the object_list is the general representation of any object in a row of a database
    return render(request, template_name, context)

class ResturantListView(ListView):
    queryset = ResturantLocation.objects.all()
    template_name = "resturants/resturants_list.html"











# from django.shortcuts import render
# from django.views.generic import TemplateView
# from django.views import View
# from .models import ResturantLocation
#
#
#
#
# def home_view(request): #first parameter that is needed to run the application, is set default by the django application,
#     # (containing info about user such as username, ip address  etc) and browser
#     context ={      #data that will be fetched to user
#         "resturants" : "109deg",
#         "Location": "Siphal",
#         "items":['asdasd', "mahsgh"]
#     }
#     return render(request,"home.html",context) #render : since the django application doesn't understand the jinja templates so it converts them to proper django render also helps to connect between those two.
#
# def resturant_list(request):
#     template_name = "resturants/resturant_list.html"
#     query_set = ResturantLocation.objects.all()
#     context = {"resturants": query_set}
#     return render(request, template_name, context)
#
#
#
# class WelcomeTemplateView(TemplateView):
#     template_name = "hotel.html"
#
#     def get_context_data(self, **kwargs):
#         context = {
#             "resturant_name":"Bajeko sekuwa",
#             "Location":"Baneswor"
#         }
#         return context
#
#
# class AboutTemplateView(TemplateView):
#     template_name = "hotel.html"
#
# # Create your views here.
