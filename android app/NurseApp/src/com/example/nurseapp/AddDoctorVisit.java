package com.example.nurseapp;

import java.io.IOException;

import classForApp.User;
import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class AddDoctorVisit extends Activity {
	User user;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_add_doctor_visit);
		user = new User();
		try {
			user.load();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		Intent intent = getIntent();
		String healthNumber = (String) intent.getSerializableExtra("Key");
		user.setCurrentPatient(healthNumber);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.add_doctor_visit, menu);
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
	/**
	 * The onclick function submitDoctorTime will add a time to the patient's record of based on the time entered by 
	 * the nurse
	 */

	public void submitDoctorTime(View view) throws IOException {
		EditText time = (EditText) findViewById(R.id.editText1);
		String input = time.getText().toString();
		if (input.length() != 8) {
			Context context1 = getApplicationContext();
			CharSequence text = "Invalid Entry";
			int duration = Toast.LENGTH_SHORT;
			Toast.makeText(context1, text, duration).show();
		} else {
			user.load();
			user.newDoctorVisit(input);
			user.save();
			Context context = getApplicationContext();
			CharSequence text = "success";
			int duration = Toast.LENGTH_SHORT;
			Toast.makeText(context, text, duration).show();
		}
	}
}
