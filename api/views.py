# from django.http.response import JsonResponse
#
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


# class HelloWorldView(APIView):
#     def get(self, request):
#         return Response({"message": "Hello World"})

@api_view(["GET", "POST"])
def hello_world(request):
    if request.method == "GET":
        return Response({"message": "Hello World"})
    else:
        name = request.data.get("name")
        if not name:
            return Response({"error":"No name"})
        return  Response({"message": "Hello {}!".format(name)})