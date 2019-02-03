from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework import viewsets
from lms.serializers import LogSerializer
from lms.models import *
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from .serializers import LoginSerializer
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


################################################
# Generic mixin based rest API CRUD operations
################################################

class LmsListView(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    serializer_class = LogSerializer
    queryset = Log.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save()

    def put(self, request, id=None):
        return self.update(request, id)

    def perform_update(self, serializer):
        #print(self.request.user)
        serializer.save()        

    def delete(self, request, id=None):
        return self.destroy(request, id)



################################################
#    class based rest API CRUD operations
################################################

import logging
logger = logging.getLogger(__name__)


class LmsAPIView(APIView):
    def get(self, request):
        lms = Log.objects.all()
        serailizer = LogSerializer(lms, many=True)
        return Response(serailizer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = LogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("hello I'm here")
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status=400)


class LmsDetailView(APIView):
    def get_object(self, id):
        try:
            return Log.objects.get(id=id)
        except Log.DoesNotExist as e:
            return Response( {"error": "Given Log object not found."}, status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        serailizer =LogSerializer(instance)
        return Response(serailizer.data)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = LogSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.erros, status=400)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return HttpResponse(status=204)


################################################
#    def based rest API CRUD operations
################################################


@csrf_exempt
def lms(request):
    if request.method == "GET":
        lms = Log.objects.all()
        serailizer = LogSerializer(lms, many=True)
        return JsonResponse(serailizer.data, safe=False)

    elif request.method == "POST":
        json_parser = JSONParser()
        data = json_parser.parse(request.data)
        serializer = LogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def lms_details(request, id):
    try:
        instance = Log.objects.get(id=id)
    except Log.DoesNotExist as e:
        return JsonResponse( {"error": "Given log object not found."}, status=404)

    if request.method == "GET":
        serailizer = LogSerializer(instance)
        return JsonResponse(serailizer.data)

    elif request.method == "PUT":
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = LogSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.erros, status=400)

    elif request.method == "DELETE":
        instance.delete()
        return HttpResponse(status=204)


##########################################################
#     API login and logout
##########################################################


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)



def HomePage(request):
    print("Hello Im here")
    return render(request,"index.html",{})