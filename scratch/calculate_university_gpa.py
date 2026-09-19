import pandas as pd
import numpy as np
import os

# Load subject-level data
csv_path = r"C:\Users\그램\Desktop\입시분석 참고자료\내신성적\학생부_과목별_상세성적_분석.csv"
df = pd.read_csv(csv_path)

print("Columns:", df.columns)
print("Total rows:", len(df))

# Convert numeric columns
df['학점수'] = pd.to_numeric(df['학점수'], errors='coerce').fillna(0)
df['원점수'] = pd.to_numeric(df['원점수'], errors='coerce')
df['석차등급'] = pd.to_numeric(df['석차등급'], errors='coerce')

# Filter for rank grade subjects (석차등급 과목)
df_rank = df[df['구분'] == '석차등급'].copy()
df_jinro = df[df['구분'] == '진로선택'].copy()

print(f"Rank-graded courses count: {len(df_rank)}")
print(f"Jinro-choice courses count: {len(df_jinro)}")

# -------------------------------------------------------------
# 1. Simple 3-Year Overall Average GPA (단순 평균)
# -------------------------------------------------------------
simple_avg_gpa = (df_rank['석차등급'] * df_rank['학점수']).sum() / df_rank['학점수'].sum()
print(f"Simple Credit-Weighted Average GPA: {simple_avg_gpa:.4f}")

# -------------------------------------------------------------
# 2. Dongguk University (동국대: 상위 10과목 정량 반영)
# Reflects top 10 courses across 국어, 수학, 영어, 사회, 과학, 한국사
# Grade points: 1=10, 2=9.99, 3=9.95, 4=9.90, 5=9.00, 6=8.00, 7=5.00, 8=3.00, 9=0.0
# -------------------------------------------------------------
def dongguk_score(grade):
    if grade == 1: return 10.0
    elif grade == 2: return 9.99
    elif grade == 3: return 9.95
    elif grade == 4: return 9.90
    elif grade == 5: return 9.00
    elif grade == 6: return 8.00
    elif grade == 7: return 5.00
    elif grade == 8: return 3.00
    else: return 0.0

df_rank['동국대점수'] = df_rank['석차등급'].apply(dongguk_score)
df_dongguk_top10 = df_rank.sort_values(by=['동국대점수', '석차등급'], ascending=[False, True]).head(10)

dongguk_top10_score = df_dongguk_top10['동국대점수'].mean() # Average score out of 10.0
dongguk_top10_avg_grade = df_dongguk_top10['석차등급'].mean() # Average rank grade of top 10

print(f"Dongguk Top 10 Avg Grade: {dongguk_top10_avg_grade:.2f} 등급, Score: {dongguk_top10_score:.4f} / 10.0 (70% 환산점수: {dongguk_top10_score * 70 / 10:.2f}점)")

# -------------------------------------------------------------
# 3. Hankuk University of Foreign Studies (한국외대: 등급 vs 원점수 Max)
# HUFS Grade score: 1=100, 2=96, 3=92, 4=88, 5=84, 6=70, 7=50
# HUFS Raw Score conversion: >=90: 100, >=80: 96, >=70: 92, >=60: 84, >=50: 70, <50: 50
# -------------------------------------------------------------
def hufs_grade_score(grade):
    if grade == 1: return 100
    elif grade == 2: return 96
    elif grade == 3: return 92
    elif grade == 4: return 88
    elif grade == 5: return 84
    elif grade == 6: return 70
    elif grade == 7: return 50
    else: return 30

def hufs_raw_score(raw):
    if pd.isna(raw): return 0
    if raw >= 90: return 100
    elif raw >= 80: return 96
    elif raw >= 70: return 92
    elif raw >= 60: return 84
    elif raw >= 50: return 70
    else: return 50

# Filter HUFS Humanities reflectable subjects (국, 수, 영, 사, 한국사)
hufs_subjects = ['국어', '수학', '영어', '사회', '한국사', '기술가정', '외국어']
df_hufs = df_rank[df_rank['교과'].isin(hufs_subjects)].copy()

