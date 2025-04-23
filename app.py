import streamlit as st
import pandas as pd

date = "April 23, 2025"
file_date = "23 Apr"
# Set page layout to wide
st.set_page_config(layout="wide")

# Add arcade-themed font CSS globally 
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    html, body, [class*="css"], .st-emotion-cache-13ln4jc h1, .st-emotion-cache-13ln4jc p, .st-emotion-cache-16txtl3 h1, .st-emotion-cache-16txtl3 p {
    font-family: 'Press Start 2P', cursive !important;
    }
    /* Improve table readability */
    table {
    font-family: 'Press Start 2P', cursive !important;
    width: 100% !important;
    margin: 0 auto !important;
    border-collapse: collapse !important;
    font-size: 0.7rem !important;
    line-height: 1.5 !important;
    }
    table td, table th {
    padding: 12px 8px !important;
    border-bottom: 2px solid #333 !important;
    }
    /* Keep the alternating row colors */
    table tr:nth-child(even) {
    background-color: rgba(255, 255, 255, 0.05) !important;
    }
    table tr:nth-child(odd) {
    background-color: rgba(0, 0, 0, 0.2) !important;
    }
    table tr:hover {
    background-color: rgba(66, 133, 244, 0.1) !important;
    }
    /* Button styling */
    .stButton>button {
    display: inline-flex !important;
    align-items: center;
    justify-content: center;
    background-color: #0F9D58 !important;
    border: 3px solid #0a7a45 !important;
    color: white !important;
    padding: 12px 20px !important;
    font-size: 12px !important;
    cursor: pointer !important;
    font-family: 'Press Start 2P', cursive !important;
    width: 160px !important;
    text-shadow: 2px 2px 0px #085e34 !important;
    box-shadow: 3px 3px 0px #333 !important;
    transition: all 0.1s !important;
    margin: 0 auto !important;
    }
    .stButton>button:hover {
    background-color: #DB4437 !important;
    border-color: #b53629 !important;
    transform: translateY(-2px) !important;
    text-shadow: 2px 2px 0px #9c2e23 !important;
    }
    .stButton>button:active {
    transform: translateY(1px) !important;
    box-shadow: 1px 1px 0px #333 !important;
    }
    /* Disabled button styling */
    .stButton>button:disabled {
    background-color: #666666 !important;
    border-color: #444444 !important;
    cursor: not-allowed !important;
    opacity: 0.6;
    text-shadow: none !important;
    box-shadow: none !important;
    }
    /* Fixed bottom navigation bar */
    .bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #121212;
    padding: 15px 0;
    z-index: 999;
    border-top: 2px solid #4285F4;
    box-shadow: 0px -5px 15px rgba(0, 0, 0, 0.5);
    }
    /* Add padding at the bottom of the page for the fixed navigation */
    .main-content {
    padding-bottom: 120px;
    }
    /* Center content in the bottom nav */
    .bottom-container {
    max-width: 1200px;
    margin: 0 auto;
    text-align: center;
    }
    /* Credits style */
    .credits {
    text-align: center;
    margin-top: 20px;
    font-family: 'Press Start 2P', cursive;
    font-size: 0.7rem;
    color: #4285F4;
    }
    /* Search box styling */
    .search-container {
    margin: 20px auto;
    max-width: 600px;
    text-align: center;
    position: relative;
    }
    .stTextInput input {
    font-family: 'Press Start 2P', cursive !important;
    font-size: 0.8rem !important;
    padding: 10px !important;
    border: 3px solid #4285F4 !important;
    border-radius: 0px !important;
    background-color: rgba(0, 0, 0, 0.7) !important;
    color: #F4B400 !important;
    box-shadow: 3px 3px 0px #1a53a1 !important;
    }
    .stTextInput input:focus {
    border-color: #DB4437 !important;
    box-shadow: 0 0 5px rgba(219, 68, 55, 0.5) !important;
    }
    /* Search label styling */
    .stTextInput label {
    font-family: 'Press Start 2P', cursive !important;
    font-size: 0.8rem !important;
    color: #4285F4 !important;
    }
    /* Make text errors use the arcade font */
    .st-emotion-cache-1wbqh8, .stAlert, .st-emotion-cache-jyd8rn {
    font-family: 'Press Start 2P', cursive !important;
    font-size: 0.7rem !important;
    }
    /* Style for the buttons container */
    .button-container {
    display: flex;
    justify-content: space-around;
    align-items: center;
    gap: 20px;
    margin-top: 15px;
    width: 100%;
    }
    /* Center the buttons within columns */
    .stButton {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    width: 100% !important;
    }
    /* Force center alignment for column containers */
    [data-testid="column"] {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    }
    /* Top 3 Winners Podium - Fixed layout */
    .top-winners {
    display: flex;
    justify-content: center;
    align-items: flex-end;
    margin: 50px auto 70px auto;
    height: 280px;
    font-family: 'Press Start 2P', cursive !important;
    }
    .podium-step {
    width: 120px;
    text-align: center;
    margin: 0 10px;
    }
    .step-1 {
    height: 180px;
    background-color: #F4B400;
    border: 4px solid #ffd54f;
    position: relative;
    }
    .step-2 {
    height: 140px;
    background-color: #4285F4;
    border: 4px solid #7baaf7;
    position: relative;
    }
    .step-3 {
    height: 100px;
    background-color: #DB4437;
    border: 4px solid #f28b82;
    position: relative;
    }
    .rank-number {
    font-size: 28px;
    margin-top: -50px;
    font-family: 'Press Start 2P', cursive !important;
    color: white;
    text-shadow: 2px 2px 0px #000;
    }
    .user-name {
    font-size: 12px;
    color: white;
    margin-top: 10px;
    padding: 0 5px;
    word-wrap: break-word;
    font-family: 'Press Start 2P', cursive !important;
    text-shadow: 1px 1px 0px #000;
    }
    .user-points {
    font-size: 16px;
    color: #F4B400;
    margin-top: 10px;
    font-family: 'Press Start 2P', cursive !important;
    text-shadow: 1px 1px 0px #000;
    }
    .crown {
    position: absolute;
    top: -40px;
    left: 45px;
    font-size: 36px;
    }
    /* Rank column styling */
    .rank-column {
    font-weight: bold;
    text-align: center;
    }
    /* Animations */
    @keyframes glow {
    0% { text-shadow: 0 0 5px #4285F4; }
    50% { text-shadow: 0 0 20px #4285F4, 0 0 30px #4285F4; }
    100% { text-shadow: 0 0 5px #4285F4; }
    }
    .glow-text {
    animation: glow 2s infinite;
    }
    /* Responsive adjustments */
    @media (max-width: 768px) {
    table {
    font-size: 0.6rem !important;
    }
    .stButton>button {
    width: 120px !important;
    font-size: 10px !important;
    padding: 8px 12px !important;
    }
    .top-winners {
    height: 200px;
    }
    .podium-step {
    width: 80px;
    }
    .step-1 {
    height: 120px;
    }
    .step-2 {
    height: 90px;
    }
    .step-3 {
    height: 60px;
    }
    .rank-number {
    font-size: 18px;
    margin-top: -35px;
    }
    .user-name {
    font-size: 8px;
    }
    .user-points {
    font-size: 10px;
    }
    .crown {
    font-size: 24px;
    top: -30px;
    left: 30px;
    }
    }
    /* Points highlight */
    .points-highlight {
    font-weight: bold;
    color: #F4B400 !important;
    text-shadow: 1px 1px 0px #333;
    }
    /* Add a blinking cursor effect to title */
    @keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
    }
    .cursor {
    display: inline-block;
    width: 10px;
    height: 24px;
    background-color: #F4B400;
    margin-left: 8px;
    animation: blink 1s step-start infinite;
    }
    /* Special fixed header for the arcade name */
    .arcade-header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: rgba(18, 18, 18, 0.8);
    border-bottom: 2px solid #4285F4;
    z-index: 999;
    text-align: center;
    padding: 5px;
    backdrop-filter: blur(5px);
    }
    .arcade-header-text {
    color: #F4B400;
    font-family: 'Press Start 2P', cursive;
    font-size: 0.7rem;
    animation: glow 2s infinite;
    }
    /* Add margin to top to account for fixed header */
    .main-content {
    margin-top: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add fixed header for arcade name
st.markdown("""
<div class="arcade-header">
    <span class="arcade-header-text">
    HIGH SCORES - GOOGLE ARCADE 2025
    </span>
</div>
""", unsafe_allow_html=True)

def google_colors_style(df):
    colors = ['#4285F4', '#DB4437', '#F4B400', '#0F9D58']
    
    def color_text(val, idx):
        return f'color: {colors[idx % len(colors)]}'
    
    styled = df.style.apply(lambda x: [color_text(v, i) for i, v in enumerate(x)], axis=1)
    return styled

def main():
    # Wrap everything in a main content div
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    # Centered arcade-style heading with blinking cursor
    st.markdown(
        """
        <h1 style="
        text-align: center;
        background: -webkit-linear-gradient(45deg, #DB4437, #4285F4, #F4B400, #0F9D58);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-family: 'Press Start 2P', cursive;
        margin-bottom: 10px;
        ">
        Google Arcade Program 2025<span class="cursor"></span>
        </h1>
        <div style="
        text-align: center;
        color: #F4B400;
        font-size: 1rem;
        margin-bottom: 20px;
        font-family: 'Press Start 2P', cursive;
        ">
        Cohort 1 - Leaderboard
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Initialize session state for pagination
    if "page_number" not in st.session_state:
        st.session_state.page_number = 0
    if "search_active" not in st.session_state:
        st.session_state.search_active = False
    if "search_results" not in st.session_state:
        st.session_state.search_results = None
    
    # Load CSV and process data
    csv_path = f"./progress_report/GCAF25C1-IN-T3K-Y7E [{file_date}].csv"
    df = pd.read_csv(csv_path)
    
    # Select & rename columns
    df_display = pd.DataFrame()
    df_display["User Name"] = df["User Name"]
    df_display["Skill Badges"] = df["# of Skill Badges Completed"]
    df_display["Arcade Games"] = df["# of Arcade Games Completed"]
    df_display["Trivia Games"] = df["# of Trivia Games Completed"]
    df_display["Lab-free Courses"] = df["# of Lab-free Courses Completed"]
    
    # Calculate Points
    df_display["Points"] = (
        df_display["Arcade Games"] +
        df_display["Trivia Games"] +
        (df_display["Skill Badges"] // 2)
    )
    
    # Sort by points
    df_sorted = df_display.sort_values(by="Points", ascending=False).reset_index(drop=True)
    
    # Get top 3 winners for podium
    top_winners = df_sorted.iloc[:3].copy() if len(df_sorted) >= 3 else df_sorted.copy()
    
    # Only create podium if we have data and not in search mode
    if not df_sorted.empty and not st.session_state.search_active:
        # Create fixed podium with clear layout
        st.markdown("""
        <div class="top-winners">
        <!-- 2nd Place -->
        <div class="podium-step step-2">
        <div class="rank-number">2</div>
        <div class="user-name">{}</div>
        <div class="user-points">{} PTS</div>
        </div>
        <!-- 1st Place -->
        <div class="podium-step step-1">
        <div class="crown">👑</div>
        <div class="rank-number">1</div>
        <div class="user-name">{}</div>
        <div class="user-points">{} PTS</div>
        </div>
        <!-- 3rd Place -->
        <div class="podium-step step-3">
        <div class="rank-number">3</div>
        <div class="user-name">{}</div>
        <div class="user-points">{} PTS</div>
        </div>
        </div>
        """.format(
            top_winners.iloc[1]["User Name"] if len(top_winners) > 1 else "N/A",
            int(top_winners.iloc[1]["Points"]) if len(top_winners) > 1 else 0,
            top_winners.iloc[0]["User Name"] if not top_winners.empty else "N/A",
            int(top_winners.iloc[0]["Points"]) if not top_winners.empty else 0,
            top_winners.iloc[2]["User Name"] if len(top_winners) > 2 else "N/A",
            int(top_winners.iloc[2]["Points"]) if len(top_winners) > 2 else 0
        ), unsafe_allow_html=True)
    
    def handle_search():
        if st.session_state.search_input:
            # Case-insensitive search in User Name column
            search_results = df_sorted[df_sorted["User Name"].str.lower().str.contains(st.session_state.search_input.lower())]
            
            if not search_results.empty:
                st.session_state.search_results = search_results
                st.session_state.search_active = True
            else:
                st.error("PLAYER NOT FOUND! TRY AGAIN.")
                st.session_state.search_active = False
        else:
            st.session_state.search_active = False
    

    
    # Add search functionality with improved UI
    st.markdown('<div class="search-container">', unsafe_allow_html=True)
    
    # Centered search input with a more arcade-style look
    search_query = st.text_input("👾 SEARCH PLAYER:", key="search_input",
                                help="Enter a username to find specific players", placeholder="Press 🔍 SEARCH or hit ENTER to find a player...", on_change=handle_search)
    
    # IMPROVED BUTTON LAYOUT: Center-aligned using custom markup
    st.markdown('<div style="display: flex; justify-content: center; width: 100%;">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Use custom HTML for proper centering of button containers
        st.markdown('<div style="display: flex; justify-content: space-around; width: 100%;">', unsafe_allow_html=True)
        button_cols = st.columns(2)
        
        with button_cols[0]:
            if st.button("🔍 SEARCH", key="search_button"):
                if search_query:
                    # Case-insensitive search in User Name column
                    search_results = df_sorted[df_sorted["User Name"].str.lower().str.contains(search_query.lower())]
                    
                    if not search_results.empty:
                        st.session_state.search_results = search_results
                        st.session_state.search_active = True
                    else:
                        st.error("PLAYER NOT FOUND! TRY AGAIN.")
                        st.session_state.search_active = False
                else:
                    st.session_state.search_active = False
                    
        with button_cols[1]:
            if st.button("🔄 RESET", key="reset_button"):
                st.session_state.search_active = False
                st.session_state.search_results = None
        
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Determine what to display: search results or paginated data
    if st.session_state.search_active and st.session_state.search_results is not None:
        # Display search results
        search_df = st.session_state.search_results.copy()
        
        # Add Rank column based on the original sorted dataframe
        search_df["Original Rank"] = search_df.index + 1
        search_df = search_df.reset_index(drop=True)
        search_df.insert(0, "Rank", search_df["Original Rank"])
        search_df.drop("Original Rank", axis=1, inplace=True)
        search_df.set_index("Rank", inplace=True)
        
        # Style and display search results
        styled_search = google_colors_style(search_df)
        st.markdown(f'<div style="text-align: left; font-family: \'Press Start 2P\', cursive; font-size: 1rem; color: #DB4437; margin-bottom: 10px;">Last Updated: {date}</div>', unsafe_allow_html=True)
        st.write(styled_search.to_html(), unsafe_allow_html=True)
        
        # Show search result count
        st.markdown(f'<p style="text-align: center; font-family: \'Press Start 2P\', cursive; font-size: 0.8rem; margin-top: 15px;">Found {len(search_df)} player(s)</p>', unsafe_allow_html=True)
    else:
        # Regular pagination logic
        page_size = 50
        total_records = len(df_sorted)
        total_pages = (total_records + page_size - 1) // page_size
        
        # Check page boundaries to prevent going outside valid range
        if st.session_state.page_number < 0:
            st.session_state.page_number = 0
        if st.session_state.page_number >= total_pages:
            st.session_state.page_number = total_pages - 1
            
        start_idx = st.session_state.page_number * page_size
        end_idx = start_idx + page_size
        page_df = df_sorted.iloc[start_idx:end_idx].copy()
        
        # Rank
        page_df.insert(0, "Rank", range(start_idx + 1, min(end_idx, total_records) + 1))
        page_df.set_index("Rank", inplace=True)
        
        # Style table
        styled_table = google_colors_style(page_df)
        # Display last updated date
        st.markdown(f'<div style="text-align: left; font-family: \'Press Start 2P\', cursive; font-size: 1rem; color: #DB4437; margin-bottom: 10px;">Last Updated:{date}</div>', unsafe_allow_html=True)
        st.write(styled_table.to_html(), unsafe_allow_html=True)
    
    # Close main content div
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Bottom navigation elements only show when not in search mode
    if not st.session_state.search_active:
        # Check if we're on the first page or last page
        is_first_page = st.session_state.page_number == 0
        is_last_page = st.session_state.page_number == total_pages - 1
        
        # Add fixed bottom navigation bar with page info and credits
        st.markdown(f"""
        <div class="bottom-nav">
        <div class="bottom-container">
        <div style="
        color: #FFFFFF;
        font-size: 0.8rem;
        margin-bottom: 10px;
        font-family: 'Press Start 2P', cursive;
        ">
        Page {st.session_state.page_number + 1} of {total_pages}
        </div>
        <div style="
        color: #F4B400;
        font-size: 0.6rem;
        font-family: 'Press Start 2P', cursive;
        margin-top: 5px;
        ">
        Made with ❤️ by Phalak and Paakhi
        </div>
        </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Create buttons in container that will appear above the fixed navigation
        # (buttons need to be in Streamlit layout, not in custom HTML)
        button_container = st.container()
        
        # Create a small placeholder to push the button container to bottom
        st.markdown('<div style="height: 50vh;"></div>', unsafe_allow_html=True)
        
        # IMPROVED BUTTON LAYOUT: Center align pagination buttons
        with button_container:
            # Use a narrower middle column to bring buttons closer together
            col1, col2, col3 = st.columns([3, 4, 3])
            with col2:
                
                st.markdown('<div style="display: flex; justify-content: center; width: 100%;">', unsafe_allow_html=True)
                nav_cols = st.columns(2)
                
                # Previous button
                with nav_cols[0]:
                    if st.button("⬅️ PREV", key="prev", disabled=is_first_page):
                        st.session_state.page_number -= 1
                        st.rerun()
                
                # Next button
                with nav_cols[1]:
                    if st.button("NEXT ➡️", key="next", disabled=is_last_page):
                        st.session_state.page_number += 1
                        st.rerun()
                
                st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
