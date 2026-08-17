"""
Master Pipeline Execution Script

This script runs the main data processing pipeline
for the Mutual Fund Analytics project.
"""

import subprocess
import sys


def run_script(script_name):
    """
    Execute a Python script and display its execution status.

    Parameters:
        script_name (str): Name of the Python script to execute.
    """

    print(f"\n{'=' * 50}")
    print(f"Running: {script_name}")
    print(f"{'=' * 50}")

    try:
        subprocess.run(
            [sys.executable, script_name],
            check=True
        )

        print(f"Successfully completed: {script_name}")

    except subprocess.CalledProcessError:
        print(f"Error while running: {script_name}")
        sys.exit(1)


def main():
    """
    Run all project pipeline scripts in sequence.
    """

    scripts = [
        "data_ingestion.py",
        "data_cleaning.py",
        "investor_transactions_cleaning.py",
        "scheme_performance_cleaning.py"
    ]

    print("Starting Mutual Fund Analytics Pipeline")

    for script in scripts:
        run_script(script)

    print("\n" + "=" * 50)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    main()