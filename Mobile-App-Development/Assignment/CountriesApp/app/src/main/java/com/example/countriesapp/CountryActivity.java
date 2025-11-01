package com.example.countriesapp;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class CountryActivity extends AppCompatActivity {

    TextView countryTV = null;
    ImageView countryIM = null;
    Button moreInfoBT = null;
    Country country = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_country);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        // wire
        countryIM = findViewById(R.id.imageView);
        countryTV = findViewById(R.id.textView);
        moreInfoBT = findViewById(R.id.button);

        // get data
        Intent intent = getIntent();
        Bundle bundle = intent.getExtras();
        assert bundle != null;
        country = (Country)bundle.getSerializable("country");

        // populate object with data
        assert country != null;
        countryTV.setText(country.getName());

        String imageName = country.getImage();
        imageName = imageName.substring(0,imageName.indexOf("."));
        @SuppressLint("DiscouragedApi") int imageId = this.getResources().getIdentifier(imageName, "drawable", getPackageName());
        countryIM.setImageResource(imageId);

        moreInfoBT.setOnClickListener(v -> {
            // make an explicit intent and a bundle
            Intent intent1 = new Intent(CountryActivity.this, DetailsActivity.class);
            Bundle bundle1 = new Bundle();

            // put the data into the bundle and the bundle into the intent
            bundle1.putSerializable("country", country);
            intent1.putExtras(bundle1);

            // start activity
            startActivity(intent1);
        });
    }
}



