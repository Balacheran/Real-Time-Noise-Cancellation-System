from audio_processor import AudioProcessor
import numpy as np
import wave

def main():
    audio_processor = AudioProcessor()
    scenario = input("Select scenario (single/multi): ").strip().lower()
    if scenario not in ['single', 'multi']:
        print("Invalid scenario selected. Please choose 'single' or 'multi'.")
        return

    audio_processor.start_stream()
    processed_audio_chunks = []

    try:
        while True:
            audio_chunk = audio_processor.input_stream.read(512)  # Reduced buffer size
            if not audio_chunk:
                print("No audio input detected.")
                continue

            audio_chunk = np.frombuffer(audio_chunk, dtype=np.int16)
            print(f"Captured audio chunk: {audio_chunk[:10]}")  # Print the first 10 samples for debugging

            processed_audio = audio_processor.process_audio(audio_chunk, scenario=scenario)
            processed_audio_chunks.append(processed_audio)

    except KeyboardInterrupt:
        print("KeyboardInterrupt detected. Stopping stream...")

    finally:
        audio_processor.stop_stream()
        save_processed_audio(processed_audio_chunks, 'output_audio/processed_audio.wav')
        print("Audio saved to 'output_audio/processed_audio.wav'")

def save_processed_audio(processed_audio_chunks, filename):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 bytes for int16
        wf.setframerate(44100)
        for chunk in processed_audio_chunks:
            wf.writeframes(chunk)

if __name__ == "__main__":
    main()
