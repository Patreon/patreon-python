# tier_spec.py
# This file is auto-generated from the same code that generates
# https://docs.patreon.com. Community pull requests against this
# file may not be accepted.
import pytest

from patreon.schemas import tier


@pytest.fixture
def attributes():
    return [
            'amount_cents',
            'user_limit',
            'remaining',
            'description',
            'requires_shipping',
            'created_at',
            'url',
            'patron_count',
            'post_count',
            'discord_role_ids',
            'title',
            'image_url',
            'edited_at',
            'published',
            'published_at',
            'unpublished_at',
        ]


@pytest.fixture
def relationships():
    return [
            'campaign',
            'tier_image',
            'benefits',
        ]


def test_schema_attributes_are_properly_formatted(attributes):
    for attribute_name in attributes:
        value = getattr(tier.Attributes, attribute_name, None)
        assert value is not None and value is attribute_name

def test_schema_relationships_are_properly_formatted(relationships):
    for relationship_name in relationships:
        value = getattr(tier.Relationships, relationship_name, None)
        assert value is not None and value is relationship_name
