from unittest import TestCase

from speech import Speech, AzureSpeech


class TestAzureSpeech(TestCase):

    def setUp(self):
        self.speech = Speech
        self.init_azure()
        self.speech = AzureSpeech(self.AZURE_SPEECH_KEY, self.AZURE_SERVICE_REGION)

    def init_azure(self):

        # please create your key
        self.AZURE_SPEECH_KEY = "***"
        self.AZURE_SERVICE_REGION = "***"

        self.HELLO_WORLD_TEXT = "Hello World."
        self.HELLO_WORLD_FILE = "hello_world.wav"

    def test_azure_text_to_speech(self):
        audio_filename = self.speech.text_to_speech("hello world")
        self.assertIsNotNone(audio_filename, "TTS audio not generated")

    def test_azure_speech_to_text(self):
        text = self.speech.speech_to_text(self.HELLO_WORLD_FILE)
        self.assertEqual(self.HELLO_WORLD_TEXT, text, "STT failed")
