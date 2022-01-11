from django.urls import path,re_path
from .import views
urlpatterns = [
    re_path(r'^location/$',views.RegionListAPIView.as_view(),name="RegionListAPIView"),
    re_path(r'^location/(?P<region>\w+)/$',views.CountryListAPIView.as_view(),name="CountryListAPIView"),
    re_path(r'^location/(?P<region>\w+)/(?P<country>\w+)/$',views.StateListAPIView.as_view(),name="StateListAPIView"),
    re_path(r'^location/(?P<region>\w+)/(?P<country>\w+)/(?P<state>\w+)/$',views.CityListAPIView.as_view(),name="CityListAPIView"),
    re_path(r'^location/(?P<region>\w+)/(?P<country>\w+)/(?P<state>\w+)/(?P<city>\w+)/$',views.LocationDataListAPIView.as_view(),name="LocationDataListAPIView"),
]