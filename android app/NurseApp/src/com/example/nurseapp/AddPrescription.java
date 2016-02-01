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

public class AddPrescription extends Activity {
	User user;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_add_prescription);
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
		getMenuInflater().inflate(R.menu.add_prescription, menu);
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
	 * The onclick function SubmitPrescription adds a Prescription for the current patient,
	 * throws pop message if the information is added correctly
	 */
	public void SubmitPrescription(View view) throws IOException {
		EditText prescription = (EditText) findViewById(R.id.editText1);
		String input_prescription = prescription.getText().toString();
		user.recordPrescriptions(input_prescription);
		user.save();
		Context context = getApplicationContext();
		CharSequence text = "success";
		int duration = Toast.LENGTH_SHORT;
		Toast.makeText(context, text, duration).show();
	}

}
