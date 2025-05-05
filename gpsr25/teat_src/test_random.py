import random

# weights で確率を設定（Trueが7、Falseが3 → 合計10で70%と30%）
value = random.choices([True, False], weights=[7, 3])[0]
print(value)
