def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return f"BMI: {bmi:.2f} (Zayıf)"
    elif 18.5 <= bmi < 24.9:
        return f"BMI: {bmi:.2f} (Normal)"
    elif 25 <= bmi < 29.9:
        return f"BMI: {bmi:.2f} (Fazla Kilolu)"
    else:
        return f"BMI: {bmi:.2f} (Aşırı kilolu)"


if __name__ == "__main__":
    weight = float(input("Kilonuzu girin (kg): "))
    height = float(input("Boyunuzu girin (m): "))
    print(calculate_bmi(weight, height))
