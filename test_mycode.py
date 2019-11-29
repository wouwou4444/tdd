from mycode import *


class TestMyClass():
    def test_custom_func_x(self):
        assert custom_func_x(2,3,2) == 12
        
    def test_custom_non_lin_num_list(self):
        assert custom_non_lin_num_list(10, 2, 2)[1] == 2
        assert custom_non_lin_num_list(10, 3, 3)[4] == 192
    
    def test_hello(self):
        assert hello_world() == "hello world"
    
    def test_num_list(self):
        assert len(create_num_list(10)) == 10
    #IL FAUT VERROUILLER SON POSTE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!