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

public class AddVitals extends Activity {
	User user;

	/**
	 * onCreate will initialize the intent and set current patient
	 */
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_add_vitals);

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

	/**
	 * Inflate the menu; this adds items to the action bar if it is present.
	 */
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		getMenuInflater().inflate(R.menu.add_vitals, menu);
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
	 * update the vitals for current patient and save it
	 * 
	 * @param view
	 * @throws IOException
	 */
	public void submitVitals(View view) throws IOException {
		EditText temperature = (EditText) findViewById(R.id.editText_temperature);
		String input_Temperature = temperature.getText().toString();

		EditText bloodpressure_low = (EditText) findViewById(R.id.editText_bloodPressure_low);
		String input_bloodpressure_low = bloodpressure_low.getText().toString();

		EditText bloodpressure_high = (EditText) findViewById(R.id.editText_bloodPressure_high);
		String input_bloodpressure_high = bloodpressure_high.getText()
				.toString();

		EditText heartRate = (EditText) findViewById(R.id.editText_HeartRate);
		String input_HeartRate = heartRate.getText().toString();

		String bloodPressure = input_bloodpressure_low + " "
				+ input_bloodpressure_high;
		user.updateVisit(input_Temperature, bloodPressure, input_HeartRate);
		user.save();
		Context context = getApplicationContext();
		CharSequence text = "success";
		int duration = Toast.LENGTH_SHORT;
		Toast.makeText(context, text, duration).show();
	}

}
