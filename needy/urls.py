from django.urls import path,include

from. import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/',views.create, name="create"),
    path('accounts/', include('accounts.urls')),
    path('<int:ng_id>',views.ngo_det, name = 'ngodetails'),
    path('donate/<int:ng_id>',views.donate, name = 'ngodonate'),
    path('donate/thankyou/<int:ng_id>',views.thankyou ,name = 'thankyou'),

]
