# -*- coding: utf-8 -*-
import os
import codecs

xls_path_reports = u"C:\\Users\\그램\\Documents\\antiG\\reports\\모의고사_성적_추이_분석.xls"
xls_path_desktop = u"C:\\Users\\그램\\Desktop\\프로세스\\모의고사 성적\\모의고사_성적_추이_분석.xls"
csv_path_reports = u"C:\\Users\\그램\\Documents\\antiG\\reports\\모의고사_성적_추이_분석.csv"
csv_path_desktop = u"C:\\Users\\그램\\Desktop\\프로세스\\모의고사 성적\\모의고사_성적_추이_분석.csv"

csv_content = u"""시험 구분,과목명,원 성적 (표준점수),수능 예측 (표준점수),원 성적 (백분위),수능 예측 (백분위),원 성적 (등급),수능 예측 (등급)
3월 학력평가 (3.24),국어(언어와매체),128,126,91.18,89,2등급,2등급
3월 학력평가 (3.24),수학(확률과통계),111,105,66.23,59,4등급,5등급
3월 학력평가 (3.24),지구과학I,73,72,98.24,97,1등급,1등급
3월 학력평가 (3.24),사회문화,69,66,95.82,92,1등급,2등급
6월 모의평가 (6.4),국어(언어와매체),120,119,82.00,80,3등급,3등급
6월 모의평가 (6.4),수학(확률과통계),114,112,66.00,62,4등급,4등급
6월 모의평가 (6.4),사회문화,61,60,83.00,80,3등급,3등급
6월 모의평가 (6.4),세계지리,49,48,51.00,47,5등급,5등급
7월 학력평가 (7.8),국어(언어와매체),110,106,64.13,57,4등급,5등급
7월 학력평가 (7.8),수학(확률과통계),123,120,83.10,78,3등급,3등급
7월 학력평가 (7.8),세계지리,49,47,55.62,49,5등급,5등급
7월 학력평가 (7.8),사회문화,61,59,82.91,76,3등급,3등급
"""

