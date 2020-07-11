# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
months = 0

while principal > 0:
    months = months + 1
    if months <= extra_payment_end_month and months >= extra_payment_start_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    if principal < 0:
        total_paid = total_paid + principal
        principal = 0
    output = f'{months} ${total_paid:0.2f} {principal:0.2f}'
    print(output)
    # print(months, round(total_paid,2), round(principal,2))
