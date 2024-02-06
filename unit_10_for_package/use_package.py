import my_package.str_util
my_package.my_module1.add(5, 6)
# import my_package.my_module2
# my_package.my_module2.reduce(5,6)

from my_package.file_util import reduce
reduce(5,8)

import numpy
total = numpy.add(5,6)
print(total)