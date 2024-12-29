from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect

@login_required
def dashboard(request):
    return render(request, 'employees/dashboard.html')

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

@login_required
def add_employee(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        employee_form = EmployeeForm(request.POST, request.FILES)
        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save()
            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()
            messages.success(request, 'Employee created successfully.')
            return redirect('employee_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserForm()
        employee_form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'user_form': user_form, 'employee_form': employee_form})

@login_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            messages.success(request, 'Employee updated successfully.')
            return redirect('employee_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        employee_form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_edit.html', {'employee_form': employee_form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':  # Handle POST request (confirmation)
        employee.user.delete() # Deletes the user which automatically deletes the employee profile because of on_delete=models.CASCADE
        messages.success(request, 'Employee deleted successfully.')
        return redirect('employee_list')
    return render(request, 'employees/employee_delete.html', {'employee': employee})  # Show confirmation page
def test_logout(request):
    print("Logout view called")
    logout(request)
    return redirect('login')