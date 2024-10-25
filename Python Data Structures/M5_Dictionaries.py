cabinet = dict()
cabinet['Summer'] = 12
cabinet['Winter'] = 3
cabinet['Spring'] = 75
print(cabinet)  # {'Summer': 12, 'Winter': 3, 'Spring': 75}

print(cabinet['Winter'])   # 3

cabinet['Winter'] = cabinet['Winter'] + 2

print(cabinet)  # {'Summer': 12, 'Winter': 5, 'Spring': 75}