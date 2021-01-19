import os

# print(os.environ['HOME'])
print(os.environ.get('SHELL2', '/bin/bash'))
print(os.getenv('HOME'))
print(os.getenv('MYHOME', '/root'))