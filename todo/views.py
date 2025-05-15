from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_object(self):
        try:
            
            obj = super().get_object()
            if obj.user != self.request.user:
                raise NotFound("لايمكننك القيام بهذه المهمة")
            return obj
        except Exception as e:
            raise NotFound("لا توجد مهمة مطابقة للاستعلام")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save(user=request.user)
        return Response({
            "success": True,
            "message": "تم إنشاء المهمة بنجاح",
            "data": TaskSerializer(task).data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()
        return Response({
            "success": True,
            "message": "تم تحديث المهمة بنجاح",
            "data": TaskSerializer(task).data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "success": True,
            "message": "تم حذف المهمة بنجاح"
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response({
            "success": True,
            "message": "تم جلب المهمة بنجاح",
            "data": TaskSerializer(instance).data
        }, status=status.HTTP_200_OK)