package classForApp;

import java.util.Date;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.HashMap;

public class Patient implements java.io.Serializable {

	private static final long serialVersionUID = -2998530050366788412L;

	// class variable for the list of patients
	private static HashMap<String, Patient> patientList = new HashMap<String, Patient>();

	// patient data
	private String name;
	private String birthdate;
	private String healthNum;
	private DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

	// collected data
	private ArrayList<String> arrivalTime = new ArrayList<String>();
	private HashMap<String, HashMap<String, String>> temperature = new HashMap<String, HashMap<String, String>>();
	private HashMap<String, HashMap<String, String>> bloodPressure = new HashMap<String, HashMap<String, String>>();
	private HashMap<String, HashMap<String, String>> heartRate = new HashMap<String, HashMap<String, String>>();
	private HashMap<String, HashMap<String, Integer>> category = new HashMap<String, HashMap<String, Integer>>();

	private int urgency;

	private String currentTemperature;
	private String currentPressure;
	private String currentHeartRate;
	private String currentCategory;

	private boolean seenByDoctor;

	public boolean isSeenByDoctor() {
		return seenByDoctor;
	}

	public void setSeenByDoctor(boolean seenByDoctor) {
		this.seenByDoctor = seenByDoctor;
	}

	private HashMap<String, String> doctorVisits = new HashMap<String, String>();

	public HashMap<String, String> getDoctorVisits() {
		return doctorVisits;
	}

	public void setDoctorVisits(HashMap<String, String> doctorVisits) {
		this.doctorVisits = doctorVisits;
	}

	HashMap<String, String> prescriptions = new HashMap<String, String>();

	public HashMap<String, String> getPrescriptions() {
		return prescriptions;
	}

	public void setPrescriptions(HashMap<String, String> prescriptions) {
		this.prescriptions = prescriptions;
	}

	public static void setPatientList(HashMap<String, Patient> patientList) {
		Patient.patientList = patientList;
	}

	private HashMap<String, HashMap<String, String>> symptoms = new HashMap<String, HashMap<String, String>>();

	public Patient(Patient p) {
		Patient.patientList.put(p.getHealthNum(), p);
	}

	public Patient(String name, String birthdate, String healthNum) {
		this.name = name;
		this.birthdate = birthdate;
		this.healthNum = healthNum;
		Patient.patientList.put(healthNum, this);
	}

	/**
	 * @return the name
	 */
	public String getName() {
		return name;
	}

	/**
	 * @return the birthdate
	 */
	public String getBirthdate() {
		return birthdate;
	}

	/**
	 * @return the healthNum
	 */
	public String getHealthNum() {
		return healthNum;
	}

	/**
	 * @return the arrivalTime
	 */
	public ArrayList<String> getArrivalTime() {
		return arrivalTime;
	}

	/**
	 * @param arrivalTime
	 */
	public void setArrivalTime(ArrayList<String> arrivalTime) {
		this.arrivalTime = arrivalTime;
	}

	/**
	 * @return the temperature
	 */
	public HashMap<String, HashMap<String, String>> getTemperature() {
		return temperature;
	}

	/**
	 * @param temperature
	 */
	public void setTemperature(
			HashMap<String, HashMap<String, String>> temperature) {
		this.temperature = temperature;
	}

	public String getCurrentTemperature() {
		return currentTemperature;
	}

	public void setCurrentTemperature(String currentTemperature) {
		this.currentTemperature = currentTemperature;
	}

	public String getCurrentPressure() {
		return currentPressure;
	}

	public void setCurrentPressure(String currentPressure) {
		this.currentPressure = currentPressure;
	}

	public String getCurrentHeartRate() {
		return currentHeartRate;
	}

	public void setCurrentHeartRate(String currentHeartRate) {
		this.currentHeartRate = currentHeartRate;
	}

	public String getCurrentCategory() {
		return currentCategory;
	}

	public void setCurrentCategory(String currentCategory) {
		this.currentCategory = currentCategory;
	}

