$data = @(
    [PSCustomObject]@{ Date="2026-10-04"; Univ="홍익대(서울)"; Track="논술전형(자연/인문)"; Time="10:00 / 15:00"; MinStat="2개 합 5"; MinDetail="국,수,영,탐(1) 중 2개 합 5, 史4"; QuotaDetail="자전38, 경영48, 법학24, 경제8 등"; Ratio="논술90+교과10"; Note="수능 전 논술" },
    [PSCustomObject]@{ Date="2026-10-04"; Univ="성신여대"; Track="논술우수자"; Time="10:00 / 14:00"; MinStat="2개 합 7"; MinDetail="국,수,영,탐(1) 중 2개 합 7"; QuotaDetail="경영6, 법학8, 정외3, 사복5 등"; Ratio="논술100"; Note="수능 전 논술" },
    [PSCustomObject]@{ Date="2026-10-10"; Univ="연세대(서울)"; Track="논술전형"; Time="15:30~17:30"; MinStat="최저 無"; MinDetail="수능 최저 미적용"; QuotaDetail="경영15, 경제5, 정외6, 자유12 등"; Ratio="논술100"; Note="★ 수능 전 / 논술100 / 수리+영어제시문" },
    [PSCustomObject]@{ Date="2026-10-11"; Univ="중앙대(창의형)"; Track="창의형논술"; Time="10:00~12:00"; MinStat="최저 無"; MinDetail="수능 최저 미적용 (고3 현역만 지원)"; QuotaDetail="경영18, 경제4, 영문4, 미커4, 심리4 등"; Ratio="논술70+교과20+출결10"; Note="★ 수능 전 / 고3현역만 / 누락 보정항목" },
    [PSCustomObject]@{ Date="2026-10-11"; Univ="가톨릭대"; Track="논술전형"; Time="15:00~16:30"; MinStat="최저 無"; MinDetail="수능 최저 미적용"; QuotaDetail="경영5, 회계5, 국제5, 법학4 등"; Ratio="논술100"; Note="수능 전 논술" },
    [PSCustomObject]@{ Date="2026-10-11"; Univ="한국항공대"; Track="논술우수자"; Time="15:00~16:30"; MinStat="2개 합 6"; MinDetail="국,수,영,탐(1) 중 2개 합 6"; QuotaDetail="항공경영19, 자전7"; Ratio="논술100"; Note="수능 전 논술" },
    [PSCustomObject]@{ Date="2026-10-16"; Univ="연세대(미래)"; Track="창의인재논술"; Time="시간 미정"; MinStat="최저 無"; MinDetail="수능 최저 미적용"; QuotaDetail="자율융합계열 87"; Ratio="논술90+교과10"; Note="수능 전 논술" },
    [PSCustomObject]@{ Date="2026-10-18"; Univ="단국대"; Track="논술우수자"; Time="09:30 / 15:00"; MinStat="최저 無"; MinDetail="수능 최저 미적용"; QuotaDetail="경영29, 퇴계혁신20, 법학10, 경제10 등"; Ratio="논술90+교과10"; Note="수능 전 논술" },
    [PSCustomObject]@{ Date="2026-10-30"; Univ="상명대"; Track="약술형논술"; Time="시간 미정"; MinStat="최저 無"; MinDetail="수능 최저 미적용 (60분 약술)"; QuotaDetail="경영5, 자전11, 행정4 등"; Ratio="논술90+교과10"; Note="★ 약술형 논술 / 수능 전" },
    
    [PSCustomObject]@{ Date="2026-11-21"; Univ="건국대"; Track="KU논술우수자"; Time="09:20~11:00"; MinStat="2개 합 5"; MinDetail="국,수,영,탐(1) 중 2개 합 5, 史5"; QuotaDetail="KU자전65, 경영15, 무역7, 미커6 등"; Ratio="논술100"; Note="수능 후 1주차" },
    [PSCustomObject]@{ Date="2026-11-21"; Univ="숭실대"; Track="논술우수자"; Time="15:00~16:40"; MinStat="2개 합 6"; MinDetail="국,수,영,탐(1) 중 2개 합 6"; QuotaDetail="경영16, 글통10, 경제5, 행정6 등"; Ratio="논술90+교과10"; Note="수능 후 1주차" },
    [PSCustomObject]@{ Date="2026-11-21"; Univ="서울여대"; Track="논술우수자"; Time="10:00~11:30"; MinStat="최저 無"; MinDetail="수능 최저 미적용"; QuotaDetail="자유전공 80"; Ratio="논술80+교과20"; Note="수능 후 1주차" },
    [PSCustomObject]@{ Date="2026-11-21"; Univ="성균관대"; Track="논술우수자"; Time="08:30 / 13:00"; MinStat="3개 합 6"; MinDetail="국,수,영,탐(평) 중 3개 합 6 (글로벌 3개 합 5)"; QuotaDetail="인문계열38, 사회계열40, 경영20, 글경10 등"; Ratio="논술100"; Note="★ 수능 후 1주차 / 최저 3합6" },
    [PSCustomObject]@{ Date="2026-11-22"; Univ="고려대"; Track="논술전형"; Time="08:30 입실"; MinStat="4개 합 8"; MinDetail="국,수,영,탐(1) 중 4개 합 8, 史4"; QuotaDetail="경영12, 경제11, 자전15, 통계7, 미디어6 등"; Ratio="논술100"; Note="★ 수능 후 1주차 / 최저 4합8 고난도" },
    [PSCustomObject]@{ Date="2026-11-22"; Univ="서강대"; Track="논술전형"; Time="16:00 / 19:00"; MinStat="3개 합 7"; MinDetail="국,수,영,탐(1) 중 3개 합 7, 史4"; QuotaDetail="경영38, 경제21, 사과13, 인문15 등"; Ratio="논술100"; Note="★ 수능 후 1주차 / 논술100" },
    [PSCustomObject]@{ Date="2026-11-22"; Univ="경희대"; Track="논술우수자"; Time="15:00~17:00"; MinStat="2개 합 5"; MinDetail="국,수,영,탐(평) 중 2개 합 5, 史5"; QuotaDetail="경영회계27, 자전8, 경제7, 무역7 등"; Ratio="논술100"; Note="수능 후 1주차" },
    [PSCustomObject]@{ Date="2026-11-22"; Univ="숙명여대"; Track="논술우수자"; Time="10:00~11:40"; MinStat="2개 합 5"; MinDetail="국,수,영,탐(1) 중 2개 합 5"; QuotaDetail="한국어문12, 중문12, 영문11, 아동9 등"; Ratio="논술90+교과10"; Note="수능 후 1주차" },
    [PSCustomObject]@{ Date="2026-11-22"; Univ="동국대"; Track="논술전형"; Time="13:00 / 16:30"; MinStat="2개 합 5 (경찰 2합4)"; MinDetail="국,수,영,탐(1) 중 2개 합 5, 史4"; QuotaDetail="경영37, 국통12, 정외6, 행정6, 경찰13 등"; Ratio="논술70+교과20+출결10"; Note="★ 수능 후 1주차 / 상위10과목 환산" },
    [PSCustomObject]@{ Date="2026-11-22"; Univ="홍익대(세종)"; Track="논술전형"; Time="시간 미정"; MinStat="1개 4등급"; MinDetail="국,수,영,탐(1) 중 1개 4등급"; QuotaDetail="자전31, 상경30, 광고14"; Ratio="논술90+교과10"; Note="세종캠퍼스 시험" },
    [PSCustomObject]@{ Date="2026-11-22"; Univ="수원대"; Track="약술형논술"; Time="시간 미정"; MinStat="최저 無"; MinDetail="수능 최저 미적용 (80분 약술)"; QuotaDetail="인문사회융합 70, 경영공학 63"; Ratio="논술80+교과20"; Note="약술형 논술" },
    [PSCustomObject]@{ Date="2026-11-27"; Univ="경기대"; Track="논술우수자"; Time="시간 미정"; MinStat="최저 無"; MinDetail="수능 최저 미적용"; QuotaDetail="자전(수원) 93, 자전(서울) 41"; Ratio="논술90+교과10"; Note="수능 후 2주차 금요일" },
    [PSCustomObject]@{ Date="2026-11-28"; Univ="이화여대"; Track="논술전형"; Time="08:30 / 14:20"; MinStat="2개 합 5"; MinDetail="국어 포함 2개 합 5 (스크랜튼 3개 합 5)"; QuotaDetail="경영19, 경제10, 스크랜튼13, 인문1 등"; Ratio="논술100"; Note="★ 수능 후 2주차 / 논술100" },
    [PSCustomObject]@{ Date="2026-11-28"; Univ="동덕여대"; Track="약술형논술"; Time="10:00 / 14:30"; MinStat="2개 합 6"; MinDetail="국,수,영,탐(1) 중 2개 합 6"; QuotaDetail="경영40, 커뮤11, 영어12, 중문11 등"; Ratio="논술100"; Note="약술형 논술" },
    [PSCustomObject]@{ Date="2026-11-28"; Univ="한국외대"; Track="논술전형(T1/T2)"; Time="10:00 / 15:00"; MinStat="2개 합 4"; MinDetail="국,수,영,탐(1) 중 2개 합 4 (글로벌 2합6)"; QuotaDetail="자전(서울)24, 경제11, 미디어10, 정외8 등"; Ratio="논술100"; Note="★ 수능 후 2주차 / 영어제시문(T1)" },
    [PSCustomObject]@{ Date="2026-11-28"; Univ="한양대"; Track="논술전형"; Time="09:30 / 13:30 / 17:00"; MinStat="3개 합 7"; MinDetail="국,수,영,탐(1) 중 3개 합 7"; QuotaDetail="인터컬리지15, 경영12, 경제금융9 등"; Ratio="논술100"; Note="★ 수능 후 2주차 / 논술100" },
    [PSCustomObject]@{ Date="2026-11-28"; Univ="세종대"; Track="논술우수자"; Time="09:00~11:00"; MinStat="2개 합 5"; MinDetail="국,수,영,탐(1) 중 2개 합 5"; QuotaDetail="자전71, 국제10, 경영9, 호텔경영9 등"; Ratio="논술80+교과20"; Note="수능 후 2주차" },
    [PSCustomObject]@{ Date="2026-11-29"; Univ="중앙대(일반형)"; Track="논술전형"; Time="10:00 / 14:00"; MinStat="3개 합 6"; MinDetail="국,수,영,탐(1) 중 3개 합 6, 英2->1, 史4"; QuotaDetail="경영36, 간호13, 경제12, 독문8, 불문8 등"; Ratio="논술70+교과20+출결10"; Note="★ 수능 후 2주차 / 최저 3합6" },
    [PSCustomObject]@{ Date="2026-11-29"; Univ="한국외대"; Track="논술전형(T3/T4)"; Time="10:00 / 15:00"; MinStat="2개 합 4"; MinDetail="국,수,영,탐(1) 중 2개 합 4"; QuotaDetail="자전(글로벌)40, 경영27, 융재10 등"; Ratio="논술100"; Note="★ 수능 후 2주차 / 영어제시문(T3)" },
    [PSCustomObject]@{ Date="2026-11-29"; Univ="광운대"; Track="논술우수자"; Time="10:00 / 14:30"; MinStat="최저 無"; MinDetail="수능 최저 미적용"; QuotaDetail="경영12, 법학10, 미커8, 동북아6 등"; Ratio="논술80+교과20"; Note="★ 수능 후 2주차 / 최저無" },
    [PSCustomObject]@{ Date="2026-11-29"; Univ="덕성여대"; Track="논술전형"; Time="시간 미정"; MinStat="2개 합 7"; MinDetail="국,수,영,탐(1) 중 2개 합 7"; QuotaDetail="글로벌융합대학 65"; Ratio="논술100"; Note="수능 후 2주차" },
    [PSCustomObject]@{ Date="2026-11-30"; Univ="가천대"; Track="약술형논술"; Time="시간 미정"; MinStat="1개 3등급"; MinDetail="국,수,영,탐(1) 중 1개 3등급 (80분 약술)"; QuotaDetail="AI인문73, 법대46, 경영40, 회계16 등"; Ratio="논술100"; Note="★ 약술형 논술" },

    [PSCustomObject]@{ Date="2026-12-05"; Univ="인하대"; Track="논술우수자"; Time="시간 미정"; MinStat="최저 無"; MinDetail="수능 최저 미적용"; QuotaDetail="경영22, 영미유럽14, 경제11, 행정10 등"; Ratio="논술80+교과20"; Note="★ 수능 후 3주차 / 최저無" },
    [PSCustomObject]@{ Date="2026-12-05"; Univ="국민대"; Track="약술형논술"; Time="시간 미정"; MinStat="2개 합 6"; MinDetail="국,수,영,탐(1) 중 2개 합 6, 史필 (90분 약술)"; QuotaDetail="법학20, 경영11, 행정6, 정외3 등"; Ratio="논술100"; Note="★ 약술형 논술 / 신설 보정항목" },
    [PSCustomObject]@{ Date="2026-12-06"; Univ="아주대"; Track="논술우수자"; Time="09:00~11:00"; MinStat="최저 無"; MinDetail="수능 최저 미적용"; QuotaDetail="경영15, 국문5, 자전5 등"; Ratio="논술80+교과20"; Note="★ 수능 후 3주차 / 최저無" }
)

