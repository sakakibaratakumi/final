from django.shortcuts import render
from . models import Order
# Create your views here.
def home_page(request):
	if request.method == 'POST':
		our_item = request.POST.get('item')
		our_address = request.POST.get('address')
		order_obj = Order.objects.create(
			item = our_item,
			address = our_address	
		)
		return render(request,'order/home_page.html',{'item':our_item, 'address':our_address})
	return render(request, 'order/home_page.html')
	