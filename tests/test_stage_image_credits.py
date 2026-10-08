"""Commons photos credited "Name / Wikimedia Commons" aren't labelled personal photography."""
from stage_youtube_text import describe_image_sources, extract_image_credit


def test_slash_commons_credit_keeps_its_repository():
    credit = extract_image_credit("The memorial. (Photo: Bijay Chaurasia / Wikimedia Commons, CC BY-SA 4.0)")
    assert credit == "Bijay Chaurasia, CC BY-SA 4.0, via Wikimedia Commons"


def test_slash_commons_credit_without_photo_prefix():
    credit = extract_image_credit("Inside the bank. (Imperial War Museums / Wikimedia Commons, public domain)")
    assert credit == "Imperial War Museums, public domain, via Wikimedia Commons"


def test_plain_via_commons_credit_unchanged():
    credit = extract_image_credit("A note. (National Museum of American History, public domain, via Wikimedia Commons)")
    assert credit == "National Museum of American History, public domain, via Wikimedia Commons"


def test_commons_only_credits_are_not_personal_photography():
    lines = [extract_image_credit("x (Photo: Bijay Chaurasia / Wikimedia Commons, CC BY-SA 4.0)"),
             extract_image_credit("y (Photo: Wombatjpw / Wikimedia Commons, CC BY-SA 4.0)")]
    assert describe_image_sources([f"- {line}" for line in lines]) == "Wikimedia Commons"


def test_personal_photo_still_labelled():
    assert describe_image_sources(["- Chris Lee", "- Someone, CC BY-SA 4.0, via Wikimedia Commons"]) == \
        "personal photography and Wikimedia Commons"
