# benefit_spec.py
# This file is auto-generated from the same code that generates
# https://docs.patreon.com. Community pull requests against this
# file may not be accepted.
import pytest

from patreon.schemas import benefit


@pytest.fixture
def attributes():
    return [
        'title',
        'description',
        'benefit_type',
        'rule_type',
        'created_at',
        'delivered_deliverables_count',
        'not_delivered_deliverables_count',
        'deliverables_due_today_count',
        'next_deliverable_due_date',
        'tiers_count',
        'is_deleted',
        'is_published',
        'app_external_id',
        'app_meta',
    ]


@pytest.fixture
def relationships():
    return [
        'tiers',
        'deliverables',
        'campaign',
        'campaign_installation',
    ]


def test_schema_attributes_are_properly_formatted(attributes):
    for attribute_name in attributes:
        value = getattr(benefit.Attributes, attribute_name, None)
        assert value is not None and value is attribute_name

def test_schema_relationships_are_properly_formatted(relationships):
    for relationship_name in relationships:
        value = getattr(benefit.Relationships, relationship_name, None)
        assert value is not None and value is relationship_name