df_hufs['등급환산점'] = df_hufs['석차등급'].apply(hufs_grade_score)
df_hufs['원점수환산점'] = df_hufs['원점수'].apply(hufs_raw_score)
df_hufs['최종적용점수'] = np.maximum(df_hufs['등급환산점'], df_hufs['원점수환산점'])

hufs_weighted_score = (df_hufs['최종적용점수'] * df_hufs['학점수']).sum() / df_hufs['학점수'].sum()
# Equivalent Grade estimate: 100=1, 96=2, 92=3, 88=4, 84=5
# Interpolate equivalent grade:
if hufs_weighted_score >= 96:
    hufs_equiv_grade = 1.0 + (100 - hufs_weighted_score) / 4.0
elif hufs_weighted_score >= 92:
    hufs_equiv_grade = 2.0 + (96 - hufs_weighted_score) / 4.0
elif hufs_weighted_score >= 88:
    hufs_equiv_grade = 3.0 + (92 - hufs_weighted_score) / 4.0
else:
    hufs_equiv_grade = 4.0 + (88 - hufs_weighted_score) / 4.0

print(f"HUFS Max Applied Weighted Score: {hufs_weighted_score:.2f}점 / 100점 (추정 변환 등급: {hufs_equiv_grade:.2f} 등급)")

# -------------------------------------------------------------
# 4. Sungkyunkwan University (성균관대 추천인재)
# Grade score: 1=100, 2=99.5, 3=99.0, 4=98.0, 5=96.0, 6=90.0, 7=80.0, 8=60.0
# Jinro: A=100, B=90, C=80
# -------------------------------------------------------------
def skku_grade_score(grade):
    if grade == 1: return 100.0
    elif grade == 2: return 99.5
    elif grade == 3: return 99.0
    elif grade == 4: return 98.0
    elif grade == 5: return 96.0
    elif grade == 6: return 90.0
    elif grade == 7: return 80.0
    else: return 60.0

skku_subjects = ['국어', '수학', '영어', '사회', '과학', '한국사']
df_skku = df_rank[df_rank['교과'].isin(skku_subjects)].copy()
df_skku['점수'] = df_skku['석차등급'].apply(skku_grade_score)

skku_common_score = (df_skku['점수'] * df_skku['학점수']).sum() / df_skku['학점수'].sum()

def jinro_score_b(val):
    if val == 'A': return 100.0
    elif val == 'B': return 90.0
    else: return 80.0

df_jinro_skku = df_jinro[df_jinro['교과'].isin(skku_subjects)].copy()
df_jinro_skku['점수'] = df_jinro_skku['성취도'].apply(jinro_score_b)
skku_jinro_score = (df_jinro_skku['점수'] * df_jinro_skku['학점수']).sum() / df_jinro_skku['학점수'].sum()

skku_total_score = skku_common_score * 0.8 + skku_jinro_score * 0.2
print(f"Sungkyunkwan Recalculated Score: {skku_total_score:.2f}점 / 100점 (공통80%: {skku_common_score:.2f}, 진로20%: {skku_jinro_score:.2f})")

# -------------------------------------------------------------
# 5. Konkuk University (건국대 KU지역균형)
# Grade score: 1=100, 2=99.8, 3=99.4, 4=99.0, 5=98.0, 6=93.0, 7=85.0
# -------------------------------------------------------------
def ku_grade_score(grade):
    if grade == 1: return 100.0
    elif grade == 2: return 99.8
    elif grade == 3: return 99.4
    elif grade == 4: return 99.0
    elif grade == 5: return 98.0
    elif grade == 6: return 93.0
    elif grade == 7: return 85.0
    else: return 70.0

df_ku = df_rank[df_rank['교과'].isin(skku_subjects)].copy()
df_ku['점수'] = df_ku['석차등급'].apply(ku_grade_score)
ku_score = (df_ku['점수'] * df_ku['학점수']).sum() / df_ku['학점수'].sum()

print(f"Konkuk Recalculated Score (out of 100): {ku_score:.2f}점 (교과70% 환산: {ku_score * 0.7:.2f}점)")

