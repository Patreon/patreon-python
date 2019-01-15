# member_spec.py
# This file is auto-generated from the same code that generates
# https://docs.patreon.com. Community pull requests against this
# file may not be accepted.
import pytest

from patreon.schemas import member


@pytest.fixture
def attributes():
    return [
            'patron_status',
            'is_follower',
            'full_name',
            'email',
            'pledge_relationship_start',
            'lifetime_support_cents',
            'currently_entitled_amount_cents',
            'last_charge_date',
            'last_charge_status',
            'note',
            'will_pay_amount_cents',
        ]


@pytest.fixture
def relationships():
    return [
            'address',
            'campaign',
            'currently_entitled_tiers',
            'user',
        ]


def test_schema_attributes_are_properly_formatted(attributes):
    for attribute_name in attributes:
        value = getattr(member.Attributes, attribute_name, None)
        assert value is not None and value is attribute_name

def test_schema_relationships_are_properly_formatted(relationships):
    for relationship_name in relationships:
        value = getattr(member.Relationships, relationship_name, None)
        assert value is not None and value is relationship_name
