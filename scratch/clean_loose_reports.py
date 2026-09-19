# -*- coding: utf-8 -*-
import os

workspace_reports = u"C:\\Users\\그램\\Documents\\antiG\\reports"

loose_files_to_remove = [
    u"2027_jinseon_hybrid_johap_nonsul_strategy.html",
    u"2027_수시_통합_월달력_일정표.html",
    u"2027_면접고사_월달력_일정표.html",
    u"unist_business_diagnosis_report.html",
    u"2027_논술전형_날짜별_일정_참고자료.md",
    u"2027_종합전형_날짜별_면접일정_참고자료.md",
    u"admission_summary.md",
    u"admission_folder_structure.md"
]

for lf in loose_files_to_remove:
    p = os.path.join(workspace_reports, lf)
    if os.path.exists(p):
        os.remove(p)

print "CLEANED_LOOSE_REPORTS_SUCCESSFULLY"
