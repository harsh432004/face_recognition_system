import pandas as pd
import streamlit as st
import datetime

# Placeholder function for retrieving data from Redis


def retrieve_data(name):
    return pd.DataFrame({'Name': ['John', 'Alice'], 'Role': ['Student', 'Teacher']})


# Tabs setup
tab1, tab2, tab3 = st.columns(3)

# Tab 1: Registered Data
with tab1:
    st.subheader('Registered Data')
    if st.button('Refresh Data'):
        with st.spinner('Retrieving Data from Redis DB ...'):
            redis_face_db = retrieve_data(name='academy:register')
            st.dataframe(redis_face_db[['Name', 'Role']])

# Tab 2: Logs
with tab2:
    st.subheader('Logs')
    if st.button('Refresh Logs'):
        # Placeholder for load_logs() function
        st.write("Logs will appear here")

# Tab 3: Attendance Report
with tab3:
    st.subheader('Attendance Report')

    # Placeholder for logs processing
    logs_df = pd.DataFrame({
        'Name': ['John', 'Alice'],
        'Role': ['Student', 'Teacher'],
        'Timestamp': [datetime.datetime.now(), datetime.datetime.now() - datetime.timedelta(hours=2)]
    })

    # Processing logs into a report
    report_df = logs_df.groupby(['Name', 'Role']).agg(
        In_time=pd.NamedAgg(column='Timestamp', aggfunc='min'),
        Out_time=pd.NamedAgg(column='Timestamp', aggfunc='max')
    ).reset_index()

    report_df['Duration'] = report_df['Out_time'] - report_df['In_time']
    report_df['Duration_hours'] = report_df['Duration'] / pd.Timedelta(hours=1)

    # Displaying complete and filtered reports
    tab1, tab2 = st.columns(2)

    with tab1:
        st.subheader('Complete Report')
        st.dataframe(report_df)

    with tab2:
        st.subheader('Search Records')

        date_in = st.date_input('Filter Date', datetime.datetime.now().date())
        name_list = report_df['Name'].unique().tolist()
        name_in = st.selectbox('Select Name', ['ALL'] + name_list)

        role_list = report_df['Role'].unique().tolist()
        role_in = st.selectbox('Select Role', ['ALL'] + role_list)

        duration_in = st.slider('Filter Duration in Hours', 0, 24, 6)

        status_list = ['Present', 'Absent',
                       'Half Day (less than 4 hours)', 'Absent (Less than 1 hr)']
        status_in = st.multiselect(
            'Select Status', status_list, default=status_list)

        if st.button('Submit'):
            filter_df = report_df.copy()
            filter_df['Duration_hours'] = filter_df['Duration'] / \
                pd.Timedelta(hours=1)

            if name_in != 'ALL':
                filter_df = filter_df[filter_df['Name'] == name_in]

            if role_in != 'ALL':
                filter_df = filter_df[filter_df['Role'] == role_in]

            if duration_in > 0:
                filter_df = filter_df[filter_df['Duration_hours']
                                    > duration_in]

            if 'Present' not in status_in:
                filter_df = filter_df[~filter_df['Duration_hours'].isnull()]

            st.dataframe(filter_df)
