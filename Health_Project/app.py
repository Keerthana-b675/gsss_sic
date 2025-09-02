import streamlit as st
import pandas as pd
from datetime import date
from io import BytesIO
import matplotlib.pyplot as plt
import os

# ------------------- CONFIG -------------------
st.set_page_config(page_title="🏥 Healthcare Patient Admission Portal", layout="wide")

DATA_FILE = "patient_admissions.csv"  # Auto-save file

st.title("🏥 Welcome to Healthcare Point!")
st.write("Upload CSV or add new patient records. Once data is available, you can filter, edit, delete, visualize, and download.")

# ------------------- INITIALIZE SESSION STATE -------------------
if "df" not in st.session_state:
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        st.session_state.df = pd.read_csv(
            DATA_FILE,
            parse_dates=["AdmissionDate", "DischargeDate"],
            dayfirst=True
        )
    else:
        st.session_state.df = pd.DataFrame(columns=[
            "PatientID", "Name", "Age", "Gender", "Department", "Diagnosis", "Doctor Name",
            "AdmissionDate", "DischargeDate"
        ])

if "show_features" not in st.session_state:
    st.session_state.show_features = False  # Control showing advanced features

# ------------------- STEP 1: UPLOAD CSV -------------------
uploaded_file = st.file_uploader("📤 Upload patient_admissions.csv", type=["csv"])
if uploaded_file:
    st.session_state.df = pd.read_csv(
        uploaded_file,
        parse_dates=["AdmissionDate", "DischargeDate"],
        dayfirst=True
    )
    st.session_state.df.to_csv(DATA_FILE, index=False)  # Auto-save
    st.success("✅ File uploaded and saved!")
    st.session_state.show_features = True

# ------------------- STEP 2: ADD NEW PATIENT -------------------
with st.expander("➕ Add New Patient Record"):
    with st.form("add_form"):
        col1, col2 = st.columns(2)
        with col1:
            patient_id = st.text_input("Patient ID")
            name = st.text_input("Name")
            age = st.number_input("Age", min_value=0, max_value=120)
            gender = st.selectbox("Gender", ["M", "F"])
        with col2:
            department = st.text_input("Department")
            diagnosis = st.text_input("Diagnosis")
            doctor_name = st.text_input("Doctor Name")
            admission_date = st.date_input("Admission Date", value=date.today())
            discharge_date = st.date_input("Discharge Date", value=None)

        submitted = st.form_submit_button("Add Record")
        if submitted:
            if patient_id.strip() == "" or name.strip() == "":
                st.error("⚠ Patient ID and Name cannot be empty!")
            else:
                new_row = {
                    "PatientID": patient_id,
                    "Name": name,
                    "Age": age,
                    "Gender": gender,
                    "Department": department,
                    "Diagnosis": diagnosis if diagnosis else "Unknown",
                    "Doctor Name": doctor_name,
                    "AdmissionDate": pd.to_datetime(admission_date),
                    "DischargeDate": pd.to_datetime(discharge_date) if discharge_date else pd.NaT
                }
                st.session_state.df = pd.concat(
                    [st.session_state.df, pd.DataFrame([new_row])],
                    ignore_index=True
                )
                st.session_state.df.to_csv(DATA_FILE, index=False)  # Auto-save
                st.success("✅ Record Added & Saved Successfully!")
                st.session_state.show_features = True

