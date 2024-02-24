from django.shortcuts import render
from . import models
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def auto_register(request):

    if request.method == 'POST':

        title  = request.POST.get('title')
        price = request.POST.get('price')
        extra_data = request.POST.get('extra_data', None)
        print(title)
        if title == 'دریافتی':
            type_of_transaction = models.Types.objects.get(title = 'در انتظار تایید')
            models.Transactions.objects.create(title=title, price = price, extra_data=extra_data, is_cost=False)
            return HttpResponse('Income Object Created!')


        elif title == 'هزینه':
            type_of_transaction = models.Types.objects.get(title = 'در انتظار تایید')
            models.Transactions.objects.create(title=title, price = price, extra_data=extra_data, is_cost=True)
            return HttpResponse ('Cost Object Created')
        
        return HttpResponse('400: Bad Request!')

