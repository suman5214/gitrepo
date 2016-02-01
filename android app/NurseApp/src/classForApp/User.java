package classForApp;

// check the newVisit method, see if it works without last line

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.io.FileInputStream;
import java.util.Scanner;

import classForApp.Patient;

public class User implements Serializable {

	private static HashMap<String, ArrayList<String>> users = new HashMap<String, ArrayList<String>>();
	private Patient currentPatient;
	private Calendar cal;
	private DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
	private DateFormat timeFormat = new SimpleDateFormat("HH:mm:ss");
	private String date;
	private String time;
	private HashMap<String, Patient> patientList;

	public User() {
	}

	/**
	 * @return the arrivalTime for the current patient
	 */
	public ArrayList<String> getArrivalTime() {
		return currentPatient.getArrivalTime();
	}

	/**
	 * @return the list of all Patients in the system
	 */
	public HashMap<String, Patient> getPatientList() {
		patientList = Patient.getPatientList();
		return patientList;
	}

	/**
	 * @param healthNum
	 * @return true if the patient with healthNum exists in the system
	 */
	public boolean checkPatient(String healthNum) {
		patientList = Patient.getPatientList();
		return patientList.containsKey(healthNum);
	}

	/**
	 * 
	 * @param healthNum
	 * @return an ArrayList of the patient's health card number, name and birth
	 *         date.
	 * 
	 */
	public ArrayList<Object> lookUpPatient(String healthNum) {
		patientList = Patient.getPatientList();
		currentPatient = patientList.get(healthNum);
		ArrayList<Object> data = new ArrayList<Object>();
		data.add(currentPatient.getHealthNum());
		data.add(currentPatient.getName());
		data.add(currentPatient.getBirthdate());
		return data;
	}

	/**
	 * loads Patient class instances from patient_records.txt or from the
	 * Serializable file patient_data
	 * 
	 * returns true if Serializable file exists and data is loaded from it false
	 * if Serializable file does not exists and data is loaded from the text
	 * file
	 * 
	 * @return boolean
	 * @throws IOException
	 */
	public boolean load() throws IOException {

		File data = new File(
				"/data/data/com.example.nurseapp/files/patientRecord/patient_data");

		File txt = new File(
				"/data/data/com.example.nurseapp/files/patientRecord/patient_records.txt");
		if (!txt.exists()) {
			Patient emptyPatient = new Patient("a", "a", "a");
			return false;
		}

		Scanner pr_reader = new Scanner(
				new FileInputStream(
						"/data/data/com.example.nurseapp/files/patientRecord/patient_records.txt"));

		if (data.exists()) {
			ObjectInputStream objectinputstream = null;
			FileInputStream fileInput = null;
			try {
				fileInput = new FileInputStream(
						"/data/data/com.example.nurseapp/files/patientRecord/patient_data");
				objectinputstream = new ObjectInputStream(fileInput);
				ArrayList<Patient> patientList = (ArrayList<Patient>) objectinputstream
						.readObject();
				for (Patient p : patientList) {
					Patient newPatient = new Patient(p);
				}

			} catch (Exception e) {

				e.printStackTrace();
			} finally {
				if (objectinputstream != null) {
					objectinputstream.close();
				}
			}
			return true;
		}

		else {

			String pr_line = null;

			// reads patients from patient_records.txt which is constant
			while (pr_reader.hasNextLine()) {
				pr_line = pr_reader.nextLine();
				String num = pr_line.split(",")[0];
				String name = pr_line.split(",")[1];
				String birthdate = pr_line.split(",")[2];
				Patient pat = new Patient(name, birthdate, num);
			}
			pr_reader.close();
			return false;
		}

	}

	/**
	 * saves patients to the text file new_patient_records.txt.
	 * 
	 * @throws IOException
	 */

	public void save() throws IOException {
		ObjectOutputStream oos = null;
		FileOutputStream fout = null;
		File data = new File(
				"/data/data/com.example.nurseapp/files/patientRecord/patient_data");
		try {
			data.delete();
			fout = new FileOutputStream(
					"/data/data/com.example.nurseapp/files/patientRecord/patient_data",
					true);
			oos = new ObjectOutputStream(fout);
			ArrayList<Patient> patientList = new ArrayList<Patient>();
			patientList.addAll(Patient.getPatientList().values());
			oos.writeObject(patientList);
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			if (oos != null) {
				oos.close();
			}
		}

	}

