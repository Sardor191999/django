# from django.http import HttpResponse
# from django.shortcuts import render
# from .models import Countries
# # Create your views here.
# def orm_list(request):
#    queryset = Countries.objects.all()
#    print(queryset.query)
#    country_list = ""
#    for post in queryset:
#        country_list += f"<li>{post.country_name}</li>"
#    return HttpResponse(f"<ul>{country_list}</ul>")
from django.shortcuts import render
from .models import Countries, Employees, Locations, Jobs, Dependents
from django.http import HttpResponse
from django.db.models import Q, Count


# MVT - Model, Views, Templates


def index_page(request):

    return render(request, "index.html")


def get_max_salary_employees(request, top):
    queryset = Employees.objects.all().order_by('-salary')[:top]
    return render(request, "max_salary.html", {"max_salary": queryset})


def get_dependents(request, employee_id):
    queryset = Dependents.objects.all().filter(employee=employee_id)
    employee = Employees.objects.get(employee_id=employee_id)
    context = {"deps": queryset, "employee": employee}
    return render(request, "dependents.html", context)