$target1 = "C:\Users\그램\Desktop\입시분석 참고자료\논술일정표"
$target2 = "C:\Users\그램\Desktop\입시분석 참고자료\2027 종합전형"

# Write CSV with UTF8 BOM
$data | Export-Csv -Path (Join-Path $target1 "2027_수시_논술전형_통합DB.csv") -Encoding utf8 -NoTypeInformation
$data | Export-Csv -Path (Join-Path $target1 "2027_수시_논술전형_통합DB.xls") -Encoding utf8 -NoTypeInformation
$data | Export-Csv -Path (Join-Path $target1 "2027_논술고사_날짜별_달력일정.csv") -Encoding utf8 -NoTypeInformation
$data | Export-Csv -Path (Join-Path $target1 "2027_논술고사_날짜별_달력일정.xls") -Encoding utf8 -NoTypeInformation

$data | Export-Csv -Path (Join-Path $target2 "2027_수시_논술전형_통합DB.csv") -Encoding utf8 -NoTypeInformation
$data | Export-Csv -Path (Join-Path $target2 "2027_수시_논술전형_통합DB.xls") -Encoding utf8 -NoTypeInformation
$data | Export-Csv -Path (Join-Path $target2 "2027_논술고사_날짜별_달력일정.csv") -Encoding utf8 -NoTypeInformation
$data | Export-Csv -Path (Join-Path $target2 "2027_논술고사_날짜별_달력일정.xls") -Encoding utf8 -NoTypeInformation

Write-Host "All CSV and XLS files successfully exported!"
