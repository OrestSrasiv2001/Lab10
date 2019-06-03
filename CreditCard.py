class CreditCard:
    security_at_the_creditcard = "Safely"

    def __init__(self, number_of_card=None, type_of_card=None, currency_type=None,
                 card_holder_name=None,  payment_commission=None, cvc=None):
        self.number_of_card = number_of_card
        self.type_of_card = type_of_card
        self.currency_type = currency_type
        self.card_holder_name = card_holder_name
        self.payment_commission = payment_commission
        self.cvc = cvc

    def __str__(self):
        print("\nnumber_of_card =", self.number_of_card,
              "\ntype_of_card:", self.type_of_card,
              "\ncurrency_type:", self.currency_type,
              "\ncard_holder_name =", self.card_holder_name,
              "\npayment_commission:", self.payment_commission,
              "\ncvc:", self.cvc,"\n")

    @staticmethod
    def security():
        print("Level of security in the credit card: ", CreditCard.security_at_the_creditcard)

    def __del__(self):
        pass


    @staticmethod
    def World():
        print("Hello world")







