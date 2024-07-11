import unittest
import selenium
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    #setUp 和 tearDown 是特殊的方法，分别在各个测试方法之前和之后运行
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('To-Do', self.browser.title)
        ## 输入一个代办事项
        ### 在文本框中输入代办
        ### 回车保存输入，并刷新页面，且表格中出现了刚才填写的代办
        ### 页面又出现了一个输入框，并且可以再次输入
        ### 再次写入并保存
        ## 看看能否长久保存
        ### 保存url
        ### 关闭当前浏览器并保存url
        ### 再次访问url，检查代办事项是否还在
if __name__ == '__main__': # Python 脚本使用这个语句检查自己是否在命令行中运行，而不是在其他脚本中导入
    unittest.main(warnings='ignore') # warnings='ignore' 的作用是禁止抛出ResourceWarning 异常