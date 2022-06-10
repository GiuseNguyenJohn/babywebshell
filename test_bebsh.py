#!/usr/bin/env python3
"""Tests for bebsh.py"""

import unittest
from webwizard import webwizard

class BebshTestCase(unittest.TestCase):
    """Tests for bebsh.py"""

    def __init__(self):
        self.wizard = webwizard.Wizard('https:/google.com')
        pass