from products.models import Products


class Cart():
    "uma classe base que prove funções para o funcionamento do carrinho "

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] ={}
        self.cart = cart

    def add(self, product, qty):
        product_id = str(product.id) 
        
        if product_id is self.cart:
            self.cart[product_id]['qty'] = qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': qty}
        
        self.save()

    def update(self, product, qty):
        """
        Update values in session data
        """
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
        self.save()

    def delete(self, product):

        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            print(product_id)
            self.save()
    

    def get_total_price(self):
        return sum(float(item['price']) * float(item['qty']) for item in self.cart.values())

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.cart.keys()
        products = Products.products.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item
    
    def __len__(self):

        return sum(item['qty']for item in self.cart.values()) 

    def save(self):
        self.session.modified = True

