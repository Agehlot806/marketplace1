from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def demo(request):
    user_type = "Admin"
    return render(request, "admin/dashboard.html", {'user_type':user_type})