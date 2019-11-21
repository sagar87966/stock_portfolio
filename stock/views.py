from django.shortcuts import render, redirect
import requests
import json
from django.contrib import messages
from .forms import StockForm
from .models import AddStocks

def home(request):
    #
    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get(
            f"https://cloud.iexapis.com/stable/stock/{ticker}/quote?token=pk_8da87c55a3da4493b3b772b2e7008b68")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'index.html', {'api': api})
    else:
        return render(request, 'index.html', {'ticker': "Enter the ticker symbol above...."})


def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    all_stocks = AddStocks.objects.all()
    all_companies = []
    for ticker in all_stocks:
        api_request = requests.get(
            f"https://cloud.iexapis.com/stable/stock/{ticker}/quote?token=pk_8da87c55a3da4493b3b772b2e7008b68")
        api = json.loads(api_request.content)
        api['id'] = ticker.id
        all_companies.append(api)
    if request.method == 'POST':
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Stocks has been added!!!")
            return redirect('add_stock')
        else:
            messages.error(request, "Invalid data!!!")


    return render(request, 'add_stock.html', {'all_stocks': all_stocks,'api':all_companies})


def delete(request, ticker_id):
    item = AddStocks.objects.get(pk=ticker_id)
    item.delete()
    messages.success(request, "Stocks has been deleted!!!")
    return redirect('add_stock')