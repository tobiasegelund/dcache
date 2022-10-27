# dcache
A disk cache program to store cache of slow functions using the decorator design pattern. As default, the program store cached items to /tmp directory with the option to change to a different directory.

The program hashes the input and the function itself to control if any changes happens to the input a new output must be generated. For example, the function is highly relevant to use on functions using SQL queries as the SQL query itself (as string) will be hashed.

Notice, the program offers the options to specify the directory to store cache, as well as the expiration time of cached items.

Currently, the program does not support methods but only functions. Though, the feature will be included soon.

## Installation
To install the library use the following command

```bash
pip install git+https://github.com/tobiasegelund/dcache.git
```

## Usage
Follow the below instructions in order to use the library

```python
import time
from dcache import dcache, clear_dcache

# Optionally, to clear cache related to dcache by the following function
clear_dcache()

@dcache
def long_func() -> int:
    time.sleep(10)
    return 10

print(long_func())
print(long_func())

# Cache will instead be saved to ./cache_tmp dir with expiration time on 10 minutes
@dcache(cache_dir="./cache_tmp", expiration_time=10)
def long_func() -> int:
    time.sleep(10)
    return 10

print(long_func())
print(long_func())
```
