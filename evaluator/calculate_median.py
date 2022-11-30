from operator import itemgetter


def get_median(queryset):

    return (
        queryset[len(queryset) // 2 + 1].grade
        if len(queryset) % 2 != 0
        else (
            queryset[len(queryset) // 2 + 1].grade
            + queryset[len(queryset) // 2].grade
        )
        // 2
    )
