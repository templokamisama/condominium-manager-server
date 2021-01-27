from rest_framework import viewsets
from rest_framework.response import Response


class ProprietorViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response("List")

    def post(self, request):
        return Response("Post")
