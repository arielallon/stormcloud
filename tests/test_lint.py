#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2012 Caffeinated Code <caffeinatedco.de>
# Copyright (C) 2012 Jono Cooper
# Thanks to <adamwhitcroft.com> for Climacons!
# 
# DON'T BE A DICK PUBLIC LICENSE
# 
#                     Version 1, December 2009
# 
#  Copyright (C) 2009 Philip Sturgeon <email@philsturgeon.co.uk>
#  
#  Everyone is permitted to copy and distribute verbatim or modified
#  copies of this license document, and changing it is allowed as long
#  as the name is changed.
# 
#                   DON'T BE A DICK PUBLIC LICENSE
#     TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
# 
#   1. Do whatever you like with the original work, just don't be a dick.
# 
#      Being a dick includes - but is not limited to - the following instances:
# 
#  1a. Outright copyright infringement - Don't just copy this and change the name.
#  1b. Selling the unmodified original with no work done what-so-ever, that's REALLY being a dick.
#  1c. Modifying the original work to contain hidden harmful content. That would make you a PROPER dick.
# 
#   2. If you become rich through modifications, related works/services, or supporting the original work,
#  share the love. Only a dick would make loads off this work and not buy the original works 
#  creator(s) a pint.
#  
#   3. Code is provided with no warranty. Using somebody else's code and bitching when it goes wrong makes 
#  you a DONKEY dick. Fix the problem yourself. A non-dick would submit the fix back.#  you a DONKEY dick. Fix the problem yourself. A non-dick would submit the fix back.#  you a DONKEY dick. Fix the problem yourself. A non-dick would submit the fix back.#  you a DONKEY dick. Fix the problem yourself. A non-dick would submit the fix back.#  you a DONKEY dick. Fix the problem yourself. A non-dick would submit the fix back.### END LICENSE

import unittest
import subprocess

class TestPylint(unittest.TestCase):
    def test_project_errors_only(self):
        '''run pylint in error only mode
        
        your code may well work even with pylint errors
        but have some unusual code'''
        return_code = subprocess.call(["pylint", '-E', 'stormcloud'])
        # not needed because nosetests displays pylint console output
        #self.assertEqual(return_code, 0)

    # un-comment the following for loads of diagnostics   
    #~ def test_project_full_report(self):
        #~ '''Only for the brave
#~ 
        #~ you will have to make judgement calls about your code standards
        #~ that differ from the norm'''
        #~ return_code = subprocess.call(["pylint", 'stormcloud'])

if __name__ == '__main__':
    'you will get better results with nosetests'
    unittest.main()