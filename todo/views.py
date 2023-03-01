from django.shortcuts import render

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib import messages

from django.template import loader
## import todo form and models

from .forms import TodoForm
from .models import Todo

###############################################

def index1(request):
    item_list = Todo.objects.all()
    if request.method == "POST":
        k=Todo.objects.create(title=request.POST.get('title'),
                              details=request.POST.get('detail'))
        k.save()
        return redirect('todo')
    form = TodoForm()


    page = {
             "forms" : form,
             "list" : item_list,
           }
    return render(request, 'todo/index1.html', page)


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')


# this function is for update
def update_data(request,id):
    if request.method == 'POST':
        pi = Todo.objects.get(pk=id)
        fm = TodoForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Todo.objects.get(pk=id)
        fm = TodoForm(instance=pi)

    return render(request,'todo/updatestudent.html', {'form':fm})


def updaterecord(request, id):
  title = request.POST['title']
  details = request.POST['details']
  member = Todo.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('todo'))
