from common.readYaml import GettingDate
from common.assert_result import *
from common.logger import Logger
import traceback, logging, allure
from common.queries import *
from conf import Api_Url as c
from httpRequests._requests import *

'''
测试用例模板
不需读取用例文件的脚本将caseName,casedata行删除即可
Looger('')中的传参控制生成的日志文件名
FileLevel控制写入日志文件的日志等级
'''

#caseName, casedata = GettingDate('.yml').return_data()  #GettingDate中输入yml配置文件名，可读取文件中数据，返回两组数据（用例标题，用例数据）
logger = Logger('用户信息', FileLevel=logging.INFO).getlog()  # FileLevel设置写入log日志中的等级，第一个参数是生成的日志文件名


@allure.feature('用户信息')
@allure.story('获取用户纪念值')
@allure.severity('blocker')
class Test_userFlow:
    '''
    测试手机号为隐形个人手机号，
    后期若需要更换账号进行测试只需要更改phone= 和 password=
    result是对返回的success进行断言，1为True， 0为False
    目前用例内需要准备url和参数
    noToken的请求是不带x-stream-id 非Token
    '''

    def setup(self):
        self.url = c.release + c.userFlow

    @allure.title('获取纪念值收入信息')
    def test_get_user_flow_income(self):
        params = {'pageSize':1000000}
        logger.info(f'获取纪念值收入信息,params = {params}')
        res = http_get(self.url, params=params)
        if check_result(len(res['msg']['data']),res['msg']['total'],logger) == 0:
            raise AssertionError(traceback.format_exc())

    @allure.title('获取纪念值支出信息')
    def test_get_user_flow_outcome(self):
        params = {'pageSize':100000, 'type':"outcome"}
        logger.info(f'获取纪念值支出信息,params = {params}')
        res = http_get(self.url, params=params)
        if check_result(len(res['msg']['data']),res['msg']['total'],logger) == 0:
            raise AssertionError(traceback.format_exc())

    @allure.title('不传参数获取纪念值信息')
    def test_get_user_flow_no_params(self):
        logger.info('不传参数获取纪念值信息')
        res = http_get(self.url)
        if check_result_is_true(res['msg'], logger) == 0:
            raise AssertionError(traceback.format_exc())

    @allure.title('不带x-stream-id获取纪念值信息')
    def test_get_user_flow_no_x_stream_id(self):
        logger.info('不带x-stream-id获取纪念值信息')
        res = http_get_noToken(self.url, result=0)
        if check_result(res['error_code'], 401, logger) == 0:
            raise AssertionError(traceback.format_exc())