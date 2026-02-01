from django.contrib.auth.models import User, Group, Permission
from django.test import TestCase, Client
from django.urls import reverse
from .models import Internationalregion, Country
from .forms import CountryForm, InternationalregionForm , UserPasswordUpdateForm, UserRegistrationForm, UserForm, GroupForm
from adminsettings import commonsettings
# Create your tests here.

class UserTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser('testuser', 'test@example.com', 'password123')
        self.client.login(username='testuser', password='password123')

    def test_password_reset_view(self):
        url = reverse('password_reset')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset.html')
    
    def test_change_password(self):
        url = reverse('change_password')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administrator/password_change_form.html')

        form = UserPasswordUpdateForm(data={
            'password': '45656',
            'password2': '45656'
        })

        self.assertTrue(form.is_valid())
        response = self.client.post(url, {
            'password': '45656',
            'password2': '45656'
        })

        self.user.refresh_from_db()  # Reload the user from the database
        self.assertTrue(self.user.check_password('45656'))

    def test_signup(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

        form = UserRegistrationForm(data={
            'username': 'admiiinm',
            'email': 'admin22@gmail.com',
            'password': '45656',
            'password2': '45656',
            'agree_to_terms': 1
        })
        self.assertTrue(form.is_valid())

        self.assertTrue(form.is_valid())
        response = self.client.post(url, {
            'username': 'admiiinm',
            'email': 'admin22@gmail.com',
            'password': '45656',
            'password2': '45656',
            'agree_to_terms': 1
        })
        
        self.assertTemplateUsed(response, 'registration/signup_complete.html')
    
    def test_impersonate(self):
        client_user = User.objects.create(username="clientuser", email="client@example.com", password="clientpass")
        response = self.client.get(reverse('impersonate_user', args=[client_user.pk]))
        self.assertEqual(response.status_code, 302)

class AdministrationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.email = 'admin@example.com'
        self.password='password'
        self.user = User.objects.create_superuser(username='testuser', email=self.email, password=self.password)
        self.client.login(username='testuser', password='password')

        # urls
        self.login_url = reverse('login')
        self.dashboard_url = reverse('dashboard')

    def test_login(self):
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        
        if commonsettings.DASHBOARD_CONFIG == 'web':
            self.assertTemplateUsed(response, 'registration/login.html')
        else:
            self.assertTemplateUsed(response, 'registration/login_soft.html')

    def test_dashbaord(self):
        response = self.client.get(self.dashboard_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administrator/dashboard.html')

    def test_dashboard_not_logged_in(self):
        self.client.logout()

        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 302)

    def test_user(self):
        view = reverse('list_user')
        add_item = reverse('add', args=['user', 2])
        edit_item = reverse('change', args=[self.user.pk, 'auth', 'user', 2])
        response = self.client.get(view)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administrator/admin/user/list_user.html')

        form = UserForm(data={
            'username': 'admiiinm',
            'email': 'admin22@gmail.com',
            'password': '45656',
            'password2': '45656',
        })
        self.assertTrue(form.is_valid())

        response = self.client.post(add_item, {
            'username': 'adminanup',
            'email': 'admin22@gmail.com',
            'password': '45656',
            'password2': '45656',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='adminanup').exists())
        
        adminanup = User.objects.get(username='adminanup')
        response = self.client.delete(reverse('delete', args=[adminanup.pk, 'auth', 'user']))
        self.assertEqual(response.status_code, 302)

        response = self.client.post(edit_item, {
            'first_name': 'Updated',
            'last_name': 'User',
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Updated')


class GroupPermissionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.email = 'admin@example.com'
        self.password='password'
        self.user = User.objects.create_superuser(username='testuser', email=self.email, password=self.password)
        self.client.login(username='testuser', password='password')

        # urls
        self.login_url = reverse('login')
        self.dashboard_url = reverse('dashboard')

    def test_group(self):
        permission1 = Permission.objects.create(codename='test_permission1', name='Test Permission 1', content_type_id=1)
        permission2 = Permission.objects.create(codename='test_permission2', name='Test Permission 2', content_type_id=1)
        view = reverse('list_group')
        add_item = reverse('add', args=['group', 2])
        response = self.client.get(view)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administrator/admin/group/list_group.html')

        form = GroupForm(data={
            'name':'Test Group'
        })
        self.assertTrue(form.is_valid())

        response = self.client.post(add_item, {
            'name':'Test Group2',
            'permissions': [permission1.pk, permission2.pk],
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Group.objects.filter(name='Test Group2').exists())
        
        getgroup = Group.objects.get(name='Test Group2')
        response = self.client.delete(reverse('delete', args=[getgroup.pk, 'auth', 'group']))
        self.assertEqual(response.status_code, 302)
        
        group = Group.objects.create(name='TestGroup')
        response = self.client.post(reverse('change', args=[group.pk, 'auth', 'group', 2]), {
            'name':'Updated'
        })
        group.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        
        self.assertEqual(group.name, 'Updated')
        
        

class InternationalRegionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')
        self.internation_region = Internationalregion.objects.create(international_region_name="Asia")
        self.list_internationalregion = reverse('list_internationalregion')
        self.add_item_internationalregion = reverse('add', args=['internationalregion', 2])
        self.edit_item_internationalregion = reverse('change', args=[self.internation_region.id, 'administrator', 'internationalregion', 2])
        self.delete_item_internationalregion = reverse('delete', args=[self.internation_region.id, 'administrator', 'internationalregion'])

    def test_get_internationalregion(self):
        region = Internationalregion.objects.get(international_region_name="Asia")
        self.assertEqual(region.international_region_name, 'Asia')
        self.assertTrue(isinstance(region, Internationalregion))

    def test_list_internationalregion(self):
        response = self.client.get(self.list_internationalregion)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administrator/international_region/list_international_region.html')

    def test_add_internationalregion(self):
        response = self.client.post(self.add_item_internationalregion, {'international_region_name':'Test Item 3'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Internationalregion.objects.last().international_region_name, 'Test Item 3')

    def test_edit_internationalregion(self):
        response = self.client.post(self.edit_item_internationalregion, {'international_region_name':'Update Test Item 3'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Internationalregion.objects.first().international_region_name, 'Update Test Item 3')

    def test_delete_internationalregion(self):
        response = self.client.delete(self.delete_item_internationalregion)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Internationalregion.objects.count(), 0)

    def test_InternationalForm(self):
        form = InternationalregionForm(data={
            'international_region_name': 'John'
        })

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['international_region_name'], 'John')
    
    def test_Invalid_InternationalForm(self):
        form = InternationalregionForm(data={
            'international_region_name': ''
        })

        self.assertFalse(form.is_valid())
        self.assertIn('international_region_name', form.errors)



class CountryTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')
        self.internation_region = Internationalregion.objects.create(international_region_name="Asia")
        self.country = Country.objects.create(
            iso2 = '20',
            country_name = 'BD',
            international_region = self.internation_region
            )
        self.list_country = reverse('list_country')
        self.add_item_country = reverse('add', args=['country', 2])
        self.edit_item_country = reverse('change', args=[self.country.id, 'administrator', 'country', 2])
        self.delete_item_country = reverse('delete', args=[self.country.id, 'administrator', 'country'])

    def test_get_country(self):
        country = Country.objects.get(country_name="BD")
        self.assertEqual(str(country.country_name), 'BD')
        self.assertTrue(isinstance(country, Country))
    
    def test_list_country(self):
        response = self.client.get(self.list_country)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'administrator/country/list_country.html')

    def test_add_country(self):
        response = self.client.post(self.add_item_country, {'iso2':'20', 'country_name': 'BD', 'international_region': self.internation_region.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Country.objects.last().country_name, 'BD')

    def test_edit_country(self):
        response = self.client.post(self.edit_item_country, {'iso2':'20', 'country_name': 'BDD', 'international_region': self.internation_region.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Country.objects.first().country_name, 'BDD')

    def test_delete_country(self):
        response = self.client.delete(self.delete_item_country)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Country.objects.count(), 0)

    def test_CountryForm(self):
        form = CountryForm(data={
            'iso2':'20', 'country_name': 'BDD', 'international_region': self.internation_region
        })

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['country_name'], 'BDD')
    
    def test_Invalid_CountryForm(self):
        form = CountryForm(data={
            'iso2':'20', 'country_name': '', 'international_region': self.internation_region
        })

        self.assertFalse(form.is_valid())
        self.assertIn('country_name', form.errors)