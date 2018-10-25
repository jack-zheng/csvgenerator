print(generate_row('suffix', [1,3,5], ['a', 'b', 'c', 'd', 'e', 'f']))
'''
Testing:
Data Prepare:
position_list = [1,3,5]
headers = [
        ['COL0', 'COL1', 'COL2', 'COL3', 'COL4', 'COL5', 'COL6'],
        ['col0', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6']
    ]
    
template_row = ['a', 'b', 'c', 'd', 'e', 'f']
increment_count = 4
'''

headers = [
        ['COL0', 'COL1', 'COL2', 'COL3', 'COL4', 'COL5', 'COL6'],
        ['col0', 'col1', 'col2', 'col3', 'col4', 'col5', 'col6']
    ]
template_row = ['a', 'b', 'c', 'd', 'e', 'f']
generate_file([1,3,5], headers, template_row, 4)