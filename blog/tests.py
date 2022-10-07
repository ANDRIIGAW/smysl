from django.urls import resolve
from django.test import TestCase
from blog.views import home_page  
from blog.models import Article
from django.http import HttpRequest
from datetime import datetime

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home_page)  

    def test_home_page_returns_correct_html(self):
            request = HttpRequest()  
            response = home_page(request)  
            html = response.content.decode('utf8')  
            self.assertTrue(html.startswith('<html>'))  
            self.assertIn('<title>WaterinTap</title>', html)  
            self.assertIn('<h1>WaterinTap</h1>', html)  
            self.assertTrue(html.endswith('</html>'))  


class ArticlModelTest(TestCase):

    def test_article_model_save_and_retrieve(self):
        # створити статтю 1
        # зберегти статю 1 в базі
        article1 = Article(
            title='article 1',
            full_text='full_text 1',
            summary='summary 1',
            category='category 1',
            pubdate=datetime.now()
        )
        article1.save()
        # створити статтю 2
        # зберегти статю 2 в базі
        article2 = Article(
            title='article 2',
            full_text='full_text 2',
            summary='summary 2',
            category='category 2',
            pubdate=datetime.now()
        )
        article2.save()

        # загрузи з бази всі статті
        all_articles = Article.objects.all()

        # провір статті має бути 2
        self.assertEqual(len(all_articles), 2)
        # перевір 1 загружена стаття == статті 1
        self.assertEqual(
            all_articles[0].title,
            article1.title
        )
        # перевір 2 загружена стаття == статті 2
        self.assertEqual(
            all_articles[1].title,
            article2.title
        )