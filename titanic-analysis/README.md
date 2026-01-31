# 🚢 Titanic Survival Analysis

A comprehensive data analysis project exploring the factors that influenced passenger survival during the Titanic disaster of 1912.

---

## 📊 Project Overview

This project analyzes the famous Titanic dataset to understand survival patterns based on:
- **Passenger Class** (1st, 2nd, 3rd)
- **Gender** (Male, Female)
- **Age** (Children, Adults, Elderly)
- **Combined Demographics**

---

## 📁 Project Structure

```
titanic-analysis/
│
├── data/
│   ├── train.csv              # Raw dataset
│   └── titanic.db               # SQLite database 
│
├── notebooks/
│   └── titanic.ipynb            # Main analysis notebook
│
└── README.md                     # This file
```

---

## 🎯 Key Visualizations

### 1. Survival Rate by Passenger Class
**Bar Chart** showing survival rates across three passenger classes.

**Key Findings:**
- 1st Class: 63% survival rate
- 2nd Class: 47% survival rate  
- 3rd Class: 24% survival rate

### 2. Survival Rate by Class and Gender
**Grouped Bar Chart** comparing survival rates for men and women in each class.

**Key Findings:**
- 1st class women: 96.8% survival rate
- 3rd class men: 13.5% survival rate
- Women consistently had higher survival rates across all classes

### 3. Overall Survival Distribution
**Pie Chart** showing the overall proportion of survivors vs non-survivors.

**Key Findings:**
- 38.4% overall survival rate (342 survived)
- 61.6% mortality rate (549 died)

### 4. Age Distribution by Survival Status
**Histogram** comparing age distributions of survivors vs non-survivors.

**Key Findings:**
- Children under 10 had elevated survival rates
- Most fatalities were adults aged 20-40
- "Women and children first" policy visible in data

---

## 🔍 Dataset Information

**Source:** Kaggle Titanic Dataset

**Total Records:** 891 passengers

**Key Features:**
- `PassengerId`: Unique identifier
- `Survived`: Survival status (0 = No, 1 = Yes)
- `Pclass`: Passenger class (1, 2, 3)
- `Name`: Passenger name
- `Sex`: Gender (male, female)
- `Age`: Age in years
- `SibSp`: Number of siblings/spouses aboard
- `Parch`: Number of parents/children aboard
- `Ticket`: Ticket number
- `Fare`: Passenger fare
- `Cabin`: Cabin number
- `Embarked`: Port of embarkation (C=Cherbourg, Q=Queenstown, S=Southampton)

---

## 🚀 How to Run

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- Required libraries 

### Steps

1. **Navigate to project folder:**
```bash
cd data_analysis_projects/titanic-analysis
```

2. **Launch Jupyter Notebook:**
```bash
jupyter notebook notebooks/titanic.ipynb
```

3. **Run all cells** to reproduce the analysis and visualizations

---

## 📈 Analysis Methods

**Data Cleaning:**
- Handled missing values in Age, Cabin, and Embarked columns
- Removed duplicates
- Validated data types

**Exploratory Data Analysis:**
- Descriptive statistics
- Distribution analysis
- Correlation analysis
- Group-by aggregations

**Visualization Techniques:**
- Bar charts for categorical comparisons
- Pie charts for proportion analysis
- Histograms for distribution analysis
- Color coding for clarity

---

## 💡 Key Insights & Conclusions

1. **Class Disparity:** Strong correlation between passenger class and survival - higher class passengers had significantly better survival rates.

2. **Gender Impact:** The "women and children first" evacuation protocol was clearly followed, with women having much higher survival rates than men across all classes.

3. **Age Factor:** Young children (under 10) had better survival rates than adults, supporting the priority given to children during evacuation.

4. **Combined Effects:** The interaction between class and gender was significant - 1st class women had the highest survival rate (96.8%), while 3rd class men had the lowest (13.5%).

5. **Socioeconomic Factors:** Access to better cabin locations and lifeboats likely contributed to the survival advantage of 1st class passengers.

---

## 🛠️ Technologies Used

- **Python 3.8+** - Programming language
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **NumPy** - Numerical operations
- **Jupyter Notebook** - Interactive development environment

---

## 📚 Future Enhancements

- [ ] Build predictive model for survival using machine learning
- [ ] Add statistical significance tests (chi-square, t-tests)
- [ ] Analyze fare impact on survival
- [ ] Explore cabin location effects
- [ ] Create interactive dashboard with Plotly
- [ ] Add more detailed age group analysis


---


## 👤 Author

**Hema Pavuluri**

Questions or feedback? Feel free to reach out!

---

## 📄 License

This project is open source and available under the MIT License.

---

[← Back to Portfolio](../)
