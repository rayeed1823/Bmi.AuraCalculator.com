from django.shortcuts import render


def bmi_calculator(request):
    context = {}


    if request.method == "POST":

        height_unit = request.POST.get("height_unit")
        height_m = 0.0

        if height_unit == "ft":

            ft = float(request.POST.get("ft") or 0)
            inch = float(request.POST.get("inch") or 0)
            total_inches = (ft * 12) + inch
            height_m = total_inches * 0.0254
        elif height_unit == "cm":
            cm = float(request.POST.get("cm") or 0)
            height_m = cm * 0.01

        age = int(request.POST.get("age") or 25)
        gender = request.POST.get("gender") or "other"
        weight_unit = request.POST.get("weight_unit")
        weight_input = float(request.POST.get("weight") or 0)
        weight_kg = 0.0

        if weight_unit == "kg":
            weight_kg = weight_input
        elif weight_unit == "lbs":
            weight_kg = weight_input * 0.453592


        if height_m > 0 and weight_kg > 0:
            bmi = weight_kg / (height_m ** 2)

            if bmi <= 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 25:
                category = "Normal weight"
            elif 25 <= bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"



        context = {
            'bmi': bmi if 'bmi' in locals() else None,
            'category': category if 'category' in locals() else "",
            'age': age if 'age' in locals() else 25,
            'gender': gender if 'gender' in locals() else "other",
        }
        return render(request, 'index.html', context)