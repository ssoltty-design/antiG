import pandas as pd
import os

essay_data = [
    # 10월 수능 전
    {'date': '2026-10-04', 'univ': '홍익대(서울)', 'track': '논술전형(자연/인문)', 'time': '10:00 / 15:00', 'min_stat': '2개 합 5', 'min_detail': '국,수,영,탐(1) 중 2개 합 5, 史4', 'quota_detail': '자전38, 경영48, 법학24, 경제8 등', 'ratio': '논술90+교과10', 'note': '수능 전 논술'},
    {'date': '2026-10-04', 'univ': '성신여대', 'track': '논술우수자', 'time': '10:00 / 14:00', 'min_stat': '2개 합 7', 'min_detail': '국,수,영,탐(1) 중 2개 합 7', 'quota_detail': '경영6, 법학8, 정외3, 사복5 등', 'ratio': '논술100', 'note': '수능 전 논술'},
    {'date': '2026-10-10', 'univ': '연세대(서울)', 'track': '논술전형', 'time': '15:30~17:30', 'min_stat': '최저 無', 'min_detail': '수능 최저 미적용', 'quota_detail': '경영15, 경제5, 정외6, 자유12 등', 'ratio': '논술100', 'note': '★ 수능 전 / 논술100 / 수리+영어제시문'},
    {'date': '2026-10-11', 'univ': '중앙대(창의형)', 'track': '창의형논술', 'time': '10:00~12:00', 'min_stat': '최저 無', 'min_detail': '수능 최저 미적용 (고3 현역만 지원)', 'quota_detail': '경영18, 경제4, 영문4, 미커4, 심리4 등', 'ratio': '논술70+교과20+출결10', 'note': '★ 수능 전 / 고3현역만 / 누락 보정항목'},
    {'date': '2026-10-11', 'univ': '가톨릭대', 'track': '논술전형', 'time': '15:00~16:30', 'min_stat': '최저 無', 'min_detail': '수능 최저 미적용', 'quota_detail': '경영5, 회계5, 국제5, 법학4 등', 'ratio': '논술100', 'note': '수능 전 논술'},
    {'date': '2026-10-11', 'univ': '한국항공대', 'track': '논술우수자', 'time': '15:00~16:30', 'min_stat': '2개 합 6', 'min_detail': '국,수,영,탐(1) 중 2개 합 6', 'quota_detail': '항공경영19, 자전7', 'ratio': '논술100', 'note': '수능 전 논술'},
    {'date': '2026-10-16', 'univ': '연세대(미래)', 'track': '창의인재논술', 'time': '시간 미정', 'min_stat': '최저 無', 'min_detail': '수능 최저 미적용', 'quota_detail': '자율융합계열 87', 'ratio': '논술90+교과10', 'note': '수능 전 논술'},
    {'date': '2026-10-18', 'univ': '단국대', 'track': '논술우수자', 'time': '09:30 / 15:00', 'min_stat': '최저 無', 'min_detail': '수능 최저 미적용', 'quota_detail': '경영29, 퇴계혁신20, 법학10, 경제10 등', 'ratio': '논술90+교과10', 'note': '수능 전 논술'},
    {'date': '2026-10-30', 'univ': '상명대', 'track': '약술형논술', 'time': '시간 미정', 'min_stat': '최저 無', 'min_detail': '수능 최저 미적용 (60분 약술)', 'quota_detail': '경영5, 자전11, 행정4 등', 'ratio': '논술90+교과10', 'note': '★ 약술형 논술 / 수능 전'},

    # 11월 수능 후
    {'date': '2026-11-21', 'univ': '건국대', 'track': 'KU논술우수자', 'time': '09:20~11:00', 'min_stat': '2개 합 5', 'min_detail': '국,수,영,탐(1) 중 2개 합 5, 史5', 'quota_detail': 'KU자전65, 경영15, 무역7, 미커6 등', 'ratio': '논술100', 'note': '수능 후 1주차'},
    {'date': '2026-11-21', 'univ': '숭실대', 'track': '논술우수자', 'time': '15:00~16:40', 'min_stat': '2개 합 6', 'min_detail': '국,수,영,탐(1) 중 2개 합 6', 'quota_detail': '경영16, 글통10, 경제5, 행정6 등', 'ratio': '논술90+교과10', 'note': '수능 후 1주차'},
    {'date': '2026-11-21', 'univ': '서울여대', 'track': '논술우수자', 'time': '10:00~11:30', 'min_stat': '최저 無', 'min_detail': '수능 최저 미적용', 'quota_detail': '자유전공 80', 'ratio': '논술80+교과20', 'note': '수능 후 1주차'},
    {'date': '2026-11-21', 'univ': '성균관대', 'track': '논술우수자', 'time': '08:30 / 13:00', 'min_stat': '3개 합 6', 'min_detail': '국,수,영,탐(평) 중 3개 합 6 (글로벌 3개 합 5)', 'quota_detail': '인문계열38, 사회계열40, 경영20, 글경10 등', 'ratio': '논술100', 'note': '★ 수능 후 1주차 / 최저 3합6'},
    {'date': '2026-11-22', 'univ': '고려대', 'track': '논술전형', 'time': '08:30 입실', 'min_stat': '4개 합 8', 'min_detail': '국,수,영,탐(1) 중 4개 합 8, 史4', 'quota_detail': '경영12, 경제11, 자전15, 통계7, 미디어6 등', 'ratio': '논술100', 'note': '★ 수능 후 1주차 / 최저 4합8 고난도'},
    {'date': '2026-11-22', 'univ': '서강대', 'track': '논술전형', 'time': '16:00 / 19:00', 'min_stat': '3개 합 7', 'min_detail': '국,수,영,탐(1) 중 3개 합 7, 史4', 'quota_detail': '경영38, 경제21, 사과13, 인문15 등', 'ratio': '논술100', 'note': '★ 수능 후 1주차 / 논술100'},
    {'date': '2026-11-22', 'univ': '경희대', 'track': '논술우수자', 'time': '15:00~17:00', 'min_stat': '2개 합 5', 'min_detail': '국,수,영,탐(평) 중 2개 합 5, 史5', 'quota_detail': '경영회계27, 자전8, 경제7, 무역7 등', 'ratio': '논술100', 'note': '수능 후 1주차'},
    {'date': '2026-11-22', 'univ': '숙명여대', 'track': '논술우수자', 'time': '10:00~11:40', 'min_stat': '2개 합 5', 'min_detail': '국,수,영,탐(1) 중 2개 합 5', 'quota_detail': '한국어문12, 중문12, 영문11, 아동9 등', 'ratio': '논술90+교과10', 'note': '수능 후 1주차'},
    {'date': '2026-11-22', 'univ': '동국대', 'track': '논술전형', 'time': '13:00 / 16:30', 'min_stat': '2개 합 5 (경찰 2합4)', 'min_detail': '국,수,영,탐(1) 중 2개 합 5, 史4', 'quota_detail': '경영37, 국통12, 정외6, 행정6, 경찰13 등', 'ratio': '논술70+교과20+출결10', 'note': '★ 수능 후 1주차 / 상위10과목 환산'},
    {'date': '2026-11-22', 'univ': '홍익대(세종)', 'track': '논술전형', 'time': '시간 미정', 'min_stat': '1개 4등급', 'min_detail': '국,수,영,탐(1) 중 1개 4등급', 'quota_detail': '자전31, 상경30, 광고14', 'ratio': '논술90+교과10', 'note': '세종캠퍼스 시험'},
    {'date': '2026-11-22', 'univ': '수원대', 'track': '약술형논술', 'time': '시간 미정', 'min_stat': '최저 無', 'min_detail': '수능 최저 미적용 (80분 약술)', 'quota_detail': '인문사회융합 70, 경영공학 63', 'ratio': '논술80+교과20', 'note': '약술형 논술'},
    {'date': '2026-11-27', 'univ': '경기대', 'track': '논술우수자', 'time': '시간 미정', 'min_stat': '최저 無', 'min_detail': '수능 최저 미적용', 'quota_detail': '자전(수원) 93, 자전(서울) 41', 'ratio': '논술90+교과10', 'note': '수능 후 2주차 금요일'},
    {'date': '2026-11-28', 'univ': '이화여대', 'track': '논술전형', 'time': '08:30 / 14:20', 'min_stat': '2개 합 5', 'min_detail': '국어 포함 2개 합 5 (스크랜튼 3개 합 5)', 'quota_detail': '경영19, 경제10, 스크랜튼13, 인문1 등', 'ratio': '논술100', 'note': '★ 수능 후 2주차 / 논술100'},
    {'date': '2026-11-28', 'univ': '동덕여대', 'track': '약술형논술', 'time': '10:00 / 14:30', 'min_stat': '2개 합 6', 'min_detail': '국,수,영,탐(1) 중 2개 합 6', 'quota_detail': '경영40, 커뮤11, 영어12, 중문11 등', 'ratio': '논술100', 'note': '약술형 논술'},
    {'date': '2026-11-28', 'univ': '한국외대', 'track': '논술전형(T1/T2)', 'time': '10:00 / 15:00', 'min_stat': '2개 합 4', 'min_detail': '국,수,영,탐(1) 중 2개 합 4 (글로벌 2합6)', 'quota_detail': '자전(서울)24, 경제11, 미디어10, 정외8 등', 'ratio': '논술100', 'note': '★ 수능 후 2주차 / 영어제시문(T1)'},
    {'date': '2026-11-28', 'univ': '한양대', 'track': '논술전형', 'time': '09:30 / 13:30 / 17:00', 'min_stat': '3개 합 7', 'min_detail': '국,수,영,탐(1) 중 3개 합 7', 'quota_detail': '인터컬리지15, 경영12, 경제금융9 등', 'ratio': '논술100', 'note': '★ 수능 후 2주차 / 논술100'},
    {'date': '2026-11-28', 'univ': '세종대', 'track': '논술우수자', 'time': '09:00~11:00', 'min_stat': '2개 합 5', 'min_detail': '국,수,영,탐(1) 중 2개 합 5', 'quota_detail': '자전71, 국제10, 경영9, 호텔경영9 등', 'ratio': '논술80+교과20', 'note': '수능 후 2주차'},
    {'date': '2026-11-29', 'univ': '중앙대(일반형)', 'track': '논술전형', 'time': '10:00 / 14:00', 'min_stat': '3개 합 6', 'min_detail': '국,수,영,탐(1) 중 3개 합 6, 英2->1, 史4', 'quota_detail': '경영36, 간호13, 경제12, 독문8, 불문8 등', 'ratio': '논술70+교과20+출결10', 'note': '★ 수능 후 2주차 / 최저 3합6'},
    {'date': '2026-11-29', 'univ': '한국외대', 'track': '논술전형(T3/T4)', 'time': '10:00 / 15:00', 'min_stat': '2개 합 4', 'min_detail': '국,수,영,탐(1) 중 2개 합 4', 'quota_detail': '자전(글로벌)40, 경영27, 융재10 등', 'ratio': '논술100', 'note': '★ 수능 후 2주차 / 영어제시문(T3)'},
    {'date': '2026-11-29', 'univ': '광운대', 'track': '논술우수자', 'time': '10:00 / 14:30', 'min_stat': '최저 無', 'min_detail': '수능 최저 미적용', 'quota_detail': '경영12, 법학10, 미커8, 동북아6 등', 'ratio': '논술80+교과20', 'note': '★ 수능 후 2주차 / 최저無'},
    {'date': '2026-11-29', 'univ': '덕성여대', 'track': '논술전형', 'time': '시간 미정', 'min_stat': '2개 합 7', 'min_detail': '국,수,영,탐(1) 중 2개 합 7', 'quota_detail': '글로벌융합대학 65', 'ratio': '논술100', 'note': '수능 후 2주차'},
    {'date': '2026-11-30', 'univ': '가천대', 'track': '약술형논술', 'time': '시간 미정', 'min_stat': '1개 3등급', 'min_detail': '국,수,영,탐(1) 중 1개 3등급 (80분 약술)', 'quota_detail': 'AI인문73, 법대46, 경영40, 회계16 등', 'ratio': '논술100', 'note': '★ 약술형 논술'},

    # 12월 수능 후 3주차
    {'date': '2026-12-05', 'univ': '인하대', 'track': '논술우수자', 'time': '시간 미정', 'min_stat': '최저 無', 'min_detail': '수능 최저 미적용', 'quota_detail': '경영22, 영미유럽14, 경제11, 행정10 등', 'ratio': '논술80+교과20', 'note': '★ 수능 후 3주차 / 최저無'},
    {'date': '2026-12-05', 'univ': '국민대', 'track': '약술형논술', 'time': '시간 미정', 'min_stat': '2개 합 6', 'min_detail': '국,수,영,탐(1) 중 2개 합 6, 史필 (90분 약술)', 'quota_detail': '법학20, 경영11, 행정6, 정외3 등', 'ratio': '논술100', 'note': '★ 약술형 논술 / 신설 보정항목'},
    {'date': '2026-12-06', 'univ': '아주대', 'track': '논술우수자', 'time': '09:00~11:00', 'min_stat': '최저 無', 'min_detail': '수능 최저 미적용', 'quota_detail': '경영15, 국문5, 자전5 등', 'ratio': '논술80+교과20', 'note': '★ 수능 후 3주차 / 최저無'}
]

