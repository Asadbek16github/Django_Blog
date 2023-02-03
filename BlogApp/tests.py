from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model

# Create your tests here.
class BlogTests(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'User',
            email ='test@gmail.com',
            password ='secret',
        )

        self.post = Post.objects.create(
            title = 'Sarlovha',
            author = self.user,
            text = 'Xabarning matni',
            short_info = 'Bu yerda qisqa matn bor'
        )


    def test_string_representation(self):
        self.assertEqual(str(self.post.title), 'Sarlovha')


    def test_given_object_informatins(self):
        self.assertEqual(self.post.title, 'Sarlovha')
        self.assertEqual(self.post.text, 'Xabarning matni')
        self.assertEqual(self.post.short_info, 'Bu yerda qisqa matn bor')
        self.assertEqual(f'{self.post.author}', 'User')
        self.assertEqual(self.user.username, 'User')
        self.assertEqual(self.user.email, 'test@gmail.com')


    def test_post_list_view(self):
        request = self.client.get('')
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'all_post_view.html')

    def test_one_post_showing_page(self):
        request = self.client.get('/post/1/')
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'see_only_one_post.html')

