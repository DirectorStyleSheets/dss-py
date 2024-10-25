from dss.assets.core import ModelAuthor
from dss.assets.audio import ElevenLabsAsset
from datetime import datetime, timedelta


def test_eleven_labs_asset_creation():
    audio_text = "Text to audio with Eleven Labs."
    model_id = "pavlov"
    asset = ElevenLabsAsset()
    # Verify timestamp
    now = datetime.utcnow()
    assert abs((now - asset.timestamp).total_seconds()) < 1
    # Verify author information
    assert isinstance(asset.author, ModelAuthor)
    assert asset.author.provider == "Eleven Labs"
    # Verify content
    assert asset.content.text == None
    assert asset.content.file_location == None

def test_eleven_labs_asset_creation_and_generation():
    audio_text = "Text to audio with Eleven Labs."
    model_id = "pavlov"
    asset = ElevenLabsAsset()
    # Verify empty content
    assert asset.content.file_location == None
    assert asset.content.file_format == None
    # Verify content exists after generation
    asset.generate(audio_text)
    assert asset.content.file_location == "/tmp"
    assert asset.content.file_format == "mp3"