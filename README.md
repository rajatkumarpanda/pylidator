# pylidator
Python Schema Validator

## Create schema:
```
schema = Schema({
    'user_id': import_schema_for_filed(required=True, var_type=str, length=5, regex=""),
    'mobile_no': import_schema_for_filed(required=False, var_type=str, length=0, regex='(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$'),
})
```

## Check schema:
```
payload = {'handler': 'dummy', 'user_id': '12345','mobile_no': "9492393425"}
schema.check_schema(payload)
```
