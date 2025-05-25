import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# Page configuration
st.set_page_config(
    page_title="Nordic Explorer - Adventure Travel Platform",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2E86AB;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2E86AB 0%, #A23B72 100%);
    }
</style>
""", unsafe_allow_html=True)

# Language selection
languages = {
    "English": "en",
    "Svenska": "sv", 
    "Norsk": "no",
    "Suomi": "fi"
}

# Sidebar for navigation
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=300&h=200&fit=crop", 
             caption="Nordic Explorer", width=250)
    
    selected_lang = st.selectbox("🌍 Language / Språk", list(languages.keys()))
    
    st.markdown("---")
    
    page = st.radio("📍 Navigation", [
        "🏠 Home",
        "🗺️ Trip Planner", 
        "🏔️ Adventures",
        "🏨 Accommodations",
        "📊 Analytics",
        "💳 Booking"
    ])

# Main content based on page selection
if page == "🏠 Home":
    st.markdown('<h1 class="main-header">🏔️ Nordic Explorer</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center; color: #666;">Discover the Magic of Scandinavian Adventures</h3>', unsafe_allow_html=True)
    
    # Hero metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🌍 Destinations", "247", delta="12 new")
    with col2:
        st.metric("🎿 Activities", "89", delta="5 added")
    with col3:
        st.metric("⭐ Avg Rating", "4.8/5", delta="0.2")
    with col4:
        st.metric("🧑‍🤝‍🧑 Happy Travelers", "15,432", delta="234")
    
    st.markdown("---")
    
    # Featured destinations
    st.subheader("🌟 Featured Nordic Destinations")
    
    destinations_data = {
        'Country': ['Norway', 'Sweden', 'Finland', 'Denmark', 'Iceland'],
        'Popular Activities': ['Fjord Tours', 'Northern Lights', 'Lapland Adventures', 'Copenhagen Culture', 'Glacier Hiking'],
        'Best Season': ['Jun-Aug', 'Dec-Mar', 'Dec-Mar', 'May-Sep', 'Jun-Aug'],
        'Avg Cost (€)': [1200, 980, 850, 750, 1400],
        'Rating': [4.9, 4.7, 4.8, 4.6, 4.9]
    }
    
    df_destinations = pd.DataFrame(destinations_data)
    st.dataframe(df_destinations, use_container_width=True)
    
    # Interactive map
    st.subheader("📍 Nordic Adventure Map")
    
    # Sample coordinates for Nordic countries
    map_data = pd.DataFrame({
        'lat': [60.4720, 60.1282, 61.9241, 56.2639, 64.9631],
        'lon': [8.4689, 18.6435, 25.7482, 9.5018, -19.0208],
        'city': ['Oslo', 'Stockholm', 'Helsinki', 'Copenhagen', 'Reykjavik'],
        'adventures': [45, 38, 32, 28, 52]
    })
    
    st.map(map_data)

elif page == "🗺️ Trip Planner":
    st.header("🗺️ Smart Trip Planner")
    st.markdown("Plan your perfect Nordic adventure with AI-powered recommendations")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Trip Preferences")
        
        budget = st.slider("💰 Budget (EUR)", 500, 5000, 1500)
        duration = st.slider("📅 Trip Duration (days)", 3, 21, 7)
        
        interests = st.multiselect("🎯 Interests", [
            "Northern Lights", "Fjord Tours", "Hiking", "Winter Sports",
            "Cultural Sites", "Food & Drink", "Wildlife", "Photography"
        ], default=["Northern Lights", "Hiking"])
        
        travel_style = st.radio("🎒 Travel Style", [
            "Budget Backpacker", "Mid-range Explorer", "Luxury Traveler"
        ])
        
        season = st.selectbox("🌤️ Preferred Season", [
            "Spring (Mar-May)", "Summer (Jun-Aug)", 
            "Autumn (Sep-Nov)", "Winter (Dec-Feb)"
        ])
    
    with col2:
        st.subheader("Recommended Itinerary")
        
        if st.button("🚀 Generate Trip Plan"):
            with st.spinner("Creating your perfect Nordic adventure..."):
                # Simulate AI processing
                import time
                time.sleep(2)
                
                st.success("✅ Your personalized itinerary is ready!")
                
                # Sample itinerary based on preferences
                st.markdown("### 🗓️ 7-Day Norway Adventure")
                
                itinerary = [
                    {"Day": 1, "Location": "Oslo", "Activity": "City exploration & Viking Museum", "Cost": "€120"},
                    {"Day": 2, "Location": "Bergen", "Activity": "Fjord cruise & Fish Market", "Cost": "€180"},
                    {"Day": 3, "Location": "Geiranger", "Activity": "Geirangerfjord tour", "Cost": "€200"},
                    {"Day": 4, "Location": "Ålesund", "Activity": "Art Nouveau architecture tour", "Cost": "€90"},
                    {"Day": 5, "Location": "Trondheim", "Activity": "Nidaros Cathedral & Old Town", "Cost": "€110"},
                    {"Day": 6, "Location": "Tromsø", "Activity": "Northern Lights hunting", "Cost": "€250"},
                    {"Day": 7, "Location": "Tromsø", "Activity": "Husky sledding & departure", "Cost": "€180"}
                ]
                
                df_itinerary = pd.DataFrame(itinerary)
                st.dataframe(df_itinerary, use_container_width=True)
                
                total_cost = sum([int(item["Cost"].replace("€", "")) for item in itinerary])
                st.metric("💰 Total Estimated Cost", f"€{total_cost}", delta=f"€{budget-total_cost} under budget")

elif page == "🏔️ Adventures":
    st.header("🏔️ Nordic Adventures")
    
    # Filter section
    col1, col2, col3 = st.columns(3)
    with col1:
        country_filter = st.selectbox("🌍 Country", ["All", "Norway", "Sweden", "Finland", "Denmark", "Iceland"])
    with col2:
        activity_filter = st.selectbox("🎯 Activity Type", ["All", "Winter Sports", "Hiking", "Water Sports", "Cultural", "Wildlife"])
    with col3:
        difficulty_filter = st.selectbox("📊 Difficulty", ["All", "Easy", "Moderate", "Challenging", "Expert"])
    
    # Sample adventures data
    adventures = [
        {"Name": "Lofoten Islands Hiking", "Country": "Norway", "Type": "Hiking", "Difficulty": "Moderate", "Duration": "5 days", "Price": "€899", "Rating": 4.9},
        {"Name": "Northern Lights Safari", "Country": "Finland", "Type": "Wildlife", "Difficulty": "Easy", "Duration": "3 days", "Price": "€599", "Rating": 4.8},
        {"Name": "Ice Hotel Experience", "Country": "Sweden", "Type": "Cultural", "Difficulty": "Easy", "Duration": "2 days", "Price": "€450", "Rating": 4.7},
        {"Name": "Glacier Hiking", "Country": "Iceland", "Type": "Hiking", "Difficulty": "Challenging", "Duration": "1 day", "Price": "€180", "Rating": 4.9},
        {"Name": "Fjord Kayaking", "Country": "Norway", "Type": "Water Sports", "Difficulty": "Moderate", "Duration": "4 days", "Price": "€720", "Rating": 4.8},
        {"Name": "Reindeer Farm Visit", "Country": "Finland", "Type": "Cultural", "Difficulty": "Easy", "Duration": "1 day", "Price": "€120", "Rating": 4.6}
    ]
    
    # Display adventures as cards
    for i, adventure in enumerate(adventures):
        with st.container():
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            
            with col1:
                st.markdown(f"### {adventure['Name']}")
                st.markdown(f"📍 {adventure['Country']} • 🎯 {adventure['Type']} • 📊 {adventure['Difficulty']}")
            
            with col2:
                st.metric("⏰ Duration", adventure['Duration'])
            
            with col3:
                st.metric("💰 Price", adventure['Price'])
            
            with col4:
                st.metric("⭐ Rating", adventure['Rating'])
            
            if st.button(f"Book Now", key=f"book_{i}"):
                st.success(f"✅ {adventure['Name']} added to cart!")
            
            st.markdown("---")

elif page == "🏨 Accommodations":
    st.header("🏨 Nordic Accommodations")
    st.markdown("From ice hotels to cozy cabins - find your perfect Nordic stay")
    
    # Search filters
    col1, col2, col3 = st.columns(3)
    with col1:
        location = st.text_input("📍 Location", placeholder="Enter city or region")
    with col2:
        checkin = st.date_input("📅 Check-in", datetime.now())
    with col3:
        checkout = st.date_input("📅 Check-out", datetime.now() + timedelta(days=3))
    
    col1, col2, col3 = st.columns(3)
    with col1:
        guests = st.number_input("👥 Guests", min_value=1, max_value=10, value=2)
    with col2:
        accommodation_type = st.selectbox("🏠 Type", ["All", "Hotel", "Cabin", "Hostel", "Unique Stay"])
    with col3:
        price_range = st.slider("💰 Price Range (per night)", 50, 500, (100, 300))
    
    # Sample accommodations
    accommodations = [
        {"Name": "Arctic TreeHouse Hotel", "Location": "Rovaniemi, Finland", "Type": "Unique Stay", "Price": 280, "Rating": 4.9, "Image": "🏔️"},
        {"Name": "Ice Hotel", "Location": "Jukkasjärvi, Sweden", "Type": "Unique Stay", "Price": 320, "Rating": 4.8, "Image": "🧊"},
        {"Name": "Bergen Boutique Hotel", "Location": "Bergen, Norway", "Type": "Hotel", "Price": 150, "Rating": 4.6, "Image": "🏨"},
        {"Name": "Lakeside Cabin", "Location": "Finnish Lakeland", "Type": "Cabin", "Price": 120, "Rating": 4.7, "Image": "🏘️"},
        {"Name": "Northern Lights Lodge", "Location": "Tromsø, Norway", "Type": "Hotel", "Price": 200, "Rating": 4.8, "Image": "🌌"},
        {"Name": "Copenhagen Central Hostel", "Location": "Copenhagen, Denmark", "Type": "Hostel", "Price": 75, "Rating": 4.4, "Image": "🏠"}
    ]
    
    # Filter accommodations based on criteria
    filtered_accommodations = [acc for acc in accommodations if price_range[0] <= acc["Price"] <= price_range[1]]
    
    # Display accommodations
    for acc in filtered_accommodations:
        with st.container():
            col1, col2, col3, col4, col5 = st.columns([1, 3, 1, 1, 1])
            
            with col1:
                st.markdown(f"<div style='font-size: 3rem; text-align: center;'>{acc['Image']}</div>", unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"### {acc['Name']}")
                st.markdown(f"📍 {acc['Location']} • 🏠 {acc['Type']}")
            
            with col3:
                st.metric("💰 Per Night", f"€{acc['Price']}")
            
            with col4:
                st.metric("⭐ Rating", acc['Rating'])
            
            with col5:
                if st.button("Book", key=f"acc_{acc['Name']}"):
                    st.success("Added to booking!")
            
            st.markdown("---")

elif page == "📊 Analytics":
    st.header("📊 Platform Analytics")
    
    # Generate sample analytics data
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    bookings_data = pd.DataFrame({
        'Date': dates,
        'Bookings': np.random.poisson(15, len(dates)) + 5,
        'Revenue': np.random.normal(2500, 500, len(dates))
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Booking Trends")
        fig = px.line(bookings_data, x='Date', y='Bookings', title='Daily Bookings Over Time')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("💰 Revenue Analysis")
        fig = px.bar(bookings_data.groupby(bookings_data['Date'].dt.month)['Revenue'].sum().reset_index(), 
                     x='Date', y='Revenue', title='Monthly Revenue')
        st.plotly_chart(fig, use_container_width=True)
    
    # Popular destinations
    st.subheader("🌟 Popular Destinations")
    dest_data = pd.DataFrame({
        'Destination': ['Norway', 'Iceland', 'Sweden', 'Finland', 'Denmark'],
        'Bookings': [1250, 980, 750, 650, 420],
        'Revenue': [250000, 196000, 150000, 130000, 84000]
    })
    
    col1, col2 = st.columns(2)
    with col1:
        fig = px.pie(dest_data, values='Bookings', names='Destination', title='Bookings by Country')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.bar(dest_data, x='Destination', y='Revenue', title='Revenue by Country')
        st.plotly_chart(fig, use_container_width=True)

elif page == "💳 Booking":
    st.header("💳 Booking Summary")
    
    # Sample cart items
    if 'cart_items' not in st.session_state:
        st.session_state.cart_items = []
    
    if not st.session_state.cart_items:
        st.info("🛒 Your cart is empty. Browse our adventures and accommodations to start planning!")
        if st.button("🏔️ Browse Adventures"):
            st.rerun()
    else:
        st.subheader("🛒 Your Selected Items")
        
        total_cost = 0
        for item in st.session_state.cart_items:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{item['name']}**")
                st.write(f"{item['details']}")
            with col2:
                st.write(f"€{item['price']}")
            with col3:
                if st.button("Remove", key=f"remove_{item['name']}"):
                    st.session_state.cart_items.remove(item)
                    st.rerun()
            
            total_cost += item['price']
            st.markdown("---")
        
        st.metric("💰 Total Cost", f"€{total_cost}")
        
        # Payment form
        st.subheader("💳 Payment Information")
        
        col1, col2 = st.columns(2)
        with col1:
            payment_method = st.radio("Payment Method", ["Credit Card", "PayPal", "Bank Transfer"])
            if payment_method == "Credit Card":
                st.text_input("Card Number", placeholder="1234 5678 9012 3456")
                col_a, col_b = st.columns(2)
                with col_a:
                    st.text_input("Expiry", placeholder="MM/YY")
                with col_b:
                    st.text_input("CVV", placeholder="123")
        
        with col2:
            st.text_input("Full Name", placeholder="John Doe")
            st.text_input("Email", placeholder="john@example.com")
            st.text_input("Phone", placeholder="+47 123 45 678")
        
        if st.button("🚀 Complete Booking", type="primary"):
            with st.spinner("Processing your booking..."):
                import time
                time.sleep(3)
                st.success("🎉 Booking confirmed! Check your email for details.")
                st.balloons()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <h4>🏔️ Nordic Explorer</h4>
    <p>Your gateway to Scandinavian adventures | Contact: info@nordicexplorer.com</p>
    <p>🌍 Available in: English • Svenska • Norsk • Suomi</p>
</div>
""", unsafe_allow_html=True)