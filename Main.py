# -*- coding: utf-8 -*-

import wget
import time

print('Beginning file download with requests')

raw = 'https://cfvod.kaltura.com/hls/p/1660902/sp/166090200/serveFlavor/entryId/1_gr6opqrk/v/1/ev/5/flavorId/1_f4r6gday/name/a.mp4/seg-8-v1-a1.ts'
numberPart = raw.find('seg-')
afterNumberPart = raw.find('-v1-')

for i in range(10000):
    if i == 0:
        continue
    url = raw[0:numberPart + 4] + str(i) + raw[afterNumberPart:len(raw)]
    filename = 'C:\\Users\\Clayton\\Downloads\\LectureVideo\\' + str(i) + '.ts'
    wget.download(url, filename)
    time.sleep(.5)