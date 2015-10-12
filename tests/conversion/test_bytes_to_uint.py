import pytest


@pytest.mark.parametrize(
    ('val,expected'),
    (
        ('0', 0),
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
        ('6', 6),
        ('7', 7),
        ('8', 8),
        ('9', 9),
        ('10', 10),
        ('010', 10),
        ('1234567890', 1234567890),
        ('9876543210', 9876543210),
    )
)
def test_bytes_to_uint(deployed_contracts, val, expected):
    sl = deployed_contracts.StringUtils
    actual = sl.bytesToUInt.call(val)
    assert actual == expected
