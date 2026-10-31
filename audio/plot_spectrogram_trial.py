import soundfile as sf
from pathlib import Path
import librosa
import numpy as np
import matplotlib.pyplot as plt

TICKS = np.array([31.25, 62.5, 125, 250, 500, 1000, 2000, 4000, 8000])
TICK_LABELS = np.array(["31.25", "62.5", "125", "250", "500", "1k", "2k", "4k", "8k"])


def plot_spectrogram_and_save(signal, sample_rate, output_path: Path,
                              fft_size=2048, hop_size=None, window_size=None):
    if not window_size:
        window_size = fft_size

    if not hop_size:
        hop_size = window_size // 4

    stft = librosa.stft(signal, n_fft=fft_size, hop_length=hop_size,
                        win_length=window_size)
    spectrogram = np.abs(stft)
    spectrogram_db = librosa.amplitude_to_db(spectrogram)

    plt.figure(figsize=(10, 4))
    img = librosa.display.specshow(spectrogram_db, y_axis='log', x_axis='time',
                                   sr=sample_rate, cmap='inferno', hop_length=hop_size,
                                   win_length=window_size, n_fft=fft_size)
    plt.xlabel('Time [s]')
    plt.ylabel('Frequency [Hz]')
    plt.yticks(TICKS, TICK_LABELS)
    plt.colorbar(img, format="%+2.f dBFS")
    #plt.show()

    output_path.parent.mkdir(exist_ok=True, parents=True)

    plt.savefig(output_path.with_stem(f'{output_path.stem}_WINLEN={window_size}_HOPLEN={hop_size}'
                                      f'_NFFT={fft_size}'), dpi=300, bbox_inches='tight', transparent=False)


def main():
    plt.rcParams.update({'font.size': 7})
    signal, sample_rate = sf.read(Path('data') / 'LJ001-0023.wav')
    print(f'Sample rate: {sample_rate}')
    plot_spectrogram_and_save(signal, sample_rate, Path('img') / 'spectrogram.png',
                              window_size=2048, fft_size=8192)


if __name__ == '__main__':
    main()
