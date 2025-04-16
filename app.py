import streamlit as st
import pandas as pd

# Set page layout to wide
st.set_page_config(layout="wide")

# Add arcade-themed font CSS globally
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    
    html, body, [class*="css"], .st-emotion-cache-13ln4jc h1, .st-emotion-cache-13ln4jc p, .st-emotion-cache-16txtl3 h1, .st-emotion-cache-16txtl3 p  {
        font-family: 'Press Start 2P', cursive !important;
    }

    table {
        font-family: 'Press Start 2P', cursive !important;
        width: 100% !important;
        margin: 0 auto !important;
    }

    /* Button styling */
    .stButton>button {
        background-color: #0F9D58 !important;
        border: none !important;
        color: white !important;
        padding: 12px 20px !important;
        font-size: 12px !important;
        cursor: pointer !important;
        font-family: 'Press Start 2P', cursive !important;
        width: 160px !important;
    }

    .stButton>button:hover {
        background-color: #DB4437 !important;
    }
    
    /* Disabled button styling */
    .stButton>button:disabled {
        background-color: #cccccc !important;
        cursor: not-allowed !important;
        opacity: 0.6;
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
    }
    
    /* Add padding at the bottom of the page for the fixed navigation */
    .main-content {
        padding-bottom: 80px;
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
    }
    
    .stTextInput input {
        font-family: 'Press Start 2P', cursive !important;
        font-size: 0.8rem !important;
        padding: 10px !important;
        border: 2px solid #4285F4 !important;
        border-radius: 0px !important;
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
        justify-content: center;
        gap: 20px;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def google_colors_style(df):
    colors = ['#4285F4', '#DB4437', '#F4B400', '#0F9D58']
    def color_text(val, idx):
        return f'color: {colors[idx % len(colors)]}'
    styled = df.style.apply(lambda x: [color_text(v, i) for i, v in enumerate(x)], axis=1)
    return styled

def main():
    # Wrap everything in a main content div
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    # Centered arcade-style heading
    st.markdown(
        """
        <h1 style="
            text-align: center;
            background: -webkit-linear-gradient(45deg, #DB4437, #4285F4, #F4B400, #0F9D58);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
            font-family: 'Press Start 2P', cursive;
        ">
        Google Arcade Program 2025 Cohort 1 - Leaderboard
        </h1>
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
<<<<<<< HEAD
    csv_path = "Google-Arcade-Leaderboard\progress_report\GCAF25C1-IN-T3K-Y7E [16 Apr].csv"
    df = pd.read_csv(csv_path)

    # Select & rename columns
    df_display = pd.DataFrame()
    df_display["User Name"] = df["User Name"]
    df_display["Skill Badges Completed"] = df["# of Skill Badges Completed"]
    df_display["Arcade Games Completed"] = df["# of Arcade Games Completed"]
    df_display["Trivia Games Completed"] = df["# of Trivia Games Completed"]
    df_display["Lab Free Courses Completed"] = df["# of Lab-free Courses Completed"]

    # Calculate Points
    df_display["Points"] = (
        df_display["Arcade Games Completed"] +
        df_display["Trivia Games Completed"] +
        (df_display["Skill Badges Completed"] // 2)
    )

    # Sort by points
    df_sorted = df_display.sort_values(by="Points", ascending=False).reset_index(drop=True)
    
    # Add search functionality
    st.markdown('<div class="search-container">', unsafe_allow_html=True)
    
    # Centered search input
    search_query = st.text_input("Search by username:", key="search_input")
    
    # Centered buttons on next line
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        search_button_col, reset_button_col = st.columns(2)
        
        with search_button_col:
            if st.button("Search", key="search_button"):
                if search_query:
                    # Case-insensitive search in User Name column
                    search_results = df_sorted[df_sorted["User Name"].str.lower().str.contains(search_query.lower())]
                    if not search_results.empty:
                        st.session_state.search_results = search_results
                        st.session_state.search_active = True
                    else:
                        st.error("No users found matching that username.")
                        st.session_state.search_active = False
                else:
                    st.session_state.search_active = False
        
        with reset_button_col:
            if st.button("Reset", key="reset_button"):
                st.session_state.search_active = False
                st.session_state.search_results = None
        
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
        st.write(styled_search.to_html(), unsafe_allow_html=True)
        
        # Show search result count
        st.markdown(f'<p style="text-align: center; font-family: \'Press Start 2P\', cursive; font-size: 0.8rem;">Found {len(search_df)} results</p>', unsafe_allow_html=True)
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
        
        # Add the navigation buttons
        with button_container:
            col1, col2, col3 = st.columns([4, 2, 4])
            
            with col2:
                col_left, col_right = st.columns(2)
                
                # Previous button
                with col_left:
                    if st.button("⬅️ Prev", key="prev", disabled=is_first_page):
                        st.session_state.page_number -= 1
                        st.rerun()
                
                # Next button
                with col_right:
                    if st.button("Next ➡️", key="next", disabled=is_last_page):
                        st.session_state.page_number += 1
                        st.rerun()

if __name__ == "__main__":
    main()
