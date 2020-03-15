# The MIT License (MIT)
#
# Copyright (c) 2020 Nina Zakharenko
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`statemanager`
================================================================================

CircuitPython helper libary for maintaing and switching between different states.


* Author(s): Nina Zakharenko

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s). Use unordered list & hyperlink rST
   inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/nnja/CircuitPython_StateManager.git"


class State:

    label = "State"

    def __init__(self):
        self.state_manager = None

    def display(self):
        raise NotImplementedError

    def handle_event(self):
        raise NotImplementedError


class StateManager:

    current_state = None

    def __init__(self):
        self.states = {}
        self._previous_states = []

    def add(self, *states):
        for state in states:
            state.state_manager = self

        self.states.update({state.__class__: state for state in states})

    def previous_state(self):
        if self._previous_states:
            self.current_state = self._previous_states.pop()
            self.states[self.current_state].display()

    def check_for_event(self):
        self.states[self.current_state].handle_event()

    @property
    def state(self):
        return self.states[self.current_state]

    @state.setter
    def state(self, state):
        print("Changing state to", self.states[state].__class__)
        self._previous_states.append(self.current_state)
        self.current_state = state
        self.states[self.current_state].display()