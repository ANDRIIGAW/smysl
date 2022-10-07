from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class BasicInstallTest(unittest.TestCase):  

    # Жив був Деня
    # ему нужно отоплние
    # Зайшов в Гугл і ввів запит - монтаж отопления 

    def setUp(self):  
        self.browser = webdriver.Chrome()

    def tearDown(self):  
        self.browser.quit()

    def test_home_page_title(self): 
        # В браузері відкрився сайт за адресою 'http://127.0.0.1:8000'
        # Користувач відкриваэ ссилку на сайт "WaterinTap"
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('WaterinTap', self.browser.title)  
        
    def test_home_page_header(self): 
        # В шапці сайту написано "Messianic Missionary Website"
        self.browser.get('http://127.0.0.1:8000')
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('WaterinTap', header.text)  
        
    def test_home_page_blog(self): 
        # Під шапкою сайту "WaterinTap" є стаття
        self.browser.get('http://127.0.0.1:8000')
        article_list = self.browser.find_element_by_class_name('article_list')
        self.assertTrue(article_list) 


        def test_home_page_articles_look_correct(self): 
            # Під шапкою сайту "WaterinTap" є стаття
            self.browser.get('http://127.0.0.1:8000')
            article_title = self.browser.find_element_by_class_name('article_title')
            article_summary = self.browser.find_element_by_class_name('article_summary')
            self.assertTrue(article_title) 
            self.assertTrue(article_summary) 

if __name__ == '__main__':  
    unittest.main()


# self.fail('Finish the test!') 

# Під шапкою розташований блог з статтями
# У кожної статтіє заголовок і один абзац тексту
# Моня клікнув по заголовку і відкрилась нова сторінка з поним текстом статті
# Прочитав статтю Моня клікнув по ссилці "Messianic Missionary Website" і 
# повернувся на голвну сторінку

# Деякі статті є в адмінці , але вони не опубліковані

# Статті відкрриваються з короткою гарною адресою