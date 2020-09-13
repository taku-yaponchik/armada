from django.shortcuts import render, redirect
from .models import *
from .forms import ContactClientForm
# Create your views here.


def services_list(request):
    services = Services.objects.all()
    portfolio = Portfolio.objects.all()
    production = Production.objects.all()
    price = Price.objects.all()
    customer = Customer.objects.all()
    command = Command.objects.all()
    contact_client = ContactClient(request)

    if request.method == 'POST':
        form = ContactClientForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.save()
            return redirect(request, 'contact_form.html', {'contact': contact})
    else:
        form = ContactClientForm()

    context = {
        'services': services,
        'portfolio': portfolio,
        'production': production,
        'price': price,
        'customer': customer,
        'command': command,
        'contact_client': contact_client,
        'form': form
    }
    return render(request, 'index.html', context)


def portfolio_list(request):
    portfolio_panel = Portfolio.objects.all()



    context = {
        'portfolio_panel': portfolio_panel,


    }
    return render(request, 'portfolio_panel.html', context)
