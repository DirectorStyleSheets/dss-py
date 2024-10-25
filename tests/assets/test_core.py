import pytest
from pydantic import ValidationError
from datetime import datetime, timedelta
from dss.assets.core import BaseAuthor, ModelAuthor, BaseContent, BaseAsset


# === Author Tests

def test_create_base_author():
    author = BaseAuthor(creator='human')
    assert author.creator == 'human'

def test_create_invalid_author():
    with pytest.raises(ValidationError):
        BaseAuthor(creator='invalid')

def test_create_model_author_with_empty_body():
    author = ModelAuthor(provider='Pickford', api_url='https://pickford.ai', model="pavlov", api_token='abc123')
    assert author.creator == 'model'
    assert author.provider == 'Pickford'
    assert author.api_url == 'https://pickford.ai'
    assert author.model == 'pavlov'
    assert author.api_token == 'abc123'
    assert author.request_body == {}

def test_create_model_author_with_body():
    fake_body = {"test": "test"}
    author = ModelAuthor(provider='Pickford', api_url='https://pickford.ai', model="pavlov", api_token='abc123', request_body=fake_body)
    assert author.creator == 'model'
    assert author.provider == 'Pickford'
    assert author.api_url == 'https://pickford.ai'
    assert author.model == 'pavlov'
    assert author.api_token == 'abc123'
    assert author.request_body == fake_body


# === Content Tests

def test_create_base_content():
    content = BaseContent(file_location='/tmp/talk.mp3', file_format='mp3')
    assert content.file_location == '/tmp/talk.mp3'
    assert content.file_format == 'mp3'


# === Asset Tests

def test_create_base_asset():
    base_author = BaseAuthor(creator='human')
    asset = BaseAsset(author=base_author)

    now = datetime.utcnow()
    assert abs((now - asset.timestamp).total_seconds()) < 1
    assert asset.author == base_author
    assert asset.content == None

def test_create_invalud_base_asset():
    with pytest.raises(ValidationError):
        BaseAsset(author="invalid_author")

def test_base_asset_call_generate():
    with pytest.raises(NotImplementedError):
        asset = BaseAsset(author=BaseAuthor(creator='human'))
        asset.generate()




# def test_dss_asset_creation():
#     asset = DSSAsset(id=1, name='Generic Asset', type='Generic')
#     assert asset.id == 1
#     assert asset.name == 'Generic Asset'
#     assert asset.type == 'Generic'

# def test_audio_asset_creation():
#     audio = AudioAsset(name='Soundtrack', duration=300.0, file_format='mp3')
#     assert audio.id == None
#     assert audio.name == 'Soundtrack'
#     assert audio.type == 'Audio'
#     assert audio.duration == 300.0
#     assert audio.file_format == 'mp3'

# def test_character_asset_creation():
#     character = CharacterAsset(id=3, name='Alice', role='Protagonist', description='The main character')
#     assert character.id == 3
#     assert character.name == 'Alice'
#     assert character.type == 'Character'
#     assert character.role == 'Protagonist'
#     assert character.description == 'The main character'

# def test_set_asset_creation():
#     set_asset = SetAsset(id=4, name='Enchanted Forest', location='Mystic Woods', environment='Outdoor')
#     assert set_asset.id == 4
#     assert set_asset.name == 'Enchanted Forest'
#     assert set_asset.type == 'Set'
#     assert set_asset.location == 'Mystic Woods'
#     assert set_asset.environment == 'Outdoor'