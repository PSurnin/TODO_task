from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.serializers import TaskItemSerializer
from app.models import TaskItem


@api_view(['POST'])
def task_create(request):
    '''
    Create new task
    '''
    serializer = TaskItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        raise ValidationError("Invalid data")
    return Response(serializer.data)


@api_view(['GET'])
def tasks_list(request):
    tasks = TaskItem.objects.all()
    serializer = TaskItemSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    '''
    Return task by its id
    '''
    try:
        task = TaskItem.objects.get(id=pk)
    except TaskItem.DoesNotExist:
        raise NotFound
    return Response(TaskItemSerializer(task).data)



@api_view(['POST'])
def task_update(request, pk):
    '''
    Update existing task
    '''
    try:
        task = TaskItem.objects.get(id=pk)
    except TaskItem.DoesNotExist:
        raise NotFound
    serializer = TaskItemSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        raise ValidationError("Invalid data")
    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request, pk):
    '''
    Delete existing task
    '''
    try:
        task = TaskItem.objects.get(id=pk)
    except TaskItem.DoesNotExist:
        raise NotFound
    task.delete()
    return Response(f'Task {pk} deleted.')
