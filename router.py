# _*_ coding: utf-8_*_
#
# genral application route config:
# simplify the router config by dinamic load class
# by lwz7512
# @2016/05/17

import tornado.web

from foo import comm
from foo.auth import auth


def map():

    config = [

        # GET: 根据 HTTP header 收集客户端相关信息：是否手机、操作系统、浏览器等信息。
        (r'/', getattr(auth, 'AuthWelcomeHandler')),
        (r'/auth/login', getattr(auth, 'AuthLoginHandler')),
        (r'/auth/register', getattr(auth, 'AuthRegisterHandler')),
        (r'/auth/forgot-pwd', getattr(auth, 'AuthForgotPwdHandler')),
        (r'/auth/email/reset-pwd', getattr(auth, 'AuthEmailResetPwdHandler')),
        (r'/auth/welcome', getattr(auth, 'AuthWelcomeHandler')),
        (r'/auth/logout', getattr(auth, 'AuthLogoutHandler')),

        # comm
        ('.*', getattr(comm, 'PageNotFoundHandler'))

    ]

    return config
