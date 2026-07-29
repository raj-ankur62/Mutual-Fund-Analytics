import requests
import pandas as pd
import os
import json


schemes = {
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}


output_folder = "data/raw"

os.makedirs(output_folder, exist_ok=True)


for scheme_name, scheme_code in schemes.items():

    print("=" * 60)
    print("Scheme Name:", scheme_name)
    print("Scheme Code:", scheme_code)

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        # NAV data
        nav_df = pd.DataFrame(data["data"])

        print("\nDataset Shape:")
        print(nav_df.shape)

        print("\nFirst 5 Rows:")
        print(nav_df.head())


        # Save CSV
        csv_path = os.path.join(
            output_folder,
            f"{scheme_name}_NAV.csv"
        )

        nav_df.to_csv(
            csv_path,
            index=False
        )


        # Save JSON
        json_path = os.path.join(
            output_folder,
            f"{scheme_name}_NAV.json"
        )

        with open(json_path, "w") as file:
            json.dump(data, file, indent=4)


        print("\nCSV saved:", csv_path)
        print("JSON saved:", json_path)

    else:
        print("API Error:", response.status_code)