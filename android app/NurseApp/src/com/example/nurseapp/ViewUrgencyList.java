package com.example.nurseapp;

import java.io.IOException;

import classForApp.User;
import android.app.Activity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;

public class ViewUrgencyList extends Activity {
	User user;
	@Override
	/**
	 * when the activity is being created, it will display a list of patient that has a urgency number and not seen by a 
	 * doctor yet.
	 */
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_view_urgency_list);
		user = new User();
		try {
			user.load();
		} catch (IOException e) {
			// TODO Auto-generated catch block

		}
		TextView displayPatient = (TextView) findViewById(R.id.textView1);
		displayPatient.setText(user.viewByUrgency());
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.view_urgency_list, menu);
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
}
