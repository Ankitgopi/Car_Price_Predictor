#!/usr/bin/env python3
"""
Setup script for Car Price Predictor
This script helps set up the environment and train the model
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing requirements: {e}")
        return False
    return True

def train_model():
    """Train the machine learning model"""
    print("Training the model...")
    try:
        subprocess.check_call([sys.executable, "train_model.py"])
        print("✓ Model trained successfully!")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error training model: {e}")
        return False
    return True

def main():
    print("🚗 Car Price Predictor Setup")
    print("=" * 40)
    
    # Check if CSV file exists
    if not os.path.exists("Cleaned_Car_data.csv"):
        print("✗ Error: Cleaned_Car_data.csv not found!")
        print("Please make sure the dataset file is in the current directory.")
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Train model
    if not train_model():
        return
    
    print("\n🎉 Setup completed successfully!")
    print("\nTo run the application:")
    print("  python application.py")
    print("\nThen open your browser and go to: http://localhost:5000")

if __name__ == "__main__":
    main()
