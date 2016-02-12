from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Employee

# Create your views here.
@login_required
def esat_index(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'esat/index.html', {})
    
@login_required
def employee_new(request):
    return render(request, 'esat/add_employee.html', {})
    
@login_required
def employee_list(request):
    employees = Employee.objects.order_by('last_name')
    ctx = {'emp_list': employees}
    return render(request, 'esat/employee_list.html', ctx)

@login_required
def employee_edit(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    ctx = {'employee': emp}
    return render(request, 'esat/edit_employee.html', ctx)
    
#@login_required
#def terminate_employee(reqeust, pk):
#    emp = get_object_or_404(Employee, pk=pk)
#    ctx = {'employee': emp}
#    return render(request, 'esat/terminate_employee.html', ctx)