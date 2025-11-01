package com.example.countriesapp;

import android.annotation.SuppressLint;
import android.content.Context;
import android.util.Log;

import org.w3c.dom.Document;
import org.w3c.dom.NodeList;

import java.io.InputStream;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

public class XMLCountries {

    private final Country [] data;
    private final Context context;

    public XMLCountries(Context context){
        this.context = context;

        Log.e("ERROR", "IN PARSING NOW" );

        InputStream stream;
        DocumentBuilder builder;
        Document document = null;

        try{
            stream = context.getResources().openRawResource(R.raw.countries);
            builder = DocumentBuilderFactory.newInstance().newDocumentBuilder();
            document = builder.parse(stream);
            Log.e("ERROR", "STREAM BUILDER AND DOCUMENT GENERATED" );
        }catch (Exception ignored){
        }

        assert document != null;
        NodeList nameList = document.getElementsByTagName("name");
        NodeList capitalList = document.getElementsByTagName("capital");
        NodeList imageList = document.getElementsByTagName("image");
        NodeList urlList = document.getElementsByTagName("url");
        NodeList continentList = document.getElementsByTagName("continent");
        NodeList currencyList = document.getElementsByTagName("currency");

        data = new Country[nameList.getLength()];

        for(int i=0;i<nameList.getLength();i++){
            String name = nameList.item(i).getFirstChild().getNodeValue();
            String capital = capitalList.item(i).getFirstChild().getNodeValue();
            String image = imageList.item(i).getFirstChild().getNodeValue();
            String url = urlList.item(i).getFirstChild().getNodeValue();
            String continent = continentList.item(i).getFirstChild().getNodeValue();
            String currency = currencyList.item(i).getFirstChild().getNodeValue();
            data[i] = new Country(name, capital, image, url, continent, currency);

            Log.e("ERROR", "name found "+name);
        }
    }

    public int getCount(){return data.length;}
    public Country getCountry(int i){return data[i];}
    public String [] getNames(){
        String [] names = new String[getCount()];
        for(int i=0;i<getCount();i++)names[i] = getCountry(i).getName();
        return names;
    }

    @SuppressLint("DiscouragedApi")
    public int [] getImageIds(){
        int [] imageIds = new int[getCount()];
        for(int i=0;i<getCount();i++){
            String imageName = getCountry(i).getImage();
            imageName = imageName.substring(0, imageName.indexOf("."));
            imageIds[i] = this.context.getResources().getIdentifier(imageName,"drawable", context.getPackageName());
        }
        return imageIds;
    }
}