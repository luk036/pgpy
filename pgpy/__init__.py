"""
PgPy
=====
"""

from __future__ import absolute_import

import sys
if sys.version_info[:2] < (2, 7):
    m = "Python 2.7 or later is required for PgPy (%d.%d detected)."
    raise ImportError(m % sys.version_info[:2])
del sys

from pgpy.proj_plane import *
from pgpy.proj_line import *
from pgpy.ck_plane import *
from pgpy.persp_plane import *
from pgpy.euclid_plane import *
