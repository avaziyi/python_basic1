# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:05:12 2013

@author: Mars
"""

class ShoppingCart(object):
	"""Creates shopping cart objects
	for users of our fine website."""
	items_in_cart = {}
	def __init__(self, customer_name):
		self.customer_name = customer_name
		
	def add_item(self, product, price):
		"""Add product to the cart."""
		if not product in self.items_in_cart:
			self.items_in_cart[product] = price
			print product + " added."
		else:
			print product + " is already in the cart."
		
	def remove_item(self, product):
		"""Remove product from the cart."""
		if product in self.items_in_cart:
			del self.items_in_cart[product]
			print product + " removed."
		else:
			print product + " is not in the cart."
	
	def already_item(self):
		for name,value in self.items_in_cart.items():
			print name,value
												
my_cart = ShoppingCart("A")
my_cart.add_item("potato",2)
my_cart.add_item("lycium",20)
my_cart.add_item("lycium",20)
my_cart.already_item()