df = pd.DataFrame(essay_data)
target_dir = r'C:\Users\그램\Desktop\입시분석 참고자료\논술일정표'
csv_path = os.path.join(target_dir, '2027_수시_논술전형_통합DB.csv')
xls_path = os.path.join(target_dir, '2027_수시_논술전형_통합DB.xls')
calendar_csv = os.path.join(target_dir, '2027_논술고사_날짜별_달력일정.csv')
calendar_xls = os.path.join(target_dir, '2027_논술고사_날짜별_달력일정.xls')

df.to_csv(csv_path, index=False, encoding='utf-8-sig')
df.to_excel(xls_path, index=False, engine='openpyxl')

calendar_df = df[['date', 'univ', 'track', 'time', 'min_stat', 'quota_detail', 'note']].sort_values(by=['date', 'time'])
calendar_df.to_csv(calendar_csv, index=False, encoding='utf-8-sig')
calendar_df.to_excel(calendar_xls, index=False, engine='openpyxl')

# Also copy to '2027 종합전형'
target_dir2 = r'C:\Users\그램\Desktop\입시분석 참고자료\2027 종합전형'
df.to_csv(os.path.join(target_dir2, '2027_수시_논술전형_통합DB.csv'), index=False, encoding='utf-8-sig')
df.to_excel(os.path.join(target_dir2, '2027_수시_논술전형_통합DB.xls'), index=False, engine='openpyxl')
calendar_df.to_csv(os.path.join(target_dir2, '2027_논술고사_날짜별_달력일정.csv'), index=False, encoding='utf-8-sig')
calendar_df.to_excel(os.path.join(target_dir2, '2027_논술고사_날짜별_달력일정.xls'), index=False, engine='openpyxl')

print("SUCCESS: CSV and XLS files created.")
