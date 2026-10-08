from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import filters

from django.shortcuts import get_object_or_404

from .serializers import *
from .models import *

# Create your views here.


class TaskView(APIView):
    def get(self, request):
        tasks      = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    def get(self, request, pk):
        task       = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)

        return Response(serializer.data)

    def patch(self, request, pk):
        task       = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        task       = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskListView(generics.ListCreateAPIView):
    queryset         = Task.objects.all()
    serializer_class = TaskSerializer  

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


class TaskFilterView(APIView):
    def get(self, request):
        tasks     = Task.objects.all()
        completed = request.query_params.get('completed')

        if completed == 'true':
            tasks = tasks.filter(completed=True)

        elif completed == 'false':
            tasks = tasks.filter(completed=False)
        
        elif completed is not None:
            return Response({"error": "Invalid value for 'completed' parameter. Use 'true' or 'false'."}, status=status.HTTP_400_BAD_REQUEST)
        
        serilizer = TaskSerializer(tasks, many=True)

        return Response(serilizer.data)
        
            

