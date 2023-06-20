from todo_api.models import Todo
from todo_api.serializers import testSerializer, todoSerializer
from rest_framework import viewsets,permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date as dt
from datetime import timedelta
from django.contrib.auth.models import User
from django.db.models import Min
import calendar

class TodoViewSet(viewsets.ModelViewSet):

    serializer_class = todoSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.todos.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TodoAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,date=None):
        try:
            try:
                year, month, day = map(int, date.split("-"))
                appointmentDateSelected = dt(year=year, month=month, day=day)
            except Exception as e:
                return Response({"error": "Invalid Date, Please Provide Valid Date in Format of YYYY-MM-DD"},status=status.HTTP_400_BAD_REQUEST)
            
            # Getting delayed data
            yesterdayDate = dt.today() - timedelta(days=1)
            delayedData = Todo.objects.filter(owner=request.user,completed=False,date_completed_by__lte=yesterdayDate).values()[::-1]

            # Getting appointedDateData

            givenData = []
            if appointmentDateSelected >= dt.today():
                givenDateData = Todo.objects.filter(owner=request.user,completed=False,date_completed_by=appointmentDateSelected).values()
                if givenDateData.exists():
                    givenData = list(givenDateData)
            # # getting minimum date of incomplete task
            # minDate = Todo.objects.filter(owner=request.user,completed=False).aggregate(Min('date_completed_by')) 

            # # filtering uncompleted task
            # uncompleted = Todo.objects.filter(owner=request.user,completed=False,date_completed_by__range=[minDate['date_completed_by__min'],dt.today()]).order_by('date_completed_by') 
            # uncompletedSerial  = todoSerializer(uncompleted,many=True)
            
            # futureTodos = []
            # if dt.today() < appointmentDateSelected:
            #     # task of given date
            #     todos = Todo.objects.filter(owner=request.user,date_completed_by=appointmentDateSelected)
            #     todosSerial = todoSerializer(todos,many=True)
            #     futureTodos = todosSerial.data[::-1]
            data = delayedData + givenData
            context = {
                # 'todo' : Todo.objects.filter(owner=request.user,completed=False,date_completed_by__lte=appointmentDateSelected).values(),
                'todo' :data,
            }

            return Response(context,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChartData(APIView):
    
    def get(self, request,*args, **kwargs):
        userData = User.objects.get(id=self.request.user.id)
        todoData = Todo.objects.filter(owner=userData)
        data = []
        label = []

        if todoData:
            todo_date =todoData.filter(completed = True)

            days_list = [i for i in range(1,calendar.monthrange(dt.today().year,dt.today().month)[1]+1)]
            for i in range(1,dt.today().day+1):
                data.append(todoData.filter(completed_at__year=dt.today().year,completed_at__month=dt.today().month,completed_at__day=i,completed = True).count())

            label = days_list
                 
        return Response({"data":data,"label":label})

class FlutterChartData(APIView):
    def get(self, request,*args, **kwargs):
        
        try:
            userData = User.objects.get(id=self.request.user.id)
            todoData = Todo.objects.filter(owner=userData, completed = True)
            data = []
            taskDone = 0
            days_list = [i for i in range(1,dt.today().day+1)]
            if todoData:
                for i in days_list:
                    tp = todoData.filter(completed_at__year=dt.today().year,completed_at__month=dt.today().month,completed_at__day=i).count()
                    data.append(
                        tp
                    )
                    taskDone += tp

            res = {
                "cdate": days_list,
                "cdata":data,
                "numberOfTaskDone": taskDone
            }
        
            return Response(res,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
