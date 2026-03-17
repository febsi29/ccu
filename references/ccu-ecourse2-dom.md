# CCU eCourse2 DOM Extraction Reference

CCU eCourse2 runs on Moodle LMS. Base URL: `https://ecourse2.ccu.edu.tw`

**Moodle AJAX Web Service is disabled by CCU.** All data extraction must use Chrome DevTools MCP's `take_snapshot` + DOM parsing approach.

## General Strategy

For every piece of data:
1. `navigate_page` to the correct URL
2. Wait for page load
3. `take_snapshot` to get the accessibility tree
4. Parse the tree for the data you need
5. If there are links to follow (e.g., individual courses), `click` then `take_snapshot` again

## Authentication

eCourse2 uses CCU SSO via CAS (`cas.ccu.edu.tw`):

1. Navigate to `https://ecourse2.ccu.edu.tw`
2. `take_snapshot` — if you see a CAS login form, handle login
3. After login, you'll land on the Moodle dashboard

## 1. Course List (Dashboard)

**URL:** `https://ecourse2.ccu.edu.tw/my/`

After login, the dashboard shows all enrolled courses as course cards or a list.

`take_snapshot` and look for:
- Course names (links to `/course/view.php?id=XXXXX`)
- Extract course IDs from the URLs — you'll need these for everything else
- Course short names or codes if visible

Store the list of `{course_id, course_name}` for subsequent operations.

### Alternative: Course overview block
Some Moodle themes show courses in a sidebar or overview block. If the dashboard is sparse, try:
- `https://ecourse2.ccu.edu.tw/my/courses.php` — dedicated course listing page

## 2. Course Content (Sections & Materials)

**URL:** `https://ecourse2.ccu.edu.tw/course/view.php?id={course_id}`

Each course page shows sections (usually organized by week or topic). Each section contains:
- **Resources** (files): PDF, slides, documents — shown as links with file icons
- **Activities**: assignments, quizzes, forums — shown as links with activity icons
- **Labels**: inline text/HTML content
- **URLs**: external links (Google Slides, YouTube, etc.)

`take_snapshot` and look for:
- Section headers (Week 1, Week 2, or topic names)
- Links with file icons → these are downloadable files
- Links pointing to `/mod/assign/view.php` → assignments
- Links pointing to `/mod/forum/view.php` → forums
- Links pointing to `/mod/resource/view.php` → single files
- Links pointing to `/mod/page/view.php` → page content
- Links pointing to `/mod/url/view.php` → external URLs
- Links pointing to `/mod/quiz/view.php` → quizzes

### Downloading files
For file resources:
1. Click the file link or navigate to the resource URL
2. Moodle will either directly download or show a page with a download link
3. For `/mod/resource/view.php?id=XXX`, it usually auto-redirects to the file download

### Google Slides / Docs (external links)
If a module links to `docs.google.com`:
```
Original:  https://docs.google.com/presentation/d/{id}/edit
Export as: https://docs.google.com/presentation/d/{id}/export/pdf

Original:  https://docs.google.com/document/d/{id}/edit
Export as: https://docs.google.com/document/d/{id}/export?format=pdf
```
Navigate to the export URL to trigger download.

## 3. Announcements

Moodle announcements are forum posts, usually in a forum called "公告" or "Announcements".

**Step 1:** On the course page, find and click the announcements forum link.
- Look for links containing `/mod/forum/view.php` with text like "公告", "Announcements", or "最新消息"
- It's usually the first item in the first section

**Step 2:** `take_snapshot` on the forum page.
- Each announcement shows: title, author, date, and reply count
- Click into each announcement to read the full content

**Step 3:** For each announcement, `take_snapshot` to get:
- Full body text
- Any embedded links or attachments
- Parse for: exam dates, room changes, class cancellations, deadlines, TA info

### Reading ALL announcements
Don't just read the latest one. Go through every announcement in the forum — important policies (grading breakdown, late submission rules, exam format) are often in early-semester posts.

If the forum has multiple pages, click "Next" or page numbers to load more.

## 4. Assignments

**Option A: Assignment index (recommended — all at once)**

**URL:** `https://ecourse2.ccu.edu.tw/mod/assign/index.php?id={course_id}`

This page lists ALL assignments for a course in a table. `take_snapshot` to get:
- Assignment names
- Due dates
- Submission status
- Grades

This is much faster than clicking into each assignment individually.

**Option B: Individual assignment (for details)**

**URL:** `https://ecourse2.ccu.edu.tw/mod/assign/view.php?id={module_id}`

From the course page, click each assignment link. `take_snapshot` to get:
- Assignment name
- Due date and time
- Description / instructions (may be long)
- Submission status (submitted / not submitted)
- Grade (if released)
- Allowed submission types (file upload, online text, etc.)
- File size limits, accepted file types

