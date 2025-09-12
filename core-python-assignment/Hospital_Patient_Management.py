def search_patients(patients,disease):
    return[p["Name"] for p in patients if p["Disease"].lower()==disease.lower()]
patients=[]
n=int(input('number of patients: '))
for _ in range(n):
    name=input('Enter patient name: ')
    age=int(input('Enter patient age: '))
    disease=input('Enter patient disease: ')
    patients.append({'Name': name, 'Age': age, 'Disease': disease})
search_disease=input('disease to search: ')
print(f'Patients with {search_disease}:', search_patients(patients,search_disease))