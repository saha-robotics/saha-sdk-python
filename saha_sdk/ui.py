# saharobotik/ui.py

from .client import Robot

def send_speech_command(client: SahaRobotikClient, text: str, lang: str = "tr"):
    """
    Sends a text-to-speech command to the robot.

    Args:
        client (Robot): API client
        text (str): Text to speak
        lang (str): Language code (default "tr")

    Returns:
        dict: Result of the request
    """
    payload = {
        "lang": lang,
        "text": text
    }
    return client.post("/api/v1/ui/speech", data=payload)


def set_pixel_screen_video(client: SahaRobotikClient, url: str):
    """
    Sets the video to be shown on the robot's pixel screen.

    Args:
        client (Robot): API client
        url (str): URL of the MP4 video

    Returns:
        dict: Result of the request
    """
    return client.post("/api/v1/ui/screen/pixel", params={"url": url})
