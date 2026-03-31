class Person:
    def __init__(self,Name,Age,Gender):
        self.Name = Name
        self.Age = Age
        self.Gender = Gender                                                                                                                                                                                    
    def get_details(self):
        return f"Name: {self.Name}, Age: {self.Age}, Gender: {self.Gender}"     
                                                                        
class Patient(Person):
    def __init__(self, Name, Age, Gender, Disease):
        super().__init__(Name, Age, Gender)
        self.Disease = Disease
    def get_details(self):
        return f"{super().get_details()}, Disease: {self.Disease}"
class Doctor(Person):
    def __init__(self, Name, Age, Gender, Specialization = None):
        super().__init__(Name, Age, Gender)
        self.Specialization = Specialization
    def get_details(self):
        return f"{super().get_details()}, Specialization: {self.Specialization}"
    def assign_patient(self, patient):
        if not hasattr(self, 'patients'):
            self.patients = []
        self.patients.append(patient)               
    def get_assigned_patients(self):
        if hasattr(self, 'patients'):
            return [patient.get_details() for patient in self.patients]
        else:
            return "No patients assigned."      
    def __str__(self):
        return f"Doctor: {self.Name}, Specialization: {self.Specialization}"    
class Hospital: 
    def __init__(self):
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def assign_patient_to_doctor(self, patient_name, doctor_name):
        patient = next((p for p in self.patients if p.Name == patient_name), None)
        doctor = next((d for d in self.doctors if d.Name == doctor_name), None)
        if patient and doctor:
            doctor.assign_patient(patient)
            return f"Patient {patient_name} assigned to Doctor {doctor_name}."
        return "Patient or Doctor not found."

    def get_patients_by_doctor(self, doctor_name):
        doctor = next((d for d in self.doctors if d.Name == doctor_name), None)
        if doctor:
            return doctor.get_assigned_patients()       
        return "Doctor not found."      
    def search_patient(self, patient_name):
        patient = next((p for p in self.patients if p.Name == patient_name), None)
        if patient:
            return patient.get_details()
        return "Patient not found." 

    def display_doctors(self):
        if self.doctors:
            return [str(doctor) for doctor in self.doctors]
        return "No doctors available."          
    def display_patients(self):
        if self.patients:
            return [patient.get_details() for patient in self.patients]
        return "No patients available." 
    def menu(self): 
        while True:
            print("\nHospital Management System")
            print("1. Add Doctor")
            print("2. Add Patient")
            print("3. Assign Patient to Doctor")
            print("4. View Patients by Doctor")
            print("5. Search Patient by Name")
            print("6. Display All Doctors")
            print("7. Display All Patients")
            print("8. Exit")
            choice = input("Enter your choice: ")       
            if choice == '1':
                name = input("Enter Doctor's Name: ")
                age = input("Enter Doctor's Age: ")
                gender = input("Enter Doctor's Gender: ")
                specialization = input("Enter Doctor's Specialization: ")
                doctor = Doctor(name, age, gender, specialization)
                hospital.add_doctor(doctor)
                print(f"Doctor {name} added successfully.")
            elif choice == '2':
                name = input("Enter Patient's Name: ")
                age = input("Enter Patient's Age: ")
                gender = input("Enter Patient's Gender: ")
                disease = input("Enter Patient's Disease: ")
                patient = Patient(name, age, gender, disease)
                hospital.add_patient(patient)
                print(f"Patient {name} added successfully.") 
            elif choice == '3': 
                patient_name = input("Enter Patient's Name: ")
                doctor_name = input("Enter Doctor's Name: ")
                result = hospital.assign_patient_to_doctor(patient_name, doctor_name)
                print(result)       
            elif choice == '4': 
                doctor_name = input("Enter Doctor's Name: ")
                patients = hospital.get_patients_by_doctor(doctor_name)
                if isinstance(patients, list):
                    print(f"Patients assigned to {doctor_name}:")
                    for patient in patients:
                        print(patient)
                else:
                    print(patients)        
            elif choice == '5': 
                patient_name = input("Enter Patient's Name: ")
                result = hospital.search_patient(patient_name)
                print(result)           
            elif choice == '6':         
                doctors = hospital.display_doctors()
                if isinstance(doctors, list):
                    print("Doctors in the hospital:")
                    for doctor in doctors:
                        print(doctor)
                else:
                    print(doctors)  
            elif choice == '7': 
                patients = hospital.display_patients()
                if isinstance(patients, list):
                    print("Patients in the hospital:")
                    for patient in patients:
                        print(patient)
                else:
                    print(patients) 
            elif choice == '8':     
                print("Exiting the system. Goodbye!")
                break   
hospital = Hospital()
hospital.menu()     
