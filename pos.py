import json
from tabulate import tabulate

with open ('menu.json', 'r') as file:  # load data from json file
  data  = file.read()
menu = json.loads(data) # menu array

valid_codes = []

for food in menu:
  valid_codes.append(food['code']) # append all food code to valid codes array

class Order:

  def __init__(self):
    self.orders = [] # initialize empty order
  
  def categorize(self, prefix):
    list_of = []
    for food in menu:
      if food['code'][0] == prefix: # Prefix B, S, C, or D
        list_of.append(food['code']+' '+food['name']+' '+str(food['price']))
    return list_of

  def main(self):
    self.line()
    print('SAMPLE POINT OF SALE SYSTEM (POS)')
    print('For Fast Food Chain')
    print('Developed by: Jana Alyssa Alba')
    print('Date Developed: February 1')

    print(tabulate({ 
      '____________Burger___________': self.categorize('B'),
      '____________Pasta____________': self.categorize('S'),
      '____________Chicken__________': self.categorize('C'),
      '____________Drinks___________': self.categorize('D'),
    }, headers="keys"))
    print('\n\nNote: with 20% discount for Senior Citizen')
    self.line()

    print('CUSTOMER DETAILS')

    self.customer_name = input('Enter Customer Name: ')
    self.is_senior = input('Senior Citizen? (Y/N): ').upper()

    print('START ORDER')

    self.start_order()

  def get_order_details(self, code):
    for food in menu: # loop menu
      if food['code'] == code: # find the object if the code matched
        return food 
    else:
        return

  def line(self):
    print('---------------------------------------------------------------------------------------------------------------------------')

  def start_order(self):
    order = input('Enter Customer Order: ').upper()

    if order not in valid_codes: # if the code enter is not in valid_codes array re enter the code
      print('Please enter valid code')
      return self.start_order()

    quantity = int(input('Enter Quantity: '))
    
    # check if code exist here
    self.orders.append([order, quantity])

    continue_order = input('Any other order (Y/N): ').upper()

    if continue_order == 'Y': # if "Y" continue the order process
      return self.start_order()
    else:
      return self.process() # else proceed to order computation

  def percentage(self, num, per):
    return (num * per) / 100

  def process(self):
    price = 0
    discount = 0
    total_amount = 0

    for order in self.orders: # loop orders
      details = self.get_order_details(order[0]) # get the details in menu array
      price += details['price'] * order[1]  # increament by price times quantity

    if self.is_senior == 'Y':
      discount = self.percentage(price ,20)

    total_amount = price - discount;

    print('Total Amount: '+str(total_amount))
    self.payment = float(input('Enter Payment: '))
    
    if self.payment < price:
      print('Payment is less than the total amounts')
      return self.process()

    self.line()
    print('Customer Name: ', self.customer_name)

    for order in self.orders: # loop orders
      details = self.get_order_details(order[0]) # get the details in object
      print(str(order[1])+' '+details['name'])

    print('Total Amount: '+str(total_amount))
    print('Less Discount (20%): '+str(discount))
    print('Amount Paid: '+str(self.payment))
    self.line()
    print('Change: '+str(self.payment - total_amount))
    self.line()
    print('Thank you and Come Again')

    # clean up

order = Order()
order.main() # run the program