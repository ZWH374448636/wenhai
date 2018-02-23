# -*- coding: gbk -*-
from src.HbLogging import *
from mode.suning.mgr_login import *
from config.suning.mall_mgr_config import *
import sys
import  demjson
import Cookie
import unittest,time,urllib,urllib2
from mode.SignUtil import *
reload(sys)

class MallLogInTestCase(unittest.TestCase):
    '''管理后台-登录及注销'''
    def setUp(self):
        self.logging = HbLogging('./config/LogConfig.ini').outputLog()
        self.logging.warning("")
        self.c=''
        self.userName=mgr_login_username
        self.password=signstr(mgr_login_password)
        self.logging.info(u"执行用例归属于>>:{}".format(self.__doc__))
        self.logging.info('Username:{}'.format(mgr_login_username))
        self.logging.info( 'Password:{}'.format(self.password) )
        self.logging.info("Begin time : {}".format(time.strftime('%Y-%m-%d  %H:%M:%S  %A')))
        print "\n***** Begin time : ", time.strftime('%Y-%m-%d  %H:%M:%S  %A')

    def tearDown(self):
        # self.logging.info(u"执行文件名称:{}".format(self.__module__))

        print ''


    def testmgrlogin(self):
        '''管理后台-登录'''
        print MallMGRLogin(self,self.userName,self.password)

    def testGetshopGeneralSituation(self):
        '''管理后台-获取首页商铺状态'''
        print MGR_shopGeneralSituation(self,self.userName,self.password)


    def testmgrlogout(self):
        '''管理后台注销'''
        print ''
