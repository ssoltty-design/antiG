# PowerShell script to load JSON and generate CSV (UTF8 BOM) and XLS (HTML table format)

$desktopDir = "C:\Users\洹몃옩\Desktop\?낆떆遺꾩꽍 李멸퀬?먮즺\2027 醫낇빀?꾪삎"
$workspaceDir = "c:\Users\洹몃옩\Documents\antiG\reports"

if (-not (Test-Path $desktopDir)) { New-Item -ItemType Directory -Path $desktopDir -Force }
if (-not (Test-Path $workspaceDir)) { New-Item -ItemType Directory -Path $workspaceDir -Force }

# Read Master JSON
$masterJsonPath = "c:\Users\洹몃옩\Documents\antiG\scratch\johap_master_data.json"
$masterRaw = [System.IO.File]::ReadAllText($masterJsonPath, [System.Text.Encoding]::UTF8)
$masterData = $masterRaw | ConvertFrom-Json

# Read Calendar JSON
$calJsonPath = "c:\Users\洹몃옩\Documents\antiG\scratch\johap_calendar_data.json"
$calRaw = [System.IO.File]::ReadAllText($calJsonPath, [System.Text.Encoding]::UTF8)
$calData = $calRaw | ConvertFrom-Json

# 1. Export Master CSV & XLS
$masterCsvDesktop = Join-Path $desktopDir "2027_?숈깮遺醫낇빀?꾪삎_?듯빀DB.csv"
$masterCsvWorkspace = Join-Path $workspaceDir "2027_?숈깮遺醫낇빀?꾪삎_?듯빀DB.csv"
$masterXlsDesktop = Join-Path $desktopDir "2027_?숈깮遺醫낇빀?꾪삎_?듯빀DB.xls"
$masterXlsWorkspace = Join-Path $workspaceDir "2027_?숈깮遺醫낇빀?꾪삎_?듯빀DB.xls"

$masterData | Export-Csv -Path $masterCsvDesktop -Encoding UTF8 -NoTypeInformation
$masterData | Export-Csv -Path $masterCsvWorkspace -Encoding UTF8 -NoTypeInformation

$htmlHead = "<html><head><meta charset='utf-8'></head><body><h2>2027?숇뀈???섎룄沅?二쇱슂 ????숈깮遺 醫낇빀?꾪삎 ?듯빀 DB</h2><table border='1'>"
$htmlTh = "<tr><th>??숇챸</th><th>?꾪삎紐?/th><th>?꾪삎援щ텇</th><th>紐⑥쭛?몄썝</th><th>吏?먯옄寃?/th><th>1?④퀎</th><th>2?④퀎</th><th>理쒖??숇젰湲곗?</th><th>硫댁젒怨좎궗??/th><th>硫댁젒?좏삎</th><th>?뱀씠?ы빆</th></tr>"
$htmlRows = ""
foreach ($r in $masterData) {
    $htmlRows += "<tr><td>$($r.??숇챸)</td><td>$($r.?꾪삎紐?</td><td>$($r.?꾪삎援щ텇)</td><td>$($r.紐⑥쭛?몄썝)</td><td>$($r.吏?먯옄寃?</td><td>$($r.?④퀎1)</td><td>$($r.?④퀎2)</td><td>$($r.理쒖??숇젰湲곗?)</td><td>$($r.硫댁젒怨좎궗??</td><td>$($r.硫댁젒?좏삎)</td><td>$($r.?뱀씠?ы빆)</td></tr>"
}
$htmlTail = "</table></body></html>"
Set-Content -Path $masterXlsDesktop -Value ($htmlHead + $htmlTh + $htmlRows + $htmlTail) -Encoding UTF8
Set-Content -Path $masterXlsWorkspace -Value ($htmlHead + $htmlTh + $htmlRows + $htmlTail) -Encoding UTF8


# 2. Export Calendar CSV & XLS
$calCsvDesktop = Join-Path $desktopDir "2027_硫댁젒怨좎궗_?좎쭨蹂??щ젰?쇱젙.csv"
$calCsvWorkspace = Join-Path $workspaceDir "2027_硫댁젒怨좎궗_?좎쭨蹂??щ젰?쇱젙.csv"
$calXlsDesktop = Join-Path $desktopDir "2027_硫댁젒怨좎궗_?좎쭨蹂??щ젰?쇱젙.xls"
$calXlsWorkspace = Join-Path $workspaceDir "2027_硫댁젒怨좎궗_?좎쭨蹂??щ젰?쇱젙.xls"

$calData | Export-Csv -Path $calCsvDesktop -Encoding UTF8 -NoTypeInformation
$calData | Export-Csv -Path $calCsvWorkspace -Encoding UTF8 -NoTypeInformation

$htmlCalHead = "<html><head><meta charset='utf-8'></head><body><h2>2027?숇뀈????숇퀎 硫댁젒怨좎궗 ?좎쭨蹂??щ젰 ?쇱젙 DB</h2><table border='1'>"
$htmlCalTh = "<tr><th>?쇱옄</th><th>?붿씪</th><th>?섎뒫?꾪썑</th><th>??숇챸</th><th>?꾪삎紐?/th><th>怨꾩뿴/?숆낵</th><th>硫댁젒?좏삎</th><th>鍮꾧퀬/?꾨왂</th></tr>"
$htmlCalRows = ""
foreach ($r in $calData) {
    $htmlCalRows += "<tr><td>$($r.?쇱옄)</td><td>$($r.?붿씪)</td><td>$($r.?섎뒫?꾪썑)</td><td>$($r.??숇챸)</td><td>$($r.?꾪삎紐?</td><td>$($r.怨꾩뿴_?숆낵)</td><td>$($r.硫댁젒?좏삎)</td><td>$($r.鍮꾧퀬)</td></tr>"
}
$htmlCalTail = "</table></body></html>"
Set-Content -Path $calXlsDesktop -Value ($htmlCalHead + $htmlCalTh + $htmlCalRows + $htmlCalTail) -Encoding UTF8
Set-Content -Path $calXlsWorkspace -Value ($htmlCalHead + $htmlCalTh + $htmlCalRows + $htmlCalTail) -Encoding UTF8

Write-Host "SUCCESSFULLY_GENERATED_CSV_AND_XLS_FILES"

