from django.shortcuts import render

from todo.models import TodoList

# Create your views here.
def index(request):
    return render(
        request,
        'todo/index.html'
    )

def todos(request):
	todolist = TodoList.objects.all()
	return render(
		request,
		'todo/todos.html',
  		{
			'todolist': todolist,
			}
	)