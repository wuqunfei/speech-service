import azure.cognitiveservices.speech as speechsdk
import logging
import abc


class Speech(metaclass=abc.ABCMeta):

    @classmethod
    def text_to_speech(self, text):
        pass

    @classmethod
    def speech_to_text(self, text):
        pass


class AzureSpeech(Speech):

    def __init__(self, speech_key, service_region):
        self.speech_key = speech_key
        self.service_region = service_region
        self.speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    # https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstarts/text-to-speech-audio-file?pivots=programming-language-python
    def text_to_speech(self, text):
        audio_filename = str(hash(text)) + ".wav"
        audio_output = speechsdk.audio.AudioOutputConfig(filename=audio_filename)
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=audio_output)
        result = speech_synthesizer.speak_text_async(text).get()
        response_message = None
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            logging.info("Speech synthesized to [{}] for text [{}]".format(audio_filename, text))
            response_message = audio_filename
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            logging.info("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    logging.info("Error details: {}".format(cancellation_details.error_details))
            logging.info("Did you update the subscription info?")
        return response_message

    # https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstarts/speech-to-text-from-file?tabs=linux&pivots=programming-language-python

    def speech_to_text(self, speech_filename):
        audio_input = speechsdk.audio.AudioConfig(filename=speech_filename)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config, audio_config=audio_input)
        logging.info("recognizing now...")
        result = speech_recognizer.recognize_once()
        response_text = None
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            logging.info("Recognized: {}".format(result.text))
            response_text = result.text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            logging.error("No speech could be recognized: {}".format(result.no_match_details))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            logging.error("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                logging.error("Error details: {}".format(cancellation_details.error_details))
        return response_text


class AwsSpeech(Speech):

    # TODO implementation
    def text_to_speech(self, text):
        pass

    def speech_to_text(self, text):
        pass


class GoogleSpeech(Speech):

    # TODO implementation
    def text_to_speech(self, text):
        pass

    def speech_to_text(self, text):
        pass
