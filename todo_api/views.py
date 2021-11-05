from todo_api.models import Todo
from todo_api.serializers import testSerializer, todoSerializer
from rest_framework import viewsets,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date as dt
from django.contrib.auth.models import User
import calendar
# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):

    serializer_class = todoSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def update(self, request, *args, **kwargs):
        print(request.data)
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.todos.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class test(viewsets.ModelViewSet):
    
    queryset = Todo.objects.all()
    serializer_class = testSerializer
    permission_classes= [
        permissions.AllowAny
    ]



class ChartData(APIView):
    
    def get(self, request,*args, **kwargs):
        id = request.query_params['id']
        userData = User.objects.get(id=int(id))
        todoData = Todo.objects.filter(owner=userData)
        data = []
        label = []

        if todoData:
            todo_date =todoData.filter(completed = True)
            print(todo_date)

            days_list = [i for i in range(1,calendar.monthrange(dt.today().year,dt.today().month)[1]+1)]
            for i in range(1,dt.today().day+1):
                data.append(todoData.filter(completed_at__year=dt.today().year,completed_at__month=dt.today().month,completed_at__day=i,completed = True).count())

            label = days_list
                 
        return Response({"data":data,"label":label})

class FlutterChartData(APIView):
    def get(self, request,*args, **kwargs):
        id = request.query_params['id']
        userData = User.objects.get(id=id)
        todoData = Todo.objects.filter(owner=userData)
        data = []

        if todoData:
            todo_date =todoData.filter(completed = True)
            days_list = [i for i in range(1,calendar.monthrange(dt.today().year,dt.today().month)[1]+1)]
            for i in days_list:
                temp = {
                    "data" : todo_date.filter(completed_at__year=dt.today().year,completed_at__month=dt.today().month,completed_at__day=i).count(),
                    "date" : i 
                }
                data.append(temp)
        else:
            data.append({
                "data":0,
                "date":dt.today().day
            })   
      
        return Response({"data":data})