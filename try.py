impor streamlit as st

st.title("Student Registration Name")

name = st.text_input("Enter Name")
age = st.text_input("Enter Age")
email = st.text_input("Enter Email")
course = st.selectbox("Select Course", ["Select", "IT", "Software Engineer", "Data Science"])

if st.button("Register"):
	try:
	    # Check empty fields
	    if name == "" or age == "" or email == "" or course == "Select":
		raise ValueError("All fields are required")

	    # convert age to integer
	    age = int(age)

	    # Validate age
	    if age <= 0:
			raise ValueError("Age must be a positive number.")

	    # Validate email (simple check)
	    if "@" not in email or "." not in email:
		raise ValueError("Invalid email format")

	except ValueError as ve:
		st.error(f"Input Error: {ve}")

	except Exception as e:
		st.error("System Error: {e}")
	
	else:
	     st.success("Registration Successful")
	     st.write("Student Details")
             st.write(f"Name: {name}")
             st.write(f"Age: {age}")
             st.write(f"Email: {email}")
	     st.write(f"Course: {course}")

	finally:
	     st.info("Process Completed")