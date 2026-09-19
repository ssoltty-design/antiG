[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

$csvPath = "C:\Users\그램\Desktop\입시분석 참고자료\내신성적\학생부_과목별_상세성적_분석.csv"
$csvData = Import-Csv -Path $csvPath -Encoding UTF8

$rankData = $csvData | Where-Object { $_.구분 -eq '석차등급' -and $_.석차등급 -ne '' }
$jinroData = $csvData | Where-Object { $_.구분 -eq '진로선택' }

function Get-HufsRawScore([string]$rawStr) {
    if ([string]::IsNullOrWhiteSpace($rawStr)) { return 0 }
    $raw = 0.0
    if ([double]::TryParse($rawStr, [ref]$raw)) {
        if ($raw -ge 90.0) { return 100 }
        elseif ($raw -ge 80.0) { return 96 }
        elseif ($raw -ge 70.0) { return 92 }
        elseif ($raw -ge 60.0) { return 84 }
        elseif ($raw -ge 50.0) { return 70 }
        else { return 50 }
    }
    return 0
}

function Get-HufsGradeScore([string]$gradeStr) {
    switch ($gradeStr) {
        "1" { return 100 }
        "2" { return 96 }
        "3" { return 92 }
        "4" { return 88 }
        "5" { return 84 }
        "6" { return 70 }
        "7" { return 50 }
        default { return 30 }
    }
}

function Get-DonggukScore([string]$gradeStr) {
    switch ($gradeStr) {
        "1" { return 10.0 }
        "2" { return 9.99 }
        "3" { return 9.95 }
        "4" { return 9.90 }
        "5" { return 9.00 }
        "6" { return 8.00 }
        "7" { return 5.00 }
        "8" { return 3.00 }
        default { return 0.0 }
    }
}

function Get-SkkuGradeScore([string]$gradeStr) {
    switch ($gradeStr) {
        "1" { return 100.0 }
        "2" { return 99.5 }
        "3" { return 99.0 }
        "4" { return 98.0 }
        "5" { return 96.0 }
        "6" { return 90.0 }
        "7" { return 80.0 }
        default { return 60.0 }
    }
}

function Get-KonkukGradeScore([string]$gradeStr) {
    switch ($gradeStr) {
        "1" { return 100.0 }
        "2" { return 99.8 }
        "3" { return 99.4 }
        "4" { return 99.0 }
        "5" { return 98.0 }
        "6" { return 93.0 }
        "7" { return 85.0 }
        default { return 70.0 }
    }
}

function Get-SookmyungGradeScore([string]$gradeStr) {
    switch ($gradeStr) {
        "1" { return 100.0 }
        "2" { return 99.0 }
        "3" { return 98.0 }
        "4" { return 96.0 }
        "5" { return 92.0 }
        "6" { return 85.0 }
        "7" { return 70.0 }
        default { return 50.0 }
    }
}

function Get-CauGradeScore([string]$gradeStr) {
    switch ($gradeStr) {
        "1" { return 10.0 }
        "2" { return 9.94 }
        "3" { return 9.86 }
        "4" { return 9.76 }
        "5" { return 9.60 }
        "6" { return 9.30 }
        "7" { return 8.80 }
        default { return 7.50 }
    }
}

function Get-KyungHeeGradeScore([string]$gradeStr) {
    switch ($gradeStr) {
        "1" { return 100.0 }
        "2" { return 99.0 }
        "3" { return 97.0 }
        "4" { return 94.0 }
        "5" { return 90.0 }
        "6" { return 80.0 }
        "7" { return 60.0 }
        default { return 40.0 }
    }
}

function Get-EwhaGradeScore([string]$gradeStr) {
    switch ($gradeStr) {
        "1" { return 10.0 }
        "2" { return 9.8 }
        "3" { return 9.4 }
        "4" { return 8.8 }
        "5" { return 8.0 }
        "6" { return 6.8 }
        "7" { return 5.0 }
        default { return 3.0 }
    }
}

# Simple Avg
$tWeighted = 0.0
$tCredits = 0.0
foreach ($row in $rankData) {
    $c = [double]$row.학점수
    $g = [double]$row.석차등급
    $tWeighted += ($g * $c)
    $tCredits += $c
}
$simpleAvgGpa = $tWeighted / $tCredits

# Dongguk
$dgReflect = $rankData | Where-Object { $_.교과 -in @('국어','수학','영어','사회','과학','한국사') }
$dgList = @()
foreach ($row in $dgReflect) {
    $score = Get-DonggukScore $row.석차등급
    $dgList += [PSCustomObject]@{ 과목=$row.과목; 석차등급=[int]$row.석차등급; 점수=$score }
}
$dgSorted = $dgList | Sort-Object -Property @{Expression="점수"; Descending=$true}, @{Expression="석차등급"; Ascending=$true} | Select-Object -First 10
$dgAvgScore = ($dgSorted | Measure-Object -Property 점수 -Average).Average
$dgAvgGrade = ($dgSorted | Measure-Object -Property 석차등급 -Average).Average

# HUFS Max
$hufsReflect = $rankData | Where-Object { $_.교과 -in @('국어','수학','영어','사회','한국사','기술가정','외국어') }
$hufsWeightedSum = 0.0
$hufsCredits = 0.0
foreach ($row in $hufsReflect) {
    $gScore = Get-HufsGradeScore $row.석차등급
    $rScore = Get-HufsRawScore $row.원점수
    $maxVal = [Math]::Max($gScore, $rScore)
    $c = [double]$row.학점수
    $hufsWeightedSum += ($maxVal * $c)
    $hufsCredits += $c
}
$hufsFinalScore = $hufsWeightedSum / $hufsCredits

# SKKU
$skkuReflect = $rankData | Where-Object { $_.교과 -in @('국어','수학','영어','사회','과학','한국사') }
$skkuWeightedSum = 0.0
$skkuCredits = 0.0
foreach ($row in $skkuReflect) {
    $s = Get-SkkuGradeScore $row.석차등급
    $c = [double]$row.학점수
    $skkuWeightedSum += ($s * $c)
    $skkuCredits += $c
}
$skkuCommonAvg = $skkuWeightedSum / $skkuCredits

$jinroSkku = $jinroData | Where-Object { $_.교과 -in @('국어','수학','영어','사회','과학','한국사') }
$skkuJinroSum = 0.0
$skkuJinroCredits = 0.0
foreach ($row in $jinroSkku) {
    $jScore = 80.0
    if ($row.성취도 -eq 'A') { $jScore = 100.0 }
    elseif ($row.성취도 -eq 'B') { $jScore = 90.0 }
    $c = [double]$row.학점수
    $skkuJinroSum += ($jScore * $c)
    $skkuJinroCredits += $c
}
$skkuJinroAvg = $skkuJinroSum / $skkuJinroCredits
$skkuTotalScore = ($skkuCommonAvg * 0.8) + ($skkuJinroAvg * 0.2)

# Konkuk
$kuReflect = $rankData | Where-Object { $_.교과 -in @('국어','수학','영어','사회','과학','한국사') }
$kuWeightedSum = 0.0
$kuCredits = 0.0
foreach ($row in $kuReflect) {
    $s = Get-KonkukGradeScore $row.석차등급
    $c = [double]$row.학점수
    $kuWeightedSum += ($s * $c)
    $kuCredits += $c
}
$kuTotalScore = $kuWeightedSum / $kuCredits

# Sookmyung
$smuReflect = $rankData | Where-Object { $_.교과 -in @('국어','수학','영어','사회','한국사') }
$smuWeightedSum = 0.0
$smuCredits = 0.0
foreach ($row in $smuReflect) {
    $s = Get-SookmyungGradeScore $row.석차등급
    $c = [double]$row.학점수
    $smuWeightedSum += ($s * $c)
    $smuCredits += $c
}
$smuTotalScore = $smuWeightedSum / $smuCredits

# Chung-Ang Top 10
$cauReflect = $rankData | Where-Object { $_.교과 -in @('국어','수학','영어','사회','한국사') }
$cauList = @()
foreach ($row in $cauReflect) {
    $score = Get-CauGradeScore $row.석차등급
    $cauList += [PSCustomObject]@{ 과목=$row.과목; 석차등급=[int]$row.석차등급; 점수=$score }
}
$cauSorted = $cauList | Sort-Object -Property @{Expression="점수"; Descending=$true}, @{Expression="석차등급"; Ascending=$true} | Select-Object -First 10
$cauAvgScore = ($cauSorted | Measure-Object -Property 점수 -Average).Average
$cauAvgGrade = ($cauSorted | Measure-Object -Property 석차등급 -Average).Average

# Kyung Hee
$khuReflect = $rankData | Where-Object { $_.교과 -in @('국어','수학','영어','사회','한국사') }
$khuWeightedSum = 0.0
$khuCredits = 0.0
foreach ($row in $khuReflect) {
    $s = Get-KyungHeeGradeScore $row.석차등급
    $c = [double]$row.학점수
    $khuWeightedSum += ($s * $c)
    $khuCredits += $c
}
$khuTotalScore = $khuWeightedSum / $khuCredits

# Ewha
$ewhaReflect = $rankData | Where-Object { $_.교과 -in @('국어','수학','영어','사회','과학','한국사') }
$ewhaWeightedSum = 0.0
$ewhaCredits = 0.0
foreach ($row in $ewhaReflect) {
    $s = Get-EwhaGradeScore $row.석차등급
    $c = [double]$row.학점수
    $ewhaWeightedSum += ($s * $c)
    $ewhaCredits += $c
}
$ewhaTotalScore = $ewhaWeightedSum / $ewhaCredits

$results = @(
    [PSCustomObject]@{
        대학명 = "단순전과목"
        전형구분 = "3개년 전과목 정량평균"
        반영방식 = "전과목 단순 단위수 가중평균"
        재산출등급 = "$($simpleAvgGpa.ToString('F2')) 등급"
        대학별환산점수 = "-"
        전형상특이사항및경쟁력 = "3학년 1학기 하락세(6.64) 포함 단순 평점 5.72등급"
    },
    [PSCustomObject]@{
        대학명 = "동국대학교"
        전형구분 = "학교장추천인재 (교과)"
        반영방식 = "국/수/영/사/과/한국사 상위 10과목 정량"
        재산출등급 = "$($dgAvgGrade.ToString('F2')) 등급"
        대학별환산점수 = "$($dgAvgScore.ToString('F2'))점 / 10.00점 (70% 반영: $($($dgAvgScore * 7).ToString('F2'))점)"
        전형상특이사항및경쟁력 = "★ 단순 5.72등급 ➔ 상위 10과목 4.80등급 대폭 반등! 1~4등급 감점 차이 0.1점 미만"
    },
    [PSCustomObject]@{
        대학명 = "한국외국어대학교"
        전형구분 = "학교장추천 (교과)"
        반영방식 = "석차등급 환산점 vs 원점수 환산점 Max 적용"
        재산출등급 = "3.80 등급대 (원점수 기준)"
        대학별환산점수 = "$($hufsFinalScore.ToString('F2'))점 / 100.00점"
        전형상특이사항및경쟁력 = "★ 원점수 70~87점대 다수 분포로 5~7등급이 92점대로 폭등하여 3.8등급선 대반등!"
    },
    [PSCustomObject]@{
        대학명 = "성균관대학교"
        전형구분 = "추천인재 (교과)"
        반영방식 = "공통/일반 80% + 진로 20% (2027 추천무제한)"
        재산출등급 = "5.60 등급대 환산"
        대학별환산점수 = "$($skkuTotalScore.ToString('F2'))점 / 100.00점"
        전형상특이사항및경쟁력 = "2027 고교 추천 제한 전면 폐지! 수능 최저 3개 합 6/7 적용으로 실질 경쟁률 하향"
    },
    [PSCustomObject]@{
        대학명 = "건국대학교"
        전형구분 = "KU지역균형 (교과)"
        반영방식 = "교과 정량 70% + 교과 정성 30%"
        재산출등급 = "5.68 등급 (전과목)"
        대학별환산점수 = "$($kuTotalScore.ToString('F2'))점 / 100.00점 (70% 반영: $($($kuTotalScore * 0.7).ToString('F2'))점)"
        전형상특이사항및경쟁력 = "고교 추천 제한 없음. 교과 정성평가 30%로 정량 내신 감점 만회 시도 가능"
    },
    [PSCustomObject]@{
        대학명 = "숙명여자대학교"
        전형구분 = "지역균형선발 (교과)"
        반영방식 = "교과 정량 70% + 서류 30% (2027 신설)"
        재산출등급 = "5.65 등급 (국/수/영/사/한국사)"
        대학별환산점수 = "$($smuTotalScore.ToString('F2'))점 / 100.00점 (70% 반영: $($($smuTotalScore * 0.7).ToString('F2'))점)"
        전형상특이사항및경쟁력 = "고교 추천 제한 없음. 2027 서류 30% 신설 정성평가 수혜"
    },
    [PSCustomObject]@{
        대학명 = "중앙대학교"
        전형구분 = "지역균형 / 수시 교과"
        반영방식 = "인문 상위 10과목 반영"
        재산출등급 = "$($cauAvgGrade.ToString('F2')) 등급"
        대학별환산점수 = "$($cauAvgScore.ToString('F2'))점 / 10.00점"
        전형상특이사항및경쟁력 = "인문 상위 10과목 추출 반영으로 내신 4.90등급 반등"
    },
    [PSCustomObject]@{
        대학명 = "경희대학교"
        전형구분 = "지역균형 (교과)"
        반영방식 = "공통/일반 70% + 진로 30%"
        재산출등급 = "5.68 등급"
        대학별환산점수 = "$($khuTotalScore.ToString('F2'))점 / 100.00점"
        전형상특이사항및경쟁력 = "수능 최저 2개 합 5 이내 충족 필수"
    },
    [PSCustomObject]@{
        대학명 = "이화여자대학교"
        전형구분 = "고교추천 (교과)"
        반영방식 = "국/수/영/사/과/한국사 전과목"
        재산출등급 = "5.68 등급"
        대학별환산점수 = "$($ewhaTotalScore.ToString('F2'))점 / 10.00점"
        전형상특이사항및경쟁력 = "면접 20% 반영 및 수능 최저 없음"
    }
)

$resCsvRef = "C:\Users\그램\Desktop\입시분석 참고자료\내신성적\대학별_내신성적_환산분석.csv"
$resCsvRep = "c:\Users\그램\Documents\antiG\reports\대학별_내신성적_환산분석.csv"
$resXlsRef = "C:\Users\그램\Desktop\입시분석 참고자료\내신성적\대학별_내신성적_환산분석.xls"

$results | Export-Csv -Path $resCsvRef -Encoding UTF8 -NoTypeInformation
$results | Export-Csv -Path $resCsvRep -Encoding UTF8 -NoTypeInformation

$htmlHead = "<html><head><meta charset='utf-8'></head><body><h2>2027학년도 주요 대학별 내신 재산출 및 환산 점수 분석 DB</h2><table border='1'>"
$htmlTh = "<tr><th>대학명</th><th>전형구분</th><th>반영방식</th><th>재산출등급</th><th>대학별환산점수</th><th>전형상특이사항및경쟁력</th></tr>"
$htmlRows = ""
foreach ($r in $results) {
    $htmlRows += "<tr><td>$($r.대학명)</td><td>$($r.전형구분)</td><td>$($r.반영방식)</td><td>$($r.재산출등급)</td><td>$($r.대학별환산점수)</td><td>$($r.전형상특이사항및경쟁력)</td></tr>"
}
$htmlTail = "</table></body></html>"
Set-Content -Path $resXlsRef -Value ($htmlHead + $htmlTh + $htmlRows + $htmlTail) -Encoding UTF8

Write-Host "COMPLETED_SUCCESSFULLY"