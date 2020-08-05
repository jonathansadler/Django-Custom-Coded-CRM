from django.shortcuts import render

# Create your views here.

#from rest_framework.response import Response

#from django.contrib.auth.models import User, Group
from rest_framework import viewsets
#from core.serializers import UserSerializer, GroupSerializer

from rest_framework.permissions import (
    AllowAny, 
    IsAuthenticatedOrReadOnly, 
    IsAdminUser,
    DjangoModelPermissions,
    DjangoModelPermissionsOrAnonReadOnly
)


#from django.http.response import HttpResponseNotAllowed
#from django_filters.rest_framework import DjangoFilterBackend


from .models import (
    Lead
)


from .serializers import (
   	LeadSerializer
)


# Create your views here.


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [AllowAny,]





#from .models import Breach

#from .models import AccountAMeter

#


