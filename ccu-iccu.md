# iCCU 教務系統 Reference

URL: `https://www026220.ccu.edu.tw`

CCU's new unified academic affairs system, replacing the old kiki-based subsystems from 115 academic year onward. Handles enrollment, schedule, grades, and graduation checks.

## Authentication & Navigation

- Uses CCU SSO via CAS (`cas.ccu.edu.tw`)
- If already logged into eCourse2 or other CCU systems, SSO session should carry over
- **After login, a main menu appears** with options for different functions (schedule, grades, enrollment, etc.). Use `take_snapshot` to read the menu items and navigate to the desired function.

### Login → Menu → Function flow:
1. Navigate to `www026220.ccu.edu.tw`
2. If redirected to CAS login → handle login (same as other CCU systems)
3. After login → `take_snapshot` to see the main menu
4. Click the relevant menu item (課表, 成績, 選課, etc.)
5. `take_snapshot` again to read the data on the target page

## Network

- **May require campus network or VPN.** If connection fails, inform the user.
- The domain `www026220.ccu.edu.tw` is an internal CCU server.

## Exploration Strategy

Since this is a newer system with no public API documentation, use a discovery approach:

### Step 1: Identify the tech stack
After login, `take_snapshot` and look for clues:
- React/Vue/Angular → SPA, likely has JSON API endpoints
- Traditional server-rendered HTML → use DOM parsing
- Check `<script>` tags for framework bundles

### Step 2: If SPA — find the API
Use `evaluate_script` to check the Network tab or intercept fetch calls:
```javascript
// Override fetch to log API calls
const originalFetch = window.fetch;
window.fetchLog = [];
window.fetch = function(...args) {
  window.fetchLog.push(args[0]);
  return originalFetch.apply(this, args);
};
// Then interact with the page and check window.fetchLog
```

Or simply navigate around and use `take_snapshot` to see what data appears.

### Step 3: Extract data
Whether via API or DOM, extract:

#### 課表 (Schedule/Timetable)
- Navigate to the schedule section
- `take_snapshot` to get the timetable grid
- Parse: time slots × weekdays × course info (name, classroom)

#### 成績查詢 (Grades)
- Navigate to grade query section
- May need to select semester
- `take_snapshot` to get grade table
- Parse: course name, score, grade letter, credits, GPA

#### 選課 (Enrollment)
- Only functional during enrollment periods
- Can browse available courses, check enrollment status
- **Never auto-enroll** — only read data, don't submit enrollment actions unless explicitly asked

#### 畢業學分 (Graduation Credit Check)
- Navigate to graduation audit section
- `take_snapshot` to get credit summary
- Parse: required vs completed credits by category

## CCU Time Slots

CCU uses numbered time slots:

| Slot | Time |
|------|------|
| 1 | 08:10-09:00 |
| 2 | 09:10-10:00 |
| 3 | 10:10-11:00 |
| 4 | 11:10-12:00 |
| N | 12:10-13:00 |
| 5 | 13:10-14:00 |
| 6 | 14:10-15:00 |
| 7 | 15:10-16:00 |
| 8 | 16:10-17:00 |
| 9 | 17:10-18:00 |
| A | 18:30-19:20 |
| B | 19:25-20:15 |
| C | 20:20-21:10 |

**Note**: Verify these times against the actual iCCU schedule display. They may have been updated.

## 開課資料查詢

Two sources available:

### Option A: eCourse2 課程大綱 (Public, no login)
URL: `https://ecourse2.ccu.edu.tw/local/syllabus/syllabus_dep.php`
- Browse course syllabi by department
- No login required
- Use `take_snapshot` to parse

### Option B: iCCU (after login)
- Navigate to the course listing section in iCCU's menu after login
- May have more detailed information including enrollment counts

## 學校行事曆

Page: `https://www.ccu.edu.tw/p/412-1000-1078.php`

The academic calendar is published on CCU's official website as an embedded PDF viewer. To extract it:
1. Navigate to the page above
2. Look for the PDF embed or direct download link
3. Known PDF URL pattern: `https://www.ccu.edu.tw/var/file/0/1000/img/570/{filename}.pdf`
4. Download the PDF and read it to extract key dates (semester start/end, exam weeks, holidays, enrollment periods)

The PDF contains both semester 1 and semester 2 calendars. Parse the relevant semester based on current date.

## 學生請假系統

URL: `https://www026186.ccu.edu.tw/stu_off/`

- Uses CCU SSO
- Use `take_snapshot` after login to see the leave application interface
- Can read: leave history, leave status
- Can help fill leave application forms if user asks
- **Never auto-submit** — always confirm with the user before submitting any leave request

## 課程地圖

URL: `https://www026158.ccu.edu.tw/all_dept_list.php`

- Browse curriculum maps by department
- Use `take_snapshot` to parse department list and course requirements
- May require campus network

## Important Notes

- **Read-only by default** — never submit enrollment, drop, or modification actions unless the user explicitly asks
- If iCCU is unreachable (campus network restriction), clearly inform the user and suggest connecting to CCU VPN
- Page structure is unknown until runtime — always `take_snapshot` first to understand what you're working with
- The system may have different views depending on whether it's enrollment period or not
