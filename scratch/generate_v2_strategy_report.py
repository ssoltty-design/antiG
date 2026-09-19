# -*- coding: utf-8 -*-
import os
import shutil

workspace_reports = u"C:\\Users\\그램\\Documents\\antiG\\reports"
desktop_root = u"C:\\Users\\그램\\Desktop\\입시분석 참고자료"

# 1. Archive previous v1 file
v1_src = os.path.join(workspace_reports, u"final", u"01_2027_수시_통합_지원전략_보고서.html")
archive_dest = os.path.join(workspace_reports, u"archive_history", u"20260810_v1_01_2027_수시_통합_지원전략_보고서.html")

if os.path.exists(v1_src):
    shutil.copy2(v1_src, archive_dest)

# 2. Build V2 Strategy Report HTML Content
html_content = u"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2027학년도 진선여고 박정윤 수시 지원 5대 맞춤형 콤보 지원전략 보고서 (V2 완결판)</title>
    <style>
        :root {
            --bg-main: #f8fafc;
            --card-bg: #ffffff;
            --navy-primary: #1e3a8a;
            --blue-accent: #2563eb;
            --teal-badge: #0d9488;
            --orange-badge: #c2410c;
            --purple-badge: #7e22ce;
            --text-dark: #0f172a;
            --text-muted: #475569;
            --border-color: #cbd5e1;
        }

        body {
            font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: var(--bg-main);
            color: var(--text-dark);
            margin: 0;
            padding: 30px 15px;
            line-height: 1.6;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
        }

        .header {
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-top: 5px solid var(--navy-primary);
            border-radius: 12px;
            padding: 28px 32px;
            margin-bottom: 24px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }

        .header h1 {
            color: var(--navy-primary);
            font-size: 28px;
            font-weight: 800;
            margin: 0 0 10px 0;
        }

        .header p {
            color: var(--text-muted);
            font-size: 15px;
            margin: 0 0 16px 0;
        }

        .profile-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            background-color: #f1f5f9;
            padding: 16px;
            border-radius: 10px;
            font-size: 13px;
        }

        .profile-item {
            background: #ffffff;
            padding: 10px 14px;
            border-radius: 6px;
            border: 1px solid #e2e8f0;
        }

        .profile-item-title {
            font-weight: 700;
            color: var(--navy-primary);
            font-size: 12px;
            margin-bottom: 4px;
        }

        .profile-item-val {
            font-weight: 800;
            color: var(--text-dark);
            font-size: 14px;
        }

        /* 4-Stage Deadlines Timeline Banner */
        .deadlines-banner {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            margin: 20px 0;
            padding: 16px;
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
        }

        .deadline-card {
            padding: 10px 12px;
            border-radius: 8px;
            font-size: 12px;
            border-left: 4px solid;
        }

        .deadline-card.d1 { background-color: #fef2f2; border-color: #ef4444; color: #991b1b; }
        .deadline-card.d2 { background-color: #fefce8; border-color: #eab308; color: #854d0e; }
        .deadline-card.d3 { background-color: #eff6ff; border-color: #3b82f6; color: #1e40af; }
        .deadline-card.d4 { background-color: #faf5ff; border-color: #a855f7; color: #6b21a8; }

        .deadline-card-title {
            font-weight: 800;
            font-size: 13px;
            margin-bottom: 4px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* Inline Deadline Badges */
        .deadline-tag {
            display: inline-block;
            font-size: 10px;
            font-weight: 800;
            padding: 1px 5px;
            border-radius: 3px;
            margin-left: 4px;
            vertical-align: middle;
        }
        .tag-d1 { background-color: #fef2f2; color: #dc2626; border: 1px solid #fca5a5; }
        .tag-d2 { background-color: #fefce8; color: #ca8a04; border: 1px solid #fde047; }
        .tag-d3 { background-color: #eff6ff; color: #2563eb; border: 1px solid #93c5fd; }
        .tag-d4 { background-color: #faf5ff; color: #9333ea; border: 1px solid #d8b4fe; }

        /* Option Tabs */
        .option-tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 24px;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 12px;
            flex-wrap: wrap;
        }

        .tab-btn {
            background-color: #ffffff;
            border: 1px solid var(--border-color);
            color: var(--text-muted);
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .tab-btn.active {
            background-color: var(--navy-primary);
            color: #ffffff;
            border-color: var(--navy-primary);
            box-shadow: 0 4px 6px -1px rgba(30, 58, 138, 0.2);
        }

        .tab-btn.recommended.active {
            background-color: var(--blue-accent);
            border-color: var(--blue-accent);
        }

        .tab-btn:hover:not(.active) {
            background-color: #f1f5f9;
        }

        /* Option Content Section */
        .option-section {
            display: none;
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 28px;
            margin-bottom: 24px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }

        .option-section.active {
            display: block;
        }

        .option-header {
            border-bottom: 2px solid #f1f5f9;
            padding-bottom: 16px;
            margin-bottom: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .option-title {
            font-size: 22px;
            font-weight: 800;
            color: var(--navy-primary);
            margin: 0;
        }

        .option-badge {
            background-color: #dbeafe;
            color: #1e40af;
            font-size: 13px;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 20px;
        }

        /* Cards Grid */
        .cards-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            margin-bottom: 24px;
        }

        .univ-card {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-top: 4px solid var(--navy-primary);
            border-radius: 10px;
            padding: 18px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
            position: relative;
        }

        .univ-card.nonsul { border-top-color: var(--orange-badge); }
        .univ-card.johap { border-top-color: var(--teal-badge); }
        .univ-card.special { border-top-color: var(--purple-badge); background-color: #faf5ff; }

        .univ-name {
            font-size: 17px;
            font-weight: 800;
            color: var(--navy-primary);
            margin-bottom: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .type-badge {
            font-size: 11px;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 4px;
        }
        .type-johap { background-color: #ccfbf1; color: #0f766e; }
        .type-nonsul { background-color: #ffedd5; color: #c2410c; }
        .type-special { background-color: #f3e8ff; color: #7e22ce; }

        .card-detail {
            font-size: 13px;
            color: var(--text-dark);
            margin-bottom: 6px;
        }
        .card-detail strong {
            color: var(--text-muted);
            font-weight: 700;
        }

        .strategic-comment {
            margin-top: 10px;
            padding: 10px 12px;
            background-color: #f8fafc;
            border-radius: 6px;
            border-left: 3px solid var(--blue-accent);
            font-size: 12px;
            color: #334155;
        }

        /* Matrix Table */
        .matrix-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 24px;
            font-size: 13px;
        }

        .matrix-table th, .matrix-table td {
            border: 1px solid var(--border-color);
            padding: 12px;
            text-align: center;
        }

        .matrix-table th {
            background-color: #f1f5f9;
            color: var(--navy-primary);
            font-weight: 800;
        }

        .matrix-table tr:nth-child(even) {
            background-color: #f8fafc;
        }

        /* Print Styling */
        @media print {
            body { padding: 0; background: #fff; }
            .option-tabs { display: none; }
            .option-section { display: block !important; page-break-after: always; }
        }
    </style>
</head>
<body>

<div class="container">
    <!-- Header -->
    <div class="header">
        <h1>🎓 2027학년도 수시 지원 5대 맞춤형 콤보 지원전략 보고서 (V2 완결판)</h1>
        <p>진선여자고등학교 3학년 박정윤 학생의 내신계산법, 7월 모평 성적, 4단계 수시 원서마감 및 수능 최저 충족 가능성 입체 분석</p>

        <!-- Profile Grid -->
        <div class="profile-grid">
            <div class="profile-item">
                <div class="profile-item-title">학생 성명 / 학교</div>
                <div class="profile-item-val">박정윤 (진선여고 3)</div>
            </div>
            <div class="profile-item">
                <div class="profile-item-title">한국외대 환산내신</div>
                <div class="profile-item-val" style="color:#2563eb;">3.80등급 (82.58점)</div>
            </div>
            <div class="profile-item">
                <div class="profile-item-title">동국대 환산내신</div>
                <div class="profile-item-val" style="color:#0d9488;">4.80등급 (9.18점 / 상위10)</div>
            </div>
            <div class="profile-item">
                <div class="profile-item-title">7월 모평 / 목표 최저</div>
                <div class="profile-item-val" style="color:#c2410c;">4 3 2 3 / 2합 5 및 3합 6</div>
            </div>
        </div>

        <!-- 4-Stage Deadlines Banner -->
        <div class="deadlines-banner">
            <div class="deadline-card d1">
                <div class="deadline-card-title">🔴 1차 마감 <span>9/9(수) 17:00</span></div>
                <div>고려대 (전국 최선두 마감)</div>
            </div>
            <div class="deadline-card d2">
                <div class="deadline-card-title">🟡 2차 마감 <span>9/10(목) 17:00</span></div>
                <div>연세대(서울), 이화여대</div>
            </div>
            <div class="deadline-card d3">
                <div class="deadline-card-title">🔵 3차 마감 <span>9/11(금) 17:00</span></div>
                <div>건국대, 동국대, 숙명여대, 연세대(미래), 한국외대</div>
            </div>
            <div class="deadline-card d4">
                <div class="deadline-card-title">🟣 4차 마감 <span>9/11(금) 18:00</span></div>
                <div>서울대, 성균관대, 서강대, 한양대, 중앙대, 경희대, 세종대, 숭실대, 아주대, 가천대 등 23개교</div>
            </div>
        </div>
    </div>

    <!-- Option Navigation Tabs -->
    <div class="option-tabs">
        <button class="tab-btn active" onclick="switchOption('optA')">Option A: 상향 소신 중심형 (3합6~7 챌린지)</button>
        <button class="tab-btn" onclick="switchOption('optB')">Option B: 2합5 안정 확실형 (실질합격 극대화)</button>
        <button class="tab-btn" onclick="switchOption('optC')">Option C: 최저 미적용 & 약술형 방어 결합형</button>
        <button class="tab-btn recommended" onclick="switchOption('optD')">⭐ Option D: 하이브리드 황금 밸런스 (Recommended)</button>
        <button class="tab-btn" onclick="switchOption('optE')">Option E: 여대 프리미엄 & 인서울 특화형</button>
        <button class="tab-btn" onclick="switchOption('optMatrix')">📊 5대 옵션 한눈에 비교 분석표</button>
    </div>

    <!-- ========================================== -->
    <!-- Option A -->
    <!-- ========================================== -->
    <div id="optA" class="option-section active">
        <div class="option-header">
            <div>
                <h2 class="option-title">Option A: 상향 소신 중심형 (3합 6~7 챌린지 밸런스)</h2>
                <div style="font-size:13px; color:var(--text-muted); margin-top:4px;">수능 최저 대폭 상승 시 최고 명문대 타깃팅 | 고려대 학업우수 + 성균관대/서강대/중앙대 논술 중심</div>
            </div>
            <div class="option-badge">최저 상향 지향</div>
        </div>

        <div class="cards-grid">
            <!-- Card 1 -->
            <div class="univ-card johap">
                <div class="univ-name">
                    <span>1. 고려대 학업우수형 <span class="deadline-tag tag-d1">9/9 17시 마감</span></span>
                    <span class="type-badge type-johap">종합전형</span>
                </div>
                <div class="card-detail"><strong>모집단위 및 인원:</strong> 경영대학 12명 / 자전 15명 (총 903명)</div>
                <div class="card-detail"><strong>전형방법:</strong> 서류 100% (면접 없음)</div>
                <div class="card-detail"><strong>수능 최저기준:</strong> 4개 영역 합 8 이내 (한국사 4)</div>
                <div class="strategic-comment">★ 9/9 17시 가장 빠른 1차 마감. 4합8 최저 충족 시 실질 경쟁률이 3:1 이하로 급감하여 최저 맞추면 합격 확률 대폭 상승!</div>
            </div>
            <!-- Card 2 -->
            <div class="univ-card nonsul">
                <div class="univ-name">
                    <span>2. 성균관대 인문사회계열 <span class="deadline-tag tag-d4">9/11 18시 마감</span></span>
                    <span class="type-badge type-nonsul">논술전형</span>
                </div>
                <div class="card-detail"><strong>모집단위 및 인원:</strong> 인문계열 38명 / 사회계열 40명 / 경영 20명</div>
                <div class="card-detail"><strong>전형방법:</strong> 논술 100% (교과 감점 0점)</div>
                <div class="card-detail"><strong>수능 최저기준:</strong> 3개 영역 합 6 이내 (한국사 필수)</div>
                <div class="card-detail"><strong>시험일시:</strong> 2026-11-21 (토) 08:30 (사회) / 13:00 (인문)</div>
                <div class="strategic-comment">★ 수능 후 1주차 토요일 고사. 내신 감점이 전혀 없는 논술 100%로 3합6 최저만 통과하면 역전 가능!</div>
            </div>
            <!-- Card 3 -->
            <div class="univ-card nonsul">
                <div class="univ-name">
                    <span>3. 서강대 논술전형 <span class="deadline-tag tag-d4">9/11 18시 마감</span></span>
                    <span class="type-badge type-nonsul">논술전형</span>
                </div>
                <div class="card-detail"><strong>모집단위 및 인원:</strong> 경영학부 38명 / 경제학과 21명</div>
                <div class="card-detail"><strong>전형방법:</strong> 논술 100% (교과 감점 0점)</div>
                <div class="card-detail"><strong>수능 최저기준:</strong> 3개 영역 합 7 이내 (한국사 4)</div>
                <div class="card-detail"><strong>시험일시:</strong> 2026-11-22 (일) 16:00 (인문) / 19:00 (경영)</div>
                <div class="strategic-comment">★ 일요일 19:00 야간 고사로 고려대/동국대 고사 직후 이동 동선 완벽 수용. 논술100%로 부담 최소화.</div>
            </div>
            <!-- Card 4 -->
            <div class="univ-card nonsul">
                <div class="univ-name">
                    <span>4. 중앙대 (일반형) 논술 <span class="deadline-tag tag-d4">9/11 18시 마감</span></span>
                    <span class="type-badge type-nonsul">논술전형</span>
                </div>
                <div class="card-detail"><strong>모집단위 및 인원:</strong> 경영학부 36명 / 경제 12명</div>
                <div class="card-detail"><strong>전형방법:</strong> 논술 70% + 교과 20% + 출결 10%</div>
                <div class="card-detail"><strong>수능 최저기준:</strong> 3개 영역 합 6 이내 (영어 2->1 감안)</div>
                <div class="card-detail"><strong>시험일시:</strong> 2026-11-29 (일) 10:00 (경영) / 14:00 (인문)</div>
                <div class="strategic-comment">★ 상위 5과목 교과 반영으로 1~5등급간 감점 약 0.32점에 불과해 내신 불이익 없음. 수능 후 2주차 일요일 고사.</div>
            </div>
            <!-- Card 5 -->
            <div class="univ-card nonsul">
                <div class="univ-name">
                    <span>5. 동국대 논술전형 <span class="deadline-tag tag-d3">9/11 17시 마감</span></span>
                    <span class="type-badge type-nonsul">논술전형</span>
                </div>
                <div class="card-detail"><strong>모집단위 및 인원:</strong> 경영학과 37명 / 국제통상 12명</div>
                <div class="card-detail"><strong>전형방법:</strong> 논술 70% + 교과 20% + 출결 10%</div>
                <div class="card-detail"><strong>수능 최저기준:</strong> 2개 영역 합 5 이내 (한국사 4)</div>
                <div class="card-detail"><strong>시험일시:</strong> 2026-11-22 (일) 13:00 (인문) / 16:30 (법학)</div>
                <div class="strategic-comment">★ 박정윤 학생 동국대 환산 4.80등급 적용 시 상위 10과목 반영으로 감점 약 0.4점에 불과! 매우 확실한 안전판.</div>
            </div>
            <!-- Card 6 -->
            <div class="univ-card johap">
                <div class="univ-name">
                    <span>6. 한국외대 면접형 (종합) <span class="deadline-tag tag-d3">9/11 17시 마감</span></span>
                    <span class="type-badge type-johap">종합전형</span>
                </div>
                <div class="card-detail"><strong>모집단위 및 인원:</strong> 자유전공(서울) 24명 / 미디어 10명</div>
                <div class="card-detail"><strong>전형방법:</strong> 1단계 서류 100% (3배수) -> 2단계 면접 50%</div>
                <div class="card-detail"><strong>수능 최저기준:</strong> 수능 최저 없음 (면접100% 역전)</div>
                <div class="card-detail"><strong>면접일시:</strong> 2026-11-21 (토) 10:00</div>
                <div class="strategic-comment">★ 박정윤 학생 외대 환산내신 3.80등급으로 1단계 서류 합격 가능성 높으며, 2단계 면접 50%로 완벽 최종합격 유도.</div>
            </div>
        </div>

        <!-- 7th Special Card -->
        <div class="univ-card special">
            <div class="univ-name">
                <span>★ UNIST (울산과기원) 경영계열 <span class="deadline-tag tag-d4">9/11 18시 마감</span></span>
                <span class="type-badge type-special">무위험 7번째 카드</span>
            </div>
            <div class="card-detail"><strong>지원 자격:</strong> 수시 6회 지원 제한에 포함되지 않는 별도 과기원 카드 (무위험)</div>
            <div class="card-detail"><strong>전형방법:</strong> 서류 100% (탐구역량 40% + 학업역량 30% + 리더십 30%) | 수능 최저 없음</div>
            <div class="strategic-comment">★ 4대 과기원 중 유일하게 경영계열 별도 선발! 진선여고 인문계 생기부로 최우선 무위험 지원 가능.</div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- Option B -->
    <!-- ========================================== -->
    <div id="optB" class="option-section">
        <div class="option-header">
            <div>
                <h2 class="option-title">Option B: 수능 최저 2합5 안정 확실형 (실질합격률 극대화)</h2>
                <div style="font-size:13px; color:var(--text-muted); margin-top:4px;">7월 모평 2합5 충족 기반 확실한 합격선 구축 | 교과 감점 무력화 및 논술 100% 대학 집중</div>
            </div>
            <div class="option-badge" style="background:#ccfbf1; color:#0f766e;">안정 실리 지향</div>
        </div>

        <div class="cards-grid">
            <div class="univ-card nonsul">
                <div class="univ-name">
                    <span>1. 동국대 논술전형 <span class="deadline-tag tag-d3">9/11 17시 마감</span></span>
                    <span class="type-badge type-nonsul">논술전형</span>
                </div>
                <div class="card-detail"><strong>최저기준:</strong> 2개 영역 합 5 이내</div>
                <div class="card-detail"><strong>환산내신:</strong> 4.80등급 (상위10과목 감점 약 0.4점 불과)</div>
                <div class="strategic-comment">★ 7월 모평 수(3)+영(2) 2합5 달성으로 최저 충족률 높음. 내신 감점 영향 최소화.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name">
                    <span>2. 경희대 논술우수자 <span class="deadline-tag tag-d4">9/11 18시 마감</span></span>
                    <span class="type-badge type-nonsul">논술전형</span>
                </div>
                <div class="card-detail"><strong>최저기준:</strong> 2개 영역 합 5 이내</div>
                <div class="card-detail"><strong>전형방법:</strong> 논술 100% (교과 감점 0점)</div>
                <div class="strategic-comment">★ 경영회계 27명 대규모 선발. 논술 100%로 내신 부담 없이 2합5로 승부.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name">
                    <span>3. 건국대 KU논술우수자 <span class="deadline-tag tag-d3">9/11 17시 마감</span></span>
                    <span class="type-badge type-nonsul">논술전형</span>
                </div>
                <div class="card-detail"><strong>최저기준:</strong> 2개 영역 합 5 이내</div>
                <div class="card-detail"><strong>전형방법:</strong> 논술 100% (KU자전 65명, 경영 15명)</div>
                <div class="strategic-comment">★ KU자율전공학부 65명 모집으로 문과생 선호도 매우 높음.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name">
                    <span>4. 숭실대 논술우수자 <span class="deadline-tag tag-d4">9/11 18시 마감</span></span>
                    <span class="type-badge type-nonsul">논술전형</span>
                </div>
                <div class="card-detail"><strong>최저기준:</strong> 2개 영역 합 6 이내</div>
                <div class="card-detail"><strong>전형방법:</strong> 논술 90% + 교과 10% (경영 16명)</div>
                <div class="strategic-comment">★ 2합 6 최저기준으로 합격 안전선 확보에 최적화된 카드.</div>
            </div>
            <div class="univ-card johap">
                <div class="univ-name">
                    <span>5. 한국외대 면접형 (종합) <span class="deadline-tag tag-d3">9/11 17시 마감</span></span>
                    <span class="type-badge type-johap">종합전형</span>
                </div>
                <div class="card-detail"><strong>환산내신:</strong> 3.80등급 (우수) | 최저 없음</div>
                <div class="strategic-comment">★ 면접 50%로 박정윤 학생 발표/표현력 강점 적극 활용.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name">
                    <span>6. 중앙대 창의형 논술 <span class="deadline-tag tag-d4">9/11 18시 마감</span></span>
                    <span class="type-badge type-nonsul">논술전형</span>
                </div>
                <div class="card-detail"><strong>시험일시:</strong> 수능 전 10/11 (일) 10:00 | 최저 없음</div>
                <div class="strategic-comment">★ 고3 현역만 지원 가능하여 N수생 배제 프리미엄!</div>
            </div>
        </div>

        <div class="univ-card special">
            <div class="univ-name"><span>★ UNIST 경영계열</span><span class="type-badge type-special">무위험 7번째 카드</span></div>
            <div class="strategic-comment">★ 수시 6회 제한 미적용! 서류 100% 무위험 지원.</div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- Option C -->
    <!-- ========================================== -->
    <div id="optC" class="option-section">
        <div class="option-header">
            <div>
                <h2 class="option-title">Option C: 최저 미적용 & 약술형 방어 결합형 (수능 리스크 방어)</h2>
                <div style="font-size:13px; color:var(--text-muted); margin-top:4px;">수능 당일 컨디션 난조 대비 최저 미적용 전형 및 약술형 안전장치 확보</div>
            </div>
            <div class="option-badge" style="background:#fef3c7; color:#92400e;">리스크 제로 지향</div>
        </div>

        <div class="cards-grid">
            <div class="univ-card nonsul">
                <div class="univ-name"><span>1. 연세대 논술전형 <span class="deadline-tag tag-d2">9/10 17시 마감</span></span><span class="type-badge type-nonsul">논술전형</span></div>
                <div class="card-detail"><strong>시험일시:</strong> 수능 전 10/10 (토) | 최저 없음 | 논술 100%</div>
                <div class="strategic-comment">★ 수능 전 고사. 최저가 없어 수능 변수 전혀 없음.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name"><span>2. 중앙대 창의형 논술 <span class="deadline-tag tag-d4">9/11 18시 마감</span></span><span class="type-badge type-nonsul">논술전형</span></div>
                <div class="card-detail"><strong>시험일시:</strong> 수능 전 10/11 (일) | 최저 없음 (고3 현역만)</div>
                <div class="strategic-comment">★ 수능 전 고3 전용 전형으로 완벽한 안전장치.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name"><span>3. 광운대 논술우수자 <span class="deadline-tag tag-d3">9/11 17시 마감</span></span><span class="type-badge type-nonsul">논술전형</span></div>
                <div class="card-detail"><strong>시험일시:</strong> 수능 후 11/29 (일) | 최저 없음 | 경영 12명</div>
                <div class="strategic-comment">★ 인서울 4년제 최저 미적용 대표 카드.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name"><span>4. 인하대 논술우수자 <span class="deadline-tag tag-d4">9/11 18시 마감</span></span><span class="type-badge type-nonsul">논술전형</span></div>
                <div class="card-detail"><strong>시험일시:</strong> 수능 후 12/05 (토) | 최저 없음 | 경영 22명</div>
                <div class="strategic-comment">★ 수능 후 3주차 마지막 고사로 여유로운 시험 준비.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name"><span>5. 가천대 약술형 논술 <span class="deadline-tag tag-d4">9/11 18시 마감</span></span><span class="type-badge type-nonsul">논술전형</span></div>
                <div class="card-detail"><strong>시험일시:</strong> 수능 후 11/30 (월) | 1개 3등급 | 논술 100%</div>
                <div class="strategic-comment">★ 약술형 논술로 1개 3등급 최저 충족이 매우 용이하여 하한선 확실 방어.</div>
            </div>
            <div class="univ-card johap">
                <div class="univ-name"><span>6. 한국외대 면접형 (종합) <span class="deadline-tag tag-d3">9/11 17시 마감</span></span><span class="type-badge type-johap">종합전형</span></div>
                <div class="card-detail"><strong>환산내신:</strong> 3.80등급 | 최저 없음</div>
                <div class="strategic-comment">★ 종합전형 안전선 구축.</div>
            </div>
        </div>

        <div class="univ-card special">
            <div class="univ-name"><span>★ UNIST 경영계열</span><span class="type-badge type-special">무위험 7번째 카드</span></div>
            <div class="strategic-comment">★ 최저 없는 과기원 7번째 무위험 카드.</div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- Option D (Recommended) -->
    <!-- ========================================== -->
    <div id="optD" class="option-section">
        <div class="option-header">
            <div>
                <h2 class="option-title">⭐ Option D: 하이브리드 황금 밸런스 (Recommended)</h2>
                <div style="font-size:13px; color:var(--text-muted); margin-top:4px;">상향2 + 적정2 + 소신2의 가장 안정적이고 이상적인 하이브리드 수시 6카드 조합</div>
            </div>
            <div class="option-badge" style="background:#2563eb; color:#fff;">추천 Best 1</div>
        </div>

        <div class="cards-grid">
            <div class="univ-card johap">
                <div class="univ-name"><span>1. 고려대 학업우수형 <span class="deadline-tag tag-d1">9/9 17시 마감</span></span><span class="type-badge type-johap">초상향 종합</span></div>
                <div class="card-detail"><strong>최저기준:</strong> 4개 영역 합 8 이내</div>
                <div class="strategic-comment">★ 9/9 17시 최선두 1차 마감. 최저 충족 시 실질 경쟁률 3:1 이하로 합격 가능성 대폭 상승하는 카리스마 카드.</div>
            </div>
            <div class="univ-card johap">
                <div class="univ-name"><span>2. 한국외대 면접형 <span class="deadline-tag tag-d3">9/11 17시 마감</span></span><span class="type-badge type-johap">종합 적정</span></div>
                <div class="card-detail"><strong>환산내신:</strong> 3.80등급 | 2단계 면접 50%</div>
                <div class="strategic-comment">★ 1단계 서류 통과 가능성이 매우 높고, 2단계 면접 50%로 확실한 합격 도장.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name"><span>3. 동국대 논술전형 <span class="deadline-tag tag-d3">9/11 17시 마감</span></span><span class="type-badge type-nonsul">논술 적정/안정</span></div>
                <div class="card-detail"><strong>최저기준:</strong> 2개 영역 합 5 | 환산 4.80</div>
                <div class="strategic-comment">★ 상위 10과목 반영으로 등급 감점 0.4점에 불과한 확실한 실리적 안전판.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name"><span>4. 성균관대 인문사회 <span class="deadline-tag tag-d4">9/11 18시 마감</span></span><span class="type-badge type-nonsul">논술 상향</span></div>
                <div class="card-detail"><strong>최저기준:</strong> 3개 영역 합 6 | 논술 100%</div>
                <div class="strategic-comment">★ 3합6 달성 시 내신 감점 없는 논술 100%로 명문대 합격 역전.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name"><span>5. 서강대 논술전형 <span class="deadline-tag tag-d4">9/11 18시 마감</span></span><span class="type-badge type-nonsul">논술 상향</span></div>
                <div class="card-detail"><strong>최저기준:</strong> 3개 영역 합 7 | 논술 100%</div>
                <div class="strategic-comment">★ 일요일 19:00 야간 고사로 고려대/동국대 시험 직후 당일 동선 완벽 수용.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name"><span>6. 중앙대 창의형 논술 <span class="deadline-tag tag-d4">9/11 18시 마감</span></span><span class="type-badge type-nonsul">논술 현역특화</span></div>
                <div class="card-detail"><strong>시험일시:</strong> 수능 전 10/11 | 최저 없음 (고3만)</div>
                <div class="strategic-comment">★ 고3 현역전용 수능 전 카드로 N수생 배제 및 사전 시험 감각 극대화.</div>
            </div>
        </div>

        <div class="univ-card special">
            <div class="univ-name"><span>★ UNIST 경영계열 <span class="deadline-tag tag-d4">9/11 18시 마감</span></span><span class="type-badge type-special">무위험 7번째 카드</span></div>
            <div class="strategic-comment">★ 4대 과기원 중 유일한 경영계열 선발! 수시 6회 제한 미적용 7번째 보너스 카드.</div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- Option E -->
    <!-- ========================================== -->
    <div id="optE" class="option-section">
        <div class="option-header">
            <div>
                <h2 class="option-title">Option E: 여대 프리미엄 & 인서울 특화형</h2>
                <div style="font-size:13px; color:var(--text-muted); margin-top:4px;">이화여대, 숙명여대 등 상위권 여대 특화 지원 전략으로 경쟁률 대비 실질 합격률 향상</div>
            </div>
            <div class="option-badge" style="background:#fce7f3; color:#9d174d;">여대 특화 지향</div>
        </div>

        <div class="cards-grid">
            <div class="univ-card johap">
                <div class="univ-name"><span>1. 이화여대 미래인재 <span class="deadline-tag tag-d2">9/10 17시 마감</span></span><span class="type-badge type-johap">종합전형</span></div>
                <div class="card-detail"><strong>최저기준:</strong> 2개 영역 합 5 | 서류 100% (면접 없음)</div>
                <div class="strategic-comment">★ 9/10 17시 2차 마감. 면접 부담이 없는 수능 최저 충족형 종합전형.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name"><span>2. 이화여대 논술전형 <span class="deadline-tag tag-d2">9/10 17시 마감</span></span><span class="type-badge type-nonsul">논술전형</span></div>
                <div class="card-detail"><strong>최저기준:</strong> 2개 영역 합 5 | 논술 100%</div>
                <div class="strategic-comment">★ 논술 100% 적용으로 내신 감점 0점. 수능 후 2주차 11/28 토요일 고사.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name"><span>3. 숙명여대 논술우수자 <span class="deadline-tag tag-d3">9/11 17시 마감</span></span><span class="type-badge type-nonsul">논술전형</span></div>
                <div class="card-detail"><strong>최저기준:</strong> 2개 영역 합 5 | 논술 90% + 교과 10%</div>
                <div class="strategic-comment">★ 국,수,영,사,과 상위 3과목만 반영하여 내신 감점 최소화.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name"><span>4. 성균관대 인문사회 <span class="deadline-tag tag-d4">9/11 18시 마감</span></span><span class="type-badge type-nonsul">논술전형</span></div>
                <div class="card-detail"><strong>최저기준:</strong> 3개 영역 합 6 | 논술 100%</div>
                <div class="strategic-comment">★ 3합6 최저 도전 상향 카드.</div>
            </div>
            <div class="univ-card nonsul">
                <div class="univ-name"><span>5. 동국대 논술전형 <span class="deadline-tag tag-d3">9/11 17시 마감</span></span><span class="type-badge type-nonsul">논술전형</span></div>
                <div class="card-detail"><strong>최저기준:</strong> 2개 영역 합 5 | 환산 4.80 (감점 0.4점)</div>
                <div class="strategic-comment">★ 확실한 2합5 실리적 안전판.</div>
            </div>
            <div class="univ-card johap">
                <div class="univ-name"><span>6. 한국외대 면접형 (종합) <span class="deadline-tag tag-d3">9/11 17시 마감</span></span><span class="type-badge type-johap">종합전형</span></div>
                <div class="card-detail"><strong>환산내신:</strong> 3.80등급 | 2단계 면접 50%</div>
                <div class="strategic-comment">★ 외대 종합 적정 카드.</div>
            </div>
        </div>

        <div class="univ-card special">
            <div class="univ-name"><span>★ UNIST 경영계열</span><span class="type-badge type-special">무위험 7번째 카드</span></div>
            <div class="strategic-comment">★ 4대 과기원 경영계열 무위험 지원.</div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- Option Comparative Matrix Table -->
    <!-- ========================================== -->
    <div id="optMatrix" class="option-section">
        <div class="option-header">
            <div>
                <h2 class="option-title">📊 5대 수시지원 옵션(A~E안) 한눈에 비교 분석 표</h2>
                <div style="font-size:13px; color:var(--text-muted); margin-top:4px;">박정윤 학생의 수능 성적 변동 및 성향에 따른 옵션별 비교 평가</div>
            </div>
        </div>

        <table class="matrix-table">
            <thead>
                <tr>
                    <th>구분</th>
                    <th>Option A<br>(상향 소신)</th>
                    <th>Option B<br>(2합5 안정)</th>
                    <th>Option C<br>(최저미적용 방어)</th>
                    <th>⭐ Option D<br>(하이브리드 추천)</th>
                    <th>Option E<br>(여대 특화)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>전형 구성</strong></td>
                    <td>종합 2 + 논술 4</td>
                    <td>종합 1 + 논술 5</td>
                    <td>종합 1 + 논술 5</td>
                    <td><strong>종합 2 + 논술 4</strong></td>
                    <td>종합 2 + 논술 4</td>
                </tr>
                <tr>
                    <td><strong>목표 최저 학력</strong></td>
                    <td>4합8 / 3합6 / 3합7</td>
                    <td>2합5 위주</td>
                    <td>최저 없음 위주</td>
                    <td><strong>4합8 / 3합6 / 2합5 밸런스</strong></td>
                    <td>2합5 / 3합6</td>
                </tr>
                <tr>
                    <td><strong>내신 불이익 차단도</strong></td>
                    <td>높음 (논술100% 3개)</td>
                    <td>매우 높음 (논술100% 2개)</td>
                    <td>높음</td>
                    <td><strong>완벽 (상위과목 및 논술100%)</strong></td>
                    <td>높음</td>
                </tr>
                <tr>
                    <td><strong>수능 변수 안전성</strong></td>
                    <td>보통 (수능 당일 영향)</td>
                    <td>높음 (2합5 용이)</td>
                    <td>최상 (최저無/약술형)</td>
                    <td><strong>높음 (안정판 확실)</strong></td>
                    <td>높음</td>
                </tr>
                <tr>
                    <td><strong>원서접수 1차마감</strong></td>
                    <td>고려대 (9/9 17시)</td>
                    <td>-</td>
                    <td>-</td>
                    <td><strong>고려대 (9/9 17시)</strong></td>
                    <td>이화여대 (9/10 17시)</td>
                </tr>
                <tr>
                    <td><strong>UNIST 7차 카드</strong></td>
                    <td>포함 (서류100)</td>
                    <td>포함 (서류100)</td>
                    <td>포함 (서류100)</td>
                    <td><strong>포함 (서류100)</strong></td>
                    <td>포함 (서류100)</td>
                </tr>
                <tr>
                    <td><strong>종합 추천도</strong></td>
                    <td>★★★☆☆</td>
                    <td>★★★★☆</td>
                    <td>★★★☆☆</td>
                    <td><strong>★★★★★ (BEST 1)</strong></td>
                    <td>★★★★☆</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

<script>
    function switchOption(optId) {
        document.querySelectorAll('.option-section').forEach(el => el.classList.remove('active'));
        document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));

        document.getElementById(optId).classList.add('active');
        event.currentTarget.classList.add('active');
    }
</script>

</body>
</html>
"""

# Write to workspace final directory
workspace_final_file = os.path.join(workspace_reports, u"final", u"01_2027_수시_통합_지원전략_보고서.html")
with open(workspace_final_file, 'wb') as f:
    f.write(html_content.encode('utf-8'))

# Write to desktop 00_최종보고서_및_달력 directory
desktop_final_file = os.path.join(desktop_root, u"00_최종보고서_및_달력", u"01_2027_수시_통합_지원전략_보고서.html")
with open(desktop_final_file, 'wb') as f:
    f.write(html_content.encode('utf-8'))

print "SUCCESSFULLY_GENERATED_V2_STRATEGY_REPORT"
