from django.contrib import admin
from django.urls import path
from iplapp.views.details import SeasonView
from iplapp.views.match import MatchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('allseasons/',SeasonView.as_view(),name='season'),
    path('allseasons/<int:sid>',SeasonView.as_view(),name='details'),
    path('match/<int:id>',MatchView.as_view(),name='matchdetails')
]
