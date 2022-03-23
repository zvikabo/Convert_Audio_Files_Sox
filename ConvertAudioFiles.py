"""
This script convert music files format using sox (Free music format converter)
by using subprocess with the relevant parameters:
Channels =1 means mono
rate bit = 8000 Mhz
encoding : a-law
using soxi.exe ( Actually a copy od SOX.exe and rename it to soxi.exe return ths file properties
"""

import subprocess
import glob
import logging

sox_install_path = 'C:\\Program Files (x86)\\sox-14-4-2'
source_path = 'C:\\PythonTemp\\AudioSox\\Src'
source_file_suffix = 'WAV'
destination_path = 'C:\\PythonTemp\\AudioSox\\Dst'
convert_file_prefix = 'Heb_'
convert_file_suffix = 'wav'
channels = '1'
rate = '8000'
encoding = 'a-law'

Log_path = 'C:\\PythonTemp\\AudioSox\\Logs'
logger = logging.getLogger('ConvertAudioFiles     ')
hdlr = logging.FileHandler(Log_path + '\\' + 'ConvertAudioFiles.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

for f in glob.glob(source_path + '\\' + '*.' + source_file_suffix):
    p = subprocess.Popen([sox_install_path + '\\sox.exe', f, '-c', channels, '-r', rate, '-e', encoding,
                          destination_path + '\\' + convert_file_prefix + (f.split('.')[-2]).split('\\')[
                              -1] + '.' + convert_file_suffix], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode == 0:
        subprocess.call([sox_install_path + '\\soxi.exe',
                         destination_path + '\\' + convert_file_prefix + (f.split('.')[-2]).split('\\')[
                             -1] + '.' + convert_file_suffix])
        logger.debug(f'{f} has been converted successfully ')
    else:
        logger.debug(f'Fail to convert {f}')
