from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime


# === Author Definitions

class BaseAuthor(BaseModel):
    creator: Literal['human', 'model'] = Field(..., description="Type of the asset")

class ModelAuthor(BaseAuthor):
    provider: str = Field(..., description="The name of the model provider used for the asset")
    api_url: Optional[str] = Field(None, description="The URL to request generation from")
    model: Optional[str] = Field(None, description="Name or identifier that the API will use to select the model")
    api_token: str = Field(..., description="The users API token")
    request_body: dict = Field(default_factory=dict, description="The request body for the model API")

    def __init__(self, **data):
        super().__init__(creator='model', **data)

class HumanAuthor(BaseAuthor):
    name: str = Field(..., description="The name of the person who created the asset")

    def __init__(self, **data):
        super().__init__(creator='human', **data)


# === Content Definitions

class BaseContent(BaseModel):
    file_location: Optional[str] = Field(None, description="Location of the file - it MUST be a local or remote filepath")
    file_format: Optional[str] = Field(None, description="The format of the file")

class AudioContent(BaseContent):
    text: Optional[str] = Field(None, description="The text used to generate audio")
    
    def __init__(self, **data):
        super().__init__(**data)


# === Asset Definitions

class BaseAsset(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of instance creation")
    author: BaseAuthor = Field(..., description="Author of the asset")
    content: Optional[BaseContent] = Field(None, description="Content associated with the asset")

    def generate(self):
        raise NotImplementedError("The generate method must be implemented by subclasses.")



# class DSSAsset(BaseModel):
#     id: Optional[int] = Field(None, description="Unique identifier for the asset")
#     file_path: str = Field(..., description="Location of the file")
#     name: str = Field(..., description="Name of the asset")
#     type: Literal['audio'] = Field(..., description="Type of the asset")




# class AudioAsset(DSSAsset):
#     duration: float = Field(..., description="Duration of the audio in seconds")
#     file_format: str = Field(..., description="Audio file format (e.g., 'mp3', 'wav')")
#     purpose: Literal["dialog", 'music', 'sfx'] = Field(..., description="What is this audio used for?")

#     def __init__(self, **data):
#         super().__init__(type='audio', **data)







# class CharacterAsset(DSSAsset):
#     role: str = Field(..., description="Role of the character in the storyline")
#     description: Optional[str] = Field(None, description="Description of the character")

#     def __init__(self, **data):
#         super().__init__(type='Character', **data)

# class SetAsset(DSSAsset):
#     location: str = Field(..., description="Location of the set")
#     environment: str = Field(..., description="Environment type (e.g., 'indoor', 'outdoor')")

#     def __init__(self, **data):
#         super().__init__(type='Set', **data)