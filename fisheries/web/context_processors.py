from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from web.models import *

def cart_count(request):

    cart_details = {}
    if request.user.is_authenticated():
        cc = PersonalCart.objects.filter(user=request.user, is_paid=False).count()
        cart_details.update({'cart_c': cc})
    return cart_details
