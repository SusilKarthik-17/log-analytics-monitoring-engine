'''
--> schema files define the structure of the dataand type of the data.

--> Schema is nothing but role book of our data.

Uses of Schema Files:
1. It ensures all the rows follows the same data structure and type.
2. It helps in data validation and data cleaning(correct the data type)
3. Faster Processing, easier analytics of data files is possible 
(faster processing because it knows the data type and structure.)
(easy analysis means grouping, mapping, filtering, anamoly detection becomes simple and faster.)

'''

log_schema = {
    "timestamp" : "datetime",
    "level"     : "string",
    "service"   : "string",
    "message"   : "string"
}

#data_frame = df.astype(log_schema)