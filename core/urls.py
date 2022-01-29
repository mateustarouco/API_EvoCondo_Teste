from django.contrib import admin
from django.urls import path , include
from garage.views import GarageViwesets
from operatorcondom.views import OperatorCViwesets 
from resident.views import ResidentViwesets
from rest_framework import routers
from visitor.views import VisitorViwesets

router = routers.DefaultRouter()
router.register('residents',ResidentViwesets)
router.register('garage',GarageViwesets)
router.register('operator',OperatorCViwesets)
router.register('visitor',VisitorViwesets)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]