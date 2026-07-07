class Stripe:
    def __init__(self, user):
        self.user = user

    def make_payment(self, amount_in_dollars):
        print(f"{self.user} make payment of {amount_in_dollars}")


class StripePaymentProcessor:
    def __init__(self, user):
        self.stripe = Stripe(user)

    def pay(self, amount_in_dollars):
        self.stripe.make_payment(amount_in_dollars)


class PayPal:
    def make_payment(self, user, amount_in_dollars):
        print(f"{user} make payment of {amount_in_dollars}")


class PayPalPaymentProcessor:
    def __init__(self, user):
        self.user = user
        self.paypal = PayPal()

    def pay(self, amount_in_dollars):
        self.paypal.make_payment(self.user, amount_in_dollars)


class Store:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def purchase_book(self, quantity, price):
        self.payment_processor.pay(quantity * price)

    def purchase_course(self, quantity, price):
        self.payment_processor.pay(quantity * price)


payment_processor = StripePaymentProcessor("John Doe")
store = Store(payment_processor)
store.purchase_book(1, 5)
store.purchase_course(2, 10)

payment_processor = PayPalPaymentProcessor("Lee Young")
store = Store(payment_processor)
store.purchase_book(3, 15)
store.purchase_course(4, 20)


""" This code snippet violates Dependency Inversion Principle(DIP)
class Stripe:
    def __init__(self, user):
        self.user = user

    def make_payment(self, amount_in_dollars):
        print(f"{self.user} made payment of {amount_in_dollars}")


class Store:
    def __init__(self, user):
        self.stripe = Stripe(user)

    def purchase_book(self, quantity, price):
        self.stripe.make_payment(price * quantity)

    def purchase_course(self, quantity, price):
        self.stripe.make_payment(price * quantity)
"""
