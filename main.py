import streamlit as st
import sqlite3

# Connect to or create the database
conn = sqlite3.connect('mental_health_tracker.db')
cursor = conn.cursor()

# Create the table if it doesn't exist (ensures data persistence)
cursor.execute('''CREATE TABLE IF NOT EXISTS entries (
                  date TEXT PRIMARY KEY,
                  mood_rating INTEGER,
                  sleep_hours REAL,
                  description TEXT
                )''')
conn.commit()


# Function to add a new entry
def add_entry():
    date = st.text_input("Date (YYYY-MM-DD):")
    mood_rating = st.number_input("Mood Rating (1-5):", min_value=1, max_value=5)
    sleep_hours = st.number_input("Sleep Hours:")
    description = st.text_area("Description:")

    if st.button("Add Entry"):
        try:
            cursor.execute('''INSERT INTO entries (date, mood_rating, sleep_hours, description)
                              VALUES (?, ?, ?, ?)''', (date, mood_rating, sleep_hours, description))
            conn.commit()
            st.success("Entry added successfully!")
        except sqlite3.IntegrityError:
            st.error("Error: Entry with this date already exists. Please update or choose a different date.")


# Function to delete an entry
def delete_entry():
    date = st.text_input("Enter the date of the entry to delete (YYYY-MM-DD):")

    if st.button("Delete Entry"):
        try:
            cursor.execute('''DELETE FROM entries WHERE date = ?''', (date,))
            conn.commit()
            st.success("Entry deleted successfully!")
        except sqlite3.Error:
            st.error("Error: Entry not found.")


# Function to update an entry
def update_entry():
    date = st.text_input("Enter the date of the entry to update (YYYY-MM-DD):")
    new_mood_rating = st.number_input("Update Mood Rating (1-5):", min_value=1, max_value=5)
    new_sleep_hours = st.number_input("Update Sleep Hours:")
    new_description = st.text_area("Update Description:")

    if st.button("Update Entry"):
        try:
            cursor.execute('''UPDATE entries SET mood_rating = ?, sleep_hours = ?, description = ? WHERE date = ?''',
                            (new_mood_rating, new_sleep_hours, new_description, date))
            conn.commit()
            st.success("Entry updated successfully!")
        except sqlite3.Error:
            st.error("Error: Entry not found.")


# Function to view all entries

# ... (rest of your code)

def view_all_entries():
    cursor.execute('SELECT * FROM entries')
    rows = cursor.fetchall()

    if rows:
        st.header("All Entries")
        column_names = ["Date", "Mood Rating", "Sleep Hours", "Description"]  # Define your desired column names
        st.dataframe(rows)
    else:
        st.subheader("No entries found.")

# ... (rest of your code)

# Create the Streamlit app layout using a sidebar

st.sidebar.title("Mental Health Tracker")
page = st.sidebar.selectbox("Select a page:", ["Add Entry", "Delete Entry", "Update Entry", "View All Entries"])

if page == "Add Entry":
    add_entry()
elif page == "Delete Entry":
    delete_entry()
elif page == "Update Entry":
    update_entry()
elif page == "View All Entries":
    view_all_entries()

# Close the database connection at the end
conn.close()

'''
cd c:\Users\swagg\OneDrive\Desktop\Python fr\Mental Health Tracker\MentalHealthchatbotstreamlit


streamlit run main.py


'''