package com.example.countriesapp;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import android.graphics.Typeface;
import android.text.SpannableStringBuilder;
import android.text.style.StyleSpan;

public class DetailsActivity extends AppCompatActivity {

    TextView nameTV, capitalTV, continentTV, currencyTV ;
    Country country = null;
    Button webInfoBT = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_details);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        // wire
        nameTV = findViewById(R.id.nameTextView);
        capitalTV = findViewById(R.id.capitalTextView);
        continentTV = findViewById(R.id.continentTextView);
        currencyTV = findViewById(R.id.currencyTextView);

        webInfoBT = findViewById(R.id.button1);

        Intent intent = getIntent();
        Bundle bundle = intent.getExtras();
        assert bundle != null;
        country = (Country) bundle.getSerializable("country");

        // populate widgets with data
        assert country != null;
        SpannableStringBuilder name = new SpannableStringBuilder("Name: " + country.getName());
        name.setSpan(new StyleSpan(Typeface.BOLD), 0, 5, 0);
        nameTV.setText(name);

        SpannableStringBuilder capital = new SpannableStringBuilder("Capital: " + country.getCapital());
        capital.setSpan(new StyleSpan(Typeface.BOLD), 0, 8, 0);
        capitalTV.setText(capital);

        SpannableStringBuilder continent = new SpannableStringBuilder("Continent: " + country.getContinent());
        continent.setSpan(new StyleSpan(Typeface.BOLD), 0, 10, 0);
        continentTV.setText(continent);

        SpannableStringBuilder currency = new SpannableStringBuilder("Currency: " + country.getCurrency());
        currency.setSpan(new StyleSpan(Typeface.BOLD), 0, 9, 0);
        currencyTV.setText(currency);

        // button events
        webInfoBT.setOnClickListener(v -> {
            Intent intent1 = new Intent(DetailsActivity.this, WebActivity.class);
            Bundle bundle1 = new Bundle();
            bundle1.putString("url", country.getUrl());
            intent1.putExtras(bundle1);
            startActivity(intent1);
        });
    }
}