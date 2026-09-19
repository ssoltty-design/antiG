function Write-TextShare ($path, $content) {
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($content)
    $fs = New-Object System.IO.FileStream($path, [System.IO.FileMode]::Create, [System.IO.FileAccess]::Write, [System.IO.FileShare]::ReadWrite)
    $fs.Write($bytes, 0, $bytes.Length)
    $fs.Close()
}

$mRaw = [System.IO.File]::ReadAllText('scratch/johap_master_data.json', [System.Text.Encoding]::UTF8)
$mData = $mRaw | ConvertFrom-Json
$cRaw = [System.IO.File]::ReadAllText('scratch/johap_calendar_data.json', [System.Text.Encoding]::UTF8)
$cData = $cRaw | ConvertFrom-Json

$dDir = (Get-ChildItem '..\..\Desktop' | Where-Object { $_.Name -like '*입시분석*' } | Get-ChildItem | Where-Object { $_.Name -like '*2027*종합*' }).FullName
$wDir = (Get-Item 'reports').FullName

Write-Host "Desktop Dir: " $dDir
Write-Host "Workspace Dir: " $wDir

# Master CSV & XLS
$mData | Export-Csv -Path "$dDir\2027_학생부종합전형_통합DB.csv" -Encoding UTF8 -NoTypeInformation
$mData | Export-Csv -Path "$wDir\2027_학생부종합전형_통합DB.csv" -Encoding UTF8 -NoTypeInformation

$mTh = "<tr><th>대학명</th><th>전형명</th><th>전형구분</th><th>모집인원</th><th>지원자격</th><th>1단계</th><th>2단계</th><th>최저학력기준</th><th>면접고사일</th><th>면접유형</th><th>특이사항</th></tr>"
$mRows = ""
foreach ($r in $mData) {
    $mRows += "<tr><td>$($r.대학명)</td><td>$($r.전형명)</td><td>$($r.전형구분)</td><td>$($r.모집인원)</td><td>$($r.지원자격)</td><td>$($r.단계1)</td><td>$($r.단계2)</td><td>$($r.최저학력기준)</td><td>$($r.면접고사일)</td><td>$($r.면접유형)</td><td>$($r.특이사항)</td></tr>"
}
$mHtml = "<html><head><meta charset='utf-8'></head><body><h2>2027학년도 수도권 주요 대학 학생부 종합전형 통합 DB</h2><table border='1'>$mTh $mRows</table></body></html>"
Write-TextShare "$dDir\2027_학생부종합전형_통합DB.xls" $mHtml
Write-TextShare "$wDir\2027_학생부종합전형_통합DB.xls" $mHtml

# Calendar CSV & XLS
$cData | Export-Csv -Path "$dDir\2027_면접고사_날짜별_달력일정.csv" -Encoding UTF8 -NoTypeInformation
$cData | Export-Csv -Path "$wDir\2027_면접고사_날짜별_달력일정.csv" -Encoding UTF8 -NoTypeInformation

$cTh = "<tr><th>일자</th><th>요일</th><th>수능전후</th><th>대학명</th><th>전형명</th><th>계열/학과</th><th>면접유형</th><th>비고/전략</th></tr>"
$cRows = ""
foreach ($r in $cData) {
    $cRows += "<tr><td>$($r.일자)</td><td>$($r.요일)</td><td>$($r.수능전후)</td><td>$($r.대학명)</td><td>$($r.전형명)</td><td>$($r.계열_학과)</td><td>$($r.면접유형)</td><td>$($r.비고)</td></tr>"
}
$cHtml = "<html><head><meta charset='utf-8'></head><body><h2>2027학년도 대학별 면접고사 날짜별 달력 일정 DB</h2><table border='1'>$cTh $cRows</table></body></html>"
Write-TextShare "$dDir\2027_면접고사_날짜별_달력일정.xls" $cHtml
try {
    Write-TextShare "$wDir\2027_면접고사_날짜별_달력일정.xls" $cHtml
} catch {
    Write-Host "Workspace file locked, saved desktop file successfully."
}

Write-Host "DB_GENERATION_SUCCESSFUL"
