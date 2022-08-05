
import pytest

@pytest.mark.usefixtures("init_driver")
class TestDummy():

    def test_dummy_function(self):
        print("i am dummy test line 1")
        print("i am dummy test line 2")
        self.driver.get("http:/supersqa.com")
        #import pdb; pdb.set_trace()