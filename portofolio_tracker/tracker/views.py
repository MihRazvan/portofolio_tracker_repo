from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Portfolio, Stock, Transaction
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Cryptocurrency, Portfolio



def index(request):
    portfolios = Portfolio.objects.all()
    context = {'portfolios': portfolios}
    return render(request, 'index.html', context)


def dashboard(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    stocks = Stock.objects.filter(portfolio=portfolio)
    total_value = 0
    for stock in stocks:
        total_value += stock.shares * stock.price
    context = {'portfolio': portfolio, 'stocks': stocks, 'total_value': total_value}
    return render(request, 'dashboard.html', context)
    
def transactions(request):
    transactions = Transaction.objects.all()
    context = {'transactions': transactions}
    return render(request, 'transactions.html', context)


def settings(request):
    user = request.user
    if request.method == 'POST':
        form = SettingsForm(request.POST, instance=user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your settings have been updated.')
            return redirect('settings')
        else:
            messages.error(request, 'There was an error updating your settings.')
    else:
        form = SettingsForm(instance=user.profile)
    context = {'form': form}
    return render(request, 'settings.html', context)

def add_crypto(request):
    if request.method == 'POST':
        crypto_id = request.POST['crypto']
        quantity = float(request.POST['quantity'])
        crypto = Cryptocurrency.objects.get(id=crypto_id)
        portfolio, created = Portfolio.objects.get_or_create(user=request.user)
        portfolio.add_crypto(crypto, quantity)
        return redirect('index')
    else:
        currencies = Cryptocurrency.objects.all()
        return render(request, 'index.html', {'currencies': currencies})