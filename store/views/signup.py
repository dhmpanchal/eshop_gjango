from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer

class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')

    def validateInput(self, customer):
        errorMsg = None

        if not customer.first_name:
            errorMsg = "First name must be require"
        elif len(customer.first_name) < 4:
            errorMsg = "First name must be minimum 4 chatacter long"
        elif not customer.last_name:
            errorMsg = "Last name must be require"
        elif len(customer.last_name) < 4:
            errorMsg = "Last name must be minimum 4 chatacter long"
        elif not customer.email:
            errorMsg = "Email must be require"
        elif len(customer.email) < 5:
            errorMsg = "Email must be minimum 5 chatacter long"
        elif not customer.phone:
            errorMsg = "Phone must be require"
        elif len(customer.phone) < 10:
            errorMsg = "Phone must be 10 chatacter long"
        elif customer.isExistByEmail():
            errorMsg = "Email is already exists"

        return errorMsg
    
    def post(self, request):
        if request.method == 'POST':
            fname = request.POST.get("firstname")
            lname = request.POST.get("lastname")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            password = request.POST.get("password")

            errorMsg = None

            customer = Customer(first_name=fname,
                                last_name=lname,
                                email=email,
                                phone=phone,
                                password=password)

            errorMsg = self.validateInput(customer)
            
            values = {
                'fname': fname,
                'lname': lname,
                'email': email,
                'phone': phone
            }

            if not errorMsg:
                customer.password = make_password(customer.password)
                customer.register()
                return redirect("index")
            else:
                data = {
                    'error': errorMsg,
                    'values': values
                }
                return render(request, 'signup.html', data)
        return render(request, 'signup.html')