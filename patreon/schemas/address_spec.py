# address_spec.py
# This file is auto-generated from the same code that generates
# https://docs.patreon.com. Community pull requests against this
# file may not be accepted.
import pytest

from patreon.schemas import address


@pytest.fixture
def attributes():
    return [
            'addressee',
            'line_1',
            'line_2',
            'postal_code',
            'city',
            'state',
            'country',
            'phone_number',
            'created_at',
        ]


@pytest.fixture
def relationships():
    return [
            'user',
            'campaigns',
        ]


def test_schema_attributes_are_properly_formatted(attributes):
    for attribute_name in attributes:
        value = getattr(address.Attributes, attribute_name, None)
        assert value is not None and value is attribute_name

def test_schema_relationships_are_properly_formatted(relationships):
    for relationship_name in relationships:
        value = getattr(address.Relationships, relationship_name, None)
        assert value is not None and value is relationship_name
