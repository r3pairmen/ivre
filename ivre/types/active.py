#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of IVRE.
# Copyright 2011 - 2021 Pierre LALET <pierre@droids-corp.org>
#
# IVRE is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# IVRE is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with IVRE. If not, see <http://www.gnu.org/licenses/>.


"""
Specific type definitions for IVRE (active)
"""


from typing import Dict

try:
    from typing import TypedDict
except ImportError:
    HAS_TYPED_DICT = False
else:
    HAS_TYPED_DICT = True


if HAS_TYPED_DICT:

    class HttpHeader(TypedDict):
        name: str
        value: str


else:
    HttpHeader = Dict[str, str]  # type: ignore