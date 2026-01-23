## Builtin Functions (global):

### Type conversion functions

float()

str()

int()

bool()

### Standard I/O

input() - always returns String

print() - coerces each argument to String

### Int & Float

round()

### String methods

str.ljust(length, paddingChar) -> Pads the text to a given length with the given paddingChar

str.rjust() -> Does the same but adds padding to the left.

str.center() -> Will add padding to center the string

str.format(args) -> Writes the given arguments to designated places in the string. **Ex**:

"The sum of {} + {} is {}".format(1, 2, 3) == "The sum of {0} + {1} is {2}".format(1, 2, 3) == "The sum of {a} + {b} is {answer}".format(answer=1+2, a=1, b=2)

### Sequence types

list() -> Also declared via: var = [..., ..., ...]

tuple() -> Also declared via: var = (..., ..., ...)

range() -> range(start, end, step), start included, end excluded

Types that handle **text & binary** are also considered sequence types

str()

bytes() -> immutable

bytearray() -> mutable

memoryview()

#### Sequence types operations

in, not in, +, \*, [i], [i:j], [i:j:k], len(), min(), max()

#### For loop syntax

for x in _SEQUENCE_:

    _EXECUTE_

### Import from standard library

import _MODULE_

from _MODULE_ import _ATTRIBUTE_ as _ALIAS_

#### std library imports used

import **winsound**

- winsound.PlaySound("_PATH_", windsound.SND_FILENAME) -> Plays a .wav file

import **array** from array

- array('i', range(0, 5)) -> Generates an array of integers [0, 1, 2, 3, 4]

import **time**

- time.sleep(_SECONDS_)

import **os**

- os.system("_COMMAND_") -> Runs the given command in a subshell

import **sys**

- sys.argv -> List of commandline arguments

import **random**

- random.random() -> Random values between 0 and 1
- random.randint(1, 100) -> Start & End included
