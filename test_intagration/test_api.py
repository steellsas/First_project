from unittest.mock import patch,MagicMock
from calc.api_mo import get_only_numbers, API

def test_api_read_only_numbers():
    test_data = ["1,3,4,5,332,ab,c21,v32,v323v","521,532,633,c2c"]
    expected = "1|3|4|5|32|521|532|633"

    face_api = MagicMock()
    fake_api.get_data.return_value = test_data
    with patch('calt.api_mo.API', fake_api):
        result = get_only_numbers()
        assert result == expected
