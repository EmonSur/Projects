# CS4092 Assignment

## Description

The android app developed here aims to list and display basic information on the UN recognized countries of the world. 
It consists of four activities, each displaying progressively detailed information on a selected country.

## Features

- List all the countries in the world.
- Display basic info about a selected country.
- Display extended info about a selected country including name, capital, content, and currency.
- Link users to a selected countries Wikipedia page.

## Activities

These are the activities or pages users can interact with in the Countries App.

### Activity 1 - Countries Recycler View

- Display a scrollable list of countries in a `RecyclerView`.
- Each item shows a **flag** (in an `ImageView`) and a **country name** (in a `TextView`).
- The layout for each is defined in the `row_layout.xml`
- When a user clicks on a country, they are taken to Activity 2.

### Activity 2 - Basic Country Info View

- Displays the **flag** and **name** of a selected country.
- Contains a button that navigates to Activity 3.

### Activity 3 - Detailed Country Info View

- Shows extended information about the selected country, including **name**, **capital**, **continent**, **currency**.
- Includes a button to Activity 4.

### Activity 4 - Web View

- Displays the selected country's **Wikipedia page** in a `WebView`.
- Allows users to explore additional details beyond what's provided in the previous activity.

## Structure

```bash
|-- app/
|  |-- java/com/example/countriesapp/
|     |-- MainActivity.java → Displays list of countries (RecyclerView)
|     |-- BasicInfoActivity.java → Shows basic info about a selected country
|     |-- DetailedInfoActivity.java → Shows detailed info (name, capital, continent, currency)
|     |-- WebViewActivity.java → Displays Wikipedia page
|     |-- XMLCountries.java → Parses countries.xml and loads data
|     |-- Country.java → Class for storing country info
|     |-- ImageRecyclerAdapter.java → RecyclerView adapter for country list
|     |-- RecycleViewInterface.java → Handles click events in RecyclerView
|  |-- res/
|     |-- layout/ → XML layout files for all activities
|     |-- drawable/ → Flag images for countries
|     |-- raw/ → countries.xml raw data file
```

## Technologies Used

- **Language:** Java
- **IDE:** Android Studio
- **Target AVD**: Medium Phone, Android API 36

## Limitations/ Known Issues

- Manual updates required: No automation included which will add new countries or make changes to the existing in the ``countries.xml` file.
- Longer loading times: Due to the large data set, the app may take slightly longer to run.
- User customisation not available: User cannot currently add or edit country through the app interface.