# ------------------- SHOW FEATURES ONLY AFTER UPLOAD OR ADD -------------------
if st.session_state.show_features and not st.session_state.df.empty:
    df = st.session_state.df.copy()

    # Ensure datetime conversion
    df["AdmissionDate"] = pd.to_datetime(df["AdmissionDate"], errors="coerce", dayfirst=True)
    df["DischargeDate"] = pd.to_datetime(df["DischargeDate"], errors="coerce", dayfirst=True)

    # Fill missing diagnosis
    df["Diagnosis"].fillna("Unknown", inplace=True)

    # Only fill missing DischargeDate with today (don’t overwrite valid ones)
    df["DischargeDate"] = df["DischargeDate"].fillna(pd.Timestamp.today())

    # Create StayDuration only if AdmissionDate is valid
    df["StayDuration"] = (df["DischargeDate"] - df["AdmissionDate"]).dt.days
    df["StayDuration"] = df["StayDuration"].fillna(0).astype(int)

    st.markdown("---")
    st.subheader("📋 Patient Admission Records & Features")

    # ------------------- STEP 6: FILTERS -------------------
    st.sidebar.header("🔍 Filters")
    dept_filter = st.sidebar.multiselect("Filter by Department", df["Department"].dropna().unique())
    name_filter = st.sidebar.text_input("Search by Name")
    cardio_filter = st.sidebar.checkbox("Show only Cardiology patients with Stay > 5 days")

    filtered_df = df.copy()
    if dept_filter:
        filtered_df = filtered_df[filtered_df["Department"].isin(dept_filter)]
    if name_filter:
        filtered_df = filtered_df[filtered_df["Name"].str.contains(name_filter, case=False, na=False)]
    if cardio_filter:
        filtered_df = filtered_df[(filtered_df["Department"] == "Cardiology") & (filtered_df["StayDuration"] > 5)]

    # ------------------- STEP 8: SORTING -------------------
    st.sidebar.subheader("🔽 Sorting")
    sort_column = st.sidebar.selectbox("Sort by", filtered_df.columns)
    sort_order = st.sidebar.radio("Order", ["Ascending", "Descending"])
    filtered_df = filtered_df.sort_values(by=sort_column, ascending=(sort_order == "Ascending"))

    # ------------------- STEP 9: REMOVE DUPLICATES -------------------
    before_rows = len(filtered_df)
    filtered_df = filtered_df.drop_duplicates(subset=["PatientID", "AdmissionDate"], keep="first")
    after_rows = len(filtered_df)
    if before_rows != after_rows:
        st.warning(f"⚠ Removed {before_rows - after_rows} duplicate records (based on PatientID & AdmissionDate).")

    # ------------------- STEP 7: GROUP & AGGREGATE -------------------
    st.subheader("📊 Group & Aggregate Insights")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Number of Admissions per Department**")
        dept_count = df.groupby("Department")["PatientID"].count().reset_index(name="Admissions")
        st.dataframe(dept_count, use_container_width=True)
    with col2:
        st.write("**Average Stay Duration per Department**")
        avg_stay = df.groupby("Department")["StayDuration"].mean().reset_index(name="AvgStayDuration")
        st.dataframe(avg_stay, use_container_width=True)

    # ------------------- STEP 7 (continued): EDIT & DELETE -------------------
    st.subheader("🖊 Edit & Delete Records")
    filtered_df["Delete?"] = False
    edited_df = st.data_editor(filtered_df, num_rows="dynamic", use_container_width=True, key="editor")

    if st.button("🗑 Delete Selected Rows"):
        ids_to_delete = edited_df[edited_df["Delete?"]]["PatientID"].tolist()
        st.session_state.df = st.session_state.df[~st.session_state.df["PatientID"].isin(ids_to_delete)]
        st.session_state.df.to_csv(DATA_FILE, index=False)
        st.success("✅ Selected rows deleted & saved!")
    else:
        updated_rows = edited_df.drop(columns=["Delete?"])
        st.session_state.df.update(updated_rows)
        st.session_state.df.to_csv(DATA_FILE, index=False)

    # ------------------- STEP 7/8: CHARTS -------------------
    st.subheader("📈 Analytics & Visualizations")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Department-wise Patient Count**")
        dept_count_chart = st.session_state.df["Department"].value_counts()
        fig, ax = plt.subplots()
        dept_count_chart.plot(kind="bar", ax=ax)
        ax.set_ylabel("Patients")
        ax.set_title("Patients per Department")
        st.pyplot(fig)

    with col2:
        st.write("**Gender Distribution**")
        gender_count = st.session_state.df["Gender"].value_counts()
        fig, ax = plt.subplots()
        gender_count.plot(kind="pie", autopct="%1.1f%%", ax=ax)
        ax.set_ylabel("")
        ax.set_title("Gender Distribution")
        st.pyplot(fig)

    # ------------------- STEP 10: DOWNLOAD -------------------
    output = BytesIO()
    df.to_csv(output, index=False)  # ✅ Export transformed df with StayDuration + updated DischargeDate
    st.download_button("⬇ Download Updated CSV", output.getvalue(), "transformed_admissions.csv", "text/csv")

else:
    st.info("📌 No data available yet. Please upload a CSV file or add a patient record to get started.")
