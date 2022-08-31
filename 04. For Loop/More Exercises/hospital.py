period = int(input())
doctors = 7
all_treated_patients = 0
all_untreated_patients = 0
for i in range(1, period + 1):

    if i % 3 == 0:
        if all_untreated_patients > all_treated_patients:
            doctors += 1

    patients_for_the_day = int(input())
    if patients_for_the_day <= doctors:
        untreated_patients = 0
        treated_patients = patients_for_the_day
    else:
        untreated_patients = patients_for_the_day - doctors
        treated_patients = patients_for_the_day - untreated_patients

    all_treated_patients += treated_patients
    all_untreated_patients += untreated_patients

print(f"Treated patients: {all_treated_patients}.")
print(f"Untreated patients: {all_untreated_patients}.")