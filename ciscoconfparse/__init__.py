r""" __init__.py - Parse, Query, Build, and Modify IOS-style configurations

     Copyright (C) 2021-2023 David Michael Pennington
     Copyright (C) 2020-2021 David Michael Pennington at Cisco Systems
     Copyright (C) 2019      David Michael Pennington at ThousandEyes
     Copyright (C) 2012-2019 David Michael Pennington at Samsung Data Services
     Copyright (C) 2011-2012 David Michael Pennington at Dell Computer Corp.
     Copyright (C) 2007-2011 David Michael Pennington

     This program is free software: you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.

     This program is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     GNU General Public License for more details.

     You should have received a copy of the GNU General Public License
     along with this program.  If not, see <http://www.gnu.org/licenses/>.

     If you need to contact the author, you can do so by emailing:
     mike [~at~] pennington [.dot.] net
"""

import sys


import better_exceptions
better_exceptions.MAX_LENGTH = None
better_exceptions.SUPPORTS_COLOR = True
better_exceptions.hook()

from ciscoconfparse.ccp_util import PythonOptimizeCheck
from ciscoconfparse.ciscoconfparse import *
from ciscoconfparse.ccp_util import *
from dns.resolver import Timeout, Resolver
from dns.exception import DNSException

assert sys.version_info >= (3, 7)


# Throw errors for PYTHONOPTIMIZE and `python -O ...` by executing
#     PythonOptimizeCheck()...
_ = PythonOptimizeCheck()
