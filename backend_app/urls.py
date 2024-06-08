from django.urls import path
from .views import *

urlpatterns=[
    path('',home_page),
    path('form/',form_page),
    path('view/',view_page),
    path('delect/<int:id>',delete_student,name="delect_student"),
    path('update/<int:id>/',update_page,name="update_student"),
    
]