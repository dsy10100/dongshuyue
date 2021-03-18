"""

"""

import pytest

from pythoncode.calculator import Calculator
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

    # @pytest.mark.parametrize("a,b,expected", get_datas()[0], ids=get_datas()[1])
    @pytest.mark.add
    def test_add(self, get_calc, get_addDatas):
        print("测试加法用例")
        # result = self.calc.add(a, b)
        # assert result == expected
        result = get_calc.add(get_addDatas[0], get_addDatas[1])
        assert result == get_addDatas[2]

    # @pytest.mark.parametrize("a,b,expected", get_datas()[2], ids=get_datas()[3])
    @pytest.mark.add
    def test_adderror(self, get_calc, get_adderrorsDatas):
        print("测试加法错误用例")
        result = get_calc.add(get_adderrorsDatas[0], get_adderrorsDatas[1])
        assert result == get_adderrorsDatas[2]

    """ 测试减法用例，通过读取文件中参数"""

    # @pytest.mark.parametrize("a,b,expected", get_datas()[4], ids=get_datas()[5])
    @pytest.mark.sub
    def test_sub(self, get_calc, get_subDatas):
        print("测试加法用例")
        result = self.calc.sub(get_subDatas[0], get_subDatas[1])
        assert result == get_subDatas[2]

    """ 测试乘法用例，通过读取文件中参数"""

    # @pytest.mark.parametrize("a,b,expected", get_datas()[6], ids=get_datas()[7])
    @pytest.mark.mul
    def test_mul(self, get_calc, get_mulDatas):
        print("测试乘法用例")
        result = self.calc.mul(get_mulDatas[0], get_mulDatas[1])
        assert result == get_mulDatas[2]

    """ 测试除法用例，通过读取文件中参数"""

    # @pytest.mark.parametrize("a,b,expected", get_datas()[8], ids=get_datas()[9])
    @pytest.mark.div
    def test_div(self, get_calc, get_divDatas):
        print("测试除法-正确用例")
        result = round(self.calc.div(get_divDatas[0], get_divDatas[1]), 1)
        assert result == get_divDatas[2]

    # @pytest.mark.parametrize("a,b,expected", get_datas()[10], ids=get_datas()[11])
    @pytest.mark.div
    def test_div(self, get_calc, get_diverrorsDatas):
        try:
            result = round(self.calc.div(get_diverrorsDatas[0], get_diverrorsDatas[1]), 1)
            assert result == get_diverrorsDatas[2]
        except ZeroDivisionError:
            print("测试除法-异常用例：被除数不能为0")
        else:
            print("测试除法-错误用例")
