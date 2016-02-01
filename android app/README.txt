The android project is located at /app/PIII/NurseApp/.
Please put the patient_record.txt at /data/data/com.example.nurseapp/files/patientRecord/.
Please put the passwords.txt at /data/data/com.example.nurseapp/files/patientRecord/.

The application loads all user login data at launch.
You can then login as either a nurse or a physician.

After login, the application loads all previous data of the patients.

For a nurse:
You can look up existing patients based on health number.
- individual patient data will show up
You will then have the option to
- view previous records
- create new visits (based on current time)
- update the patient's vitals (to the latest visit)
- record the doctor visit time (to the latest visit)

Or you can create a new patient.
- you must enter their name, health number and birthday

Or you can access a list of patients.
- categorized and ordered by decreasing urgency

For a physician:
You can look up existing patients based on health number.
- individual patient data will show up
You will then have the option to
- view previous records
- create new prescriptions (to the latest visit)
