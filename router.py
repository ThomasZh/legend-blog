# _*_ coding: utf-8_*_
#
# genral application route config:
# simplify the router config by dinamic load class
# by lwz7512
# @2016/05/17

import tornado.web

from foo import comm
from foo.auth import auth_email


def map():

    config = [

        # GET: 根据 HTTP header 收集客户端相关信息：是否手机、操作系统、浏览器等信息。
        (r'/', getattr(auth_email, 'AuthWelcomeHandler')),
        (r'/auth/email/login', getattr(auth_email, 'AuthEmailLoginHandler')),
        (r'/auth/email/register', getattr(auth_email, 'AuthEmailRegisterHandler')),
        (r'/auth/email/forgot-pwd', getattr(auth_email, 'AuthEmailForgotPwdHandler')),
        (r'/auth/email/reset-pwd', getattr(auth_email, 'AuthEmailResetPwdHandler')),
        (r'/auth/welcome', getattr(auth_email, 'AuthWelcomeHandler')),
        (r'/auth/logout', getattr(auth_email, 'AuthLogoutHandler')),

        # comm
        ('.*', getattr(comm, 'PageNotFoundHandler'))

    ]

    return config
