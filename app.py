import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import json
import io

# Page configuration
st.set_page_config(
    page_title="Healthcare Contract Manager",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional healthcare styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    .metric-card {
        background: #f0f8ff;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #1f4e79;
        margin: 0.5rem 0;
    }
    .warning-box {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .success-box {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Sidebar navigation
    st.sidebar.title("🏥 Healthcare Contract Manager")
    st.sidebar.markdown("---")
    
    page = st.sidebar.selectbox(
        "Navigate to:",
        ["🏠 Dashboard", "📋 Contract Analyzer", "💰 Revenue Impact Simulator", "📅 Contract Lifecycle Tracker"]
    )
    
    if page == "🏠 Dashboard":
        show_dashboard()
    elif page == "📋 Contract Analyzer":
        show_contract_analyzer()
    elif page == "💰 Revenue Impact Simulator":
        show_revenue_simulator()
    elif page == "📅 Contract Lifecycle Tracker":
        show_lifecycle_tracker()

def show_dashboard():
    st.markdown('<h1 class="main-header">Healthcare Contract Management Dashboard</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="success-box">
        <h3>👋 Welcome to your Contract Management Hub</h3>
        <p>Streamline your managed care contract operations with AI-powered tools designed specifically for physician practice managers.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Active Contracts", "12", "2")
    with col2:
        st.metric("Contracts Expiring Soon", "3", "-1")
    with col3:
        st.metric("Monthly Revenue Impact", "$45,230", "8.2%")
    with col4:
        st.metric("Risk Score Average", "2.3/5", "-0.5")
    
    st.markdown("---")
    
    # Feature overview
    st.subheader("🚀 Available Tools")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>📋 Contract Analyzer</h3>
            <p>Upload contracts and get instant AI analysis of:</p>
            <ul>
                <li>Key terms & conditions</li>
                <li>Risk assessment</li>
                <li>Revenue opportunities</li>
                <li>Compliance issues</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>💰 Revenue Impact Simulator</h3>
            <p>Model financial scenarios including:</p>
            <ul>
                <li>Rate change impacts</li>
                <li>Volume projections</li>
                <li>Bonus calculations</li>
                <li>Cost-benefit analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>📅 Contract Lifecycle Tracker</h3>
            <p>Stay on top of all contracts with:</p>
            <ul>
                <li>Renewal reminders</li>
                <li>Performance tracking</li>
                <li>Deadline management</li>
                <li>Action item lists</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def show_contract_analyzer():
    st.title("📋 Contract Analyzer")
    st.markdown("Upload your managed care contracts for instant AI-powered analysis")
    
    # File upload
    uploaded_file = st.file_uploader(
        "Choose a contract file", 
        type=['pdf', 'docx', 'txt'],
        help="Upload PDF, Word, or text documents"
    )
    
    if uploaded_file is not None:
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        
        # Simulate contract analysis (replace with actual AI integration)
        if st.button("🔍 Analyze Contract", type="primary"):
            with st.spinner("Analyzing contract... This may take a moment."):
                # Simulate processing time
                import time
                time.sleep(2)
                
                # Mock analysis results
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📊 Contract Summary")
                    st.markdown("""
                    <div class="metric-card">
                        <strong>Contract Type:</strong> Managed Care Agreement<br>
                        <strong>Payer:</strong> BlueCross BlueShield<br>
                        <strong>Term:</strong> 3 years<br>
                        <strong>Auto-renewal:</strong> Yes (90-day notice)<br>
                        <strong>Risk Level:</strong> <span style="color: orange;">Medium</span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.subheader("⚠️ Key Risk Factors")
                    st.warning("• Capitation rate below market average")
                    st.warning("• Limited specialist referral network")
                    st.warning("• High patient satisfaction requirements")
                
                with col2:
                    st.subheader("💡 Opportunities")
                    st.success("• Quality bonus potential: $15K annually")
                    st.success("• Shared savings program available")
                    st.success("• Telemedicine reimbursement included")
                    
                    st.subheader("📈 Financial Impact")
                    revenue_data = pd.DataFrame({
                        'Category': ['Base Payments', 'Quality Bonuses', 'Shared Savings', 'Total Potential'],
                        'Annual Value': [180000, 15000, 8000, 203000]
                    })
                    st.bar_chart(revenue_data.set_index('Category'))
                
                st.subheader("📋 Action Items")
                st.markdown("""
                1. **Negotiate capitation rates** - Current rates 12% below regional average
                2. **Review quality metrics** - Ensure achievable bonus targets
                3. **Clarify termination clauses** - 90-day notice period may be tight
                4. **Verify credential requirements** - All providers must be network-approved
                """)
    else:
        st.info("👆 Please upload a contract file to begin analysis")
        
        # Demo section
        st.markdown("---")
        st.subheader("🎯 What You'll Get")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**✅ Automated Analysis:**")
            st.markdown("• Payment terms breakdown")
            st.markdown("• Risk factor identification") 
            st.markdown("• Compliance requirement review")
            st.markdown("• Performance metric analysis")
        
        with col2:
            st.markdown("**📊 Actionable Insights:**")
            st.markdown("• Revenue optimization opportunities")
            st.markdown("• Negotiation leverage points")
            st.markdown("• Red flag identification")
            st.markdown("• Benchmark comparisons")

def show_revenue_simulator():
    st.title("💰 Revenue Impact Simulator")
    st.markdown("Model different contract scenarios to understand financial impact")
    
    # Input parameters
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Contract Parameters")
        contract_type = st.selectbox("Contract Type", 
                                   ["Fee-for-Service", "Capitation", "Shared Risk", "Bundled Payment"])
        
        monthly_patients = st.number_input("Monthly Patient Volume", 
                                         min_value=100, max_value=5000, value=800)
        
        base_rate = st.number_input("Base Payment Rate ($)", 
                                  min_value=50.0, max_value=500.0, value=125.0)
        
        quality_bonus = st.slider("Quality Bonus (%)", 0, 20, 5)
        
    with col2:
        st.subheader("Scenario Modeling")
        volume_change = st.slider("Volume Change (%)", -50, 100, 0)
        rate_change = st.slider("Rate Change (%)", -25, 25, 0)
        
        months_to_model = st.selectbox("Projection Period", [6, 12, 24, 36], index=1)
    
    # Calculate projections
    if st.button("📊 Run Simulation", type="primary"):
        # Base calculations
        adjusted_volume = monthly_patients * (1 + volume_change/100)
        adjusted_rate = base_rate * (1 + rate_change/100)
        monthly_base = adjusted_volume * adjusted_rate
        monthly_bonus = monthly_base * (quality_bonus/100)
        monthly_total = monthly_base + monthly_bonus
        
        # Generate monthly data
        months = list(range(1, months_to_model + 1))
        base_revenue = [monthly_base] * months_to_model
        bonus_revenue = [monthly_bonus] * months_to_model
        total_revenue = [monthly_total] * months_to_model
        cumulative_revenue = [sum(total_revenue[:i+1]) for i in range(months_to_model)]
        
        # Results display
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Monthly Revenue", f"${monthly_total:,.0f}", 
                     f"{((monthly_total/monthly_patients/base_rate-1)*100):+.1f}%")
        with col2:
            st.metric("Annual Projection", f"${monthly_total*12:,.0f}")
        with col3:
            st.metric("Revenue per Patient", f"${monthly_total/adjusted_volume:.0f}")
        
        # Charts
        st.subheader("📈 Revenue Projections")
        
        # Monthly revenue chart
        chart_data = pd.DataFrame({
            'Month': months,
            'Base Revenue': base_revenue,
            'Quality Bonus': bonus_revenue
        })
        st.bar_chart(chart_data.set_index('Month'))
        
        # Cumulative revenue
        cumulative_data = pd.DataFrame({
            'Month': months,
            'Cumulative Revenue': cumulative_revenue
        })
        st.line_chart(cumulative_data.set_index('Month'))
        
        # Scenario comparison table
        st.subheader("📋 Scenario Summary")
        scenarios_df = pd.DataFrame({
            'Scenario': ['Current', 'Optimistic (+10% vol, +5% rate)', 'Conservative (-5% vol, -2% rate)'],
            'Monthly Revenue': [
                f"${monthly_total:,.0f}",
                f"${monthly_patients*1.1*base_rate*1.05*(1+quality_bonus/100):,.0f}",
                f"${monthly_patients*0.95*base_rate*0.98*(1+quality_bonus/100):,.0f}"
            ],
            'Annual Impact': [
                f"${monthly_total*12:,.0f}",
                f"${monthly_patients*1.1*base_rate*1.05*(1+quality_bonus/100)*12:,.0f}",
                f"${monthly_patients*0.95*base_rate*0.98*(1+quality_bonus/100)*12:,.0f}"
            ]
        })
        st.dataframe(scenarios_df, use_container_width=True)

def show_lifecycle_tracker():
    st.title("📅 Contract Lifecycle Tracker")
    st.markdown("Monitor all your contracts, renewals, and important deadlines")
    
    # Sample contract data
    contracts_data = {
        'Contract': ['BlueCross Primary Care', 'Aetna Specialty', 'Medicare Advantage', 
                    'Medicaid MCO', 'United Healthcare', 'Cigna Behavioral Health'],
        'Payer': ['BlueCross', 'Aetna', 'Medicare', 'State Medicaid', 'UHC', 'Cigna'],
        'Start Date': ['2023-01-01', '2023-03-15', '2023-01-01', '2023-07-01', '2022-12-01', '2023-06-01'],
        'Expiration': ['2025-12-31', '2024-03-14', '2024-12-31', '2024-06-30', '2025-11-30', '2024-05-31'],
        'Status': ['Active', 'Expiring Soon', 'Active', 'Expiring Soon', 'Active', 'Expired'],
        'Auto Renew': ['Yes', 'No', 'Yes', 'Yes', 'No', 'No'],
        'Monthly Revenue': [25000, 18000, 35000, 12000, 28000, 8000],
        'Risk Level': ['Low', 'Medium', 'Low', 'High', 'Medium', 'High']
    }
    
    df = pd.DataFrame(contracts_data)
    df['Start Date'] = pd.to_datetime(df['Start Date'])
    df['Expiration'] = pd.to_datetime(df['Expiration'])
    df['Days to Expiration'] = (df['Expiration'] - datetime.now()).dt.days
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Contracts", len(df))
    with col2:
        expiring_soon = len(df[df['Days to Expiration'] <= 90])
        st.metric("Expiring in 90 Days", expiring_soon, delta=None)
    with col3:
        total_revenue = df['Monthly Revenue'].sum()
        st.metric("Total Monthly Revenue", f"${total_revenue:,}")
    with col4:
        high_risk = len(df[df['Risk Level'] == 'High'])
        st.metric("High Risk Contracts", high_risk)
    
    # Contract status overview
    st.subheader("📊 Contract Portfolio Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Status distribution
        status_counts = df['Status'].value_counts()
        st.subheader("Contract Status Distribution")
        st.bar_chart(status_counts)
    
    with col2:
        # Revenue by payer
        revenue_by_payer = df.groupby('Payer')['Monthly Revenue'].sum()
        st.subheader("Monthly Revenue by Payer")
        st.bar_chart(revenue_by_payer)
    
    # Detailed contract table
    st.subheader("📋 Contract Details")
    
    # Add filters
    col1, col2, col3 = st.columns(3)
    with col1:
        status_filter = st.multiselect("Filter by Status", 
                                     options=df['Status'].unique(), 
                                     default=df['Status'].unique())
    with col2:
        risk_filter = st.multiselect("Filter by Risk Level", 
                                   options=df['Risk Level'].unique(), 
                                   default=df['Risk Level'].unique())
    with col3:
        show_expiring = st.checkbox("Show only expiring in 90 days")
    
    # Apply filters
    filtered_df = df[df['Status'].isin(status_filter) & df['Risk Level'].isin(risk_filter)]
    if show_expiring:
        filtered_df = filtered_df[filtered_df['Days to Expiration'] <= 90]
    
    # Display table with styling
    def style_status(val):
        if val == 'Expired':
            return 'color: red'
        elif val == 'Expiring Soon':
            return 'color: orange'
        else:
            return 'color: green'
    
    def style_risk(val):
        if val == 'High':
            return 'background-color: #ffebee'
        elif val == 'Medium':
            return 'background-color: #fff3e0'
        else:
            return 'background-color: #e8f5e8'
    
    display_df = filtered_df[['Contract', 'Payer', 'Expiration', 'Days to Expiration', 
                             'Status', 'Auto Renew', 'Monthly Revenue', 'Risk Level']].copy()
    display_df['Monthly Revenue'] = display_df['Monthly Revenue'].apply(lambda x: f"${x:,}")
    
    st.dataframe(display_df, use_container_width=True)
    
    # Action items
    st.subheader("⚡ Action Items")
    
    # Generate action items for expiring contracts
    expiring_contracts = df[df['Days to Expiration'] <= 90]
    
    if not expiring_contracts.empty:
        st.markdown("**🔔 Urgent Actions Required:**")
        for _, contract in expiring_contracts.iterrows():
            days = contract['Days to Expiration']
            if days < 0:
                st.error(f"**{contract['Contract']}** - EXPIRED {abs(days)} days ago!")
            elif days <= 30:
                st.warning(f"**{contract['Contract']}** - Expires in {days} days")
            else:
                st.info(f"**{contract['Contract']}** - Expires in {days} days")
    else:
        st.success("✅ No urgent contract actions required at this time")
    
    # Renewal planning
    st.markdown("---")
    st.subheader("📅 Renewal Planning Calendar")
    
    # Show contracts expiring in next 12 months
    future_expirations = df[df['Days to Expiration'] <= 365].sort_values('Days to Expiration')
    
    for _, contract in future_expirations.iterrows():
        days = contract['Days to Expiration']
        expiry_date = contract['Expiration'].strftime('%B %Y')
        revenue_risk = contract['Monthly Revenue']
        
        if days <= 30:
            color = "🔴"
        elif days <= 90:
            color = "🟡"
        else:
            color = "🟢"
        
        st.markdown(f"{color} **{contract['Contract']}** expires {expiry_date} "
                   f"(${revenue_risk:,}/month at risk)")

if __name__ == "__main__":
    main()