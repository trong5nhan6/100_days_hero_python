def calculate_can_chi_calendar(year):
    can_list = ['Canh', 'Tân', 'Nhâm', 'Quý',
                'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
    chi_list = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý',
                'Sửu', 'Dần', 'Mẹo', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']
    can_name = can_list[year % 10]
    chi_name = chi_list[year % 12]
    result = f'{can_name} {chi_name}'
    return result


print(calculate_can_chi_calendar(2024))
print(calculate_can_chi_calendar(2023))
print(calculate_can_chi_calendar(1997))
