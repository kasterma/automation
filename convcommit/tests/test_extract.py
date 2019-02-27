from convc import extract


def test_extract1():
    e1 = extract("feat: feature X fixed")
    assert e1['type'] == "feat"
    assert e1['scope'] is None
    assert e1['description'] == "feature X fixed"
    assert e1['body_and_footer'] == ""
    assert e1['breaking'] == False


def test_extract2():
    e1 = extract("feat: feature X fixed\n\nbody body\n\nfooterfooter\n")
    assert e1['type'] == "feat"
    assert e1['scope'] is None
    assert e1['description'] == "feature X fixed"
    assert e1['body_and_footer'] == "\nbody body\n\nfooterfooter\n"
    assert e1['breaking'] == False


def test_extract3():
    e1 = extract("feat: feature X fixed\n\nbody body\n\nfooterfooter\n")
    assert e1['type'] == "feat"
    assert e1['scope'] is None
    assert e1['description'] == "feature X fixed"
    assert e1['body_and_footer'] == "\nbody body\n\nfooterfooter\n"
    assert e1['breaking'] == False


def test_extract4():
    e1 = extract("feat: feature X fixed\n\nbody body\n\nBREAKING CHANGE: footerfooter\n")
    assert e1['type'] == "feat"
    assert e1['scope'] is None
    assert e1['description'] == "feature X fixed"
    assert e1['body_and_footer'] == "\nbody body\n\nBREAKING CHANGE: footerfooter\n"
    assert e1['breaking'] == True

def test_extract5():
    e1 = extract("feat(ssccooppee): feature X fixed")
    assert e1['type'] == "feat"
    assert e1['scope'] == "ssccooppee"
    assert e1['description'] == "feature X fixed"
    assert e1['body_and_footer'] == ""
    assert e1['breaking'] == False
