from django.shortcuts import render


def demo(request):
    user_type = "Supplier"
    return render(request, "supplier/index.html", {'user_type':user_type})
