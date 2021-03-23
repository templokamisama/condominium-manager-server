from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from reservation.models import Structure
from reservation.serializers import (MessageResponseSerializer,
                                     StructureEditSerializer,
                                     StructureSearchParamSerializer,
                                     StructureSerializer)


class ProprietorViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response("List")

    def post(self, request):
        return Response("Post")


class StructureViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        query_serializer=StructureSearchParamSerializer(),
        responses={
            200: StructureSerializer(many=True),
            400: MessageResponseSerializer(),
            500: MessageResponseSerializer(),
        },
    )
    def list_structures(self, request):
        structures_param_serializer = StructureSearchParamSerializer(data=request.query_params)
        structures_param_serializer.is_valid(raise_exception=True)

        structures = Structure.objects.all()
        if 'id' in structures_param_serializer.validated_data.keys():
            structures = structures.filter(id=structures_param_serializer.validated_data['id'])
        if 'name' in structures_param_serializer.validated_data.keys():
            structures = structures.filter(name=structures_param_serializer.validated_data['name'])
        if 'available' in structures_param_serializer.validated_data.keys():
            structures = structures.filter(available=structures_param_serializer.validated_data['available'])

        structure_serializer = StructureSerializer(structures, many=True)

        return Response(structure_serializer.data, status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={
            204: '',
            400: MessageResponseSerializer(),
            404: MessageResponseSerializer(),
            500: MessageResponseSerializer(),
        },
    )
    def delete_structure(self, request, id):
        structure = get_object_or_404(Structure, id=id)
        structure.delete()

        return Response({}, status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        request_body=StructureSerializer(),
        responses={
            201: StructureSerializer(),
            400: MessageResponseSerializer(),
            500: MessageResponseSerializer(),
        },
    )
    def create_structure(self, request):
        structure_serializer = StructureSerializer(data=request.data)
        structure_serializer.is_valid(raise_exception=True)
        structure_serializer.save()

        return Response(structure_serializer.data, status.HTTP_201_CREATED)

    @swagger_auto_schema(
        request_body=StructureEditSerializer(),
        responses={
            202: StructureEditSerializer(),
            400: MessageResponseSerializer(),
            404: MessageResponseSerializer(),
            500: MessageResponseSerializer(),
        },
    )
    def edit_structure(self, request, id):
        structure = get_object_or_404(Structure, id=id)
        structure_serializer = StructureEditSerializer(structure, data=request.data)
        structure_serializer.is_valid(raise_exception=True)
        structure_serializer.save()

        return Response(structure_serializer.data, status.HTTP_200_OK)