**Option C: Calendar (deadlines across ALL courses)**

**URL:** `https://ecourse2.ccu.edu.tw/calendar/view.php?view=upcoming`

Shows upcoming events across ALL courses. Best for "這週有什麼作業?" type queries.

`take_snapshot` and look for:
- Event names (assignment due dates, quiz openings, etc.)
- Course names
- Dates and times

Also try monthly view: `https://ecourse2.ccu.edu.tw/calendar/view.php?view=month`

## 5. Grades

**URL:** `https://ecourse2.ccu.edu.tw/grade/report/user/index.php?id={course_id}`

⚠️ The `id` parameter is **required** — without it the page errors.

`take_snapshot` to get the grade table:
- Grade items (assignment names, quiz names, etc.)
- Individual scores
- Percentages
- Course total
- Category subtotals

To check grades for all courses, loop through each course ID.

### Grade overview (all courses at once)

**URL:** `https://ecourse2.ccu.edu.tw/grade/report/overview/index.php`

Shows a summary of grades across all enrolled courses. `take_snapshot` to get:
- Course names
- Overall grade per course

## 6. Notifications

**URL:** `https://ecourse2.ccu.edu.tw/message/index.php`

Shows all Moodle notifications: new announcements, assignment reminders, grade releases, forum replies.

`take_snapshot` to get:
- Notification titles
- Source (which course / activity)
- Timestamps
- Read/unread status

Click individual notifications to see full content.

## 7. User Profile

**URL:** `https://ecourse2.ccu.edu.tw/user/profile.php`

`take_snapshot` to get:
- Student name
- Student ID (may be shown as username or ID number)
- Email
- Enrolled courses list

## Batch Operation Strategy

When syncing all courses (the most common operation), follow this order for efficiency:

```
1. Dashboard (/my/) → get all course IDs and names
2. Calendar upcoming → get ALL deadlines across courses in ONE page
3. Grade overview → get ALL course grades in ONE page
4. For each course:
   a. Course page → snapshot sections, collect material links
   b. Assignment index → snapshot all assignments in ONE page
   c. Announcements forum → snapshot all announcements
   d. (Optional) Grade detail → snapshot detailed grades
```

Steps 2 and 3 save a lot of time by getting cross-course data in single pages instead of visiting each course individually.

## URL Pattern Reference

| What | URL Pattern |
|------|-------------|
| Dashboard | `/my/` |
| Course list | `/my/courses.php` |
| Course page | `/course/view.php?id={course_id}` |
| Course info | `/course/info.php?id={course_id}` |
| Assignment (single) | `/mod/assign/view.php?id={module_id}` |
| Assignment index | `/mod/assign/index.php?id={course_id}` |
| Forum | `/mod/forum/view.php?id={module_id}` |
| Forum discussion | `/mod/forum/discuss.php?d={discussion_id}` |
| Resource (file) | `/mod/resource/view.php?id={module_id}` |
| Page | `/mod/page/view.php?id={module_id}` |
| Quiz | `/mod/quiz/view.php?id={module_id}` |
| Grade report | `/grade/report/user/index.php?id={course_id}` |
| Grade overview | `/grade/report/overview/index.php` |
| Calendar upcoming | `/calendar/view.php?view=upcoming` |
| Calendar monthly | `/calendar/view.php?view=month` |
| Notifications | `/message/index.php` |
| User profile | `/user/profile.php` |
| Syllabus browse | `/local/syllabus/syllabus_dep.php` |

All URLs are relative to `https://ecourse2.ccu.edu.tw`.

## Performance Tips

- **Reuse tabs**: use `list_pages` and `select_page` instead of opening new tabs for every page
- **Calendar first**: the upcoming events page gives you deadlines across all courses in one snapshot
- **Grade overview first**: the overview page gives you all course grades in one snapshot
- **Assignment index**: use `/mod/assign/index.php?id={course_id}` instead of clicking each assignment
- **Wait for load**: don't snapshot too fast — wait for page to fully load or you'll get incomplete data
- **Batch by course**: finish all pages for one course before moving to the next, to minimize back-and-forth navigation

## Common Issues

- **CAS login redirect**: if any page redirects to `cas.ccu.edu.tw`, session expired → re-login
- **"缺少必須要的參數"**: navigated to a URL without required parameters (e.g., grade page without course ID)
- **Empty sections**: some course sections are hidden or empty — normal, skip them
- **Restricted access**: some resources require specific enrollment — inform user and skip
- **Collapsed sections**: large courses may collapse sections by default — may need to click to expand
- **Pagination**: forums and file lists may span multiple pages — check for "Next" links
- **Encoding**: eCourse2 uses UTF-8, but downloaded file names may need careful handling
