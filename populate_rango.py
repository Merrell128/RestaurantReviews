import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page, Review

def populate():
	# First, we will create lists of dictionaries containing the pages 
	# we want to add into each category
	# Then we will create a dictionary of dictionaries for our categories. 
	# This might seem a little bit confusing, but it allows us to iterate
	# through each data structure, and add the data to our models

	chinese_pages = [{'title': 'Lychee Oriental', 'picture': 'profile_images/LycheeOriental.jpg', 'address': '59 Mitchell St, Glasgow G1 3LN', 'phone': '01412482240'},
					{'title': 'Amber Regent', 'picture': 'profile_images/AmberRegent.jpg', 'address': '50 W Regent St, Glasgow G2 2RA', 'phone': '01413311655'}]
		
	italian_pages = [{'title': 'Amarone', 'picture': 'profile_images/Amarone.jpg', 'address': '2 Nelson Mandela Pl, Glasgow G2 1BT', 'phone': '01413331122'},
					{'title': 'Sarti', 'picture': 'profile_images/Sarti.jpg', 'address': '42 Renfield St, Glasgow G2 1NE', 'phone': '01415727000'}]
	
		
	other_pages = [{'title': 'Hard Rock Cafe', 'picture': 'profile_images/HardRockCafe.jpg', 'address': '179 Buchanan St, Glasgow G1 2JZ', 'phone': '01413538797'},
					{'title': 'Rogano', 'picture': 'profile_images/Rogano.jpg', 'address': '11 Exchange Pl, Glasgow G1 3AN', 'phone': '01412484055'}]
								
		
	cats = {"Chinese": {"pages": chinese_pages, "views" : 128, "likes" : 64},
			"Italian": {"pages": italian_pages, "views" : 64, "likes" : 32},
			"Other Cuisines": {"pages": other_pages, "views" : 32, "likes" : 16} }
			
	reviews = {'Lychee Oriental': [{'rating': 1, 'text': 'Great place with lovely food.'},
								{'rating': 4, 'text': 'Had better'}],
				'Amber Regent': [{'rating': 3, 'text': 'Great food but got food poisoning afterwards, worth it.'}],
				'Amarone': [{'rating': 1, 'text': 'Never heard of it in my life, never been either.'}],
				'Sarti': [{'rating': 5, 'text': 'Best pizza in town,MUST TRY!!'}],
				'Hard Rock Cafe': [{ 'rating': 2, 'text': 'Had better elsewhere.'}],
				'Rogano': [{'rating': 4, 'text': 'Not bad, needs improvemnt.'}]}
	
			
	# If you want to add more catergories or pages,
	# add them to the dictionaries above. 
	
	# The code below goes through the cats dictionary, then adds each category,
	# and then adds all the associated pages for that category.
	# if you are using Python 2.x then use cats.iteritems() see 
	# http://docs.quantifiedcode.com/python-anti-patterns/readability/
	# for more information about how to iterate over a dictionary properly
	
	for cat, cat_data in cats.items():
		c = add_cat(cat, cat_data["views"], cat_data["likes"])
		for p in cat_data["pages"]:
			res = add_page(c, p["title"], p["address"], p["phone"])
			for review in reviews[p["title"]]:
				add_review(res, review["rating"], review["text"])
			
			
			
	# Print out the categories we have added.
	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))
			
def add_page(cat, title, address, phone):
	p = Page.objects.get_or_create(category=cat, title=title)[0]
	p.address=address
	p.phone=phone
	p.save()
	return p
	
def add_cat(name, views, likes):
	c = Category.objects.get_or_create(name=name)[0]
	c.views = views
	c.likes = likes
	c.save()
	return c
	
def add_review(page, rating, text):
	rev = Review.objects.get_or_create(page=page, rating = rating, text = text)[0]
	rev.save()
	return rev
# Start execution here!
if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()
