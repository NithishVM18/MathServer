from django.shortcuts import render

def churn_rate(request):
    IC = float(request.POST.get('initialcust', '0'))
    CL = float(request.POST.get('custlost', '0'))

    Churn_Rate = (CL / IC) * 100 if request.method == 'POST' else 0 

    print("Initial Customer =", IC)
    print("Customer Lost =", CL)
    print("Churn Rate =", Churn_Rate)

    return render(
        request,
        'myapp/math.html',
        {'IC': IC, 'CL': CL, 'Churn_Rate': Churn_Rate}
    )