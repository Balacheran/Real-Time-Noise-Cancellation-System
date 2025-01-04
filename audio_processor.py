import pyaudio
import wave
import numpy as np
from filters.single_speaker import SingleSpeakerFilter
from filters.multi_speaker import MultiSpeakerFilter
from utils.audio_utils import calculate_rms, trim_silence
from noise_cancellation import remove_noise

class AudioProcessor:
    def __init__(self):
        # Initialize audio input and output streams
        self.input_stream = None
        self.output_stream = None
        self.single_speaker_filter = SingleSpeakerFilter()
        self.multi_speaker_filter = MultiSpeakerFilter()
        self.p = pyaudio.PyAudio()

    def start_stream(self):
        # Start the audio input and output streams
        self.input_stream = self.p.open(format=pyaudio.paInt16,
                                        channels=1,
                                        rate=44100,
                                        input=True,
                                        frames_per_buffer=512)  # Reduced buffer size
        self.output_stream = self.p.open(format=pyaudio.paInt16,
                                         channels=1,
                                         rate=44100,
                                         output=True,
                                         frames_per_buffer=512)  # Reduced buffer size

    def stop_stream(self):
        # Stop the audio input and output streams
        if self.input_stream is not None:
            self.input_stream.stop_stream()
            self.input_stream.close()
        if self.output_stream is not None:
            self.output_stream.stop_stream()
            self.output_stream.close()
        self.p.terminate()

    def process_audio(self, audio_chunk, scenario='single'):
        # Process the incoming audio chunk
        if scenario == 'single':
            processed_audio = self.single_speaker_filter.apply_filter(audio_chunk)
        else:
            processed_audio = self.multi_speaker_filter.apply_filter(audio_chunk)

        # Apply noise cancellation
        noise_profile = np.zeros_like(audio_chunk)  # Placeholder, implement actual noise profile
        noise_profile_float = noise_profile.astype(np.float32) / 32768.0  # Convert to floating-point
        processed_audio_float = processed_audio.astype(np.float32) / 32768.0  # Convert to floating-point

        processed_audio = remove_noise(processed_audio_float, noise_profile_float)

        processed_audio_int = (processed_audio * 32768).astype(np.int16)  # Convert back to int16
        self.output_stream.write(processed_audio_int.tobytes())
        return processed_audio_int

    def save_processed_audio(self, processed_audio, filename):
        # Save the processed audio to a .wav file
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(processed_audio.tobytes())
        wf.close()

    def set_single_speaker_filter(self, filter):
        # Set the filter for single speaker scenario
        self.single_speaker_filter = filter

    def set_multi_speaker_filter(self, filter):
        # Set the filter for multiple speakers scenario
        self.multi_speaker_filter = filter
