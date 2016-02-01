package com.example.nurseapp;

import java.io.IOException;
import java.util.ArrayList;

import classForApp.User;
import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class AddNewPatient extends Activity {
	User user;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_add__new__patient);
		user = new User();
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.add__new__patient, menu);
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
	 * The onclick function CreateNewPatient adds a new patient to the patient list based on the inputs from the user, 
	 * pops a message if any inputs is empty or in incorrect form.
	 */

	public void CreateNewPatient(View view) throws IOException {
		user.load();
		EditText name = (EditText) findViewById(R.id.editText1);
		EditText birthday = (EditText) findViewById(R.id.editText3);
		EditText number = (EditText) findViewById(R.id.editText2);
		String nameinput = name.getText().toString();
		String birthdayinput = birthday.getText().toString();
		String numberinput = number.getText().toString();

		if (user.checkSameNum(numberinput)) {
			Context context = getApplicationContext();
			CharSequence text = "Health Number is existed";
			int duration = Toast.LENGTH_SHORT;
			Toast.makeText(context, text, duration).show();

		} else if (nameinput.isEmpty() | birthdayinput.isEmpty()
				| numberinput.isEmpty()) {
			Context context1 = getApplicationContext();
			CharSequence text = "Invalid Entry";
			int duration = Toast.LENGTH_SHORT;
			Toast.makeText(context1, text, duration).show();
		} else if (birthdayinput.length() != 10) {
			Context context3 = getApplicationContext();
			CharSequence text = "Invalid Entry";
			int duration = Toast.LENGTH_SHORT;
			Toast.makeText(context3, text, duration).show();
		} else {
			user.newPatient(nameinput, birthdayinput, numberinput);
			user.save();
			Context context4 = getApplicationContext();
			CharSequence text = "New Patient added";
			int duration = Toast.LENGTH_SHORT;
			Toast.makeText(context4, text, duration).show();

		}
	}
}
