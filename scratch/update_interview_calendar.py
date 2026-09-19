# -*- coding: utf-8 -*-

html_content = u"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2027학년도 대입 면접고사 월별 달력 일정표 (수시 원서접수 마감 포함)</title>
    <style>
        :root {
            --bg-main: #f8fafc;
            --card-bg: #ffffff;
            --navy-primary: #1e3a8a;
            --blue-accent: #2563eb;
            --teal-badge: #0d9488;
            --text-dark: #0f172a;
            --text-muted: #475569;
            --border-color: #cbd5e1;

            /* Event Colors */
            --csat-bg: #fee2e2;
            --csat-border: #f87171;
            --csat-text: #991b1b;

            --pre-bg: #e0e7ff;
            --pre-text: #3730a3;

            --w1-bg: #dbeafe;
            --w1-text: #1e40af;

            --w2-bg: #ccfbf1;
            --w2-text: #0f766e;

            --w3-bg: #dcfce7;
            --w3-text: #166534;

            --w4-bg: #fef3c7;
            --w4-text: #92400e;
        }

        body {
            font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: var(--bg-main);
            color: var(--text-dark);
            margin: 0;
            padding: 30px 15px;
            line-height: 1.5;
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
            padding: 24px 30px;
            margin-bottom: 24px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }

        .header h1 {
            color: var(--navy-primary);
            font-size: 26px;
            font-weight: 800;
            margin: 0 0 8px 0;
        }

        .header p {
            color: var(--text-muted);
            font-size: 14px;
            margin: 0 0 16px 0;
        }

        /* 4-Stage Deadlines Timeline Banner */
        .deadlines-banner {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            margin: 16px 0 20px 0;
            padding: 16px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
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

        /* Month Navigation Tabs */
        .month-tabs {
            display: flex;
            gap: 12px;
            margin-bottom: 20px;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 12px;
        }

        .tab-btn {
            background-color: #ffffff;
            border: 1px solid var(--border-color);
            color: var(--text-muted);
            padding: 10px 24px;
            border-radius: 8px;
            font-size: 15px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .tab-btn.active {
            background-color: var(--navy-primary);
            color: #ffffff;
            border-color: var(--navy-primary);
            box-shadow: 0 2px 4px rgba(30, 58, 138, 0.2);
        }

        .tab-btn:hover:not(.active) {
            background-color: #f1f5f9;
        }

        /* Legend */
        .legend-bar {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            background: #ffffff;
            padding: 14px 20px;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            margin-bottom: 24px;
            font-size: 13px;
            align-items: center;
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 6px;
            font-weight: 600;
        }

        .dot {
            width: 12px;
            height: 12px;
            border-radius: 3px;
            display: inline-block;
        }

        /* Calendar Grid (Zero Scrollbars - Min Height 150px Layout) */
        .calendar-section {
            display: none;
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }

        .calendar-section.active {
            display: block;
        }

        .calendar-month-title {
            color: var(--navy-primary);
            font-size: 22px;
            font-weight: 800;
            margin-top: 0;
            margin-bottom: 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .calendar-grid {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 8px;
        }

        .day-header {
            background-color: #f1f5f9;
            color: var(--navy-primary);
            font-weight: 700;
            text-align: center;
            padding: 10px;
            border-radius: 6px;
            font-size: 14px;
        }

        .day-header.sun { color: #dc2626; }
        .day-header.sat { color: #2563eb; }

        .day-cell {
            min-height: 150px;
            height: auto;
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 8px;
            display: flex;
            flex-direction: column;
            transition: border-color 0.2s;
            overflow: visible;
        }

        .day-cell.other-month {
            background-color: #f8fafc;
            opacity: 0.4;
        }

        .day-number {
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .day-cell.sun .day-number { color: #dc2626; }
        .day-cell.sat .day-number { color: #2563eb; }

        .d-day-tag {
            font-size: 10px;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 700;
        }

        .events-container {
            display: flex;
            flex-direction: column;
            gap: 5px;
            height: auto;
            overflow: visible;
        }

        .event-badge {
            font-size: 11px;
            padding: 4px 6px;
            border-radius: 4px;
            font-weight: 600;
            line-height: 1.3;
            border-left: 3px solid;
            word-break: keep-all;
        }

        /* Specific Badge Styles */
        .badge-csat {
            background-color: var(--csat-bg);
            color: var(--csat-text);
            border-color: var(--csat-border);
            font-weight: 800;
        }

        .badge-pre {
            background-color: var(--pre-bg);
            color: var(--pre-text);
            border-color: #6366f1;
        }

        .badge-w1 {
            background-color: var(--w1-bg);
            color: var(--w1-text);
            border-color: #3b82f6;
        }

        .badge-w2 {
            background-color: var(--w2-bg);
            color: var(--w2-text);
            border-color: #14b8a6;
        }

        .badge-w3 {
            background-color: var(--dcfce7);
            color: var(--w3-text);
            border-color: #22c55e;
        }

        .badge-w4 {
            background-color: var(--w4-bg);
            color: var(--w4-text);
            border-color: #f59e0b;
        }

        /* Print Styling */
        @media print {
            body { padding: 0; background: #fff; }
            .month-tabs { display: none; }
            .calendar-section { display: block !important; page-break-after: always; margin-bottom: 20px; }
            .day-cell { min-height: 120px; }
        }
    </style>
</head>
<body>

<div class="container">
    <!-- Header -->
    <div class="header">
        <h1>🗓️ 2027학년도 수도권 주요 대학 면접고사 월달력 일정표</h1>
        <p>2027학년도 대학수학능력시험일: <strong>2026년 11월 19일 (목요일)</strong> | 수도권 주요 대학 수시 학생부종합/교과 면접고사 및 원서접수 마감일시 전수 반영</p>

        <!-- 4-Stage Deadlines Timeline Banner -->
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
                <div>건국대, 경기대, 광운대, 동국대, 숙명여대, 연세대(미래), 한국외대</div>
            </div>
            <div class="deadline-card d4">
                <div class="deadline-card-title">🟣 4차 마감 <span>9/11(금) 18:00</span></div>
                <div>서울대, 성균관대, 서강대, 한양대, 중앙대, 경희대, 세종대, 숭실대, 아주대, 인하대, 가천대 등 23개교</div>
            </div>
        </div>

        <!-- Legend -->
        <div class="legend-bar">
            <span style="font-weight: 700; color: var(--navy-primary);">구분 범례:</span>
            <div class="legend-item"><span class="dot" style="background: #ef4444;"></span> 🚨 원서접수 마감</div>
            <div class="legend-item"><span class="dot" style="background: #f87171;"></span> ★ 2027 수능일 (11/19 목)</div>
            <div class="legend-item"><span class="dot" style="background: #6366f1;"></span> 수능 전 면접</div>
            <div class="legend-item"><span class="dot" style="background: #3b82f6;"></span> 수능 후 1주차 면접 (11/21~22)</div>
            <div class="legend-item"><span class="dot" style="background: #14b8a6;"></span> 수능 후 2주차 면접 (11/27~29)</div>
            <div class="legend-item"><span class="dot" style="background: #22c55e;"></span> 수능 후 3주차 면접 (12/4~6)</div>
            <div class="legend-item"><span class="dot" style="background: #f59e0b;"></span> 수능 후 4주차 면접 (12/11~14)</div>
        </div>
    </div>

    <!-- Month Navigation Tabs -->
    <div class="month-tabs">
        <button class="tab-btn" onclick="switchMonth('sep')" style="color:#dc2626; border-color:#fca5a5;">🚨 2026년 9월 (원서접수 마감)</button>
        <button class="tab-btn active" onclick="switchMonth('oct')">2026년 10월 달력 (수능전 면접)</button>
        <button class="tab-btn" onclick="switchMonth('nov')">2026년 11월 달력 (수능/피크면접)</button>
        <button class="tab-btn" onclick="switchMonth('dec')">2026년 12월 달력 (최종면접)</button>
    </div>

    <!-- ========================================== -->
    <!-- 2026년 9월 달력 (수시 원서접수 마감) -->
    <!-- ========================================== -->
    <div id="month-sep" class="calendar-section">
        <div class="calendar-month-title">
            <span>🚨 2026년 9월 (수시 원서접수 4단계 마감 타임라인)</span>
            <span style="font-size: 14px; font-weight: 600; color: #dc2626;">원서접수 기간: 2026년 9월 7일(월) ~ 9월 11일(금)</span>
        </div>

        <div class="calendar-grid">
            <div class="day-header sun">일</div>
            <div class="day-header">월</div>
            <div class="day-header">화</div>
            <div class="day-header">수</div>
            <div class="day-header">목</div>
            <div class="day-header">금</div>
            <div class="day-header sat">토</div>

            <!-- Week 1: Aug 30 - Sep 5 -->
            <div class="day-cell other-month"><div class="day-number">30</div></div>
            <div class="day-cell other-month"><div class="day-number">31</div></div>
            <div class="day-cell"><div class="day-number">1</div></div>
            <div class="day-cell"><div class="day-number">2</div></div>
            <div class="day-cell"><div class="day-number">3</div></div>
            <div class="day-cell"><div class="day-number">4</div></div>
            <div class="day-cell sat"><div class="day-number">5</div></div>

            <!-- Week 2: Sep 6 - Sep 12 -->
            <div class="day-cell sun"><div class="day-number">6</div></div>
            <div class="day-cell">
                <div class="day-number">7 <span class="d-day-tag" style="background:#e0e7ff; color:#3730a3;">접수개시</span></div>
                <div class="events-container">
                    <div class="event-badge badge-pre">📝 2027 수시 원서접수 전국 일제 개시</div>
                </div>
            </div>
            <div class="day-cell"><div class="day-number">8</div></div>

            <!-- Sep 9 (D1 Deadline) -->
            <div class="day-cell" style="background-color: #fef2f2; border: 2px solid #ef4444;">
                <div class="day-number" style="color:#dc2626;">9 <span class="d-day-tag" style="background:#dc2626; color:#fff;">🔴 1차 마감</span></div>
                <div class="events-container">
                    <div class="event-badge" style="background:#fecdd3; color:#9f1239; border-color:#f43f5e;">
                        <strong>[고려대] 17:00 마감</strong> <span class="deadline-tag tag-d1">9/9 17시</span><br>
                        전국 주요 대학 중 가장 빠른 최선두 마감!
                    </div>
                </div>
            </div>

            <!-- Sep 10 (D2 Deadline) -->
            <div class="day-cell" style="background-color: #fefce8; border: 2px solid #eab308;">
                <div class="day-number" style="color:#854d0e;">10 <span class="d-day-tag" style="background:#eab308; color:#fff;">🟡 2차 마감</span></div>
                <div class="events-container">
                    <div class="event-badge" style="background:#fef08a; color:#713f12; border-color:#eab308;">
                        <strong>[연세대(서울)] 17:00 마감</strong> <span class="deadline-tag tag-d2">9/10 17시</span><br>
                        <strong>[이화여대] 17:00 마감</strong> <span class="deadline-tag tag-d2">9/10 17시</span>
                    </div>
                </div>
            </div>

            <!-- Sep 11 (D3 & D4 Deadline) -->
            <div class="day-cell" style="background-color: #f3e8ff; border: 2px solid #a855f7;">
                <div class="day-number" style="color:#6b21a8;">11 <span class="d-day-tag" style="background:#a855f7; color:#fff;">🟣 최종 마감</span></div>
                <div class="events-container">
                    <div class="event-badge" style="background:#dbeafe; color:#1e40af; border-color:#3b82f6;">
                        <strong>🔵 17:00 3차 마감:</strong><br>
                        건국대, 동국대, 숙명여대, 한국외대, 광운대, 경기대, 연세대(미래)
                    </div>
                    <div class="event-badge" style="background:#f3e8ff; color:#6b21a8; border-color:#a855f7;">
                        <strong>🟣 18:00 4차 마감 (전국 최종):</strong><br>
                        서울대, 성균관대, 서강대, 한양대, 중앙대, 경희대, 세종대, 숭실대, 아주대, 인하대, 가천대, 서울여대, 명지대, 단국대, 상명대 등 23개교
                    </div>
                </div>
            </div>

            <div class="day-cell sat"><div class="day-number">12</div></div>

            <!-- Week 3 ~ 5 -->
            <div class="day-cell sun"><div class="day-number">13</div></div>
            <div class="day-cell"><div class="day-number">14</div></div>
            <div class="day-cell"><div class="day-number">15</div></div>
            <div class="day-cell"><div class="day-number">16</div></div>
            <div class="day-cell"><div class="day-number">17</div></div>
            <div class="day-cell"><div class="day-number">18</div></div>
            <div class="day-cell sat"><div class="day-number">19</div></div>

            <div class="day-cell sun"><div class="day-number">20</div></div>
            <div class="day-cell"><div class="day-number">21</div></div>
            <div class="day-cell"><div class="day-number">22</div></div>
            <div class="day-cell"><div class="day-number">23</div></div>
            <div class="day-cell"><div class="day-number">24</div></div>
            <div class="day-cell"><div class="day-number">25</div></div>
            <div class="day-cell sat"><div class="day-number">26</div></div>

            <div class="day-cell sun"><div class="day-number">27</div></div>
            <div class="day-cell"><div class="day-number">28</div></div>
            <div class="day-cell"><div class="day-number">29</div></div>
            <div class="day-cell"><div class="day-number">30</div></div>
            <div class="day-cell other-month"><div class="day-number">1</div></div>
            <div class="day-cell other-month"><div class="day-number">2</div></div>
            <div class="day-cell other-month"><div class="day-number">3</div></div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- 2026년 10월 달력 -->
    <!-- ========================================== -->
    <div id="month-oct" class="calendar-section active">
        <div class="calendar-month-title">
            <span>🍁 2026년 10월 (수능 전 면접 구간)</span>
            <span style="font-size: 14px; font-weight: 600; color: var(--text-muted);">수능 D-49 ~ D-19</span>
        </div>

        <div class="calendar-grid">
            <div class="day-header sun">일</div>
            <div class="day-header">월</div>
            <div class="day-header">화</div>
            <div class="day-header">수</div>
            <div class="day-header">목</div>
            <div class="day-header">금</div>
            <div class="day-header sat">토</div>

            <!-- Week 1: Sep 27 - Oct 3 -->
            <div class="day-cell other-month"><div class="day-number">27</div></div>
            <div class="day-cell other-month"><div class="day-number">28</div></div>
            <div class="day-cell other-month"><div class="day-number">29</div></div>
            <div class="day-cell other-month"><div class="day-number">30</div></div>
            <div class="day-cell"><div class="day-number">1</div></div>
            <div class="day-cell"><div class="day-number">2</div></div>
            <div class="day-cell sat"><div class="day-number">3</div></div>

            <!-- Week 2: Oct 4 - Oct 10 -->
            <div class="day-cell sun"><div class="day-number">4</div></div>
            <div class="day-cell"><div class="day-number">5</div></div>
            <div class="day-cell"><div class="day-number">6</div></div>
            <div class="day-cell"><div class="day-number">7</div></div>
            <div class="day-cell"><div class="day-number">8</div></div>
            <div class="day-cell"><div class="day-number">9</div></div>
            <div class="day-cell sat"><div class="day-number">10</div></div>

            <!-- Week 3: Oct 11 - Oct 17 -->
            <div class="day-cell sun"><div class="day-number">11</div></div>
            <div class="day-cell"><div class="day-number">12</div></div>
            <div class="day-cell"><div class="day-number">13</div></div>
            <div class="day-cell"><div class="day-number">14</div></div>
            <div class="day-cell">
                <div class="day-number">15 <span class="d-day-tag" style="background:#e0e7ff; color:#3730a3;">D-35</span></div>
                <div class="events-container">
                    <div class="event-badge badge-pre">[상명대] 국가안보 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                </div>
            </div>
            <div class="day-cell"><div class="day-number">16</div></div>
            <div class="day-cell sat"><div class="day-number">17</div></div>

            <!-- Week 4: Oct 18 - Oct 24 -->
            <div class="day-cell sun">
                <div class="day-number">18 <span class="d-day-tag" style="background:#e0e7ff; color:#3730a3;">D-32</span></div>
                <div class="events-container">
                    <div class="event-badge badge-pre">[동국대] 실기(문예창작) <span class="deadline-tag tag-d3">9/11 17시</span></div>
                </div>
            </div>
            <div class="day-cell"><div class="day-number">19</div></div>
            <div class="day-cell"><div class="day-number">20</div></div>
            <div class="day-cell"><div class="day-number">21</div></div>
            <div class="day-cell"><div class="day-number">22</div></div>
            <div class="day-cell"><div class="day-number">23</div></div>
            <div class="day-cell sat">
                <div class="day-number">24 <span class="d-day-tag" style="background:#fee2e2; color:#991b1b;">★ 납치유의</span></div>
                <div class="events-container">
                    <div class="event-badge badge-pre">[이화여대] 고교추천(교과) <span class="deadline-tag tag-d2">9/10 17시</span></div>
                </div>
            </div>

            <!-- Week 5: Oct 25 - Oct 31 -->
            <div class="day-cell sun">
                <div class="day-number">25 <span class="d-day-tag" style="background:#e0e7ff; color:#3730a3;">D-25</span></div>
                <div class="events-container">
                    <div class="event-badge badge-pre">[이화여대] 고교추천(교과) <span class="deadline-tag tag-d2">9/10 17시</span></div>
                    <div class="event-badge badge-pre">[성균관대] 성과인재(체육) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-pre">[국민대] 어학특기자 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                </div>
            </div>
            <div class="day-cell"><div class="day-number">26</div></div>
            <div class="day-cell"><div class="day-number">27</div></div>
            <div class="day-cell"><div class="day-number">28</div></div>
            <div class="day-cell"><div class="day-number">29</div></div>
            <div class="day-cell"><div class="day-number">30</div></div>
            <div class="day-cell sat">
                <div class="day-number">31 <span class="d-day-tag" style="background:#e0e7ff; color:#3730a3;">D-19</span></div>
                <div class="events-container">
                    <div class="event-badge badge-pre">[고려대] 사이버국방 <span class="deadline-tag tag-d1">9/9 17시</span></div>
                    <div class="event-badge badge-pre">[광운대] 참빛인재I/SW <span class="deadline-tag tag-d3">9/11 17시</span></div>
                    <div class="event-badge badge-pre">[명지대] 교과면접(인문) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-pre">[동덕여대] 창의리더 (60%) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                </div>
            </div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- 2026년 11월 달력 -->
    <!-- ========================================== -->
    <div id="month-nov" class="calendar-section">
        <div class="calendar-month-title">
            <span>🍂 2026년 11월 (★ 수능 시행 및 면접 피크 구간)</span>
            <span style="font-size: 14px; font-weight: 600; color: #dc2626;">★ 수능일: 11월 19일 (목)</span>
        </div>

        <div class="calendar-grid">
            <div class="day-header sun">일</div>
            <div class="day-header">월</div>
            <div class="day-header">화</div>
            <div class="day-header">수</div>
            <div class="day-header">목</div>
            <div class="day-header">금</div>
            <div class="day-header sat">토</div>

            <!-- Week 1: Nov 1 - Nov 7 -->
            <div class="day-cell sun">
                <div class="day-number">1 <span class="d-day-tag" style="background:#e0e7ff; color:#3730a3;">D-18</span></div>
                <div class="events-container">
                    <div class="event-badge badge-pre">[연세대] 특기자(국제) <span class="deadline-tag tag-d2">9/10 17시</span></div>
                    <div class="event-badge badge-pre">[성균관대] 과학인재(7배수) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-pre">[광운대] 참빛인재I/SW <span class="deadline-tag tag-d3">9/11 17시</span></div>
                    <div class="event-badge badge-pre">[명지대] 교과면접(자연) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-pre">[동덕여대] 창의리더 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                </div>
            </div>
            <div class="day-cell"><div class="day-number">2</div></div>
            <div class="day-cell"><div class="day-number">3</div></div>
            <div class="day-cell"><div class="day-number">4</div></div>
            <div class="day-cell"><div class="day-number">5</div></div>
            <div class="day-cell"><div class="day-number">6</div></div>
            <div class="day-cell sat">
                <div class="day-number">7 <span class="d-day-tag" style="background:#e0e7ff; color:#3730a3;">D-12</span></div>
                <div class="events-container">
                    <div class="event-badge badge-pre">[고려대] 계열적합(인문) <span class="deadline-tag tag-d1">9/9 17시</span></div>
                </div>
            </div>

            <!-- Week 2: Nov 8 - Nov 14 -->
            <div class="day-cell sun">
                <div class="day-number">8 <span class="d-day-tag" style="background:#e0e7ff; color:#3730a3;">D-11</span></div>
                <div class="events-container">
                    <div class="event-badge badge-pre">[고려대] 계열적합(자연) <span class="deadline-tag tag-d1">9/9 17시</span></div>
                    <div class="event-badge badge-pre">[성균관대] 성과인재 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                </div>
            </div>
            <div class="day-cell"><div class="day-number">9</div></div>
            <div class="day-cell"><div class="day-number">10</div></div>
            <div class="day-cell"><div class="day-number">11</div></div>
            <div class="day-cell"><div class="day-number">12</div></div>
            <div class="day-cell"><div class="day-number">13</div></div>
            <div class="day-cell sat">
                <div class="day-number">14</div>
                <div class="events-container">
                    <div class="event-badge badge-w1">[국민대] 알고리즘/국제 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                </div>
            </div>

            <!-- Week 3: Nov 15 - Nov 21 -->
            <div class="day-cell sun"><div class="day-number">15</div></div>
            <div class="day-cell"><div class="day-number">16</div></div>
            <div class="day-cell"><div class="day-number">17</div></div>
            <div class="day-cell"><div class="day-number">18</div></div>
            
            <!-- CSAT DAY -->
            <div class="day-cell" style="background-color: #fef2f2; border: 2px solid #ef4444;">
                <div class="day-number" style="color:#dc2626;">19 <span class="d-day-tag" style="background:#dc2626; color:#fff;">★ 수능일</span></div>
                <div class="events-container">
                    <div class="event-badge badge-csat">★ 2027 대학수학능력시험</div>
                </div>
            </div>

            <div class="day-cell"><div class="day-number">20</div></div>
            <div class="day-cell sat">
                <div class="day-number">21 <span class="d-day-tag" style="background:#dbeafe; color:#1e40af;">D+2 (수능후1주)</span></div>
                <div class="events-container">
                    <div class="event-badge badge-w1">★ [연세대] 활동우수(인문) <span class="deadline-tag tag-d2">9/10 17시</span></div>
                    <div class="event-badge badge-w1">★ [한국외대] 면접형 (50%) <span class="deadline-tag tag-d3">9/11 17시</span></div>
                    <div class="event-badge badge-w1">[이화여대] 미래인재(면접) <span class="deadline-tag tag-d2">9/10 17시</span></div>
                    <div class="event-badge badge-w1">[국민대] 프런티어(자연) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w1">[인하대] 인하미래인재 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w1">[아주대] 첨단융합인재 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w1">[덕성여대] 덕성인재II <span class="deadline-tag tag-d4">9/11 18시</span></div>
                </div>
            </div>

            <!-- Week 4: Nov 22 - Nov 28 -->
            <div class="day-cell sun">
                <div class="day-number">22 <span class="d-day-tag" style="background:#dbeafe; color:#1e40af;">D+3 (수능후1주)</span></div>
                <div class="events-container">
                    <div class="event-badge badge-w1">[연세대] 활동우수(자연) <span class="deadline-tag tag-d2">9/10 17시</span></div>
                    <div class="event-badge badge-w1">[이화여대] 미래인재(자연) <span class="deadline-tag tag-d2">9/10 17시</span></div>
                    <div class="event-badge badge-w1">[국민대] 프런티어(인문) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w1">[세종대] 세종인재(면접) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w1">[한양대] 면접형(공대비대면) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w1">[아주대] ACE(공대) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                </div>
            </div>
            <div class="day-cell"><div class="day-number">23</div></div>
            <div class="day-cell"><div class="day-number">24</div></div>
            <div class="day-cell"><div class="day-number">25</div></div>
            <div class="day-cell"><div class="day-number">26</div></div>
            <div class="day-cell">
                <div class="day-number">27 <span class="d-day-tag" style="background:#ccfbf1; color:#0f766e;">D+8 (수능후2주)</span></div>
                <div class="events-container">
                    <div class="event-badge badge-w2">★ [서울대] 일반전형 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w2">★ [숭실대] 미래인재 (50%) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                </div>
            </div>
            <div class="day-cell sat">
                <div class="day-number">28 <span class="d-day-tag" style="background:#ccfbf1; color:#0f766e;">D+9 (수능후2주)</span></div>
                <div class="events-container">
                    <div class="event-badge badge-w2">[서울대] 일반(의약학 MMI) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w2">★ [시립대] 종합I(인문 50%) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w2">[숙명여대] 숙명인재/SW <span class="deadline-tag tag-d3">9/11 17시</span></div>
                    <div class="event-badge badge-w2">[서울과기대] 학교생활우수 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w2">[명지대] 명지인재 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w2">[서울여대] 바롬인재 (50%) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w2">[숭실대] SW우수자 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                </div>
            </div>

            <!-- Week 5: Nov 29 - Nov 30 -->
            <div class="day-cell sun">
                <div class="day-number">29 <span class="d-day-tag" style="background:#ccfbf1; color:#0f766e;">D+10 (수능후2주)</span></div>
                <div class="events-container">
                    <div class="event-badge badge-w2">[연세대] 국제형 <span class="deadline-tag tag-d2">9/10 17시</span></div>
                    <div class="event-badge badge-w2">[서울시립대] 종합I(자연) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w2">[숙명여대] 숙명인재 <span class="deadline-tag tag-d3">9/11 17시</span></div>
                    <div class="event-badge badge-w2">[아주대] ACE(경영/인문) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w2">[명지대] 명지인재 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                </div>
            </div>
            <div class="day-cell"><div class="day-number">30</div></div>
            <div class="day-cell other-month"><div class="day-number">1</div></div>
            <div class="day-cell other-month"><div class="day-number">2</div></div>
            <div class="day-cell other-month"><div class="day-number">3</div></div>
            <div class="day-cell other-month"><div class="day-number">4</div></div>
            <div class="day-cell other-month"><div class="day-number">5</div></div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- 2026년 12월 달력 -->
    <!-- ========================================== -->
    <div id="month-dec" class="calendar-section">
        <div class="calendar-month-title">
            <span>❄️ 2026년 12월 (최종 면접 및 집중 구간)</span>
            <span style="font-size: 14px; font-weight: 600; color: #166534;">★ 12/5~6 주요 대학 면접 겹침 피크</span>
        </div>

        <div class="calendar-grid">
            <div class="day-header sun">일</div>
            <div class="day-header">월</div>
            <div class="day-header">화</div>
            <div class="day-header">수</div>
            <div class="day-header">목</div>
            <div class="day-header">금</div>
            <div class="day-header sat">토</div>

            <!-- Week 1: Nov 29 - Dec 5 -->
            <div class="day-cell other-month"><div class="day-number">29</div></div>
            <div class="day-cell other-month"><div class="day-number">30</div></div>
            <div class="day-cell"><div class="day-number">1</div></div>
            <div class="day-cell"><div class="day-number">2</div></div>
            <div class="day-cell"><div class="day-number">3</div></div>
            <div class="day-cell">
                <div class="day-number">4 <span class="d-day-tag" style="background:#dcfce7; color:#166534;">D+15 (수능후3주)</span></div>
                <div class="events-container">
                    <div class="event-badge badge-w3">★ [서울대] 지역균형 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                </div>
            </div>
            <div class="day-cell sat" style="background-color: #fffbeb; border: 2px solid #f59e0b;">
                <div class="day-number">5 <span class="d-day-tag" style="background:#f59e0b; color:#fff;">★ 면접 겹침 피크</span></div>
                <div class="events-container">
                    <div class="event-badge badge-w3">[서울대] 지균(의예) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w3">★ [건국대] KU자기추천 <span class="deadline-tag tag-d3">9/11 17시</span></div>
                    <div class="event-badge badge-w3">★ [경희대] 네오르네상스 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w3">★ [중앙대] CAU탐구/성장 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w3">[한양대] 면접형(의예) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w3">[단국대] DKU인재(인문) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                </div>
            </div>

            <!-- Week 2: Dec 6 - Dec 12 -->
            <div class="day-cell sun" style="background-color: #fffbeb; border: 2px solid #f59e0b;">
                <div class="day-number">6 <span class="d-day-tag" style="background:#f59e0b; color:#fff;">★ 면접 겹침 피크</span></div>
                <div class="events-container">
                    <div class="event-badge badge-w3">★ [건국대] KU자기추천 <span class="deadline-tag tag-d3">9/11 17시</span></div>
                    <div class="event-badge badge-w3">★ [경희대] 네오르네상스 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w3">★ [중앙대] 융합(의)/탐구 <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w3">[성균관대] 성균인재(지역) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w3">[한양대] 면접형(사범대) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                    <div class="event-badge badge-w3">[단국대] DKU인재(자연) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                </div>
            </div>
            <div class="day-cell"><div class="day-number">7</div></div>
            <div class="day-cell"><div class="day-number">8</div></div>
            <div class="day-cell"><div class="day-number">9</div></div>
            <div class="day-cell"><div class="day-number">10</div></div>
            <div class="day-cell">
                <div class="day-number">11 <span class="d-day-tag" style="background:#fef3c7; color:#92400e;">D+22 (수능후4주)</span></div>
                <div class="events-container">
                    <div class="event-badge badge-w4">★ [동국대] Do Dream (1차) <span class="deadline-tag tag-d3">9/11 17시</span></div>
                </div>
            </div>
            <div class="day-cell sat">
                <div class="day-number">12 <span class="d-day-tag" style="background:#fef3c7; color:#92400e;">D+23 (수능후4주)</span></div>
                <div class="events-container">
                    <div class="event-badge badge-w4">★ [동국대] Do Dream (2차) <span class="deadline-tag tag-d3">9/11 17시</span></div>
                </div>
            </div>

            <!-- Week 3: Dec 13 - Dec 19 -->
            <div class="day-cell sun">
                <div class="day-number">13 <span class="d-day-tag" style="background:#fef3c7; color:#92400e;">D+24 (수능후4주)</span></div>
                <div class="events-container">
                    <div class="event-badge badge-w4">★ [동국대] Do Dream (3차) <span class="deadline-tag tag-d3">9/11 17시</span></div>
                </div>
            </div>
            <div class="day-cell">
                <div class="day-number">14</div>
                <div class="events-container">
                    <div class="event-badge badge-w4">[아주대] ACE/의사(의약) <span class="deadline-tag tag-d4">9/11 18시</span></div>
                </div>
            </div>
            <div class="day-cell"><div class="day-number">15</div></div>
            <div class="day-cell"><div class="day-number">16</div></div>
            <div class="day-cell"><div class="day-number">17</div></div>
            <div class="day-cell"><div class="day-number">18</div></div>
            <div class="day-cell sat"><div class="day-number">19</div></div>

            <!-- Week 4: Dec 20 - Dec 26 -->
            <div class="day-cell sun"><div class="day-number">20</div></div>
            <div class="day-cell"><div class="day-number">21</div></div>
            <div class="day-cell"><div class="day-number">22</div></div>
            <div class="day-cell"><div class="day-number">23</div></div>
            <div class="day-cell"><div class="day-number">24</div></div>
            <div class="day-cell"><div class="day-number">25</div></div>
            <div class="day-cell sat"><div class="day-number">26</div></div>

            <!-- Week 5: Dec 27 - Dec 31 -->
            <div class="day-cell sun"><div class="day-number">27</div></div>
            <div class="day-cell"><div class="day-number">28</div></div>
            <div class="day-cell"><div class="day-number">29</div></div>
            <div class="day-cell"><div class="day-number">30</div></div>
            <div class="day-cell"><div class="day-number">31</div></div>
            <div class="day-cell other-month"><div class="day-number">1</div></div>
            <div class="day-cell other-month"><div class="day-number">2</div></div>
        </div>
    </div>
</div>

<script>
    function switchMonth(monthId) {
        document.querySelectorAll('.calendar-section').forEach(el => el.classList.remove('active'));
        document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));

        document.getElementById('month-' + monthId).classList.add('active');
        event.currentTarget.classList.add('active');
    }
</script>

</body>
</html>
"""

paths = [
    u"C:\\Users\\그램\\Documents\\antiG\\reports\\2027_면접고사_월달력_일정표.html",
    u"C:\\Users\\그램\\Desktop\\입시분석 참고자료\\2027 종합전형\\2027_면접고사_월달력_일정표.html",
    u"C:\\Users\\그램\\.gemini\\antigravity-ide\\brain\\dab98dcb-4efc-446d-b15d-de74f81386f5\\2027_interview_calendar.html"
]

for p in paths:
    with open(p, 'wb') as f:
        f.write(html_content.encode('utf-8'))

print "SUCCESSFULLY_UPDATED_INTERVIEW_CALENDARS"
