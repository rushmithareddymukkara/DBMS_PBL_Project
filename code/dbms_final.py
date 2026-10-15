import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Faculty Workload & Timetable Dashboard",
    page_icon="📅",
    layout="wide"
)

# Main Title & Subtitle
st.title("🎓 Faculty Workload & Timetable Management System")
st.markdown("Woxsen University — School of Technology | **DBMS PBL Project**")
st.divider()

# Sidebar Navigation
st.sidebar.header("Navigation Modules")
module = st.sidebar.radio(
    "Select Dashboard View:",
    [
        "Faculty Workload Report", 
        "Section Timetable View", 
        "Room Utilization Analysis", 
        "Schedule Clash Monitor"
    ]
)

# Mock Data matching Schema
@st.cache_data
def load_sample_data():
    faculty_df = pd.DataFrame([
        {"Employee No": "EMP101", "Faculty Name": "Dr. Sahithi", "Designation": "Assistant Professor", "Allocated Hours": 12.0, "Max Norm": 16.0, "Remaining Capacity": 4.0},
        {"Employee No": "EMP102", "Faculty Name": "Dr. Rajesh Sharma", "Designation": "Professor", "Allocated Hours": 14.0, "Max Norm": 12.0, "Remaining Capacity": -2.0},
        {"Employee No": "EMP103", "Faculty Name": "Prof. Anita Roy", "Designation": "Associate Professor", "Allocated Hours": 10.0, "Max Norm": 14.0, "Remaining Capacity": 4.0},
    ])
    
    timetable_df = pd.DataFrame([
        {"Day": "Monday", "Time Slot": "09:00 - 10:30", "Course Code": "CS201", "Course Title": "Database Management Systems", "Faculty": "Dr. Sahithi", "Room": "Lab-3"},
        {"Day": "Monday", "Time Slot": "11:00 - 12:30", "Course Code": "AI302", "Course Title": "Machine Learning", "Faculty": "Dr. Rajesh Sharma", "Room": "CR-102"},
        {"Day": "Wednesday", "Time Slot": "02:00 - 03:30", "Course Code": "CS201", "Course Title": "Database Management Systems", "Faculty": "Dr. Sahithi", "Room": "Lab-3"},
    ])
    
    room_df = pd.DataFrame([
        {"Room Code": "CR-101", "Building": "Block-A", "Capacity": 60, "Scheduled Periods/Wk": 18, "Weekly Hours": 27.0},
        {"Room Code": "CR-102", "Building": "Block-A", "Capacity": 60, "Scheduled Periods/Wk": 15, "Weekly Hours": 22.5},
        {"Room Code": "Lab-3", "Building": "Tech Hub", "Capacity": 40, "Scheduled Periods/Wk": 22, "Weekly Hours": 33.0},
    ])
    
    clash_df = pd.DataFrame([
        {"Entry ID 1": "ENTRY_012", "Entry ID 2": "ENTRY_019", "Conflict Type": "Room Double-Booking", "Resource": "CR-102", "Day / Time": "Tuesday 10:00 AM", "Status": "CRITICAL ALERT"},
    ])
    
    return faculty_df, timetable_df, room_df, clash_df

faculty_data, timetable_data, room_data, clash_data = load_sample_data()

# --- MODULE 1: FACULTY WORKLOAD ---
if module == "Faculty Workload Report":
    st.header("📊 Faculty Workload & Capacity Analysis")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Faculty Assigned", len(faculty_data))
    col2.metric("Overloaded Faculty", 1, delta="-1 Alert", delta_color="inverse")
    col3.metric("Avg Weekly Hours", "12.0 Hrs")
    
    st.subheader("Faculty Load Summary")
    st.dataframe(faculty_data, use_container_width=True)
    
    st.markdown("### Weekly Hours vs Maximum Target")
    st.bar_chart(faculty_data.set_index("Faculty Name")[["Allocated Hours", "Max Norm"]])

# --- MODULE 2: SECTION TIMETABLE ---
elif module == "Section Timetable View":
    st.header("📅 Section Master Schedule")
    
    col1, col2 = st.columns(2)
    selected_sec = col1.selectbox("Select Section:", ["AIML Rhinos - Sem 4", "CSE - Sem 4", "ECE - Sem 6"])
    selected_day = col2.selectbox("Filter Day:", ["All Days", "Monday", "Wednesday", "Friday"])
    
    st.subheader(f"Weekly Schedule for {selected_sec}")
    st.dataframe(timetable_data, use_container_width=True)

# --- MODULE 3: ROOM UTILIZATION ---
elif module == "Room Utilization Analysis":
    st.header("🏫 Room & Lab Allocation Report")
    
    st.subheader("Classroom Usage Metrics")
    st.dataframe(room_data, use_container_width=True)
    
    st.markdown("### Weekly Usage Hours per Room")
    st.bar_chart(room_data.set_index("Room Code")["Weekly Hours"])

# --- MODULE 4: SCHEDULE CLASH MONITOR ---
elif module == "Schedule Clash Monitor":
    st.header("⚠️ Timetable Integrity & Conflict Detection")
    
    st.error("1 Conflict Detected in Proposed Schedule!")
    st.dataframe(clash_data, use_container_width=True)