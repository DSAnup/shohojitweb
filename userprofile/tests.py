from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from userprofile.models import Profile, Country

User = get_user_model()

# Create your tests here.

class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.country = Country.objects.create(country_name='TestCountry')  # Assuming Country model has a 'name' field
        self.profile = Profile.objects.create(user=self.user, country=self.country)
        self.client.login(username='testuser', password='testpassword')
        self.profile_url = reverse('profile')
        self.profile_settings_url = reverse('profile_settings', kwargs={'id': self.user.pk})

    def test_profile_view(self):
        """Test profile view renders correctly for logged-in user."""
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userprofile/profile.html')

    def test_profile_settings_view_with_id(self):
        """Test profile_settings view with user id."""
        response = self.client.get(self.profile_settings_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userprofile/settings.html')
    
    def test_profile_settings_updates_user_and_profile(self):
        # Test updating the user and profile
        self.client.login(username='testuser', password='testpass')
        # Prepare a test image file for profile picture
        test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\xff\x00\xff\xff\xff\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b',
            content_type='image/jpeg'
        )
        # Prepare post data
        post_data = {
            'first_name': 'UpdatedName',  # for UserUpdateForm
            'last_name': 'UpdatedLastName',  # for UserUpdateForm
            'sex': 'M',  # for ProfileUserForm
            'dob': '1990-01-01',  # for ProfileUserForm
            'country': self.country.pk,  # for ProfileUserForm
            'profile_picture': test_image,  # ProfileUserForm (required image)
        }
        
        response = self.client.post(reverse('profile_settings', args=[self.user.id]), post_data)
        # Check for form errors (for debugging)
        # if response.context['user_form'].errors:
        #     print("User form errors:", response.context['user_form'].errors)
        # if response.context['profile_form'].errors:
        #     print("Profile form errors:", response.context['profile_form'].errors)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.user.refresh_from_db()
        self.profile.refresh_from_db()
        self.assertEqual(self.user.first_name, 'UpdatedName')
        self.assertEqual(self.user.last_name, 'UpdatedLastName')