# -*- coding: utf-8 -*-
import os
import shutil

workspace_reports = u"C:\\Users\\그램\\Documents\\antiG\\reports"
desktop_root = u"C:\\Users\\그램\\Desktop\\입시분석 참고자료"

# Directories to create
dirs_to_create = [
    os.path.join(workspace_reports, u"final"),
    os.path.join(workspace_reports, u"archive_history"),
    os.path.join(workspace_reports, u"references"),
    os.path.join(workspace_reports, u"databases"),
    os.path.join(desktop_root, u"00_최종보고서_및_달력")
]

for d in dirs_to_create:
    if not os.path.exists(d):
        os.makedirs(d)

# Final Reports Mapping
final_files_src = {
    u"01_2027_수시_통합_지원전략_보고서.html": os.path.join(workspace_reports, u"2027_jinseon_hybrid_johap_nonsul_strategy.html"),
    u"02_2027_수시_통합_월달력_일정표.html": os.path.join(workspace_reports, u"2027_수시_통합_월달력_일정표.html"),
    u"03_2027_면접고사_월달력_일정표.html": os.path.join(workspace_reports, u"2027_면접고사_월달력_일정표.html"),
    u"04_UNIST_경영계열_수시진단_보고서.html": os.path.join(workspace_reports, u"unist_business_diagnosis_report.html")
}

# 1. Copy to antiG/reports/final & Desktop/00_최종보고서_및_달력
for target_name, src_path in final_files_src.items():
    if os.path.exists(src_path):
        dest_workspace = os.path.join(workspace_reports, u"final", target_name)
        dest_desktop = os.path.join(desktop_root, u"00_최종보고서_및_달력", target_name)
        shutil.copy2(src_path, dest_workspace)
        shutil.copy2(src_path, dest_desktop)

# 2. Archive History Files
archive_files = [
    u"2027_jinseon_no_essay_strategy.html",
    u"2027_jinseon_johap_strategy.html",
    u"2027_jinseon_hybrid_strategy.html",
    u"admission_report.html"
]

for af in archive_files:
    src_p = os.path.join(workspace_reports, af)
    if os.path.exists(src_p):
        dest_p = os.path.join(workspace_reports, u"archive_history", af)
        shutil.move(src_p, dest_p)

# 3. References Files (MD)
reference_files = [
    u"2027_논술전형_날짜별_일정_참고자료.md",
    u"2027_종합전형_날짜별_면접일정_참고자료.md",
    u"admission_summary.md",
    u"admission_folder_structure.md"
]

for rf in reference_files:
    src_p = os.path.join(workspace_reports, rf)
    if os.path.exists(src_p):
        dest_p = os.path.join(workspace_reports, u"references", rf)
        shutil.copy2(src_p, dest_p)  # keep copy in references

# 4. Database Files (CSV/XLS)
database_files = [
    u"2027_univ_minimum_cutoffs.csv",
    u"2027_univ_minimum_cutoffs.xls",
    u"2027_대학별_수능최저학력기준_분석.csv",
    u"2027_대학별_수능최저학력기준_분석.xls",
    u"2027_면접고사_날짜별_달력일정.csv",
    u"2027_면접고사_날짜별_달력일정.xls",
    u"2027_학생부종합전형_통합DB.csv",
    u"2027_학생부종합전형_통합DB.xls",
    u"대학별_내신성적_환산분석.csv",
    u"모의고사_성적_추이_분석.csv",
    u"모의고사_성적_추이_분석.xls",
    u"학생부_과목별_상세성적_분석.csv",
    u"학생부_내신성적_분석.csv"
]

for df in database_files:
    src_p = os.path.join(workspace_reports, df)
    if os.path.exists(src_p):
        dest_p = os.path.join(workspace_reports, u"databases", df)
        shutil.move(src_p, dest_p)

print "SUCCESSFULLY_REORGANIZED_FILES"
