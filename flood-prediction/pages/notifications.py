# import streamlit as st
# import mongodb from "./app/mongodb.py"

# def notifications_page():
#     st.title("Notifications")
#     st.markdown("""
#     Stay updated with the latest alerts and flood warnings.
# """)

#     st.info("⚠️ Flood Alert: High-risk areas in Rangpur for the next 3 days.")
#     st.warning("🌧️ Heavy rainfall expected in Sylhet region.")
#     st.success("✔️ No major flood warnings for Dhaka this week.")
#     # Example: Sign up for alerts
#     email = st.text_input("Enter your email to receive alerts:")
#     if st.button("Subscribe"):
#         st.success(f"Thank you for subscribing! Alerts will be sent to {email}.")

#     # Example: Display recent warnings
#     st.subheader("Recent Flood Warnings")
#     warnings = [
#         "Flood warning issued for Dhaka on 2023-10-15.",
#         "Moderate flood risk in Sylhet on 2023-10-14.",
#         "No active warnings for Chittagong.",
#     ]
#     for warning in warnings:
#         st.write(warning)
from app.mongodb import save_subscription  

def notifications_page():
    st.title("Notifications")
    st.markdown("""
    Stay updated with the latest alerts and flood warnings.
    """)

    st.info("⚠️ Flood Alert: High-risk areas in Rangpur for the next 3 days.")
    st.warning("🌧️ Heavy rainfall expected in Sylhet region.")
    st.success("✔️ No major flood warnings for Dhaka this week.")
    
    # Example: Sign up for alerts
    email = st.text_input("Enter your email to receive alerts:")
    location = st.text_input("Enter your location:")
    
    if st.button("Subscribe"):
        if email and location:
            # Save subscription to the database
            save_subscription(email, location)
            st.success(f"Thank you for subscribing! Alerts will be sent to {email} for {location}.")
        else:
            st.error("Please provide both email and location.")
            
    # Example: Display recent warnings
    st.subheader("Recent Flood Warnings")
    warnings = [
        "Flood warning issued for Dhaka on 2023-10-15.",
        "Moderate flood risk in Sylhet on 2023-10-14.",
        "No active warnings for Chittagong.",
    ]
    for warning in warnings:
        st.write(warning)
