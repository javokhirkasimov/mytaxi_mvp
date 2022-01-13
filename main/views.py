from rest_framework.views import APIView
from .serializers import (OrderCreateSerializer, StatusUpdateSerializer, OrderListSerializer, OrderDetailSerializer)
from rest_framework.response import Response
from rest_framework import generics
from .models import Order
from django.shortcuts import get_object_or_404


class OrderCreateView(APIView):

    def get(self, request):
        query = Order.objects.all()
        serializer = OrderListSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serialized_data = OrderCreateSerializer(data=request.data)
        if serialized_data.is_valid():
            print('Valid!')
            obj = serialized_data.save()
            return Response({'order_id': obj.id})
        return Response({'Error': 'Wrong ID Specified'}, status=404)


class StatusUpdateView(APIView):

    def get(self, request, pk):
        obj = get_object_or_404(Order, id=pk)
        serializer = OrderListSerializer(obj)
        return Response(serializer.data)

    def put(self, requset, pk):
        saved_order = get_object_or_404(Order, id=pk)
        print(requset.data)
        if saved_order.status == 'accepted' and requset.data.get('status') == 'canceled':
            return Response({"Error": "Accepted orders cannot be canceled!"})
        serialized_data = StatusUpdateSerializer(instance=saved_order, data=requset.data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({"Success": "Status of the order has been changed"})
        return Response(status=404)


class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()


class ClientOrdersView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        from_date = self.request.query_params.get('from')
        to_date = self.request.query_params.get('to')
        if from_date and to_date:
            return queryset.filter(client_id=self.kwargs['pk'], created_date__range=[from_date, to_date])
        return queryset.filter(client_id=self.kwargs['pk'])
