# vat.py - functions for handling Belgian VAT numbers
#
# Copyright (C) 2012 Arthur de Jong
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301 USA

"""Module for handling Belgian VAT (BTW TVA NWSt) numbers.

>>> compact('BE403019261')
'0403019261'
>>> is_valid('BE 428759497')
True
>>> is_valid('BE431150351')
False
"""

from stdnum.util import clean


def compact(number):
    """Convert the number to the minimal representation. This strips the
    number of any valid separators and removes surrounding whitespace."""
    number = clean(number, ' -./').upper().strip()
    if number.startswith('BE'):
        number = number[2:]
    if number.startswith('(0)'):
        number = '0' + number[3:]
    if len(number) == 9:
        number = '0' + number  # old format had 9 digits
    return number


def checksum(number):
    """Calculate the checksum."""
    return (int(number[:-2]) + int(number[-2:])) % 97


def is_valid(number):
    """Checks to see if the number provided is a valid VAT number. This checks
    the length, formatting and check digit."""
    try:
        number = compact(number)
    except:
        return False
    return len(number) == 10 and number.isdigit() and checksum(number) == 0
