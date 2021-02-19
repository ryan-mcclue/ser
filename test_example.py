#! /usr/bin/env python3
# SPDX-License-Identifier: zlib-acknowledgement

# import pytest if wanting more
# @pytest.fixture for setup information

def sum(x, y):
    return x * y

# test_{{fnc_testable}}_{{variant}}
# test_sum_small, test_sum_large
def test_sum():
    assert sum(1, 2) == 3, "1 + 2 == 3"
