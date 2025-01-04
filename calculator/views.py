from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'calculator/index.html')  # App-specific templates

def result(request):
    if request.method == 'POST':
        try:
            num1 = int(request.POST.get('num1'))
            num2 = int(request.POST.get('num2'))
            operation = request.POST.get('operation')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiplication':
                result = num1 * num2  
            elif operation == 'divisibleby':
                result = num1 / num2   
            else:
                result = "Invalid operation"
        except (TypeError, ValueError):
            result = "Invalid input"
    else:
        result = None  # Default value for non-POST requests

    return render(request, 'calculator/result.html', {'result': result})
