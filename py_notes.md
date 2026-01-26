## Builtin Functions (global):

### Type conversion functions

float()

str() -> Technically also a sequence type

int()

bool()

### Standard I/O

input() - always returns String

print() - coerces each argument to String

### Int & Float

round()

### (Simple) Sequence types

list() -> Also declared via: var = [..., ..., ...]. A list is necessarily mutable.

tuple() -> Also declared via: var = (..., ..., ...). A tuple is necessarily immutable.

range() -> range(start, end, step), start included, end excluded

Types that handle **text & binary** are also considered sequence types

str()

bytes() -> immutable

bytearray() -> mutable

memoryview()

#### Sequence types operations

in, not in, +, \*, [i], [i:j], [i:j:k], len(), min(), max()

#### Sequence types (simple & global) functions

len(object) -> returns the length of a given sequence type/collection

sum(iterable, startValue) -> sums all the elements inside a sequence type starting from an optional int value of startValue. If they are strings, these strings will be concatenated. No join operator can be specified => str.join(sequence) is usually preferred.

all(iterable) -> Evaluates all the elements inside a sequence type and returns True only if all elements evaluate to true.

any(iterable) -> Evaluates all the elements inside a sequence type and returns True if at least one element evaluates to true

filter(callback(element), iterable) -> Applies a callback to each element of the sequence type, and returns a new iterable containing each element that returned true from the callback.

map(callback(element), iterable) -> Applies a callback to each element, and returns a new iterable containing the values returned by the callback. map() can be supplied with multiple iterables, meaning multiple values can be manipulated inside the callback before being returned as a single value inside the new iterable.

max(iterable) -> Returns the largest value of an iterable. (There are more specifics than this, but not really important.)

min(iterable) -> Returns the smallest value of an iterable. (There are more specifics than this, but not really important.)

set() -> Technically also a sequence type itself

slice()

sorted()

### Arbitrary python code evaluation & execution

exec()

eval()

### Filesystem

open()

## Import from standard library

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

## String methods & f-strings

str.ljust(length, paddingChar) -> Pads the text to a given length with the given paddingChar

str.rjust() -> Does the same but adds padding to the left.

str.center() -> Will add padding to center the string

str.format(args) -> Writes the given arguments to designated places in the string. **Ex**:

"The sum of {} + {} is {}".format(1, 2, 3) == "The sum of {0} + {1} is {2}".format(1, 2, 3) == "The sum of {a} + {b} is {answer}".format(answer=1+2, a=1, b=2)

#### f-string basics

f-strings are Formatted String Literals, you can tell the compiler to treat a string as a format string by prepending it with 'f' -> f"Formatted string syntax". This is known as a string prefix.

There are multiple different string prefixes, 'b', 'r', 'f', 't'.

'b' tells the compiler to interpret the string as raw bytes => ASCII chars to 128 and/or hex/octal/decimal escape sequences to 256.

'r' tells the compiler to interpret the string as a raw string: every char that makes up the string will be interpreted literally.

'f' is the formatted string we will discuss, and 't' is a formatted string that is interpreted slightly differently from an 'f' string, but this distinction isn't important at the moment.

Fundamentally, an f-string allows for the insertion of replacement fields that can be filled with expressions/variables that are evaluated at run time. Replacement fields can themselves contain f-strings, allowing for (almost) limitless nesting, and each of these f-strings are evaluated and formatted at run time. In addition, each replacement field can be appended with a **Format Specifier**, which can define how each expression/f-string/variable is presenting, via alignment, fill, float precision, float/int grouping, and more...

**Format Specifiers** operate within their own mini-language. [It's best to refer to the documentation for this] (https://docs.python.org/3/library/string.html#formatspec). One of the more useful specifiers when working in the console is using both align and width. As an example, appending ':<75' to a replacement field will justify it's content to the left, and pad the right-hand side of the content with empty spaces to a width of 75.

As a full example, note how there's no need to use both 'single quotes' and "double quotes", the interpreter handles nested quotes inside replacement fields just fine :

f"{f"This is a {f"very padded":>25} string":<75}: "

Logically, the "very padded" string will enforce a size of 25 chars, and it's outer string will enforce a size of 75 chars. This means that this outer string must have 50 chars to work with, and the outermost string must contain 77 characters, as it is only appending two chars ": " to the end of the first replacement field.
