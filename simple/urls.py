from django.urls import path
from.import views

app_name = 'simple'
urlpatterns= [
#URLS for myapp1 app
     #dashboard
     path('',views.MyIndexView.as_view(), name="my_index_view"),

     ]