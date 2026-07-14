# Retail Sales & Customer Analytics Engine

An end-to-end data analytics pipeline built in Python to transform, clean, and analyze over 5,000 raw retail transactional records. This project focuses on maintaining strict data integrity through statistical imputation and engineering actionable visual dashboards to isolate high-value revenue drivers and consumer demographics.

## 🚀 Project Overview & Objectives
Raw corporate retail data is frequently plagued by missing entries, recording errors, and unorganized customer details. The objective of this engine is to establish a robust data pipeline that:
*   **Enforces Data Integrity:** Implements advanced preprocessing and boolean filtering to strip out negative returns or operational anomalies.
*   **Uses Smart Imputation:** Avoids data loss from dropping rows by deploying category-level median imputation for missing pricing data.
*   **Profiles Customers:** Introduces behavioral segmentation by engineering continuous customer traits into distinct generation cohorts.
*   **Provides Executive Insights:** Evaluates product velocity and demographic trends to deliver clear, data-driven business strategies.

---

## 🛠️ Tech Stack & Key Libraries
*   **Language:** Python
*   **Data Manipulation:** Pandas, NumPy
*   **Data Visualization:** Seaborn, Matplotlib

---

## 🔍 Core Analytics Pipeline & Pipeline Logic

### 1. Data Wrangling & Preprocessing
*   **Anomaly Filtering:** Used Boolean masking to isolate and eliminate negative purchase quantities or zero-value transactions that represent return errors, ensuring they do not distort daily sales trends.
*   **Handling Missing Values:** Deployed **Category-Level Median Imputation** rather than standard arithmetic means. By grouping missing item costs by their categorical block, null items are assigned a highly realistic localized value, shielding the pipeline from being skewed by extreme luxury outliers.

### 2. Feature Engineering
*   **Demographic Cohorts:** Segmented raw, continuous age attributes into meaningful demographic buckets (`Gen Z`, `Millennials`, `Gen X`, `Boomers`) using `pd.cut()`.
*   **Chronological Tracking:** Transformed individual sales timestamps into monthly transaction intervals to enable historical time-series analytics.

### 3. Exploratory Data Analysis & Visualizations
*   **Correlation Tracking:** Designed correlation heatmaps using `.corr()` to dynamically evaluate interactions between pricing structures, quantities, and client behaviors.
*   **Dashboarding:** Implemented Seaborn and Matplotlib scripts mapping product line velocity, revenue trends, and comparative spending patterns across age brackets.

---

## 📊 Business Insights Derived
*   **High-Margin Demographics:** Isolated the `Millennial` consumer cohort as the primary driver of gross revenue, defining key marketing allocation goals.
*   **Product Line Velocity:** Provided insight into low-volume, high-ticket electronics sales performance compared to high-volume, lower-cost apparel lines.

---

## ⚙️ How to Run Locally

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
   cd YOUR_REPOSITORY_NAME
