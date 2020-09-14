from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer

class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        if request.method == 'POST':
            erroMsg = None
            email = request.POST.get("email")
            password = request.POST.get("password")
            
            user = Customer.get_user_by_email(email)

            if user:
                flag = check_password(password, user.password)
                if flag:
                    request.session["uid"] = user.id
                    if Login.return_url:
                        return HttpResponseRedirect(Login.return_url)
                    else:
                        Login.return_url = None
                        return redirect("index")
                else:
                    erroMsg = "User Name & Password is incorrect."
            else:
                erroMsg = "Email is incorrect."

            return render(request, 'login.html', {'error': erroMsg})

def logout(request):
    request.session.clear()
    return redirect('login')