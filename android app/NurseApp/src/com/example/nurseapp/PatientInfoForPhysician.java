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

public class PatientInfoForPhysician extends Activity {
	User user;

	@Override

	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_patient_info);
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

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.patient_info, menu);
		return true;
	}

	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		// Handle action bar item clicks here. The action bar will
		// automatically handle clicks on the Home/Up button, so long
		// as you specify a parent activity in AndroidManifest.xml.
		int id = item.getItemId();
		if (id == R.id.action_settings) {
			return true;
		}
		return super.onOptionsItemSelected(item);
	}
	/*
	 * The button that allows the physician to view the patient's record
	 */

	public void viewPastVisits(View view) throws IOException {
		user.load();
		if (user.getArrivalTime().size() == 0) {
			Context context = getApplicationContext();
			CharSequence text = "There is no record";
			int duration = Toast.LENGTH_SHORT;
			Toast.makeText(context, text, duration).show();

		}

		else {
			Intent intent = new Intent(PatientInfoForPhysician.this,
					PatientVisitRecord.class);
			Intent infoIntent = getIntent();
			ArrayList<Object> patientInfo = (ArrayList<Object>) infoIntent
					.getSerializableExtra("FirstInfoKey");
			intent.putExtra("Key", patientInfo.get(0).toString());
			startActivity(intent);
		}

	}
	/*
	 * The button that allows the physician to change into the activity where it can record the precription.
	 */

	public void AddPrescription(View view) throws IOException {
		user.load();
		if (user.getArrivalTime().size() == 0) {
			Context context = getApplicationContext();
			CharSequence text = "Please record the date first";
			int duration = Toast.LENGTH_SHORT;
			Toast.makeText(context, text, duration).show();
		} else {
			Intent intent = new Intent(PatientInfoForPhysician.this, AddPrescription.class);
			Intent infoIntent = getIntent();
			ArrayList<Object> patientInfo = (ArrayList<Object>) infoIntent
					.getSerializableExtra("FirstInfoKey");
			intent.putExtra("Key", patientInfo.get(0).toString());
			startActivity(intent);
		}

	}
}
