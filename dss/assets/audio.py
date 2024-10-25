from dss.assets.core import BaseAsset, ModelAuthor, AudioContent


class ElevenLabsAsset(BaseAsset):

    def __init__(self, **data):
        author = ModelAuthor(provider="Eleven Labs", api_token="")
        content = AudioContent()
        super().__init__(author=author, content=content, **data)

    def generate(self, text, model):
        self.content.file_location = "/tmp"
        self.content.file_format = "mp3"