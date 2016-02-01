package com.example.nurseapp;

import java.io.IOException;
import classForApp.User;
import java.util.ArrayList;

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
import classForApp.User;
import classForApp.Patient;

public class SearchPatient extends Activity {
	User user;

	/**
	 * As the app is opened a new user is initialized and loaded with the
	 * patient_rcord.txt
	 */
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_search_patient);
		Intent intent = getIntent();
		String username = (String) intent.getSerializableExtra("username");
		TextView userinfo = (TextView) findViewById(R.id.textView2);
		userinfo.setText("Nurse: " + username);
		user = new User();

	}

	/**
	 * Inflate the menu; this adds items to the action bar if it is present.
	 */
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		getMenuInflater().inflate(R.menu.search_patient, menu);
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
		try {
			user.load();
		} catch (IOException e) {
			// TODO Auto-generated catch block

		}
		if (user.checkPatient(input)) {
			ArrayList<Object> patientInfo = user.lookUpPatient(input);
			Intent intentSuccess = new Intent(SearchPatient.this,
					PatientInformation.class);
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
	public void addNewPatient(View view) throws IOException{
		Intent intentSuccess = new Intent(SearchPatient.this,
				AddNewPatient.class);
		startActivity(intentSuccess);
	}
	
	public void viewUrgencyList(View view){
		Intent intentSuccess = new Intent(SearchPatient.this,
				ViewUrgencyList.class);
		startActivity(intentSuccess);
		
	}

}
