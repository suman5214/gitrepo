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
import android.widget.Toast;
import classForApp.User;
import classForApp.Patient;

public class MainActivity extends Activity {
	User user;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		user = new User();
		try {
			user.loadUsers();
		} catch (IOException e) {
			// TODO Auto-generated catch block

		}
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
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
	 * This loads the user list, then it determines if the password is right and also changes to the 
	 * appropriate activity according to the user's type
	 */
	public void login(View view) throws IOException {
		EditText username = (EditText) findViewById(R.id.editText2);
		EditText password = (EditText) findViewById(R.id.editText1);
		String usernameinput = username.getText().toString();
		String passwordinput = password.getText().toString();
		if (user.login(usernameinput, passwordinput)) {
			if (user.Usertype(usernameinput).equals("nurse")) {
				Intent intentSuccess = new Intent(MainActivity.this,
						SearchPatient.class);
				intentSuccess.putExtra("username", usernameinput);
				startActivity(intentSuccess);
			} else {
				Intent intentSuccess = new Intent(MainActivity.this,
						PhysicianSearch.class);
				intentSuccess.putExtra("username", usernameinput);
				startActivity(intentSuccess);
			}

		} else {
			Context context = getApplicationContext();
			CharSequence text = "Invalid Username or Password";
			int duration = Toast.LENGTH_SHORT;

			Toast.makeText(context, text, duration).show();

		}
	}

}
