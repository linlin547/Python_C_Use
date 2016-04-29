#!/usr/bin/env python
import ctypes
import os
so = ctypes.CDLL(os.getcwd()+os.sep+"example.so")
so.fun()