package com.example.nurseapp;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Set;

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

public class PatientVisitRecord extends Activity {
	User user;

	@Override
	/**
	 * when the activity PatientVisitRecord is activated, it loads all the record for the patient and manipulating a large String that contains
	 * the patient's heart rate,blood pressure,temperature,recored time, then it displays the String with the help of Scrolling function.
	 * @see android.app.Activity#onCreate(android.os.Bundle)
	 */
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_patient_visit_record);

		user = new User();
		try {
			user.load();
		} catch (IOException e) {

			e.printStackTrace();
		}
		Intent intent = getIntent();
		String healthNumber = (String) intent.getSerializableExtra("Key");
		user.setCurrentPatient(healthNumber);

		ArrayList<String> arrivalTime = user.getArrivalTime();
		String vitalList = "";
		for (String item : arrivalTime) {

			vitalList = vitalList + "Arrival Time: " + item + "\n\n";

			if (user.viewPrescriptions(item) != null) {
				if (user.viewDoctorVisit().get(item).equals("Not Visited")) {
					vitalList = vitalList + "Doctor Visit: "
							+ "Time Not Recorded Yet" + "\n\n";
				} else {
					vitalList = vitalList + "Doctor Visit: "
							+ user.viewDoctorVisit().get(item) + "\n\n";
				}

				vitalList = vitalList + "Prescriptions: "
						+ user.viewPrescriptions(item) + "\n\n";
			} else {
				vitalList = vitalList + "Doctor Visit: "
						+ user.viewDoctorVisit().get(item) + "\n\n";

				vitalList = vitalList + "Prescriptions: "
						+ "No Prescriptions Recorded" + "\n\n";
			}
			if (user.viewVitalRecord(item) != null) {
				Set<String> keys = user.viewVitalRecord(item).keySet();
				for (String items : keys) {
					vitalList = vitalList + "Check up time: " + items + "\n";
					vitalList = vitalList + "Temperature: "
							+ user.viewVitalRecord(item).get(items).get(0)
							+ "\n";
					vitalList = vitalList + "Bloodpressure: "
							+ user.viewVitalRecord(item).get(items).get(1)
							+ "\n";
					vitalList = vitalList + "Heartrate: "
							+ user.viewVitalRecord(item).get(items).get(2)
							+ "\n" + "\n";
				}
			} else {
				vitalList = vitalList + "No Check up was done" + "\n\n";
			}

		}
		TextView textView = (TextView) findViewById(R.id.visit_record);
		textView.setText(vitalList);
	}

	/**
	 * Inflate the menu; this adds items to the action bar if it is present.
	 */
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		getMenuInflater().inflate(R.menu.patient_visit_record, menu);
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

}
