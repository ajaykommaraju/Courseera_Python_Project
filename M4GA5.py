'''Complete the code to iterate through the keys and values of the car_prices dictionary, 
printing out some information about each one.'''
def car_listing(car_prices):
  result = ""
  for x,y in car_prices.items():
    result += "{} costs {} dollars".format(x,y)+"\n"
  return result
