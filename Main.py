from CreditCard import CreditCard


def main():
    CreditCard.security()
    ivan_credit_card = CreditCard(number_of_card=8888777766665555, type_of_card="Gold", currency_type="Uah",
                               card_holder_name="Ivan", payment_commission="0,5", cvc=111)
    yura_credit_card = CreditCard(number_of_card=1232343454565678, type_of_card="Premium",
                              currency_type="$", cvc=123)
    stepan_credit_card = CreditCard(number_of_card=1111222233334444, type_of_card="Standard")

    ivan_credit_card.__str__()
    yura_credit_card.__str__()
    stepan_credit_card.__str__()


main()




