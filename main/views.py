from django.shortcuts import render, redirect, HttpResponse
def index(request):
    return render(request, "index.html")

def processing_form_data(request):
    print("Processing form data")
    print(request.POST)
    name = request.POST['name']
    age = request.POST['age']
    email = request.POST['email']
    password = request.POST['password']
    return redirect(f'/success/{name}/{age}/{email}/{password}')

def success(request, name, age, email, password):
    context = {
        'name': name,
        'age': age,
        'email': email,
        'password': password
    }
    return render(request, "success.html", context)