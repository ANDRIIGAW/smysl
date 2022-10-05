from selenium import webdriver
import unittest

class BasicInstallTest(unittest.TestCase):  

    # Жив був Моня
    # Вирішив поглибити зання про Бога
    # Зайшов в Гугл і ввів запит - віра 

    def setUp(self):  
        self.browser = webdriver.Chrome()

    def tearDown(self):  
        self.browser.quit()

    def test_home_page_title(self): 
        # В браузері відкрився сайт за адресою 'http://127.0.0.1:8000'
        # Користувач выдкриваэ ссилку на сайт "Messianic Missionary Website"
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Messianic Missionary Website', self.browser.title)  
        
    def test_home_page_header(self): 
        # В шапці сайту написано "Messianic Missionary Website"
        browser = self.browser.get('http://127.0.0.1:8000')
        header = browser.find_elements_by_tag_name('h1')[0]
        self.assertIn('Messianic Missionary Website', header)  
        

# Під шапкою розташований блог з статтями
# У кожної статтіє заголовок і один абзац тексту
# Моня клікнув по заголовку і відкрилась нова сторінка з поним текстом статті
# Прочитав статтю Моня клікнув по ссилці "Messianic Missionary Website" і 
# повернувся на голвну сторінку


if __name__ == '__main__':  
    unittest.main()


# self.fail('Finish the test!') 