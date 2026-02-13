# which is used to handle the data logic and reusable code, which is separate from the dask.

#here we are going to write the code which can be used repeatedly.

'''
loading the data, 
analysing the data, 
transforming the data, 
parsing the data, 
structure the data and load it using injection files

such activities can be done using injection files.
'''

# parser is a python method which is used to convert the raw data into structured data based on the schema which we have defined - (translator)

'''
without parser:
-> no columns are defined
-> no filtering can be done
-> anamolies can't be detected
-> no aggregation is done

with parsing:
-> we can filter the error logs
-> we can detect the unusual patterns
-> used to convert raw log data to a machine readable language.
''' 

import re

LOG_PATTERN = re.compile(
    r"(?P<timestamp>[\d\-:\s]+)\s"
    r"(?P<level>\w+)\s"
    r"(?P<service>\w+)\s"
    r"(?P<message>.*?)(?:\suser_id=(?P<user_id>\d+))?$"
)


# Groupdict()
# Strip()
# re.compile() - it is a method which is used to create regex patterns. 

# python regex: python regular expressions are used for searching, matching, and extracting the data pattern from the given text.  
# 
'''
 r --> raw data
 ? --> starting of the pattern, from this the line is started
 P<timestamp>, P<level>, P<services>, P<message> --> for the capturing names of particular data
 \s --> to remove the white spaces between the name or text we've given
''' 