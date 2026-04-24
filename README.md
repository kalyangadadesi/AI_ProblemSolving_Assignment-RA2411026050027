# AI Problem Solving Assignment

This repository contains the implementations for two AI problems:
1. **Problem 6: Sudoku Solver using CSP**
2. **Problem 18: Student Performance Predictor using Machine Learning**

Both solutions are implemented in Python and feature interactive graphical user interfaces (GUI) built using **Streamlit**. 

---

## 🧩 Problem 6: Sudoku Solver (CSP)

### Problem Description
Sudoku is a logic-based number placement puzzle played on a 9×9 grid. The objective is to fill the cells so that every row, column, and 3×3 subgrid contains the digits 1–9 without repetition. The user can interactively fill out the grid, check if they've won, or have the AI automatically solve it.

### Algorithm Used
**Constraint Satisfaction Problem (CSP) via Backtracking**  
The solver uses a backtracking algorithm that tries to fill empty cells one by one. It assigns a valid number (1-9) that does not violate any constraints (row, column, and 3x3 box). If a conflict occurs later, it backtracks and tries the next number.

### Execution Steps
1. Install dependencies: `pip install -r requirements.txt`
2. Run the Streamlit app: `streamlit run sudoku.py`
3. A web browser will open with the interactive Sudoku grid.
4. Try to fill it yourself and click **Check Solution**, or click **Auto Solve (CSP)** to see the AI solve it.

### Sample Output
- User enters valid numbers and clicks **Check Solution**: Output -> *"You won!"* (with balloons!)
- User enters invalid numbers and clicks **Check Solution**: Output -> *"Try again. Constraints violated!"*
- User clicks **Auto Solve**: The grid is instantly filled with the correct solution computed by the CSP algorithm.

---

## 📈 Problem 18: Student Performance Predictor

### Problem Description
An EdTech platform aims to predict students' exam scores based on features like hours studied, attendance, prior performance, and assignments completed. The system allows users to view/upload datasets, preprocesses the data, trains a machine learning regression model, and predicts scores for new inputs.

### Algorithm Used
**Random Forest Regressor**  
A machine learning ensemble regression algorithm is used. It builds multiple decision trees during training and outputs the average prediction of the individual trees, providing a robust prediction for the exam score.

### Execution Steps
1. Install dependencies: `pip install -r requirements.txt`
2. Run the Streamlit app: `streamlit run student_predictor.py`
3. The app will automatically generate and save a synthetic dataset (`student_data.csv`) if one isn't uploaded.
4. Missing values (if any) are automatically filled with column means during preprocessing.
5. Review the model metrics (R² Score and Mean Absolute Error) displayed on the screen.
6. Use the form at the bottom to input new student details and click **Predict Exam Score** to see the model's prediction.

### Sample Output
- **Model Evaluation**: 
  - *R² Score*: ~0.95 (varies)
  - *Mean Absolute Error*: ~3.5 (varies)
- **Prediction**:
  - *Input*: Hours = 5, Attendance = 85%, Prior Score = 75, Assignments = 5
  - *Output*: *"Predicted Exam Score: 78.40 / 100"*
