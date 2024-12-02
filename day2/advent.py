with open('input.txt') as f:
    reports = [[int(level) for level in report.split(' ')] for report in f.read().split('\n')]


def is_safe(report):
    diffs = []
    for i in range(len(report)-1):
        level, next = report[i], report[i+1]
        diff = level - next
        diffs.append(diff)
    return all(-4 < diff < 0 for diff in diffs) or all(4 > diff > 0 for diff in diffs)


def is_safe_2(report):
    for i in range(len(report)):
        subset = report[:i] + report[i+1:]
        if (is_safe(subset)):
            return True

safe_reports_1, safe_reports_2 = 0, 0
for report in reports:
    if (is_safe(report)):
        safe_reports_1 += 1
    else:
        if (is_safe_2(report)):
            safe_reports_2 += 1

answer1, answer2 = safe_reports_1, safe_reports_1 + safe_reports_2
print(answer1, answer2)
