# webhook_spec.py
# This file is auto-generated from the same code that generates
# https://docs.patreon.com. Community pull requests against this
# file may not be accepted.
import pytest

from patreon.schemas import webhook


@pytest.fixture
def attributes():
    return [
            'triggers',
            'uri',
            'paused',
            'last_attempted_at',
            'num_consecutive_times_failed',
            'secret',
        ]


@pytest.fixture
def relationships():
    return [
            'client',
            'campaign',
        ]


def test_schema_attributes_are_properly_formatted(attributes):
    for attribute_name in attributes:
        value = getattr(webhook.Attributes, attribute_name, None)
        assert value is not None and value is attribute_name

def test_schema_relationships_are_properly_formatted(relationships):
    for relationship_name in relationships:
        value = getattr(webhook.Relationships, relationship_name, None)
        assert value is not None and value is relationship_name
