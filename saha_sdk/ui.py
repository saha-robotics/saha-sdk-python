from .client import Robot
from .models import SpeechModel, ResponseModel

def speak_text(client: Robot, speech_model: SpeechModel) -> ResponseModel:
    """
    Send a text to speech command to the robot.

    Args:
        client (Robot): API client
        speech_model (SpeechModel): Text and language code to speak.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post("/api/v1/ui/speech", data=speech_model.dict())
    return ResponseModel(**response)

def change_pixel_screen_video(client: Robot, url: str) -> ResponseModel:
    """
    Change the pixel screen video of the robot.

    Args:
        client (Robot): API client
        url (str): MP4 file URL for the video.

    Returns:
        ResponseModel: Result of the request
    """
    response = client.post(f"/api/v1/ui/screen/pixel?url={url}")
    return ResponseModel(**response)