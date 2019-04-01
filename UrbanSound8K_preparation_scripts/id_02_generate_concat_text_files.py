"""
This script generates repetition of the file name for each sound file to be used by ffmpeg to concatenate
 Several files together
make sure to configure the source and destination folders before your execute this script
 Fady Medhat
 version 0.1
"""

import os
import wave
from fnmatch import fnmatch

DATASET_PATH = 'I:\UrbanSound8KunifiedSampling'
CONCAT_COUNT = 100

folder_list =  os.walk(DATASET_PATH).next()[1] #os.listdir(DATASET_PATH)
folder_list.sort()
bat_file = open( os.path.join(DATASET_PATH, 'id_03_generate_concat_sound_files.bat'), 'a')

for i in range(0, len(folder_list)):
    files = os.listdir(os.path.join(DATASET_PATH , folder_list[i]))
    files.sort()
    for name in sorted(files):
        if fnmatch(name, "*.wav"):
            file_path = os.path.join(DATASET_PATH, folder_list[i] , name)

            # for j in range(CONCAT_COUNT):
            #     file.write('file \'' +  str.replace(name, '.txt', '.wav') + '\'\n')
            # file.close()

            #fullFilePath = os.path.join(fullCategoryPath, file)
            wavFile = wave.open(file_path, 'r')
            frames = wavFile.getnframes()
            rate = wavFile.getframerate()
            duration = frames / float(rate)
            rawLine = ''
            if duration < 4:
                for j in range(100):
                    rawLine = rawLine + 'file \'' + name + '\'\n'
                f = open(file_path.replace('.wav', '.txt'), 'w')
                f.write(rawLine)
                f.close()

                ffmpegCommand = 'ffmpeg -f concat -safe 0 -i "%src_location%/' + os.path.join(folder_list[i] , name.replace('.wav', '.txt')) + '" -c copy "%dst_location%/' + os.path.join(folder_list[i] , name) + '"\n'
                bat_file.write(ffmpegCommand)


            print(duration)
            print(wavFile.getparams())

bat_file.close()
