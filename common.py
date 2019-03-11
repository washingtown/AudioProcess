#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author:washingtown
'''一些通用方法'''
from datetime import datetime

def utc_timestamp():
    return int(round(datetime.now().timestamp()))