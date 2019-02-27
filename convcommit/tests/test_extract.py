from convc import extract


def test_extract1():
    e1 = extract("feat: feature X fixed")
    assert e1['type'] == "feat"
    assert e1['description'] == "feature X fixed"
    assert e1['body'] == ""
    assert e1['footer'] == ""