	/**
	 * @return the bloodPressure
	 */
	public HashMap<String, HashMap<String, String>> getBloodPressure() {
		return bloodPressure;
	}

	/**
	 * @param bloodPressure
	 */
	public void setBloodPressure(
			HashMap<String, HashMap<String, String>> bloodPressure) {
		this.bloodPressure = bloodPressure;
	}

	/**
	 * @return the heartRate
	 */
	public HashMap<String, HashMap<String, String>> getHeartRate() {
		return heartRate;
	}

	/**
	 * @param heartRate
	 */
	public void setHeartRate(HashMap<String, HashMap<String, String>> heartRate) {
		this.heartRate = heartRate;
	}

	/**
	 * @return the category
	 */
	public HashMap<String, HashMap<String, Integer>> getCategory() {
		return category;
	}

	/**
	 * @param category
	 */
	public void setCategory(HashMap<String, HashMap<String, Integer>> category) {
		this.category = category;
	}

	/**
	 * @return the symptoms
	 */
	public HashMap<String, HashMap<String, String>> getSymptoms() {
		return symptoms;
	}

	/**
	 * @param symptoms
	 */
	public void setSymptoms(HashMap<String, HashMap<String, String>> symptoms) {
		this.symptoms = symptoms;
	}

	/**
	 * @return the patientList
	 */
	public static HashMap<String, Patient> getPatientList() {
		return patientList;
	}

	public void assignUrgency() {

		int urgency = 0;

		Calendar currentDate = Calendar.getInstance();

		String[] birthData = this.getBirthdate().split("-");
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
		long currTemp = Long.parseLong(this.getCurrentTemperature());
		if (currTemp > 39.0) {
			urgency += 1;
		}

		long currHR = Long.parseLong(this.getCurrentHeartRate());
		if (currHR >= 100 || currHR <= 100) {
			urgency += 1;
		}

		String[] pressure = this.getCurrentPressure().split(" ");
		if (Integer.parseInt(pressure[0]) >= 90
				|| Integer.parseInt(pressure[1]) >= 140) {
			urgency += 1;
		}

		this.setUrgency(urgency);

	}


	public static ArrayList<Patient> getPatientListUrgency() {
		ArrayList<Patient> listByUrgency = new ArrayList<Patient>();
		ArrayList<Patient> urgencyZero = new ArrayList<Patient>();
		ArrayList<Patient> urgencyOne = new ArrayList<Patient>();
		ArrayList<Patient> urgencyTwo = new ArrayList<Patient>();
		ArrayList<Patient> urgencyThree = new ArrayList<Patient>();
		ArrayList<Patient> urgencyFour = new ArrayList<Patient>();

		for (Patient p : Patient.getPatientList().values()) {
			if (!p.seenByDoctor && !p.getArrivalTime().isEmpty()) {
				if (p.urgency == 1) {
					urgencyOne.add(p);
				} else if (p.urgency == 2) {
					urgencyTwo.add(p);
				} else if (p.urgency == 3) {
					urgencyThree.add(p);
				} else if (p.urgency == 4) {
					urgencyFour.add(p);
				} else if (p.urgency == 0) {
					urgencyZero.add(p);
				}
			}
		}

		listByUrgency.addAll(urgencyFour);
		listByUrgency.addAll(urgencyThree);
		listByUrgency.addAll(urgencyTwo);
		listByUrgency.addAll(urgencyOne);
		listByUrgency.addAll(urgencyZero);

		return listByUrgency;

	}

	public int getUrgency() {
		return urgency;
	}

	public void setUrgency(int urgency) {
		this.urgency = urgency;
	}

	/**
	 * @return the patientList sorted by arrival time
	 */
	// public static Map<String, Patient> getPatientListArrivalTime() {}

	/**
	 * @return the patientList sorted by urgency
	 */
	// public static Map<String, Patient> getPatientListUrgency() {}

}
