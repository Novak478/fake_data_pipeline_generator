#usr/bin/python3.6
# coding=utf-8
from faker import Faker
from faker.providers import internet
import json

#TODO: Delete references below when pushing to server test
##workon fake_data_pipeline_generator
#git guide: https://rogerdudler.github.io/git-guide/

fake = Faker()
txn_creator = Txn_Creator()

#########################
# INITIALIZE GENERATORS #
#########################
fake.name()
fake.street_name()
fake.street_address()
fake.secondary_address()
fake.state()
fake.state_abbr(include_territories=False)
fake.address()
fake.building_number()
fake.city()
fake.zipcode()
fake.zipcode_plus4()
fake.country()
fake.country_code(representation="alpha-2")
fake.address()
fake.text()
fake.add_provider(internet)
fake.email()
fake.domain_name()
fake.ipv4_public(network=False, address_class=None)
fake.mac_address()
fake.ipv6(network=False)
fake.phone_number()
fake.user_agent()
fake.currency()
fake.currency_name()
fake.currency_code()

fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")
fake.credit_card_full(card_type=None)
fake.credit_card_number(card_type=None)
fake.credit_card_provider(card_type=None)
fake.credit_card_security_code(card_type=None)
my_word_list = [
'danish','cheesecake','sugar',
'Lollipop','wafer','Gummies',
'sesame','Jelly','beans',
'pie','bar','Ice','oat' ]

fake.sentence(ext_word_list=my_word_list)
# 'Oat beans oat Lollipop bar cheesecake.'

fake.latitude()
fake.longitude()

fake.ean(length=13) #item sku
fake.color_name() #random color
fake.bs() #item description
fake.catch_phrase() #item
fake.company() #company



##################
# END GENERATORS #
##################

for _ in range(10):
  #data = {}
  #data['transactions'] = []
  print("----------------------")
  print("Name: {}".format(fake.name()))
  print("Street Name: {}".format(fake.street_name()))
  print("Street Address: {}".format(fake.street_address()))
  print("Secondary Address: {}".format(fake.secondary_address()))
  print("State: {}".format(fake.state()))
  print("City: {}".format(fake.city()))
  print("Zipcode: {}".format(fake.zipcode()))
  print("Zipcode+4: {}".format(fake.zipcode_plus4()))
  # print("Country: {}".format(fake.country()))
  print("Country: {}".format("United States"))
  print("Country Code: {}".format("USA"))
  print("Transaction Amount Raw: {}".format(txn_creator.raw_txn()))
  print("Transaction Amount Formatted: {}".format(txn_creator.formatted_txn()))
  print("Email: {}".format(fake.email()))
  print("Domain Name: {}".format(fake.domain_name()))
  print("IPV4: {}".format(fake.ipv4_public(network=False, address_class=None)))
  print("IPV6: {}".format(fake.ipv6(network=False)))
  print("MAC Address: {}".format(fake.mac_address()))
  print("Phone Number: {}".format(fake.phone_number()))
  print("User Agent: {}".format(fake.user_agent()))
  #print("Currency: {}".format(fake.currency()))
  print("Currency: {}".format("US"))  
  print("CC Expiration Date: {}".format(fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")))
  #print("CC Full: {}".format(fake.credit_card_full(card_type=None)))
  print("CC Number: {}".format(fake.credit_card_number(card_type=None)))
  print("CC Provider: {}".format(fake.credit_card_provider(card_type=None)))
  print("CC Security Code: {}".format(fake.credit_card_security_code(card_type=None)))
  print("Latitude: {}".format(fake.latitude()))
  print("Longitude: {}".format(fake.longitude()))
  print("EAN: {}".format(fake.ean(length=13)))
  print("Color: {}".format(fake.color_name()))
  print("Item: {}".format(fake.catch_phrase()))
  print("Item Description:: {}".format(fake.bs()))
  print("Company: {}".format(fake.company()))
  print("-----------------")
  #with open('data.txt', 'w') as outfile:
    #json.dump(data, outfile)