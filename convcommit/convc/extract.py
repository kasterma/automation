import re

type_scope_re = re.compile(r"([^(]+)\(([^)]+)\)")


def extract(commitm):
    commitm = commitm.split('\n', 1)
    header = commitm[0].split(":")
    body_and_footer = "" if len(commitm) == 1 else commitm[1]
    breaking = any(l.startswith("BREAKING CHANGE:") for l in body_and_footer.split("\n"))
    if len(header) > 1:
        scope_match = type_scope_re.match(header[0])
        if scope_match:
            commit_type = scope_match.group(1).strip()
            commit_scope = scope_match.group(2)
        else:
            commit_type = header[0]
            commit_scope = None
        rv = {
            'type': commit_type,
            'scope': commit_scope,
            'description': header[1].strip() if len(header) > 1 else header[0],
            'body_and_footer': body_and_footer,
            'breaking': breaking
        }
    else:
        rv = {
            'type': None,
            'scope': None,
            'description': header[0],
            'body_and_footer': body_and_footer,
             'breaking': breaking
        }
    return rv
