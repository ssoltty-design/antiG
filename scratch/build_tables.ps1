# PowerShell script to load JSON and generate CSV (UTF8 BOM) and XLS (HTML table format)

$desktopDir = "C:\Users\그램\Desktop\입시분석 참고자료\2027 종합전형"
$workspaceDir = "c:\Users\그램\Documents\antiG\reports"

if (-not (Test-Path $desktopDir)) { New-Item -ItemType Directory -Path $desktopDir -Force }
if (-not (Test-Path $workspaceDir)) { New-Item -ItemType Directory -Path $workspaceDir -Force }

# Read Master JSON
$masterJsonPath = "c:\Users\그램\Documents\antiG\scratch\johap_master_data.json"
$masterRaw = [System.IO.File]::ReadAllText($masterJsonPath, [System.Text.Encoding]::UTF8)
$masterData = $masterRaw | ConvertFrom-Json

# Read Calendar JSON
$calJsonPath = "c:\Users\그램\Documents\antiG\scratch\johap_calendar_data.json"
$calRaw = [System.IO.File]::ReadAllText($calJsonPath, [System.Text.Encoding]::UTF8)
$calData = $calRaw | ConvertFrom-Json

# 1. Export Master CSV & XLS
$masterCsvDesktop = Join-Path $desktopDir "2027_학생부종합전형_통합DB.csv"
$masterCsvWorkspace = Join-Path $workspaceDir "2027_학생부종합전형_통합DB.csv"
$masterXlsDesktop = Join-Path $desktopDir "2027_학생부종합전형_통합DB.xls"
$masterXlsWorkspace = Join-Path $workspaceDir "2027_학생부종합전형_통합DB.xls"

$masterData | Export-Csv -Path $masterCsvDesktop -Encoding UTF8 -NoTypeInformation
$masterData | Export-Csv -Path $masterCsvWorkspace -Encoding UTF8 -NoTypeInformation

$htmlHead = "<html><head><meta charset='utf-8'></head><body><h2>2027학년도 수도권 주요 대학 학생부 종합전형 통합 DB</h2><table border='1'>"
$htmlTh = "<tr><th>대학명</th><th>전형명</th><th>전형구분</th><th>모집인원</th><th>지원자격</th><th>1단계</th><th>2단계</th><th>최저학력기준</th><th>면접고사일</th><th>면접유형</th><th>특이사항</th></tr>"
$htmlRows = ""
foreach ($r in $masterData) {
    $htmlRows += "<tr><td>$($r.대학명)</td><td>$($r.전형명)</td><td>$($r.전형구분)</td><td>$($r.모집인원)</td><td>$($r.지원자격)</td><td>$($r.단계1)</td><td>$($r.단계2)</td><td>$($r.최저학력기준)</td><td>$($r.면접고사일)</td><td>$($r.면접유형)</td><td>$($r.특이사항)</td></tr>"
}
$htmlTail = "</table></body></html>"
Set-Content -Path $masterXlsDesktop -Value ($htmlHead + $htmlTh + $htmlRows + $htmlTail) -Encoding UTF8
Set-Content -Path $masterXlsWorkspace -Value ($htmlHead + $htmlTh + $htmlRows + $htmlTail) -Encoding UTF8


# 2. Export Calendar CSV & XLS
$calCsvDesktop = Join-Path $desktopDir "2027_면접고사_날짜별_달력일정.csv"
$calCsvWorkspace = Join-Path $workspaceDir "2027_면접고사_날짜별_달력일정.csv"
$calXlsDesktop = Join-Path $desktopDir "2027_면접고사_날짜별_달력일정.xls"
$calXlsWorkspace = Join-Path $workspaceDir "2027_면접고사_날짜별_달력일정.xls"

$calData | Export-Csv -Path $calCsvDesktop -Encoding UTF8 -NoTypeInformation
$calData | Export-Csv -Path $calCsvWorkspace -Encoding UTF8 -NoTypeInformation

$htmlCalHead = "<html><head><meta charset='utf-8'></head><body><h2>2027학년도 대학별 면접고사 날짜별 달력 일정 DB</h2><table border='1'>"
$htmlCalTh = "<tr><th>일자</th><th>요일</th><th>수능전후</th><th>대학명</th><th>전형명</th><th>계열/학과</th><th>면접유형</th><th>비고/전략</th></tr>"
$htmlCalRows = ""
foreach ($r in $calData) {
    $htmlCalRows += "<tr><td>$($r.일자)</td><td>$($r.요일)</td><td>$($r.수능전후)</td><td>$($r.대학명)</td><td>$($r.전형명)</td><td>$($r.계열_학과)</td><td>$($r.면접유형)</td><td>$($r.비고)</td></tr>"
}
$htmlCalTail = "</table></body></html>"
Set-Content -Path $calXlsDesktop -Value ($htmlCalHead + $htmlCalTh + $htmlCalRows + $htmlCalTail) -Encoding UTF8
Set-Content -Path $calXlsWorkspace -Value ($htmlCalHead + $htmlCalTh + $htmlCalRows + $htmlCalTail) -Encoding UTF8

Write-Host "SUCCESSFULLY_GENERATED_CSV_AND_XLS_FILES"
