# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys
import json
import random
import string
from typing import List

from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
            access_key_id: str,
            access_key_secret: str,
    ) -> Dysmsapi20170525Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id="LTAI5tRwoNHdspauY5qkVafP",
            # 必填，您的 AccessKey Secret,
            access_key_secret="q4M2FBjFNDZSZtyFvOC2u4dabwZUmN"
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Dysmsapi
        config.endpoint = f'dysmsapi.aliyuncs.com'
        return Dysmsapi20170525Client(config)

    @staticmethod
    def main(
            args: List[str],
            phone_number: str,
            random_code: str
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = Sample.create_client(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
                                      os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'])
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            phone_numbers=phone_number,
            sign_name='阅读图书管理系统',
            template_code='SMS_463220264',
            template_param='{"code":"' + random_code + '"}',
            sms_up_extend_code='',
            out_id=''
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            client.send_sms_with_options(send_sms_request, runtime)
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
            args: List[str],
            phone_number: str,
            random_code: str
    ) -> None:
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html
        client = Sample.create_client(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
                                      os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'])
        print("2" + phone_number)
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            phone_numbers=phone_number,
            sign_name='阅读图书管理系统',
            template_code='SMS_463220264',
            template_param='{"code":"' + random_code + '"}',
            sms_up_extend_code='',
            out_id=''
        )
        print("2" + random_code)
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.send_sms_with_options_async(send_sms_request, runtime)
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)


def sms(phone_number):
    # 随机数验证码
    def generate_random_code():
        return str(random.randint(1000, 9999))

    random_code = generate_random_code()
    # 添加一个新参数 phone_number
    Sample.main(sys.argv[1:], phone_number, random_code)  # 在这里传递 phone_number
    return random_code
