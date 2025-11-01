package com.example.countriesapp;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

public class MainActivity extends AppCompatActivity implements RecycleViewInterface{
    RecyclerView list = null;
    ImageRecyclerAdapter adapter = null;
    String [] countries = null;
    int    [] imageIds  = null;
    XMLCountries data = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        list = findViewById(R.id.recyclerView);

        // get the data from model
        data = new XMLCountries(this);
        countries = data.getNames();
        imageIds = data.getImageIds();
        adapter = new ImageRecyclerAdapter(getApplicationContext(), R.layout.row_layout, countries, imageIds,this);

        list.setLayoutManager(new LinearLayoutManager(this));
        list.setAdapter(adapter);
    }

    @Override
    public void onItemClick(int position) {
        Toast.makeText(this,"selected "+countries[position], Toast.LENGTH_SHORT).show();

        // make intent and bundle
        Intent intent = new Intent(MainActivity.this, CountryActivity.class);
        Bundle bundle = new Bundle();
        bundle.putSerializable("country", data.getCountry(position));
        intent.putExtras(bundle);
        startActivity(intent);
    }
}