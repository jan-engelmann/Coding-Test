from django.shortcuts import render
from .forms import AmountForm

# Create your views here.


# Function to get real time currency exchange
def return_exchange_rate(from_currency, to_currency):
    # importing required libraries
    import requests, json
    api_key = "97T2Z6HHEBAJKBSV"
    # base_url variable store base url
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

    # main_url variable store complete url
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key

    # get method of requests module
    # return response object
    req_ob = requests.get(main_url)

    # json method return json format
    # data into python dictionary data type.

    # result contains list of nested dictionaries
    result = req_ob.json()

    return float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])


def calculator(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AmountForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            amount = float(form['AMOUNT'].value())
            from_curr = form['START_CURRENCY'].value()
            to_curr = form['END_CURRENCY'].value()
            rate = return_exchange_rate(from_curr, to_curr)
            return render(request, 'currency_conv/calculator.html', {'form': form,
                                                                     'result': amount * rate})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AmountForm()

    return render(request, 'currency_conv/calculator.html', {'form': form})
