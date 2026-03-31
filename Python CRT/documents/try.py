'''
Here is a detailed real-time scenario-based problem statement for a Python Object-Oriented Programming (OOP) project on Hospital Management System, written in a clean and formal style without emojis.

---

## Project Title: Hospital Management System using Python OOP

---

## Problem Statement

In a medium-sized city, *Vignan Multi-Specialty Hospital* has been managing its operations manually. The hospital currently stores all doctor and patient details in physical registers. As the patient count grows, the management finds it increasingly difficult to manage and retrieve information efficiently. There are frequent delays in assigning patients to doctors, and the administrative staff often struggle to track ongoing treatments.

The hospital administration has decided to move to a basic software system that will help them manage patient and doctor records digitally. Since the hospital does not have a large IT budget, they need a lightweight, console-based application that can be developed quickly and maintained easily.

As a Python developer, you are tasked with building this system using Object-Oriented Programming principles. The system should allow hospital staff to add doctor and patient details, assign patients to specific doctors, and retrieve reports based on doctor or patient names.

---

## Functional Requirements

1. Create a Person class that serves as a base class for both doctors and patients. This class should contain:

   * Name
   * Age
   * Gender
   * A method to return formatted personal details

2. Create a Patient class that inherits from Person and includes:

   * Disease information
   * A method to return full patient details

3. Create a Doctor class that inherits from Person and includes:

   * Specialization
   * A private list to store assigned patients
   * Methods to assign a patient, retrieve doctor details, and list assigned patients

4. Implement a menu-driven interface that allows the following actions:

   * Add a new doctor
   * Add a new patient
   * Assign a patient to a doctor
   * View all patients assigned to a particular doctor
   * Search and view details of a specific patient

5. Use the following OOP principles:
   * Encapsulation: Use private variables where necessary (e.g., patient list inside the doctor class)
   * Inheritance: Use a base class (Person) to reduce code duplication
   * Constructors: Use __init__ methods to initialize class objects
   * Method overriding and reuse using super()
---
## Use Case Scenario
Dr. Anjali, a cardiologist at the hospital, is registered in the system. A new patient, Arun, visits the hospital and is diagnosed with a heart condition. His details are entered into the system, and he is assigned to Dr. Anjali. The hospital staff later want to view all the patients under Dr. Anjali’s care and verify Arun’s medical records. This should be done quickly through the system without manually browsing through any physical files.
---

## Expected Features

* Doctors can be registered with their specialization and personal details.
* Patients can be registered with their disease and personal details.
* Patients can be assigned to doctors.
* Doctor records include all assigned patients.
* A search functionality to find a patient’s information by name.
* All data should be handled in memory using class objects (file handling is optional).'''