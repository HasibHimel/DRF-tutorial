# from django.http.response import JsonResponse
#
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .serializers import HelloWorldSerializer
from .serializers import SubscriberSerializer
from .models import Subscriber


# class HelloWorldView(APIView):
#     def get(self, request):
#         return Response({"message": "Hello World"})
#
#     def post(self, request):
#         serializer = HelloWorldSerializer(data=request.data)
#         if serializer.is_valid():
#             valid_data = serializer.data
#
#             name = valid_data.get("name")
#             age = valid_data.get("age")
#
#             return Response({"message": "Hello {}, you're {} years old". format(name, age)})
#         else:
#             return Response({"errors": serializer.errors})


class SubscriberView(APIView):
    def get(self, request):
        all_subscribers = Subscriber.objects.all()
        serialized_subscribers = SubscriberSerializer(all_subscribers, many=True)
        return Response(serialized_subscribers.data)

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            subscriber_instance = Subscriber.objects.create(**serializer.data)
            return Response({"message": "Created subscriber {}".format(subscriber_instance.id)})
        else:
            return Response({"errors": serializer.errors})


# @api_view(["GET", "POST"])
# def hello_world(request):
#     if request.method == "GET":
#         return Response({"message": "Hello World"})
#     else:
#         name = request.data.get("name")
#         if not name:
#             return Response({"error":"No name"})
#         return Response({"message": "Hello {}!".format(name)})
#