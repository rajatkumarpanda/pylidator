import re
from abc import ABC, abstractmethod


class Check(ABC):

    @abstractmethod
    def check_schema(self, key, request):
        pass


class _Required(Check):
    def __init__(self, required: bool):
        self.required = required

    def check_schema(self, key, request):
        if bool(request.get(key, {})) != self.required:
            raise Exception(f'Required field {key} missing.')


class _Length(Check):
    def __init__(self, length: int):
        self.len = length

    def check_schema(self, key, request):
        if self.len != len(request.get(key, {})):
            raise Exception(f'Does not match the length specified in Schema for {key}.')


class _DocType(Check):
    def __init__(self):
        pass

    def check_schema(self, key, request):
        pass


class _Regex(Check):
    def __init__(self, regex):
        self.regex = regex

    def check_schema(self, key, request):
        if not re.search(self.regex, request.get(key, {})):
            raise Exception(f'Regex seach failed for {key}')


class _Type(Check):
    def __init__(self, var_type: str):
        self.type = var_type

    def check_schema(self, key, request):
        if not type(request[key]).__name__ == self.type:
            raise Exception(f'Type does not match for specified in schema for {key}.')


class _Range(Check):

    def __init__(self, val_range: range):
        self.val_range = val_range

    def check_schema(self, key, request):
        if not request[key] in self.val_range:
            raise Exception(f'Value {request[key]} not in the specified range.')


class _Date(Check):

    def check_schema(self, key, request):
        pass


class Schema:
    def __init__(self, schema: dict):
        self.schema = schema

    def check_schema(self, request):
        for key, values in self.schema.items():
            for constraint in values:
                constraint.check_schema(key, request)


def import_schema_for_filed(required: bool, var_type: type, length: int, regex: str, val_range: tuple = (0, 0)):
    schema_for_field = []

    if required:
        schema_for_field.append(_Required(required))
    if length:
        schema_for_field.append(_Length(length))
    if regex:
        schema_for_field.append(_Regex(regex))
    if var_type:
        schema_for_field.append(_Type(var_type.__name__))
    if val_range:
        schema_for_field.append(_Range(range(val_range[0], val_range[1])))

    return schema_for_field
