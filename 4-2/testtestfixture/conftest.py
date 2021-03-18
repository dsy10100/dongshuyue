import os
from typing import List

import allure
import pytest
import yaml

from pythoncode.calculator import Calculator


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # 修改编码
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# 实例化被测试的计算机类
@pytest.fixture(scope="class")
def get_calc():
    print("\n-开始计算-")
    calc = Calculator()
    yield calc
    print("-结束计算-")


# 从.yml文件中读取测试数据
def get_datas():
    # os.path.dirname(__file__) 代表当前这个文件的路径

    mydatapath = os.path.dirname(__file__) + "/datas/calculator.yml"
    print("**", os.path.dirname(__file__))
    with open(mydatapath, encoding="utf-8") as f:
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
    return [[add_mydatas, add_myids],
            [adderrors_mydatas, adderrors_myids],
            [sub_mydatas, sub_myids],
            [mul_mydatas, mul_myids],
            [div_mydatas, div_myids],
            [diverrors_mydatas, diverrors_myids]]


@pytest.fixture(params=get_datas()[0][0], ids=get_datas()[0][1])
def get_addDatas(request):
    return request.param


@pytest.fixture(params=get_datas()[1][0], ids=get_datas()[1][1])
def get_adderrorsDatas(request):
    return request.param


@pytest.fixture(params=get_datas()[2][0], ids=get_datas()[2][1])
def get_subDatas(request):
    return request.param


@pytest.fixture(params=get_datas()[3][0], ids=get_datas()[3][1])
def get_mulDatas(request):
    return request.param


@pytest.fixture(params=get_datas()[4][0], ids=get_datas()[4][1])
def get_divDatas(request):
    return request.param


@pytest.fixture(params=get_datas()[5][0], ids=get_datas()[5][1])
def get_diverrorsDatas(request):
    return request.param
