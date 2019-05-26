# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @File  : test.py
# @Author: 杨崇
# @Date  : 2019/5/26
# @Desc  : null
import subprocess
from timeit import timeit


def execute_cmd(cmd):

    p = subprocess.Popen(cmd,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        print("stdout:" + stdout.decode('gbk'))
        print("stderr:" + stderr.decode('gbk'))
        return p.returncode, stderr
    else:
        return p.returncode, stdout


if __name__ == '__main__':
    cmd = 'dir'
    returncode, out = execute_cmd(cmd)
    out1 = out.decode('gbk')
    if returncode != 0:
        raise SystemExit('execute {0} err :{1}'.format(cmd, out1))
    else:
        print("execute command ({0} sucessful)".format(cmd))
