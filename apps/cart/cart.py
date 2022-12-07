from django.conf import settings

from apps.product.models import Product


class Cart(object):
    def __init__(self, request):  # to set a var cart
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)  # initialize session (set in settings)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}  # create a new session if there is not

        self.cart = cart  # set a cart (see line 9) or set a new cart (see line 12)

    def __iter__(self):  # iteration
        for p in self.cart.keys():  # iterate thru the keys
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)  # get a property of the key from the object in DB

        for item in self.cart.values():
            item['total_price'] = item['product'].price * item['quantity']  # counting a price of items in cart

            yield item

    def __len__(self):  # counting the items in the cart - quantity
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product_id, quantity=1, update_quantity=False):  # adding quantity of the product and updating total
        product_id = str(product_id)  # converting id to str

        if product_id not in self.cart:  # creating new quantity if the product yet is not in the cart
            self.cart[product_id] = {'quantity': 1, 'id': product_id}

        if update_quantity:  # updating quantity of the product if the product is already in the cart
            self.cart[product_id]['quantity'] += int(quantity)

            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)

        self.save()

    def remove(self, product_id):
        if product_id in self.cart: # check if the product in the cart, if positive -  delete it
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart # all info in the cart save to session data
        self.session.modified = True

    def clear(self):  # clear the session in the history of the browser
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        return sum(item['quantity'] * item['product'].price for item in self.cart.values())