	/**
	 * records a date of the new visit (current date) for the current patient
	 */
	public void newVisit() {
		currentPatient = Patient.getPatientList().get(currentPatient.getHealthNum());
		ArrayList<String> oldVisits = Patient.getPatientList()
				.get(currentPatient.getHealthNum()).getArrivalTime();
		HashMap<String, String> oldDoctorVisits = currentPatient
				.getDoctorVisits();
		cal = Calendar.getInstance();
		date = dateFormat.format(cal.getTime());
		if (!oldVisits.contains(date)) {
			oldVisits.add(date);
			currentPatient.setArrivalTime(oldVisits);
			Patient.setPatientList(patientList);
			oldDoctorVisits.put(date, "Not Visited");
			currentPatient.setDoctorVisits(oldDoctorVisits);
			currentPatient.setSeenByDoctor(false);
			int urgency = 0;
			Calendar currentDate = Calendar.getInstance();

			String[] birthData = currentPatient.getBirthdate().split("-");
			int y = Integer.parseInt(birthData[0]);
			int m = Integer.parseInt(birthData[1]);
			int d = Integer.parseInt(birthData[2]);

			Calendar birthDate = Calendar.getInstance();

			birthDate.set(y, m, d);

			long currentTime = currentDate.getTimeInMillis();
			long birthTime = birthDate.getTimeInMillis();

			long diffenerce = (currentTime - birthTime) / (60 * 60 * 1000 * 24);
			if (diffenerce / 365 < 2) {
				urgency += 1;
			}
			currentPatient.setUrgency(urgency);
		}
		patientList = Patient.getPatientList();
		patientList.put(currentPatient.getHealthNum(), currentPatient);
		Patient.setPatientList(patientList);

	}

	/**
	 * Update the current visit with the patient's vitals.
	 * 
	 * @param time
	 * @param temperature
	 * @param bloodPressure
	 * @param heartRate
	 */
	public void updateVisit(String temperature, String bloodPressure,
			String heartRate) {

		cal = Calendar.getInstance();
		time = timeFormat.format(cal.getTime());
		date = currentPatient.getArrivalTime().get(
				currentPatient.getArrivalTime().size() - 1);
		HashMap<String, HashMap<String, String>> oldTemperature = currentPatient
				.getTemperature();
		if (oldTemperature.containsKey(date)) {
			oldTemperature.get(date).put(time, temperature);
			currentPatient.setTemperature(oldTemperature);
		} else {
			HashMap<String, String> newVisit = new HashMap<String, String>();
			newVisit.put(time, temperature);
			oldTemperature.put(date, newVisit);
			currentPatient.setTemperature(oldTemperature);
		}

		HashMap<String, HashMap<String, String>> oldBloodPressure = currentPatient
				.getBloodPressure();
		if (oldBloodPressure.containsKey(date)) {
			oldBloodPressure.get(date).put(time, bloodPressure);
			currentPatient.setBloodPressure(oldBloodPressure);
		} else {
			HashMap<String, String> newVisit = new HashMap<String, String>();
			newVisit.put(time, bloodPressure);
			oldBloodPressure.put(date, newVisit);
			currentPatient.setBloodPressure(oldBloodPressure);
		}

		HashMap<String, HashMap<String, String>> oldHeartRate = currentPatient
				.getHeartRate();
		if (oldHeartRate.containsKey(date)) {
			oldHeartRate.get(date).put(time, heartRate);
			currentPatient.setHeartRate(oldHeartRate);
		} else {
			HashMap<String, String> newVisit = new HashMap<String, String>();
			newVisit.put(time, heartRate);
			oldHeartRate.put(date, newVisit);
			currentPatient.setHeartRate(oldHeartRate);
		}
		currentPatient.setCurrentHeartRate(heartRate);
		currentPatient.setCurrentPressure(bloodPressure);
		currentPatient.setCurrentTemperature(temperature);
		currentPatient.assignUrgency();

		patientList = Patient.getPatientList();
		patientList.put(currentPatient.getHealthNum(), currentPatient);
		Patient.setPatientList(patientList);

	}

	/**
	 * Return a hashmap for the specified date, with the time as the key and a
	 * list of temperature, blood pressure and heart rate as the value.
	 * 
	 * @param date
	 * @return a map of the visit time to the recorded vitals at that time.
	 */
	public HashMap<String, ArrayList<String>> viewVitalRecord(String date) {
		HashMap<String, ArrayList<String>> record = new HashMap<String, ArrayList<String>>();

		if (!currentPatient.getTemperature().containsKey(date)
				&& !currentPatient.getBloodPressure().containsKey(date)
				&& !currentPatient.getHeartRate().containsKey(date)) {
			return null;
		}

		// Create the set of times that data was collected during this visit.
		Set<String> copyOfTime = new TreeSet<String>();
		copyOfTime.addAll(currentPatient.getTemperature().get(date).keySet());
		copyOfTime.addAll(currentPatient.getBloodPressure().get(date).keySet());
		copyOfTime.addAll(currentPatient.getHeartRate().get(date).keySet());

		// Iterate over the collection times for the specified visit, and map
		// the vitals to the
		// corresponding time if any vitals were recorded.
		for (String time : copyOfTime) {
			ArrayList<String> vitals = new ArrayList<String>();
			if (currentPatient.getTemperature().get(date).containsKey(time)) {
				vitals.add(currentPatient.getTemperature().get(date).get(time));
			} else {
				vitals.add(null);
			}
			if (currentPatient.getBloodPressure().get(date).containsKey(time)) {
				vitals.add(currentPatient.getBloodPressure().get(date)
						.get(time));
			} else {
				vitals.add(null);
			}
			if (currentPatient.getHeartRate().get(date).containsKey(time)) {
				vitals.add(currentPatient.getHeartRate().get(date).get(time));
			} else {
				vitals.add(null);
			}
			record.put(time, vitals);
		}
		return record;
	}

