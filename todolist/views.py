from django.shortcuts import render

# Create your views here.
from .models import Todolist

def index(request):
    
    todo_items = Todolist.objects.order_by('id')
    context = {'todo_items' : todo_items}

    return render(request,'todolist/index.html', context)