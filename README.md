# Spectrum-analysis-over-time-for-sound
This is a hobby project where the goal is to create an animation of sound. This animation is based on the frequencies and their corresponding amplitude. 
At the moment I have created a soundbar animation. Which can be sound in the underneath figure.

## Spectrum part
Before creating the animation you first need to get the frequencies and amplitudes. This can be done using a Fast Fourier Transform. 
### Implementation
1. load the song and choose one of the channels if it is stereo.
2. devide the song into blocks which consists of samples from the time domain. On each block a FFT will be executed. The amount of samples per block = samples per second or sampling rate / framerate of your animation.
This is done so you can choose how often you want to update your animation.
3. Perform the FFT analaysis on every block. We only care about the positive frequencies. You can choose how many frequencies you want by changing parameter: top_N_frequncies, often from 0-8000 most frequencies are found.
4. Because there many frequencies we can group them in histograms by taking averages of groups. The amount of groups can be specified N_soundbar.
5. The result will be the blocks of frequencies with their amplitudes in groups 

## Animation part
In this part I created an animation based on the blocks of frequencies with their amplitudes in groups. In this implementation I created soundbars which represent a frequency, change of height given the amplitude of the frequency per frame.
The visuals are made with a library called pygame. You can also only use the first part and create whatever animation you want.
### Implementation
1. Pick a MP3 file, set the frame rate and the amount of soundbars you want.
2. load the sepectrum data of the song
3. Set the soundbars which represent a group of frequencies at their position and set their corresping amplitudes given the spectrum data.
4. Start playing the sound
5. Loop through the bars and change height given the amplitude every frame 
