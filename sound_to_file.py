#create your own soundwave to test 
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

#create samples given frequency, amplitude and time
def create_samples(f,a,t):
    samples = []
    for t in time:
        wave_sample = a*np.sin(2*np.pi*f*t)
        samples.append(wave_sample)
    return samples

# Time domain
sampling_rate = 44100  # Number of samples per second
duration = 2  # Total duration of the signal in seconds
time = np.linspace(0, duration, int(sampling_rate * duration))

#for frequency of 10,2000 and 7000 create samples of the waves
samples1 = create_samples(10,5,time)
samples2 = create_samples(2000,5,time)
samples3 = create_samples(7000,5,time)

#concat the 3 waves
total_samples = samples1+samples2+samples3
 
# Save as mp3 file at correct sampling rate
sf.write('myfile.mp3', total_samples, sampling_rate)  