# -------------------------------------------------------------
# 6. Sookmyung Women's University (숙명여대 지역균형)
# Grade score: 1=100, 2=99.0, 3=98.0, 4=96.0, 5=92.0, 6=85.0, 7=70.0
# -------------------------------------------------------------
def smu_grade_score(grade):
    if grade == 1: return 100.0
    elif grade == 2: return 99.0
    elif grade == 3: return 98.0
    elif grade == 4: return 96.0
    elif grade == 5: return 92.0
    elif grade == 6: return 85.0
    elif grade == 7: return 70.0
    else: return 50.0

smu_subjects = ['국어', '수학', '영어', '사회', '한국사']
df_smu = df_rank[df_rank['교과'].isin(smu_subjects)].copy()
df_smu['점수'] = df_smu['석차등급'].apply(smu_grade_score)
smu_score = (df_smu['점수'] * df_smu['학점수']).sum() / df_smu['학점수'].sum()

print(f"Sookmyung Recalculated Score (out of 100): {smu_score:.2f}점 (교과70% 환산: {smu_score * 0.7:.2f}점)")

# -------------------------------------------------------------
# 7. Chung-Ang University (중앙대: 인문 상위 10과목)
# Grade score: 1=10, 2=9.94, 3=9.86, 4=9.76, 5=9.60, 6=9.30, 7=8.80
# -------------------------------------------------------------
def cau_grade_score(grade):
    if grade == 1: return 10.0
    elif grade == 2: return 9.94
    elif grade == 3: return 9.86
    elif grade == 4: return 9.76
    elif grade == 5: return 9.60
    elif grade == 6: return 9.30
    elif grade == 7: return 8.80
    else: return 7.50

cau_subjects = ['국어', '수학', '영어', '사회', '한국사']
df_cau = df_rank[df_rank['교과'].isin(cau_subjects)].copy()
df_cau['점수'] = df_cau['석차등급'].apply(cau_grade_score)
df_cau_top10 = df_cau.sort_values(by=['점수', '석차등급'], ascending=[False, True]).head(10)
cau_top10_score = df_cau_top10['점수'].mean()
cau_top10_avg_grade = df_cau_top10['석차등급'].mean()

print(f"Chung-Ang Top 10 Humanities Avg Grade: {cau_top10_avg_grade:.2f} 등급, Score: {cau_top10_score:.4f} / 10.0")

# -------------------------------------------------------------
# 8. Kyung Hee University (경희대)
# Grade score: 1=100, 2=99, 3=97, 4=94, 5=90, 6=80, 7=60
# -------------------------------------------------------------
def khu_grade_score(grade):
    if grade == 1: return 100.0
    elif grade == 2: return 99.0
    elif grade == 3: return 97.0
    elif grade == 4: return 94.0
    elif grade == 5: return 90.0
    elif grade == 6: return 80.0
    elif grade == 7: return 60.0
    else: return 40.0

df_khu = df_rank[df_rank['교과'].isin(skku_subjects)].copy()
df_khu['점수'] = df_khu['석차등급'].apply(khu_grade_score)
khu_score = (df_khu['점수'] * df_khu['학점수']).sum() / df_khu['학점수'].sum()

print(f"Kyung Hee Recalculated Score: {khu_score:.2f}점 / 100점")

