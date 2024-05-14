from django.urls import path,include
from . import views
urlpatterns = [
   
    path('',views.home,name="home"),

    path('currency',views.currency,name="currency"),
    path('currencypredict',views.currency_pred,name='currencypredict'),


    path('news',views.news,name="news"),
    path('website',views.website,name="website"),
    path('feedback',views.feedback,name="feedback"),
]



# path('tomatoleaf',views.welcomepred,name='tomatoleaf'),
#     path('tomatoleafpredict',views.tomatoleafpredict,name='tomatoleafpredict'),
