temperature_exact = '39.3' # (жара)
temperature_approx = int(float(temperature_exact)) + 1 # преобразуйте значение в целое и прибавьте 1
print("За окном", str(temperature_exact), "градусов Цельсия. Это почти", str(temperature_approx))