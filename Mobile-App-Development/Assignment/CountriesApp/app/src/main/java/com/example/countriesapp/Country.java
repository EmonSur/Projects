package com.example.countriesapp;

import java.io.Serializable;

public class Country implements Serializable {
    private String name, image, capital, url, continent, currency;

    public Country(String name, String capital, String image, String url, String continent, String currency) {
        this.name = name;
        this.capital = capital;
        this.image = image;
        this.url = url;
        this.continent = continent;
        this.currency = currency;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUrl() {return url;}

    public void setUrl(String url) {this.url = url;}

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public String getCapital() { return capital; }

    public void setCapital(String capital) {
        this.capital = capital;
    }

    public String getContinent() { return continent; }

    public void setContinent(String continent) {
        this.continent = continent;
    }

    public String getCurrency() { return currency; }

    public void setCurrency(String currency) {
        this.currency = currency;
    }

}