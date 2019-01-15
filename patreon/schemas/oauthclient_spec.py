# oauthclient_spec.py
# This file is auto-generated from the same code that generates
# https://docs.patreon.com. Community pull requests against this
# file may not be accepted.
import pytest

from patreon.schemas import oauthclient


@pytest.fixture
def attributes():
    return [
        'client_secret',
        'name',
        'description',
        'author_name',
        'domain',
        'version',
        'icon_url',
        'privacy_policy_url',
        'tos_url',
        'redirect_uris',
        'default_scopes',
    ]


@pytest.fixture
def relationships():
    return [
        'user',
        'campaign',
        'creator_token',
        'apps',
    ]


def test_schema_attributes_are_properly_formatted(attributes):
    for attribute_name in attributes:
        value = getattr(oauthclient.Attributes, attribute_name, None)
        assert value is not None and value is attribute_name

def test_schema_relationships_are_properly_formatted(relationships):
    for relationship_name in relationships:
        value = getattr(oauthclient.Relationships, relationship_name, None)
        assert value is not None and value is relationship_name
