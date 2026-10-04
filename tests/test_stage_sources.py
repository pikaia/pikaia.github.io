"""The YouTube Sources list leaves out Commons file pages (already in Images)."""
from stage_youtube_text import extract_sources

POST = """Text.

**Sources**

- ["Fort Fullerton," Singapore Infopedia](https://www.nlb.gov.sg/x)
- [File:Fort Gate, Fort Canning, Singapore - 20090103.jpg, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Fort_Gate.jpg>)
- [File:KITLV - 29173 - circa 1860.tif, Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:KITLV_(1).tif>) (gallery)
- [OpenStreetMap contributors](https://www.openstreetmap.org/copyright)
"""


def test_commons_file_pages_are_left_out():
    assert extract_sources(POST) == ['- "Fort Fullerton," Singapore Infopedia', "- OpenStreetMap contributors"]
