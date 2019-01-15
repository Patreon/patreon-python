# campaign_spec.py
# This file is auto-generated from the same code that generates
# https://docs.patreon.com. Community pull requests against this
# file may not be accepted.
import pytest

from patreon.schemas import campaign


@pytest.fixture
def attributes():
    return [
            'summary',
            'creation_name',
            'pay_per_name',
            'one_liner',
            'main_video_embed',
            'main_video_url',
            'image_url',
            'image_small_url',
            'thanks_video_url',
            'thanks_embed',
            'thanks_msg',
            'is_monthly',
            'has_rss',
            'has_sent_rss_notify',
            'rss_feed_title',
            'rss_artwork_url',
            'is_nsfw',
            'is_charged_immediately',
            'created_at',
            'published_at',
            'pledge_url',
            'patron_count',
            'discord_server_id',
            'google_analytics_id',
            'earnings_visibility',
        ]


@pytest.fixture
def relationships():
    return [
            'tiers',
            'creator',
            'benefits',
            'goals',
        ]


def test_schema_attributes_are_properly_formatted(attributes):
    for attribute_name in attributes:
        value = getattr(campaign.Attributes, attribute_name, None)
        assert value is not None and value is attribute_name

def test_schema_relationships_are_properly_formatted(relationships):
    for relationship_name in relationships:
        value = getattr(campaign.Relationships, relationship_name, None)
        assert value is not None and value is relationship_name
