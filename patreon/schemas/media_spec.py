# media_spec.py
# This file is auto-generated from the same code that generates
# https://docs.patreon.com. Community pull requests against this
# file may not be accepted.
import pytest

from patreon.schemas import media


@pytest.fixture
def attributes():
    return [
            'file_name',
            'size_bytes',
            'mimetype',
            'state',
            'owner_type',
            'owner_id',
            'owner_relationship',
            'upload_expires_at',
            'upload_url',
            'upload_parameters',
            'download_url',
            'created_at',
            'metadata',
        ]


@pytest.fixture
def relationships():
    return [
        ]


def test_schema_attributes_are_properly_formatted(attributes):
    for attribute_name in attributes:
        value = getattr(media.Attributes, attribute_name, None)
        assert value is not None and value is attribute_name

