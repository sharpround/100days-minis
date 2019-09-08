from make_data import parse_name_line
import pandas as pd

def test_parse_name_line():
    index = 34
    line = '{"state":"OH","gender":"F","year":"1910","name":"Mary","number":"1099"}'
    
    expected = pd.DataFrame(index=[index], data={"state":"OH","gender":"F","year":1910,"name":"Mary", "number":1099})

    result = name_line_to_row(index, line)

    assert result == expected