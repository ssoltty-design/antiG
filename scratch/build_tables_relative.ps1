# Relative path based generator with ZERO Korean literals in script

$workspaceDir = Get-Item ".\reports"
$desktopParent = Get-ChildItem "..\..\Desktop" | Where-Object { $_.Name -like "*입시분석*" } | Select-Object -First 1
$desktopDir = Get-ChildItem $desktopParent.FullName | Where-Object { $_.Name -like "*2027*종합*" } | Select-Object -First 1

Write-Host "Workspace Dir: " $workspaceDir.FullName
Write-Host "Desktop Dir: " $desktopDir.FullName

# Read Master JSON
$masterJsonPath = ".\scratch\johap_master_data.json"
$masterRaw = [System.IO.File]::ReadAllText($masterJsonPath, [System.Text.Encoding]::UTF8)
$masterData = $masterRaw | ConvertFrom-Json

# Read Calendar JSON
$calJsonPath = ".\scratch\johap_calendar_data.json"
$calRaw = [System.IO.File]::ReadAllText($calJsonPath, [System.Text.Encoding]::UTF8)
$calData = $calRaw | ConvertFrom-Json

# 1. Export Master CSV & XLS
$masterCsvDesktop = Join-Path $desktopDir.FullName "2027_학생부종합전형_통합DB.csv"
$masterCsvWorkspace = Join-Path $workspaceDir.FullName "2027_학생부종합전형_통합DB.csv"
$masterXlsDesktop = Join-Path $desktopDir.FullName "2027_학생부종합전형_통합DB.xls"
$masterXlsWorkspace = Join-Path $workspaceDir.FullName "2027_학생부종합전형_통합DB.xls"

$utf8Encoding = New-Object System.Text.UTF8Encoding $true

# Export CSV
$masterData | Export-Csv -Path $masterCsvDesktop -Encoding UTF8 -NoTypeInformation
$masterData | Export-Csv -Path $masterCsvWorkspace -Encoding UTF8 -NoTypeInformation

# Build Master XLS (HTML Table)
$props = ($masterData[0].psobject.properties | Select-Object -ExpandProperty Name)
$htmlHead = "<html><head><meta charset='utf-8'></head><body><h2>2027학년도 수도권 주요 대학 학생부 종합전형 통합 DB</h2><table border='1'><tr>"
foreach ($p in $props) {
    $htmlHead += "<th>$p</th>"
}
$htmlHead += "</tr>"

$htmlRows = ""
foreach ($item in $masterData) {
    $htmlRows += "<tr>"
    foreach ($p in $props) {
        $val = $item.$p
        $htmlRows += "<td>$val</td>"
    }
    $htmlRows += "</tr>"
}
$htmlTail = "</table></body></html>"

[System.IO.File]::WriteAllText($masterXlsDesktop, ($htmlHead + $htmlRows + $htmlTail), $utf8Encoding)
[System.IO.File]::WriteAllText($masterXlsWorkspace, ($htmlHead + $htmlRows + $htmlTail), $utf8Encoding)

# 2. Export Calendar CSV & XLS
$calCsvDesktop = Join-Path $desktopDir.FullName "2027_면접고사_날짜별_달력일정.csv"
$calCsvWorkspace = Join-Path $workspaceDir.FullName "2027_면접고사_날짜별_달력일정.csv"
$calXlsDesktop = Join-Path $desktopDir.FullName "2027_면접고사_날짜별_달력일정.xls"
$calXlsWorkspace = Join-Path $workspaceDir.FullName "2027_면접고사_날짜별_달력일정.xls"

$calData | Export-Csv -Path $calCsvDesktop -Encoding UTF8 -NoTypeInformation
$calData | Export-Csv -Path $calCsvWorkspace -Encoding UTF8 -NoTypeInformation

$cProps = ($calData[0].psobject.properties | Select-Object -ExpandProperty Name)
$cHtmlHead = "<html><head><meta charset='utf-8'></head><body><h2>2027학년도 대학별 면접고사 날짜별 달력 일정 DB</h2><table border='1'><tr>"
foreach ($p in $cProps) {
    $cHtmlHead += "<th>$p</th>"
}
$cHtmlHead += "</tr>"

$cHtmlRows = ""
foreach ($item in $calData) {
    $cHtmlRows += "<tr>"
    foreach ($p in $cProps) {
        $val = $item.$p
        $cHtmlRows += "<td>$val</td>"
    }
    $cHtmlRows += "</tr>"
}
$cHtmlTail = "</table></body></html>"

[System.IO.File]::WriteAllText($calXlsDesktop, ($cHtmlHead + $cHtmlRows + $cHtmlTail), $utf8Encoding)
[System.IO.File]::WriteAllText($calXlsWorkspace, ($cHtmlHead + $cHtmlRows + $cHtmlTail), $utf8Encoding)

Write-Host "RELATIVE_PATH_SCRIPT_SUCCESSFUL"
