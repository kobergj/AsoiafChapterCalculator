
def mapChapters(yamlbook, bname):
    values = []

    for i, chaptername in enumerate(yamlbook.keys()):
        values.append([yamlbook[chaptername][0],
                       yamlbook[chaptername][1],
                       chaptername,
                       i,
                       bname]
                    )

    return values
