# Output Format Specification

All output files are created in the user's current working directory.

## File Structure

```
{current_directory}/
├── COURSE_SUMMARY.md          # Master course summary (primary output)
├── schedule.md                # Weekly timetable
├── deadlines.md               # Consolidated deadlines sorted by date
├── {CourseName}/              # Per-course folder (English, underscores)
│   ├── Week{N}/               # Weekly materials (if download opted in)
│   │   ├── lecture_slides.pdf
│   │   └── reading.pdf
│   └── Homework/              # Assignment-related files
│       └── HW1_instructions.pdf
```

## Naming Conventions

- **Folder names**: English, underscores for spaces (e.g., `Data_Structures/`, `Operating_Systems/`)
- **Week folders**: `Week1/`, `Week2/`, etc.
- **File names**: Keep original filenames from eCourse2 when downloading
- **Semester format**: `114-2` (academic year - semester), e.g., 114-2 = 2026 Spring
- **Dates**: Always `YYYY-MM-DD` format

## COURSE_SUMMARY.md Format

```markdown
# CCU eCourse2 - {semester} ({year} {Spring/Fall}) Course Summary
**Student:** {student_id}
**Last updated:** {YYYY-MM-DD}

---

## Course {N}: {course_name}
**Course ID:** {moodle_course_id}
**URL:** https://ecourse2.ccu.edu.tw/course/view.php?id={id}
**Instructor:** {teacher_name}

### Announcements
1. **{title}** ({YYYY-MM-DD})
   - {summary content}

2. **{title}** ({YYYY-MM-DD})
   - {summary content}

### Sections / Materials
**{section_name}**
- ✅ `{filename}` (downloaded)
- ⬜ [{title}]({url}) ({type}: Google Slides / PDF / Video)

### Assignments
1. **{assignment_name}** ⚠️ **DUE: {YYYY-MM-DD}**
   - Submission: {type}
   - URL: {url}

### Grades
- {item_name}: {score} ({percentage})

---

## ⚠️ Action Items & Deadlines

| Deadline | Course | Task |
|----------|--------|------|
| {YYYY-MM-DD} | {course} | {task description} |

---

## File Structure
```
(tree view of created directories and files)
```
```

## schedule.md Format

```markdown
# {semester} Weekly Schedule (課表)
**Last updated:** {YYYY-MM-DD}

| Time | Mon | Tue | Wed | Thu | Fri | Sat |
|------|-----|-----|-----|-----|-----|-----|
| 1 (08:10-09:00) | | | | | | |
| 2 (09:10-10:00) | | | | | | |
| 3 (10:10-11:00) | | | | | | |
| 4 (11:10-12:00) | | | | | | |
| N (12:10-13:00) | | | | | | |
| 5 (13:10-14:00) | | | | | | |
| 6 (14:10-15:00) | | | | | | |
| 7 (15:10-16:00) | | | | | | |
| 8 (16:10-17:00) | | | | | | |
| 9 (17:10-18:00) | | | | | | |
| A (18:30-19:20) | | | | | | |
| B (19:25-20:15) | | | | | | |
| C (20:20-21:10) | | | | | | |

Cell format: `{course_short_name} @{classroom}`
```

## deadlines.md Format

```markdown
# {semester} Deadlines
**Last updated:** {YYYY-MM-DD}

## Upcoming

| Date | Course | Assignment | Status |
|------|--------|-----------|--------|
| {YYYY-MM-DD} | {course} | {name} | ⬜ Not submitted |
| {YYYY-MM-DD} | {course} | {name} | ✅ Submitted |

## Past Due

| Date | Course | Assignment | Status |
|------|--------|-----------|--------|
| {YYYY-MM-DD} | {course} | {name} | ✅ Submitted |
```

## Update Rules

1. **Check before writing**: Always read existing files first
2. **Merge, don't overwrite**: If COURSE_SUMMARY.md exists, update sections rather than replacing the whole file
3. **Preserve user edits**: If user has added notes or modified content, keep their changes
4. **Update timestamp**: Always update "Last updated" date
5. **Mark downloads**: Use ✅ for downloaded files, ⬜ for pending/link-only
6. **Flag urgency**: Use ⚠️ for deadlines within 7 days, mark "TODAY" for same-day deadlines
