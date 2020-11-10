from produtos.models import Camisa, Chuteira
from produtos.serializers import CamisaSerializer, ChuteiraSerializer
from rest_framework import viewsets


class CamisaViewSet(viewsets.ModelViewSet):
    queryset = Camisa.objects.all()
    serializer_class = CamisaSerializer


class ChuteiraViewSet(viewsets.ModelViewSet):
    queryset = Chuteira.objects.all()
    serializer_class = ChuteiraSerializer


# @api_view(['GET'])
# def chuteira_list(request):
#     chuteira = Chuteira.objects.all()
#     serializer = ChuteiraSerializer(chuteira, many=True)
#     return Response(serializer.data)
#

# class CamisaListCreate(generics.ListCreateAPIView):
#     queryset = Camisa.objects.all()
#     serializer_class = CamisaSerializer
#
#
# class CamisaDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Camisa.objects.all()
#     serializer_class = CamisaSerializer
#

# class CamisaListCreate(APIView):
#     def get(self, request):
#         camisa = Camisa.objects.all()
#         serializer = CamisaSerializer(camisa, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = CamisaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CamisaDetail(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Camisa.objects.get(pk=pk)
#         except Camisa.DoesNotExist:
#             raise NotFound()
#
#     def get(self, request, pk):
#         camisa = self.get_object(pk)
#         serializer = CamisaSerializer(camisa)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         camisa = self.get_object(pk)
#         serializer = CamisaSerializer(camisa, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         camisa = self.get_object(pk)
#         camisa.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def camisa_list(request):
#     if request.method == 'GET':
#         camisa = Camisa.objects.all()
#         serializer = CamisaSerializer(camisa, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CamisaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def camisa_detail(request, pk):
#     try:
#         camisa = Camisa.objects.get(pk=pk)
#     except Camisa.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = CamisaSerializer(camisa)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = CamisaSerializer(camisa, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         camisa.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
