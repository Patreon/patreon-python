# user_spec.py
# This file is auto-generated from the same code that generates
# https://docs.patreon.com. Community pull requests against this
# file may not be accepted.
import pytest

from patreon.schemas import user


@pytest.fixture
def attributes():
    return [
        'email',
        'first_name',
        'last_name',
        'full_name',
        'is_email_verified',
        'vanity',
        'about',
        'image_url',
        'thumb_url',
        'can_see_nsfw',
        'created',
        'url',
        'like_count',
        'hide_pledges',
        'social_connections',
    ]


@pytest.fixture
def relationships():
    return [
        'memberships',
        'campaign',
    ]


def test_schema_attributes_are_properly_formatted(attributes):
    for attribute_name in attributes:
        value = getattr(user.Attributes, attribute_name, None)
        assert value is not None and value is attribute_name

def test_schema_relationships_are_properly_formatted(relationships):
    for relationship_name in relationships:
        value = getattr(user.Relationships, relationship_name, None)
        assert value is not None and value is relationship_name
