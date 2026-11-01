import streamlit as st
import re
from datetime import datetime, date

# Set page configuration
#st.set_page_config(page_title="Employee Registration", layout="centered")

st.title("Employee Registration Form")
st.write("Please fill out the form below to register a new employee.")

# Create the form
with st.form("registration_form", clear_on_submit=False):
    st.subheader("Personal Information")
    
    # Full Name
    full_name = st.text_input("Full Name *")
    
    # Email Address
    email = st.text_input("Email Address *")
    
    # Phone Number
    phone = st.text_input("Phone Number * (e.g., +1234567890 or 123-456-7890)")
    
    # Date of Birth (Must be at least 18 years old)
    max_birth_year = date.today().year - 18
    dob = st.date_input(
        "Date of Birth *", 
        value=date(max_birth_year, 1, 1),
        max_value=date.today()
    )
    
    st.markdown("---")
    st.subheader("Job Details")
    
    # Department & Position
    department = st.selectbox(
        "Department *", 
        ["Select Department", "HR", "Engineering", "Data Science", "Marketing", "Sales", "Finance"]
    )
    position = st.text_input("Job Title / Position *")
    
    # Joining Date
    joining_date = st.date_input("Joining Date *", value=date.today())
    
    # Employment Type
    emp_type = st.radio("Employment Type *", ["Full-Time", "Part-Time", "Contract", "Intern"])
    
    # Submit Button
    submitted = st.form_submit_button("Register Employee")

# Validation Logic
if submitted:
    errors = []
    
    # 1. Validate Name
    if not full_name.strip():
        errors.append("Full Name is required.")
    elif len(full_name.strip()) < 2:
        errors.append("Full Name must be at least 2 characters long.")
        
    # 2. Validate Email using Regex
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not email.strip():
        errors.append("Email Address is required.")
    elif not re.match(email_regex, email.strip()):
        errors.append("Please enter a valid email address.")
        
    # 3. Validate Phone Number (Basic regex for digits, dashes, and plus signs)
    phone_regex = r"^\+?[0-9\s\-]{7,15}$"
    if not phone.strip():
        errors.append("Phone Number is required.")
    elif not re.match(phone_regex, phone.strip()):
        errors.append("Please enter a valid phone number.")
        
    # 4. Validate Age (Must be >= 18)
    age = (date.today() - dob).days // 365
    if age < 18:
        errors.append("Employee must be at least 18 years old.")
        
    # 5. Validate Department
    if department == "Select Department":
        errors.append("Please select a valid Department.")
        
    # 6. Validate Position
    if not position.strip():
        errors.append("Job Title / Position is required.")

    # Display Results or Errors
    if errors:
        for error in errors:
            st.error(error)
    else:
        st.success(f"🎉 Success! **{full_name}** has been successfully registered as a **{position}** in the **{department}** department.")
        
        # Display a summary of the registered data
        st.balloons()
        st.snow()
        st.write("### Submitted Employee Profile Summary:")
        summary_data = {
            "Full Name": full_name,
            "Email": email,
            "Phone": phone,
            "Age": age,
            "Department": department,
            "Position": position,
            "Joining Date": joining_date.strftime("%Y-%m-%d"),
            "Employment Type": emp_type
        }
        st.json(summary_data)