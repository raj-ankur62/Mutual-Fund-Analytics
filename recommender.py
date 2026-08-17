"""
Mutual Fund Recommender Module

This script recommends the top 3 mutual funds based on
user risk appetite and Sharpe Ratio.

Risk grades are derived using Maximum Drawdown as a
project-level risk proxy.
"""

import pandas as pd


def assign_risk_grade(drawdown):
    """
    Assign a risk grade based on Maximum Drawdown.

    Parameters:
        drawdown (float): Maximum Drawdown value.

    Returns:
        str: Low, Moderate, or High risk grade.
    """

    if drawdown >= -0.10:
        return "Low"
    elif drawdown >= -0.25:
        return "Moderate"
    else:
        return "High"


def recommend_funds(df, risk_appetite, top_n=3):
    """
    Recommend top mutual funds based on risk appetite.

    Parameters:
        df (pd.DataFrame): Fund scorecard dataset.
        risk_appetite (str): Low, Moderate, or High.
        top_n (int): Number of recommendations.

    Returns:
        pd.DataFrame: Top recommended funds.
    """

    df = df.copy()

    # Create risk grades
    df["risk_grade"] = df["Maximum_Drawdown"].apply(assign_risk_grade)

    # Filter funds by user risk appetite
    recommendations = df[
        df["risk_grade"].str.lower() == risk_appetite.lower()
    ].copy()

    # Sort by Sharpe Ratio
    recommendations = recommendations.sort_values(
        by="Sharpe_Ratio",
        ascending=False
    )

    return recommendations.head(top_n)[
        [
            "amfi_code",
            "risk_grade",
            "Sharpe_Ratio",
            "Fund_Score",
            "Overall_Rank"
        ]
    ]


def main():
    """
    Load the fund scorecard and generate recommendations.
    """

    file_path = "data/processed/fund_scorecard.csv"

    try:
        df = pd.read_csv(file_path)

        risk_appetite = input(
            "Enter your risk appetite (Low/Moderate/High): "
        ).strip()

        valid_risk_levels = ["Low", "Moderate", "High"]

        if risk_appetite not in valid_risk_levels:
            print("Invalid input. Please enter Low, Moderate, or High.")
            return

        recommendations = recommend_funds(
            df,
            risk_appetite
        )

        if recommendations.empty:
            print("No matching fund recommendations found.")
        else:
            print("\nTop 3 Fund Recommendations:")
            print(recommendations.to_string(index=False))

    except FileNotFoundError:
        print(f"File not found: {file_path}")


if __name__ == "__main__":
    main()