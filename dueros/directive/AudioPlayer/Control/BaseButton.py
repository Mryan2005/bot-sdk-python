#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/5/28

"""
    desc:pass
"""


class BaseButton:

    def __init__(self, type, name):
        self.data = {}
        self.data['type'] = type
        self.data['name'] = name

    def getData(self):
        return self.data

    pass


if __name__ == '__main__':
    pass