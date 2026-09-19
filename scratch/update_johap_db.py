# -*- coding: utf-8 -*-
import os

p1_csv = u"C:\\Users\\그램\\Desktop\\입시분석 참고자료\\2027 종합전형\\2027_학생부종합전형_통합DB.csv"
p1_xls = u"C:\\Users\\그램\\Desktop\\입시분석 참고자료\\2027 종합전형\\2027_학생부종합전형_통합DB.xls"
p2_csv = u"C:\\Users\\그램\\Desktop\\입시분석 참고자료\\2027 종합전형\\2027_면접고사_날짜별_달력일정.csv"
p2_xls = u"C:\\Users\\그램\\Desktop\\입시분석 참고자료\\2027 종합전형\\2027_면접고사_날짜별_달력일정.xls"

def update_file(filepath):
    with open(filepath, 'rb') as f:
        raw = f.read()
        if raw.startswith('\xef\xbb\xbf'):
            raw = raw[3:]
        content = raw.decode('utf-8')
    
    # Simple replace approach for exact column insertion
    content = content.replace(u'"대학명","전형명",', u'"대학명","전형명","원서접수 마감일시",')
    content = content.replace(u'"고려대",', u'"고려대","2026-09-09 17:00",')
    content = content.replace(u'"연세대",', u'"연세대","2026-09-10 17:00",')
    content = content.replace(u'"이화여대",', u'"이화여대","2026-09-10 17:00",')
    content = content.replace(u'"건국대",', u'"건국대","2026-09-11 17:00",')
    content = content.replace(u'"동국대",', u'"동국대","2026-09-11 17:00",')
    content = content.replace(u'"한국외대",', u'"한국외대","2026-09-11 17:00",')
    content = content.replace(u'"광운대",', u'"광운대","2026-09-11 17:00",')
    content = content.replace(u'"숙명여대",', u'"숙명여대","2026-09-11 17:00",')
    content = content.replace(u'"경기대",', u'"경기대","2026-09-11 17:00",')
    
    lines = content.splitlines()
    out = []
    for l in lines:
        if l.startswith(u'"대학명"'):
            out.append(l)
        elif u'2026-09-' not in l and l.strip():
            parts = l.split(u'","')
            if len(parts) >= 2:
                parts.insert(2, u'2026-09-11 18:00')
                out.append(u'","'.join(parts))
            else:
                out.append(l)
        else:
            out.append(l)
            
    final_txt = u'\n'.join(out)
    with open(filepath, 'wb') as f:
        f.write('\xef\xbb\xbf' + final_txt.encode('utf-8'))

for p in [p1_csv, p1_xls, p2_csv, p2_xls]:
    if os.path.exists(p):
        update_file(p)

print "SUCCESSFULLY_UPDATED_JOHAP_DBS"
