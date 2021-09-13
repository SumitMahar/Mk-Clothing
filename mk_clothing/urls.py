
from django.urls import path


from .views import (
    mk_home,
    AboutView,
    ContactView
)

app_name = 'mk_clothing'
urlpatterns = [
    path('', mk_home, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),

]



