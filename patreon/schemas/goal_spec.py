# goal_spec.py
# This file is auto-generated from the same code that generates
# https://docs.patreon.com. Community pull requests against this
# file may not be accepted.
import pytest

from patreon.schemas import goal


@pytest.fixture
def attributes():
    return [
        'amount_cents',
        'title',
        'description',
        'created_at',
        'reached_at',
        'completed_percentage',
    ]


@pytest.fixture
def relationships():
    return [
        'campaign',
    ]


def test_schema_attributes_are_properly_formatted(attributes):
    for attribute_name in attributes:
        value = getattr(goal.Attributes, attribute_name, None)
        assert value is not None and value is attribute_name

def test_schema_relationships_are_properly_formatted(relationships):
    for relationship_name in relationships:
        value = getattr(goal.Relationships, relationship_name, None)
        assert value is not None and value is relationship_name
