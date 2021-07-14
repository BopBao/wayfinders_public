from rest_framework import viewsets
from .serializers import MemberSerializer
from .serializers import MemberUserSerializer
from .serializers import UserToMemberSerializer
from .serializers import PermissionsSerializer
from .serializers import UserRoleSerializer
from .serializers import GallerySerializer
from .serializers import ApplicationSerializer
from .models import Member
from .models import MemberUser
from .models import UserToMember
from .models import Permissions
from .models import UserRole
from .models import Gallery
from .models import Application
from wayfinders.functions import add_to_queryset


class MemberAPI(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    http_method_names = ['get', 'head', 'post', 'put']

    def get_queryset(self):
        name = self.request.query_params.get('name')
        description = self.request.query_params.get('description')
        website = self.request.query_params.get('website')
        public = self.request.query_params.get('public')

        queryset_params = {}
        add_to_queryset(queryset_params, 'name__icontains', name)
        add_to_queryset(queryset_params, 'description__icontains', description)
        add_to_queryset(queryset_params, 'website__icontains', website)
        
        if(public == "true"):
            add_to_queryset(queryset_params, 'public', True)
        elif(public == "false"):
            add_to_queryset(queryset_params, 'public', False)

        if queryset_params:
            return Member.objects.filter(**queryset_params)
        return Member.objects.all()

class MemberUserAPI(viewsets.ModelViewSet):
    serializer_class = MemberUserSerializer
    http_method_names = ['get', 'head', 'post', 'put']
    
    def get_queryset(self):
        primary_member = self.request.query_params.get('primary_member')
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')

        queryset_params = {}
        add_to_queryset(queryset_params, 'primary_member__pk', primary_member)
        add_to_queryset(queryset_params, 'first_name', first_name)
        add_to_queryset(queryset_params, 'website', last_name)

        if queryset_params:
            return MemberUser.objects.filter(**queryset_params)
        return MemberUser.objects.all()

class UserToMemberAPI(viewsets.ModelViewSet):
    serializer_class = UserToMemberSerializer
    http_method_names = ['get', 'head', 'post', 'put']
    queryset = UserToMember.objects.all()

class PermissionsAPI(viewsets.ModelViewSet):
    serializer_class = PermissionsSerializer
    http_method_names = ['get', 'head', 'post', 'put']
    queryset = Permissions.objects.all()

class UserRoleAPI(viewsets.ModelViewSet):
    serializer_class = UserRoleSerializer
    http_method_names = ['get', 'head', 'post', 'put']
    queryset = UserRole.objects.all()

class GalleryAPI(viewsets.ModelViewSet):
    serializer_class = GallerySerializer
    http_method_names = ['get', 'head', 'post', 'put']
    queryset = Gallery.objects.all()

class ApplicationAPI(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    http_method_names = ['get', 'head', 'post', 'put']
    queryset = Application.objects.all()
