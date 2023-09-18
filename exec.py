from utils import parse_date, time_delta, extract_lines

print(parse_date("30 de Agosto de 2023"))
print(time_delta('18 de Janeiro de 2023','18 de Janeiro de 2024'))

l_file = extract_lines('input_text.txt')[0]
l_file2 = extract_lines('input_text.txt')[1]
print(time_delta(l_file,l_file2))