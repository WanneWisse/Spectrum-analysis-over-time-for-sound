
import soundfile as sf
import numpy as np

#get spectrum for amount of samples per block
def get_spectrum(block,fs,N_soundbar,top_N_frequencies,normalisation_value):
    frequency_spectrum = np.fft.fft(block)
    frequencies = np.fft.fftfreq(len(block), 1/fs)

    positive_frequencies = frequencies[:len(frequencies) // 2]
    positive_spectrum = np.abs(frequency_spectrum)[:len(frequencies) // 2]
    
    positive_frequencies = positive_frequencies[:top_N_frequencies]
    positive_spectrum = positive_spectrum[:top_N_frequencies]

    p_fs_range = np.linspace(0,len(positive_frequencies),N_soundbar+1)
    normalised_pf = []
    normalised_ps = []
    #create histogram of frequencies
    for f_index in range(len(p_fs_range)-1):
        value_block = np.average(positive_spectrum[int(p_fs_range[f_index]):int(p_fs_range[f_index+1])])
        frequency_block = np.average(positive_frequencies[int(p_fs_range[f_index]):int(p_fs_range[f_index+1])])
        normalised_pf.append(frequency_block)
        normalised_ps.append(value_block*normalisation_value)
    return normalised_pf,normalised_ps

    
#load song and get the blocks with the f and their corresponding value or amplitude
def load_song(filename, stereo, N_blocks,N_soundbar):
    # Extract data and sampling rate from file
    data, fs = sf.read(filename, dtype='float32')  
    if stereo:
        data = data[:,1]
    #create blocks of different values of frequencies per second
    block_size = int(fs/N_blocks) #amount of samples per block determined by framerate
    blocks = []
    for sample_index in range(0,len(data),block_size):
        block = data[sample_index:sample_index+block_size]
        frequencies,values = get_spectrum(block,fs,N_soundbar)
        blocks.append([frequencies,values])
    return data,fs,blocks

    #TODO: More normalisation
    # #get max of blocks
    # max_fs_amplitude = [0 for i in range(N_soundbar)]
    # for b in blocks:
    #     for column in range(len(b)):
    #         if b[1][column] > max_fs_amplitude[column]:
    #             max_fs_amplitude[column] = b[1][column]
    # #sum blocks 
    # blocks_sum = 0
    # for b in blocks:
    #     blocks_sum += np.sum(b[1])

    #print(max_fs_amplitude)
    #normalise all values using max
    # for b in blocks:
    #     for i in range(len(b[1])):
    #         #print(len(max_fs_amplitude))
    #         #print(len(b[1]))
    #         if max_fs_amplitude[i] != 0:
    #             b[1][i] = b[1][i]/max_fs_amplitude[i]*500
    