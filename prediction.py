import pandas as pd
from joblib import load
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import numpy as np

# 1. Load model
model = load('model.joblib')  # Pastikan file model ada di folder yang sama

# 2. Buka file explorer untuk pilih CSV
Tk().withdraw()  # Hide the main window
file_path = askopenfilename(title="Pilih file CSV", filetypes=[("CSV files", "*.csv")])

if not file_path:
    print("Tidak ada file yang dipilih. Program dihentikan.")
    exit()

print(f"File yang dipilih: {file_path}")

# 3. Baca data
data = pd.read_csv(file_path, sep= ';')
# Simpan kolom Id sebelum filtering
id_column = data['EmployeeId']  # Simpan dulu


# 4. Kolom fitur yang digunakan saat training
fitur_training = ['Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome', 'Education',
                  'EducationField', 'EmployeeCount', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate',
                  'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome',
                  'MonthlyRate', 'NumCompaniesWorked', 'Over18', 'OverTime', 'PercentSalaryHike', 'PerformanceRating',
                  'RelationshipSatisfaction', 'StandardHours', 'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
                  'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']

# 5. Filter hanya fitur yang diperlukan
try:
    data = data[fitur_training]
except KeyError as e:
    print(f"Ada kolom yang kurang di file CSV: {e}")
    raise

# 6. Encoding kolom kategorikal
cat_mapping = {
    'BusinessTravel': {'Non-Travel': 0, 'Travel_Frequently': 1, 'Travel_Rarely': 2},
    'Department': {'Human Resources': 0, 'Research & Development': 1, 'Sales': 2},
    'EducationField': {'Human Resources': 0, 'Life Sciences': 1, 'Marketing': 2, 'Medical': 3, 'Other': 4, 'Technical Degree': 5},
    'Gender': {'Female': 0, 'Male': 1},
    'JobRole': {'Healthcare Representative': 0, 'Human Resources': 1, 'Laboratory Technician': 2, 'Manager': 3, 'Manufacturing Director': 4,
                'Research Director': 5, 'Research Scientist': 6, 'Sales Executive': 7, 'Sales Representative': 8},
    'MaritalStatus': {'Divorced': 0, 'Married': 1, 'Single': 2},
    'Over18': {'Y': 0},
    'OverTime': {'Yes': 1, 'No': 0}
}

for col, mapping in cat_mapping.items():
    if col in data.columns:
        data[col] = data[col].map(mapping)

# 7. Prediksi
prediksi = model.predict(data)

# Tambahkan kembali kolom Id
data['EmployeeId'] = id_column.values

# 8. Tambahkan hasil ke dataframe
data['Attrition_Predicted'] = prediksi
data['Attrition_Predicted'] = data['Attrition_Predicted'].replace({0: 'Tidak Attrition', 1: 'Attrition'})

data = data[['EmployeeId', 'Attrition_Predicted']]

# 9. Simpan hasil prediksi
output_file = os.path.splitext(file_path)[0] + '_predicted.csv'
data.to_csv(output_file, index=False)
print(f"Hasil prediksi disimpan ke: {output_file}")
