### 17-2 -- Regex Digit Search.
#
# Come up with a regular expression that matches all the digits in the string 
# Arizona 479, 501, 807. California 209, 213, 650.
#
###
 

#!/bin/bash

echo Arizona 479, 501, 807. California 209, 213, 650. | grep -o [[:digit:]] 
