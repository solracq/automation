'''
@author Solracq
'''

import pytest

class TestStringContent:
    def test_one(self):
        s = "this"
        assert 'h' in s

    @pytest.mark.skip
    def test_two(self):
        s = 'hello'
        assert hasattr(s, 'hello')