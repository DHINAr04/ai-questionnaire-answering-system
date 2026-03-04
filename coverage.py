def coverage_summary(results):

    total = len(results)

    answered = 0
    not_found = 0

    for q, a, c in results:

        if a == "Not found in references.":
            not_found += 1
        else:
            answered += 1

    coverage = (answered / total) * 100 if total > 0 else 0

    return {
        "total_questions": total,
        "answered": answered,
        "not_found": not_found,
        "coverage_percent": round(coverage, 2)
    }