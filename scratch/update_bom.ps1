$utf8 = [System.Text.Encoding]::UTF8

$p1 = 'C:\Users\그램\Desktop\입시분석 참고자료\논술일정표\2027_수시_논술전형_통합DB.csv'
$p2 = 'C:\Users\그램\Desktop\입시분석 참고자료\논술일정표\2027_수시_논술전형_통합DB.xls'
$p3 = 'C:\Users\그램\Desktop\입시분석 참고자료\논술일정표\2027_논술고사_날짜별_달력일정.csv'
$p4 = 'C:\Users\그램\Desktop\입시분석 참고자료\논술일정표\2027_논술고사_날짜별_달력일정.xls'
$p5 = 'C:\Users\그램\Desktop\입시분석 참고자료\2027 종합전형\2027_수시_논술전형_통합DB.csv'
$p6 = 'C:\Users\그램\Desktop\입시분석 참고자료\2027 종합전형\2027_수시_논술전형_통합DB.xls'
$p7 = 'C:\Users\그램\Desktop\입시분석 참고자료\2027 종합전형\2027_논술고사_날짜별_달력일정.csv'
$p8 = 'C:\Users\그램\Desktop\입시분석 참고자료\2027 종합전형\2027_논술고사_날짜별_달력일정.xls'

$lines = [System.IO.File]::ReadAllLines($p1, $utf8)

$out = @()
foreach ($l in $lines) {
    if ($l -like "대학명,전형명,*") {
        $out += $l.Replace("대학명,전형명,", "대학명,전형명,원서접수 마감일시,")
    } elseif ($l -like "고려대,*") {
        $out += $l.Replace("고려대,논술전형,", "고려대,논술전형,2026-09-09 17:00,")
    } elseif ($l -like "연세대(서울),*") {
        $out += $l.Replace("연세대(서울),논술전형,", "연세대(서울),논술전형,2026-09-10 17:00,")
    } elseif ($l -like "이화여대,*") {
        $out += $l.Replace("이화여대,논술전형,", "이화여대,논술전형,2026-09-10 17:00,")
    } elseif ($l -like "건국대,*") {
        $out += $l.Replace("건국대,KU논술우수자,", "건국대,KU논술우수자,2026-09-11 17:00,")
    } elseif ($l -like "동국대,*") {
        $out += $l.Replace("동국대,논술전형,", "동국대,논술전형,2026-09-11 17:00,")
    } elseif ($l -like "한국외대(T1/T2),*") {
        $out += $l.Replace("한국외대(T1/T2),논술전형,", "한국외대(T1/T2),논술전형,2026-09-11 17:00,")
    } elseif ($l -like "한국외대(T3/T4),*") {
        $out += $l.Replace("한국외대(T3/T4),논술전형,", "한국외대(T3/T4),논술전형,2026-09-11 17:00,")
    } elseif ($l -like "광운대,*") {
        $out += $l.Replace("광운대,논술우수자,", "광운대,논술우수자,2026-09-11 17:00,")
    } elseif ($l -like "숙명여대,*") {
        $out += $l.Replace("숙명여대,논술우수자,", "숙명여대,논술우수자,2026-09-11 17:00,")
    } elseif ($l -like "연세대(미래),*") {
        $out += $l.Replace("연세대(미래),창의인재,", "연세대(미래),창의인재,2026-09-11 17:00,")
    } elseif ($l -like "경기대,*") {
        $out += $l.Replace("경기대,논술우수자,", "경기대,논술우수자,2026-09-11 17:00,")
    } else {
        # All other universities 9/11 18:00
        $parts = $l.Split(',')
        if ($parts.Count -ge 2) {
            $u = $parts[0]
            $j = $parts[1]
            $target = "$u,$j,"
            $repl = "$u,$j,2026-09-11 18:00,"
            $out += $l.Replace($target, $repl)
        } else {
            $out += $l
        }
    }
}

$allTargets = @($p1, $p2, $p3, $p4, $p5, $p6, $p7, $p8)
foreach ($t in $allTargets) {
    [System.IO.File]::WriteAllLines($t, $out, $utf8)
}

Write-Host "Success updating CSV files!"
