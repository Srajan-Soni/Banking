
from django.urls import path
from app import views
from django.conf.urls import url

urlpatterns = [
    path('index/',views.IndexView.as_view()),
    path('showuser/',views.UserView.as_view()),
    # path('showuser/',views.showuser)
    path('transferto/',views.transferview),
    path('sendmoney/',views.sendmoney),
    # path('history/',views.viewhistory)
    path('history/',views.ViewHistory.as_view()),
    path('del/',views.deltransac),
    path('repeat/',views.repeat_transac),
    path('customers/',views.Customers.as_view()),
    path('profile/',views.profile),
    path('yourtransac',views.your_transactions),
    path('about/',views.AboutPage.as_view())

]