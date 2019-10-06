import wave
import struct
import math
from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile


def add_note(sample_rate, audio, freq=None, duration_milliseconds=250, volume=0.5):

    number_of_samples = duration_milliseconds * (sample_rate / 1000.0)
    if freq:
        for x in range(int(number_of_samples)):
            audio.append(volume * math.sin(2 * math.pi * freq * (x / sample_rate)))
    else:
        audio.append(0.0)


def write_to_file(filename, audio, sample_rate):

    wav_file = wave.open(filename, 'w')

    # wav parameters
    channels = 1
    sample_width = 2
    frames = len(audio)
    compressive_type = 'NONE'
    compressive_name = 'not compressed'

    wav_file.setparams((channels, sample_width, sample_rate, frames, compressive_type, compressive_name))

    for sample in audio:
        wav_file.writeframes(struct.pack('h', int(sample * 32767.0)))

    wav_file.close()


def add_sample(source_audio_fname, sample_fname):

    source_audio = AudioSegment.from_wav(source_audio_fname)
    sample = AudioSegment.from_wav(sample_fname)

    new_audio = source_audio.overlay(sample)
    new_audio.export('new_output.wav', format='wav')

    return new_audio
    
    
def fade_audio(audio):    
    source_audio = AudioSegment.from_wav(audio)
    new_audio = source_audio.fade_in(3000).fade_out(3000)
    new_audio.export('new_output.wav', format='wav')


def create_frequency_spectrogram(audio):
    
    sample_rate, samples = wavfile.read(audio)
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
    plt.pcolormesh(times * 1000, frequencies, 10 * np.log10(spectrogram))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [ms]')
    plt.show()


def create_amplitude_spectrogram(audio):

    sample_rate, samples = wavfile.read(audio)

    samples = samples / (2. ** 15)
    sample_points = float(samples.shape[0])
    mono_audio = samples[:, 0]

    times = np.arange(0, sample_points, 1) / sample_rate * 1000

    plt.plot(times, mono_audio, color='R')
    plt.ylabel('Amplitude')
    plt.xlabel('Time [ms]')
    plt.show()


def main():
    
    sample_rate = 44100.
    
    # change it, if u need
    notes_in_freq = {'C5': 523.25, 'D5': 587.33, 'E5': 659.26, 'F5': 698.46, 'G5': 783.99, 'A5': 880., 'H5': 987.77,
                     'C6': 1046.5, 'C7': 1046.5,
                     'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23, 'G4': 392.00, 'A4': 440., 'H4': 493.88}
    
    # create simple melody for example
    audio = []
    add_note(sample_rate, audio, notes_in_freq['G4'], 500)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['E4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['E4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['G4'], 500)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['E4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['E4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['G4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['F4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['E4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['D4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['C4'], 1000)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['A4'], 500)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['C6'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['A4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['G4'], 500)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['E4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['E4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['G4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['F4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['E4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['D4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['C4'], 1000)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['A4'], 500)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['C6'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['A4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['G4'], 500)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['E4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['E4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['G4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['F4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['E4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['D4'], 250)
    add_note(sample_rate, audio, duration_milliseconds=100)
    add_note(sample_rate, audio, notes_in_freq['C4'], 1000)
    add_note(sample_rate, audio, duration_milliseconds=100)

    write_to_file('output.wav', audio, sample_rate)

    # create a sample with an octave interval from source audio
    sample = []

    add_note(sample_rate, sample, notes_in_freq['G5'], 500)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['E5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['E5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['G5'], 500)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['E5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['E5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['G5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['F5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['E5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['D5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['C5'], 1000)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['A5'], 500)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['C7'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['A5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['G5'], 500)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['E5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['E5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['G5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['F5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['E5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['D5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['C5'], 1000)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['A5'], 500)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['C6'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['A5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['G5'], 500)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['E5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['E5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['G5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['F5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['E5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['D5'], 250)
    add_note(sample_rate, sample, duration_milliseconds=100)
    add_note(sample_rate, sample, notes_in_freq['C5'], 1000)
    add_note(sample_rate, sample, duration_milliseconds=100)

    write_to_file('sample.wav', sample, sample_rate)

    audio, sample = 'output.wav', 'sample.wav'
    add_sample(audio, sample)
    audio = 'new_output.wav'

    create_frequency_spectrogram(audio)

    audio, sample = 'new_output.wav', 'new_sample.wav'
    add_sample(audio, sample)
    audio = 'new_output.wav'
    fade_audio(audio)

    create_amplitude_spectrogram(audio)


if __name__ == "__main__":
    main()
