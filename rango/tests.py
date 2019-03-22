from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders

# General Tests
class GeneralTests(TestCase):
    def test_using_css(self):
        # Check is css is used
        result = finders.find('css/styles.css')
        self.assertIsNotNone(result)

# Tests for Index Page
class IndexPageTests(TestCase):
         
    def test_index_using_template(self):
        # Check the template used to render index page
        # Chapter 4
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'rango/index.html')
    
    def test_index_has_title(self):
        # Check to make sure that the title tag has been used
        # And that the template contains the HTML from Chapter 4 
        response = self.client.get(reverse('index'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)


# Tests for the About Page
class AboutPageTests(TestCase):
        
    def test_about_contains_create_message(self):
        # Check if in the about page is there - and contains the specified message
        # Exercise from Chapter 4
        response = self.client.get(reverse('about'))
        self.assertIn(b'This is Restaurant Reviews Here you can add your own restaurant, as well as view and review restaurants', response.content)
        
    def test_about_using_template(self):
        # Check the template used to render index page
        # Exercise from Chapter 4 
        response = self.client.get(reverse('about'))

        self.assertTemplateUsed(response, 'rango/about.html')
        
        
# Tests for the Models        
class ModelTests(TestCase):

    def setUp(self):
        try:
            from populate_rango import populate
            populate()
        except ImportError:
            print('The module populate_rango does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')
        
        
    def get_category(self, name):
        
        from rango.models import Category
        try:                  
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:    
            cat = None
        return cat
        
    def test_python_cat_added(self):
        cat = self.get_category('Chinese')  
        self.assertIsNotNone(cat)
        
    def test_python_cat_with_likes(self):
        cat = self.get_category('Chinese')
        self.assertEquals(cat.likes, 64)

    def get_restaurant(self, name):

        from rango.models import Page
        try:
            res = Page.objects.get(name=name)
        except Page.DoesNotExist:
            res = None
        return res

    def test_python_res_added(self):
        res = self.get_restaurant('Richmond Oriental')
        self.assertIsNotNone(res)
		
    def test_python_res_with_views(self):
        res = self.get_restaurant('Richmond Oriental')
        self.assertEquals(res.views, 64)

    def test_python_res_with_url(self):
        res = self.get_restaurant('Richmond Oriental')
        self.assertEquals(res.url, "https://www.richmond-oriental.com/")
        

# Tests for the Views
class ViewTests(TestCase):
  
    def test_about_using_template(self):
        # Check the template used to render index page
        # Exercise from Chapter 4
        response = self.client.get(reverse('about'))

        self.assertTemplateUsed(response, 'rango/about.html')

    def test_about_contains_create_message(self):
        # Check if in the about page contains the message from the exercise
        response = self.client.get(reverse('about'))
        self.assertIn('This is Restaurant Reviews Here you can add your own restaurant, as well as view and review restaurants', response.content)


    def setUp(self):
        try:
            from populate_rango import populate
            populate()
        except ImportError:
            print('The module populate_rango does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')


    def get_category(self, name):

        from rango.models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None
        return cat
		
    def get_restaurant(self, name):

        from rango.models import Page
        try:
            res = Page.objects.get(name=name)
        except Page.DoesNotExist:
            res = None
        return res	
		

    def test_python_cat_added(self):
        cat = self.get_category('Chinese')
        self.assertIsNotNone(cat)

    def test_python_cat_with_views(self):
        cat = self.get_category('Chinese')
        self.assertEquals(cat.views, 128)
		
    def test_python_res_added(self):
        res = self.get_restaurant('Richmond Oriental')
        self.assertIsNotNone(res)
		
    def test_python_res_with_views(self):
        res = self.get_restaurant('Richmond Oriental')
        self.assertEquals(res.views, 64)

    def test_python_res_with_url(self):
        res = self.get_restaurant('Richmond Oriental')
        self.assertEquals(res.url, "https://www.richmond-oriental.com/")

    def test_view_has_title(self):
        response = self.client.get(reverse('index'))

        #Check title used correctly
        self.assertIn('<title>', response.content)
        self.assertIn('</title>', response.content)

    # Need to add tests to:
    # check admin interface - is it configured and set up

    def test_admin_interface_page_view(self):
        from rango.admin import PageAdmin
        self.assertIn('category', PageAdmin.list_display)
        self.assertIn('slug', PageAdmin.list_display)

    # are categories displayed on index page?

    # does the category model have a slug field?


    # test the slug field works..
    def test_does_slug_field_work(self):
        from rango.models import Category
        cat = Category(name='how do i create a slug in django')
        cat.save()
        self.assertEqual(cat.slug,'how-do-i-create-a-slug-in-django')

    # test category view does the page exist?


    # test whether you can navigate from index to a category page


    # test does index page contain top five pages?

    # test does index page contain the words "most liked" and "most viewed"

    # test does category page contain a link back to index page?

	
    def setUp2(self):
        try:
            from rango.forms import PageForm
            from rango.forms import CategoryForm

        except ImportError:
            print('The module forms does not exist')
        except NameError:
            print('The class PageForm does not exist or is not correct')
        except:
            print('Something else went wrong :-(')

    pass
    # test is there a PageForm in rango.forms

    # test is there a CategoryForm in rango.forms

    # test is there an add page page?

    # test is there an category page?


    # test if index contains link to add category page
    #<a href="/rango/add_category/">Add a New Category</a><br />


    # test if the add_page.html template exists.
