package com.example.nurseapp;

import java.io.IOException;
import java.util.ArrayList;
import classForApp.User;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

public class PatientInformation extends Activity {
	User user;

	@Override
	/**
	 * onCreate will initialize the intent that was passed down from the
	 * previous activity MainActivity and using the infoKey to display the
	 * patient's information.
	 */
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_patient_information);

		Intent intent = getIntent();
		ArrayList<Object> patientInfo = (ArrayList<Object>) intent
				.getSerializableExtra("FirstInfoKey");
		TextView displayPatient = (TextView) findViewById(R.id.display_Info);
		displayPatient.setText("Patient Information of: "
				+ patientInfo.get(0).toString() + "\n" + "Name: "
				+ patientInfo.get(1).toString() + "\n" + "Birthday: "
				+ patientInfo.get(2).toString());

		user = (User) intent.getSerializableExtra("ClassKey");
	}

	/**
	 * Inflate the menu; this adds items to the action bar if it is present.
	 */
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		getMenuInflater().inflate(R.menu.patient_information, menu);
		return true;
	}

	/**
	 * Handle action bar item clicks here. The action bar will automatically
	 * handle clicks on the Home/Up button, so long as you specify a parent
	 * activity in AndroidManifest.xml.
	 */
	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		int id = item.getItemId();
		if (id == R.id.action_settings) {
			return true;
		}
		return super.onOptionsItemSelected(item);
	}

	/**
	 * the method viewPastVisits is the onclick function for the View Past
	 * Visits button, it checks if there is a record for that patient and starts
	 * a new activity PatientVisitRecord to display the records.
	 */
	public void viewPastVisits(View view) throws IOException {
		user.load();
		if (user.getArrivalTime().size() == 0) {
			Context context = getApplicationContext();
			CharSequence text = "Please record the date first";
			int duration = Toast.LENGTH_SHORT;
			Toast.makeText(context, text, duration).show();

		}
		else {
			Intent intent = new Intent(PatientInformation.this,
					PatientVisitRecord.class);
			Intent infoIntent = getIntent();
			ArrayList<Object> patientInfo = (ArrayList<Object>) infoIntent
					.getSerializableExtra("FirstInfoKey");
			intent.putExtra("Key", patientInfo.get(0).toString());
			startActivity(intent);
		}

	}

	/**
	 * the onClick function records NewVisit in related to the button Record New
	 * Visit, it creates a String of date that will be put into the patient's
	 * visit record.
	 */

	public void recordNewVisit(View view) throws IOException {

		user.load();
		user.newVisit();
		user.save();

		Context context = getApplicationContext();
		CharSequence text = "New Visit Added";
		int duration = Toast.LENGTH_SHORT;
		Toast.makeText(context, text, duration).show();

		

	}

	/**
	 * The onClick function changeToRecordPage is related to the button update
	 * vitals, it creates a new intent and using it to pass the patient's info
	 * the next activity AddVitals.
	 */

	public void changeToRecordPage(View view) {
		if (user.getArrivalTime().size() == 0) {
			Context context = getApplicationContext();
			CharSequence text = "Please record the date first";
			int duration = Toast.LENGTH_SHORT;
			Toast.makeText(context, text, duration).show();

		} else {
			Intent intent = new Intent(PatientInformation.this, AddVitals.class);
			Intent infoIntent = getIntent();
			ArrayList<Object> patientInfo = (ArrayList<Object>) infoIntent
					.getSerializableExtra("FirstInfoKey");
			intent.putExtra("Key", patientInfo.get(0).toString());

			startActivity(intent);
		}
	}
	/**
	 * The onClick function addDoctorTime will change in the activity to AddDoctorVisit
	 * where it record the time seen by a doctor
	 */

	public void addDoctorTime(View view) throws IOException {
		if (user.getArrivalTime().size() == 0) {
			Context context = getApplicationContext();
			CharSequence text = "Please record the date first";
			int duration = Toast.LENGTH_SHORT;
			Toast.makeText(context, text, duration).show();

		} else {
			Intent intent = new Intent(PatientInformation.this, AddDoctorVisit.class);
			Intent infoIntent = getIntent();
			ArrayList<Object> patientInfo = (ArrayList<Object>) infoIntent
					.getSerializableExtra("FirstInfoKey");
			intent.putExtra("Key", patientInfo.get(0).toString());

			startActivity(intent);
		}
	}

	}
