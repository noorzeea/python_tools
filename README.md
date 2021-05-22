# Python tools

-------------------------------
A package with various functions for various things

## How to install

-------------------------------
<code>pip install git+https://git@github.com/noorzeea/python-tools.git</code>
 
## What's inside

-------------------------------
### Data structures operations
Function | Parameters type | Description | Return type
------------ | ------------- | ------------- | -------------
tupleToList | tuple | Transforms an uneditable tuple of tuples into an editable list of lists | list 
listToTuple | list | Transforms an editable list of lists into an uneditable lists of lists | tuple 

<br>

### Datetime operations

Function | Parameters type | Description | Return type
------------ | ------------- | ------------- | -------------
naturalDatetime | datetime | Translate system's datetime format into a human readable one | string 
isCurrentWeek | date | Checks if input day is in 7 days | bool 