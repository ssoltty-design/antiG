import pandas as pd
import os

gpa_data = [
    {"구분": "전학년 평균등급", "학년_학기": "전학년 (3개년)", "평균등급": 5.72, "이수과목_단위": "진로선택 9과목", "비고": "전교과 단순 평균등급"},
    {"구분": "1학년 평균등급", "학년_학기": "1학년 (1학기+2학기)", "평균등급": 5.40, "이수과목_단위": "입력완료", "비고": "1학년 전교과 평균"},
    {"구분": "2학년 평균등급", "학년_학기": "2학년 (1학기+2학기)", "평균등급": 5.86, "이수과목_단위": "입력완료", "비고": "2학년 전교과 평균"},
    {"구분": "3학년 평균등급", "학년_학기": "3학년 (1학기)", "평균등급": 6.64, "이수과목_단위": "1학기 입력 / 2학기 미입력", "비고": "수시 반영 3학년 1학기 내신"},
    {"구분": "봉사활동", "학년_학기": "3개년 누적", "평균등급": None, "이수과목_단위": "총 16시간", "비고": "수시 비교과 봉사"},
    {"구분": "출결사항", "학년_학기": "3개년 누적", "평균등급": None, "이수과목_단위": "총 결석 1일", "비고": "수시 비교과 출결"},
    {"구분": "공동교육과정", "학년_학기": "3개년 누적", "평균등급": None, "이수과목_단위": "이수 내역 없음", "비고": "공동교육과정 미이수"}
]

df = pd.DataFrame(gpa_data)

paths = [
    r"C:\Users\그램\Desktop\입시분석 참고자료\내신성적",
    r"c:\Users\그램\Documents\antiG\reports"
]

for p in paths:
    os.makedirs(p, exist_ok=True)
    csv_path = os.path.join(p, "학생부_내신성적_분석.csv")
    xls_path = os.path.join(p, "학생부_내신성적_분석.xls")
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    df.to_excel(xls_path, index=False)
    print(f"Saved to {csv_path} and {xls_path}")

print("GPA Data Generation Complete!")