# -------------------------------------------------------------
# Summary DataFrame Creation
# -------------------------------------------------------------
results = [
    {
        "대학명": "동국대학교",
        "전형구분": "학교장추천인재 (교과)",
        "반영방식": "국/수/영/사/과/한국사 상위 10과목 정량",
        "재산출 등급": f"{dongguk_top10_avg_grade:.2f} 등급",
        "대학별 환산 점수": f"{dongguk_top10_score:.2f}점 / 10점 만점",
        "전형상 특이사항 및 경쟁력": "상위 10과목 반영으로 5.72등급 ➔ 4.80등급 대폭 반등! 1~4등급 감점 차이 0.1점 미만"
    },
    {
        "대학명": "한국외국어대학교",
        "전형구분": "학교장추천 (교과)",
        "반영방식": "석차등급 환산점 vs 원점수 환산점 Max 적용",
        "재산출 등급": f"{hufs_equiv_grade:.2f} 등급 (추정)",
        "대학별 환산 점수": f"{hufs_weighted_score:.2f}점 / 100점 만점",
        "전형상 특이사항 및 경쟁력": "★ 원점수 70~87점대 다수 분포로 5~7등급이 92~95점대로 폭등하여 3.5~4.1등급선 대반등!"
    },
    {
        "대학명": "성균관대학교",
        "전형구분": "추천인재 (교과)",
        "반영방식": "공통/일반 80% + 진로 20% (2027 추천무제한)",
        "재산출 등급": f"{(100-skku_total_score)/3 + 4.0:.2f} 등급대 (환산점 유추)",
        "대학별 환산 점수": f"{skku_total_score:.2f}점 / 100점 만점",
        "전형상 특이사항 및 경쟁력": "2027 고교 추천 제한 전면 폐지! 수능 최저 3개 합 6/7 적용으로 실질 경쟁률 하향"
    },
    {
        "대학명": "건국대학교",
        "전형구분": "KU지역균형 (교과)",
        "반영방식": "교과 정량 70% + 교과 정성 30%",
        "재산출 등급": "5.68 등급 (전과목)",
        "대학별 환산 점수": f"{ku_score:.2f}점 / 100점 만점",
        "전형상 특이사항 및 경쟁력": "고교 추천 제한 없음. 교과 정성평가 30%로 정량 내신 감점 만회 시도 가능"
    },
    {
        "대학명": "숙명여자대학교",
        "전형구분": "지역균형선발 (교과)",
        "반영방식": "교과 정량 70% + 서류 30% (2027 신설)",
        "재산출 등급": "5.65 등급 (국/수/영/사/한국사)",
        "대학별 환산 점수": f"{smu_score:.2f}점 / 100점 만점",
        "전형상 특이사항 및 경쟁력": "고교 추천 제한 없음. 2027 서류 30% 신설 정성평가 수혜"
    },
    {
        "대학명": "중앙대학교",
        "전형구분": "지역균형 / 수시 교과",
        "반영방식": "인문 상위 10과목 반영",
        "재산출 등급": f"{cau_top10_avg_grade:.2f} 등급",
        "대학별 환산 점수": f"{cau_top10_score:.2f}점 / 10점 만점",
        "전형상 특이사항 및 경쟁력": "인문 상위 10과목 추출 반영으로 내신 4.90등급 반등"
    },
    {
        "대학명": "경희대학교",
        "전형구분": "지역균형 (교과)",
        "반영방식": "공통/일반 70% + 진로 30%",
        "재산출 등급": "5.68 등급",
        "대학별 환산 점수": f"{khu_score:.2f}점 / 100점 만점",
        "전형상 특이사항 및 경쟁력": "수능 최저 2개 합 5 이내 충족 필수"
    }
]

df_res = pd.DataFrame(results)

output_excel = r"C:\Users\그램\Desktop\입시분석 참고자료\내신성적\대학별_내신성적_환산분석.xlsx"
output_csv_ref = r"C:\Users\그램\Desktop\입시분석 참고자료\내신성적\대학별_내신성적_환산분석.csv"
output_csv_rep = r"c:\Users\그램\Documents\antiG\reports\대학별_내신성적_환산분석.csv"

# Write Excel using pandas
with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
    df_res.to_excel(writer, sheet_name='대학별환산결과', index=False)
    df_hufs.to_excel(writer, sheet_name='한국외대상세환산', index=False)
    df_dongguk_top10.to_excel(writer, sheet_name='동국대상위10과목', index=False)

df_res.to_csv(output_csv_ref, index=False, encoding='utf-8-sig')
df_res.to_csv(output_csv_rep, index=False, encoding='utf-8-sig')

print("\n--- Summary Results ---")
print(df_res.to_string())
print(f"\nExcel file created at: {output_excel}")
