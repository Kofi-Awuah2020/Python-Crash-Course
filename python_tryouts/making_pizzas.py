# Importing an Entire Module
"""
import make_pizza2

make_pizza2.make_pizza(16, 'pepperoni')
make_pizza2.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""
# Importing a Specific Funtion
from make_pizza2 import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') # No need for dot notation

# Using 'as' to Give a Function an Alias
"""
from make_pizza2 import make_pizza as mp
mp(16, 'pepperoni')
"""

# Using 'as' to Give a Module an Alias
"""
import make_pizza2 as p
p.make_pizza(16, 'pepproni')
"""

# Importing All Functions in a Module
"""
from make_pizza2 import *

make_pizza(16, 'pepperoni')
"""