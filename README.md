# Python tools

A package with various functions for various things

## How to install

`pip install git+https://git@github.com/noorzeea/python-tools.git`
 
## What's inside

### Data structures operations
Function | Params type | Description | Return type
------------ | ------------- | ------------- | -------------
`tupleToList(params)` | tuple | Transforms an uneditable tuple of tuples into an editable list of lists | list 
`listToTuple(params)` | list | Transforms an editable list of lists into an uneditable lists of lists | tuple 

#### How to use 
`from data_structures import tupleToList, listToTuple`
<br>
<br>

### Datetime operations

Function | Params type | Description | Return type
------------ | ------------- | ------------- | -------------
`naturalDatetime(params)` | datetime | Translate system's datetime format into a human readable one | string 
`isCurrentWeek(params)` | date | Checks if input day is in 7 days | bool 

#### How to use 
`from datetime_operations import naturalDatetime, isCurrentWeek`