from django.shortcuts import render,redirect,get_object_or_404
from todo.forms import TaskForm
from todo.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

@login_required
def todopage(request):
    return render(request,"todo_page.html")

@login_required
def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user     
            task.save()
            return redirect("list_task")
        
    elif request.method == "GET": 
        form = TaskForm()
    return render(request,'todo/create_task.html' , {'form':form})

@login_required
def list(request):
    # objects = Task.objects.all() # for everyone
    objects = Task.objects.filter(user=request.user) # for user specific

    
    return render(request,"todo/list_task.html",{"objects" : objects})

@login_required
def update(request,pk):

    # Step 1: Find the task by ID (pk)
    # task = get_object_or_404(Task, pk=pk)
    task = get_object_or_404(Task, pk=pk, user=request.user)# for user specific


    # Step 2: If the user submitted the form
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)  # bind form with task
        if form.is_valid():
            form.save()  # update existing task
            return redirect("list_task")  # go back to task list
    else:
        # Step 3: If GET request, show form with current task values
        form = TaskForm(instance=task)

    # Step 4: Render the form
    return render(request, "todo/update_task.html", {"form": form})

@login_required    
def delete(request,pk):
    # task = get_object_or_404(Task,pk=pk)
    task = get_object_or_404(Task, pk=pk, user=request.user) # for user specific


    task.delete()

    return redirect("list_task")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)  # auto login after register
            return redirect("list_task")
    else : 
        form = UserCreationForm()
    return render(request, "todo/register.html",{"form":form})
