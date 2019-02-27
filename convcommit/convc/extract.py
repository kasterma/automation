def extract(commitm):
    commitm = commitm.split('\n')
    header = commitm[0].split(":")
    rv = {
        'type': header[0] if len(header) > 1 else "",
        'description': header[1].strip() if len(header) > 1 else header[0],
        'body': "",
        'footer': ""
    }
    return rv
