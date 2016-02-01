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
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class PhysicianSearch extends Activity {
	User user;

	/**
	 * As the app is opened a new user is initialized and loaded with the
	 * patient_rcord.txt
	 */
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_doctor);
		Intent intent = getIntent();
		String username = (String) intent.getSerializableExtra("username");
		TextView userinfo = (TextView) findViewById(R.id.textView1);
		userinfo.setText("Physician: " + username);
		user = new User();
		try {
			user.load();
		} catch (IOException e) {
			// TODO Auto-generated catch block

		}

	}

	/**
	 * Inflate the menu; this adds items to the action bar if it is present.
	 */
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		getMenuInflater().inflate(R.menu.doctor, menu);
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
	 * The method searchForPatient takes in a String using a EditText
	 * editTextSearch and passes the String to the user to check if it is a
	 * valid entry. If it is valid it passes the information of that search to
	 * the next activity.
	 * 
	 */
	public void searchForPatient(View view) throws IOException {

		EditText patientNumber = (EditText) findViewById(R.id.editTextSearch);
		String input = patientNumber.getText().toString();
		if (user.checkPatient(input)) {
			ArrayList<Object> patientInfo = user.lookUpPatient(input);
			Intent intentSuccess = new Intent(PhysicianSearch.this,
					PatientInfoForPhysician.class);
			intentSuccess.putExtra("FirstInfoKey", patientInfo);
			intentSuccess.putExtra("ClassKey", user);
			startActivity(intentSuccess);

		} else {
			Context context = getApplicationContext();
			CharSequence text = "Invalid Entry";
			int duration = Toast.LENGTH_SHORT;

			Toast.makeText(context, text, duration).show();
		}

	}
}
