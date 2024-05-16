from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.


def list(request):
    sort_by = request.GET.get('sort_by')
    if sort_by == 'name':
        employee_list = Employee.objects.all().order_by('fullname')
    elif sort_by == 'time':
        employee_list = Employee.objects.all().order_by('-registration_time')
    else:
        employee_list = Employee.objects.all()

    context = {'employee_list': employee_list}
    return render(request, "employee_register/employee_list.html", context)

def search_employees(request):
    query = request.GET.get('q')
    if query:
        employees = Employee.objects.filter(fullname__icontains=query)
    else:
        employees = Employee.objects.all()
    return render(request, 'employee_register/employee_list.html', {'employee_list': employees, 'query': query})

def form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')