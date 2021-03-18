import pytest
import yaml

from pythoncode.calculator import Calculator
from testing.conftest import get_datas

def get_datas():
    with open("./datas/calculator.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        add_mydatas = datas["add"]["mydatas"]
        add_myids = datas["add"]["myids"]
        adderrors_mydatas = datas["adderrors"]["mydatas"]
        adderrors_myids = datas["adderrors"]["myids"]

        sub_mydatas = datas["sub"]["mydatas"]
        sub_myids = datas["sub"]["myids"]

        mul_mydatas = datas["mul"]["mydatas"]
        mul_myids = datas["mul"]["myids"]

        div_mydatas = datas["div"]["mydatas"]
        div_myids = datas["div"]["myids"]
        diverrors_mydatas = datas["diverrors"]["mydatas"]
        diverrors_myids = datas["diverrors"]["myids"]

    return [add_mydatas, add_myids, adderrors_mydatas, adderrors_myids, sub_mydatas, sub_myids,
            mul_mydatas, mul_myids,  div_mydatas, div_myids, diverrors_mydatas, diverrors_myids]



class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("类开始运行")

    def teardown_class(self):
        print("类结束运行")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束运算")

    """ 测试加法用例，通过读取文件中参数"""

    @pytest.mark.parametrize("a,b,expected", get_datas()[0], ids=get_datas()[1])
    @pytest.mark.add
    def test_add(self, a, b, expected):
        print("测试加法用例")
        result = self.calc.add(a, b)
        assert result == expected

    # @pytest.mark.parametrize("a,b,expected", get_datas()[2], ids=get_datas()[3])
    # @pytest.mark.add
    # def test_adderror(self, a, b, expected):
    #     print("测试加法错误用例")
    #     result = self.calc.add(a, b)
    #     assert result == expected
    #
    # """ 测试减法用例，通过读取文件中参数"""

    @pytest.mark.parametrize("a,b,expected", get_datas()[4], ids=get_datas()[5])
    @pytest.mark.sub
    def test_sub(self, a, b, expected):
        print("测试加法用例")
        result = self.calc.sub(a, b)
        assert result == expected

    """ 测试乘法用例，通过读取文件中参数"""

    @pytest.mark.parametrize("a,b,expected", get_datas()[6], ids=get_datas()[7])
    @pytest.mark.mul
    def test_mul(self, a, b, expected):
        print("测试乘法用例")
        result = self.calc.mul(a, b)
        assert result == expected

    """ 测试除法用例，通过读取文件中参数"""

    @pytest.mark.parametrize("a,b,expected", get_datas()[8], ids=get_datas()[9])
    @pytest.mark.div
    def test_div(self, a, b, expected):
        print("测试除法-正确用例")
        result = round(self.calc.div(a, b), 1)
        assert result == expected

    @pytest.mark.parametrize("a,b,expected", get_datas()[10], ids=get_datas()[11])
    @pytest.mark.div
    def test_div(self, a, b, expected):
        try:
            result = round(self.calc.div(a, b), 1)
            assert result == expected
        except ZeroDivisionError:
            print("测试除法-异常用例：被除数不能为0")
        else:
            print("测试除法-错误用例")