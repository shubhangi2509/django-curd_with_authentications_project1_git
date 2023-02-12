from django.shortcuts import render,redirect
from .forms import StudentForm,Student
from .models import Student
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='signin_url')
def add_student_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'crud_app/add.html'
    context = {'form':form}
    return render(request, template_name, context)


@login_required(login_url='signin_url')
def show_view(request):
    obj = Student.objects.all()
    template_name = 'crud_app/show.html'
    context = {'data':obj}
    return render(request, template_name, context)




def update_view(request,pk):
    obj = Student.objects.get(id=pk)
    form = StudentForm(instance=obj)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'crud_app/add.html'
    context = {'form':form}
    return render(request, template_name, context)



def delete_view(request,pk):
    obj = Student.objects.get(id=pk)
    if request.method =='POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'crud_app/del_confirm.html'
    context = {'data':obj}
    return render(request, template_name, context)