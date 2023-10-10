def replace_data(replaceItems: list, data: list) -> list:
    result = []
    sizeRepItems = len(replaceItems)

    for str in data:
        for indPair in range(sizeRepItems):
            repEl = replaceItems[sizeRepItems - 1 - indPair]["replacement"]
            sourceEl = replaceItems[sizeRepItems - 1 - indPair]["source"]
            if (repEl in str):
                if (sourceEl is None):
                    str = str.replace(repEl, "")
                else:
                    str = str.replace(repEl, sourceEl)
        if str != "":
            result.append(str)
    
    return result