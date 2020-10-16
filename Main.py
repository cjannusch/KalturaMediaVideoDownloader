# -*- coding: utf-8 -*-

import wget

print('Beginning file download with requests')

raw = 'https://cfvod.kaltura.com/hls/p/1660902/sp/166090200/serveFlavor/entryId/1_t8hy4wqs/v/1/ev/5/flavorId/1_joh8ocz7/name/a.mp4/seg-2-v1-a1.ts'
numberPart = raw.find('seg-')
count = 1
afterNumberPart = raw.find('-v1-')

url = raw[0:numberPart + 4] + str(count) + raw[afterNumberPart:len(raw)]

filename = 'C:\\Users\\Clayton\\Downloads\\LectureVideo\\' + str(count) + '.ts'

wget.download(url, filename)

for i in range(10000):
    if i == 0:
        continue
    count = i
    url = raw[0:numberPart + 4] + str(count) + raw[afterNumberPart:len(raw)]
    filename = 'C:\\Users\\Clayton\\Downloads\\LectureVideo\\' + str(count) + '.ts'
    wget.download(url, filename)