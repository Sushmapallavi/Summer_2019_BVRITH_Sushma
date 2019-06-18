from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from onlineapp import views
from onlineapp.views import *
from onlineapp.views.studentserializer import StudentDetail, Studentserializer
from onlineapp.views.token import CustomAuthToken

if settings.DEBUG:
   import debug_toolbar
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('login/', LoginView.as_view(), name="login"),
       path('signup/', SignupView.as_view(), name="signup"),
       path('colleges/', CollegeView.as_view(),name="allcolleges"),
       path('colleges/<str:acronym>/' ,CollegeView.as_view(),name='students'),
       path('college/addcollege/', AddcollegeView.as_view(), name="addcolleges"),
       path('colleges/editcollege/<int:id>/', AddcollegeView.as_view(), name="editcolleges"),
       path('colleges/deletecollege/<int:id>/', AddcollegeView.as_view(), name="deletecolleges"),
       path('stduents/<int:id>',StudentView.as_view(),name="studentmarks"),
       path('addstudent/<str:acronym>/',AddstudentView.as_view(),name="addstudent"),
       path('addstudent/edit/<int:id>',AddstudentView.as_view(),name="editstudent"),
       path('addstudent/delete/<int:id>', AddstudentView.as_view(), name="deletestudent"),
       path('logout/',logout_user,name='logout'),

        path('api/v1/colleges/',Collegeserializer,name='collegesapi'),
       path('api/v1/colleges/<int:pk>/', colleges_detail),
       path('api/v1/colleges/<int:pk>/student/',Studentserializer.as_view()),
       path('api/v1/colleges/<int:pk>/student/<int:cid>/', StudentDetail.as_view())
   ]

   urlpatterns += [
       url('api-token-auth/', CustomAuthToken.as_view())
   ]