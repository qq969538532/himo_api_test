from common.readYaml import GettingDate
from common.assert_result import *
from common.logger import Logger
import traceback, logging, allure
from common.queries import *
from conf import Api_Url as c
from httpRequests._requests import *

"""
测试用例模板
不需读取用例文件的脚本将caseName,casedata行删除即可
Looger('')中的传参控制生成的日志文件名
FileLevel控制写入日志文件的日志等级
"""

# caseName, casedata = GettingDate('.yml').return_data()  #GettingDate中输入yml配置文件名，可读取文件中数据，返回两组数据（用例标题，用例数据）
logger = Logger('电子发票', FileLevel=logging.INFO).getlog()  # FileLevel设置写入log日志中的等级，第一个参数是生成的日志文件名


@allure.feature('电子发票')
@allure.story('可开发票列表')
@allure.severity('blocker')
class Test_invoiceList:
    """
    测试手机号为隐形个人手机号，
    后期若需要更换账号进行测试只需要更改phone= 和 password=
    result是对返回的success进行断言，1为True， 0为False
    目前用例内需要准备url和参数
    noToken的请求是不带x-stream-id 非Token
    """

    def setup(self):
        self.url = c.release + c.invoiceList

    @allure.title('获取可开发票列表')
    def test_get_invoice_list(self):
        res = http_get(self.url, phone=13676561839)
        data = get_user_invoice_list()
        if check_result(len(res['msg']['data']), len(data), logger) == 0:
            raise AssertionError(traceback.format_exc())
        else:
            raise AssertionError(traceback.format_exc())

    @allure.title('不带x-stream-id获取可开发票列表')
    def test_get_invoice_list_not_x_stream_id(self):
        res = http_get_noToken(self.url, result=0)
        if check_result_is_401(res, logger) == 0:
            raise AssertionError(traceback.format_exc())

    @allure.title('获取可开发票为0')
    def test_get_invoice_list(self):
        res = http_get(self.url, phone=13676561840)
        data = get_user_invoice_list()
        if check_result(res['msg'], data, logger) == 0:
            raise AssertionError(traceback.format_exc())