	/**
	 * sets the patient with healthNum as the current patient
	 * 
	 * @param healthNum
	 */
	public void setCurrentPatient(String healthNum) {
		currentPatient = Patient.getPatientList().get(healthNum);
	}

	public void newPatient(String name, String birthdate, String healthnum) {
		Patient p = new Patient(name, birthdate, healthnum);

	}

	public void newDoctorVisit(String time) {
		cal = Calendar.getInstance();
		date = currentPatient.getArrivalTime().get(
				currentPatient.getArrivalTime().size() - 1);
		HashMap<String, String> oldDoctorVisit = currentPatient
				.getDoctorVisits();
		oldDoctorVisit.put(date, time);
		currentPatient.setDoctorVisits(oldDoctorVisit);
		currentPatient.setSeenByDoctor(true);

		patientList = Patient.getPatientList();
		patientList.put(currentPatient.getHealthNum(), currentPatient);
		Patient.setPatientList(patientList);
	}

	public boolean seenByDoctor() {
		return currentPatient.isSeenByDoctor();
	}

	public String viewByUrgency() {
		ArrayList<Patient> patients = Patient.getPatientListUrgency();
		String list = "Urgercy Name HeatlthNumber\n";
		for (Patient p : patients) {
			list = list + p.getUrgency() + " " + p.getName() + " "
					+ p.getHealthNum() + "\n";
		}
		return list;
	}

	public void recordPrescriptions(String prescription) {
		date = currentPatient.getArrivalTime().get(
				currentPatient.getArrivalTime().size() - 1);
		HashMap<String, String> oldPrescriptions = currentPatient
				.getPrescriptions();
		if (oldPrescriptions.containsKey(date)) {
			String oldPrescription = oldPrescriptions.get(date);
			oldPrescription = oldPrescription + "\n" + prescription;
			oldPrescriptions.put(date, oldPrescription);
		} else {
			oldPrescriptions.put(date, prescription);
		}
		currentPatient.setPrescriptions(oldPrescriptions);
	}

	public String viewPrescriptions(String date) {
		if (currentPatient.getPrescriptions().containsKey(date)) {
			return currentPatient.getPrescriptions().get(date);
		}
		return null;
	}

	public boolean loadUsers() throws IOException {
		File txt = new File(
				"/data/data/com.example.nurseapp/files/patientRecord/passwords.txt");
		if (!txt.exists()) {
			ArrayList<String> userData = new ArrayList<String>();
			users.put("", userData);
			return false;
		}

		Scanner pr_reader = new Scanner(
				new FileInputStream(
						"/data/data/com.example.nurseapp/files/patientRecord/passwords.txt"));

		String pr_line = null;

		// reads users from passwords.txt which is constant
		while (pr_reader.hasNextLine()) {
			pr_line = pr_reader.nextLine();
			String username = pr_line.split(",")[0];
			String password = pr_line.split(",")[1];
			String userType = pr_line.split(",")[2];
			ArrayList<String> userData = new ArrayList<String>();
			userData.add(password);
			userData.add(userType);
			users.put(username, userData);
		}
		return true;
	}

	public boolean login(String username, String password) {
		if (users.containsKey(username)) {
			if (users.get(username).get(0).equals(password)) {
				return true;
			} else {
				return false;
			}
		} else {
			return false;
		}
	}

	public String Usertype(String username) {
		return users.get(username).get(1);

	}

	public HashSet<String> numList() {
		HashSet<String> list = new HashSet<String>();
		for (Patient p : Patient.getPatientList().values()) {
			list.add(p.getHealthNum());
		}
		return list;

	}

	public boolean checkSameNum(String num) {
		return numList().contains(num);
	}

	public HashMap<String, String> viewDoctorVisit() {
		return currentPatient.getDoctorVisits();
	}

}