from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from model_mommy import mommy
from django.conf import settings





class RegisterViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('accounts:register')

        def test_register_ok(self):
            data = {'username': 'herdeson', 'password': 'aquietrabalho3150', 'password2': 'aquietrabalho3150'}
            data['email'] = 'test1@gmail.com'
            response = self.client.post(self.register_url, data)
            index_url = reverse('index')
            self.assertRedirects(response, index_url)
            self.assertEquals(User.objects.count(),1)

        def test_register_error(self):
            data = {'username': 'herdeson', 'password': 'aquietrabalho3150', 'password2': 'aquietrabalho3150'}
            response = self.client.post(self.register_url, data)
            self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')


class UpdateUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:update_user')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_user_ok(self):
        data = {'name':'teste', 'email':'test@test.com'}
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.username, password='123')
        response = self.client.post(self.url, data)

        accounts_index_url = reverse('accounts:index')
        self.assertRedirects(response, accounts_index_url)
        #self.User.objects.get(username=self.user.username)
        self.user.refresh_from_db()
        self.assertEquals(self.user.email , 'test@test.com')

    def test_update_user_error(self):
        data = {}
        self.client.login(username=self.user.username, password='123')
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'email','Este campo é obrigatório.')

class UpdatePasswordTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('accounts:update_password')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_update_password_ok(self):
        data = {'old_password':'123', 'new_password1':'123teste', 'new_password2':'123teste'}
        self.client.login(username=self.user.username, password='123')

        response = self.client.post(self.url, data)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('123teste'))
