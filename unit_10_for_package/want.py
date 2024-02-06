import my_package.str_util
print(my_package.str_util.str_reverse("帅豪祖"))
from my_package.file_util import append_to_file
from my_package.file_util import print_file_info

append_to_file("D:/code/ctext/google.txt","大帅哥杨祖豪")
print_file_info("D:/code/ctext/google.txt")