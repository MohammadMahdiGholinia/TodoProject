from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from django.shortcuts import get_object_or_404

from .serializers import *
from .models import *

# Create your views here.


class TaskView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks      = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        task       = get_object_or_404(Task, pk=pk, user=request.user)
        serializer = TaskSerializer(task)

        return Response(serializer.data)

    def patch(self, request, pk):
        task       = get_object_or_404(Task, pk=pk, user=request.user)
        serializer = TaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        task       = get_object_or_404(Task, pk=pk, user=request.user)
        serializer = TaskSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskListView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskFilterView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks     = Task.objects.filter(user=request.user)
        completed = request.query_params.get('completed')

        if completed == 'true':
            tasks = tasks.filter(completed=True)

        elif completed == 'false':
            tasks = tasks.filter(completed=False)
        
        elif completed is not None:
            return Response({"error": "Invalid value for 'completed' parameter. Use 'true' or 'false'."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)


class TaskOrderingView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        ordering = request.query_params.get('ordering')

        allowed_orderings = ['created_at', '-created_at', 'due_date', '-due_date']

        if ordering is not None:
            if ordering not in allowed_orderings:
                return Response({"error": "Invalid value for 'ordering' parameter. Use 'created_at', '-created_at', 'due_date', or '-due_date'."}, status=status.HTTP_400_BAD_REQUEST)
            
            tasks = tasks.order_by(ordering)
        
        serializer = TaskSerializer(tasks, many=True)
        
        return Response(serializer.data)