html_xls = u"""<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<!--[if gte mso 9]>
<xml>
 <x:ExcelWorkbook>
  <x:ExcelWorksheets>
   <x:ExcelWorksheet>
    <x:Name>모의고사 성적 추이</x:Name>
    <x:WorksheetOptions>
     <x:DisplayGridlines/>
    </x:WorksheetOptions>
   </x:ExcelWorksheet>
  </x:ExcelWorksheets>
 </x:ExcelWorkbook>
</xml>
<![endif]-->
<style>
  body { font-family: 'Malgun Gothic', '맑은 고딕', sans-serif; }
  table { border-collapse: collapse; width: 100%; }
  th { background-color: #1e3a8a; color: #ffffff; font-weight: bold; border: 1px solid #cbd5e1; padding: 10px; text-align: center; }
  td { border: 1px solid #cbd5e1; padding: 8px; font-size: 13px; text-align: center; }
  .title-bg { background-color: #0f172a; color: #38bdf8; font-size: 18px; font-weight: bold; text-align: center; padding: 15px; }
  .exam-bg { background-color: #eff6ff; font-weight: bold; color: #1e40af; }
  .pred-val { color: #dc2626; font-weight: bold; }
</style>
</head>
<body>
<table>
  <tr>
    <td colspan="8" class="title-bg">3월 / 6월 / 7월 모의고사 성적 및 수능 예측 비교 분석표</td>
  </tr>
  <tr>
    <th width="15%">시험 구분</th>
    <th width="15%">과목명</th>
    <th width="12%">원 표점</th>
    <th width="12%">수능예측 표점</th>
    <th width="12%">원 백분위</th>
    <th width="12%">수능예측 백분위</th>
    <th width="11%">원 등급</th>
    <th width="11%">수능예측 등급</th>
  </tr>
  <tr>
    <td class="exam-bg" rowspan="4">3월 학력평가 (3.24)</td>
    <td>국어 (언어와매체)</td>
    <td>128</td>
    <td class="pred-val">126</td>
    <td>91.18</td>
    <td class="pred-val">89</td>
    <td>2</td>
    <td class="pred-val">2</td>
  </tr>
  <tr>
    <td>수학 (확률과통계)</td>
    <td>111</td>
    <td class="pred-val">105</td>
    <td>66.23</td>
    <td class="pred-val">59</td>
    <td>4</td>
    <td class="pred-val">5</td>
  </tr>
  <tr>
    <td>지구과학I</td>
    <td>73</td>
    <td class="pred-val">72</td>
    <td>98.24</td>
    <td class="pred-val">97</td>
    <td>1</td>
    <td class="pred-val">1</td>
  </tr>
  <tr>
    <td>사회문화</td>
    <td>69</td>
    <td class="pred-val">66</td>
    <td>95.82</td>
    <td class="pred-val">92</td>
    <td>1</td>
    <td class="pred-val">2</td>
  </tr>
  <tr>
    <td class="exam-bg" rowspan="4">6월 모의평가 (6.4)</td>
    <td>국어 (언어와매체)</td>
    <td>120</td>
    <td class="pred-val">119</td>
    <td>82.00</td>
    <td class="pred-val">80</td>
    <td>3</td>
    <td class="pred-val">3</td>
  </tr>
  <tr>
    <td>수학 (확률과통계)</td>
    <td>114</td>
    <td class="pred-val">112</td>
    <td>66.00</td>
    <td class="pred-val">62</td>
    <td>4</td>
    <td class="pred-val">4</td>
  </tr>
  <tr>
    <td>사회문화</td>
    <td>61</td>
    <td class="pred-val">60</td>
    <td>83.00</td>
    <td class="pred-val">80</td>
    <td>3</td>
    <td class="pred-val">3</td>
  </tr>
  <tr>
    <td>세계지리</td>
    <td>49</td>
    <td class="pred-val">48</td>
    <td>51.00</td>
    <td class="pred-val">47</td>
    <td>5</td>
    <td class="pred-val">5</td>
  </tr>
  <tr>
    <td class="exam-bg" rowspan="4">7월 학력평가 (7.8)</td>
    <td>국어 (언어와매체)</td>
    <td>110</td>
    <td class="pred-val">106</td>
    <td>64.13</td>
    <td class="pred-val">57</td>
    <td>4</td>
    <td class="pred-val">5</td>
  </tr>
  <tr>
    <td>수학 (확률과통계)</td>
    <td>123</td>
    <td class="pred-val">120</td>
    <td>83.10</td>
    <td class="pred-val">78</td>
    <td>3</td>
    <td class="pred-val">3</td>
  </tr>
  <tr>
    <td>세계지리</td>
    <td>49</td>
    <td class="pred-val">47</td>
    <td>55.62</td>
    <td class="pred-val">49</td>
    <td>5</td>
    <td class="pred-val">5</td>
  </tr>
  <tr>
    <td>사회문화</td>
    <td>61</td>
    <td class="pred-val">59</td>
    <td>82.91</td>
    <td class="pred-val">76</td>
    <td>3</td>
    <td class="pred-val">3</td>
  </tr>
</table>
</body>
</html>
"""

# Write CSV with BOM
with open(csv_path_reports, "wb") as f:
    f.write(codecs.BOM_UTF8)
    f.write(csv_content.encode("utf-8"))
with open(csv_path_desktop, "wb") as f:
    f.write(codecs.BOM_UTF8)
    f.write(csv_content.encode("utf-8"))

# Write XLS HTML
with open(xls_path_reports, "wb") as f:
    f.write(html_xls.encode("utf-8"))
with open(xls_path_desktop, "wb") as f:
    f.write(html_xls.encode("utf-8"))

print("Mock exam score Excel files generated successfully!")
