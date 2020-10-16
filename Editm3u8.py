# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:25:24 2020

@author: Clayton
"""

filename = 'index.M3U8'

file = open(filename, 'r')
raw = 'https://cfvod.kaltura.com/hls/p/1660902/sp/166090200/serveFlavor/entryId/1_t8hy4wqs/v/1/ev/5/flavorId/1_joh8ocz7/name/a.mp4/seg-1-v1-a1.ts'

newFile = open('CLICKTOWATCH.m3u8', 'w+')

index = raw.find('seg-')
secondIndex = raw.find('-v1-')
count = raw[index+4:secondIndex]
print(count)

for line in file:
    #print(line)
    if line.find('https://') != -1:
        index = line.find('seg-')
        secondIndex = line.find('-v1-')
        count = line[index+4:secondIndex]
        line = 'C://Users/Clayton/Downloads/LectureVideo/' + str(count) + '.ts\n'

    newFile.write(line)