# _*_ coding: utf-8_*_
#
# genral application route config:
# simplify the router config by dinamic load class
# by lwz7512
# @2016/05/17

import tornado.web

from foo import comm
from foo.api import api_auth
from foo.auth import auth


def map():

    config = [

        # GET: 根据 HTTP header 收集客户端相关信息：是否手机、操作系统、浏览器等信息。
        (r'/', getattr(auth, 'AuthWelcomeHandler')),
        (r'/auth/login', getattr(auth, 'AuthLoginHandler')),
        (r'/auth/register', getattr(auth, 'AuthRegisterHandler')),
        (r'/auth/forgot-pwd', getattr(auth, 'AuthForgotPwdHandler')),
        (r'/auth/welcome', getattr(auth, 'AuthWelcomeHandler')),

        # 登录
        # 登出（删除access_token）
        # 检验授权凭证（access_token）是否有效
        ('/api/auth/token', getattr(api_auth, 'ApiAuthTokenXHR')),
        # 刷新（代替重新登录）
        ('/api/auth/refresh-token', getattr(api_auth, 'ApiAuthRefreshTokenXHR')),
        # 注册
        ('/api/auth/accounts', getattr(api_auth, 'ApiAuthAccountXHR')),
        # 查询用户账号基本信息
        # 修改用户账号基本信息
        ('/accounts/basic/([a-z0-9]*)', getattr(api_auth, 'ApiAuthAccountXHR')),
        # 获取验证码
        ('/auth/verify-code', getattr(api_auth, 'ApiAuthVerifyCodeXHR')),
        # 修改密码
        ('/auth/pwd', getattr(api_auth, 'ApiAuthPwdXHR')),

        # comm
        ('.*', getattr(comm, 'PageNotFoundHandler'))

    ]

    return config
