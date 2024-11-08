import streamlit as st

# Custom CSS and HTML for styling
st.markdown(
    """
    <style>
    /* Background and container styling */
    .stApp {
        background-color: #00000;
        color: #333333;
    }
    .main-container {
        padding: 20px;
        background-color: #00000;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        color: white;
    }

    /* Title styling */
    h1 {
        font-family: Arial, sans-serif;
        color: #ff6f61;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }

    /* Input and select box styling */
    .stNumberInput, .stSelectbox, .stTextInput {
        background-color: #00000;
        color: #004d40;
        font-size: 16px;
    }

    /* Result text styling */
    .result-text {
        font-size: 24px;
        font-weight: bold;
        color: #1976d2;
        margin-top: 20px;
    }
    </style>
    <div class="main-container">
    """,
    unsafe_allow_html=True
)

# Title of the app
st.title("MINION Make Me Crazy")

def main():
    # User input
    minion_max = st.number_input("Enter max number of minions (5-26)", min_value=5, max_value=26, step=1)
    minion_have = st.number_input("Enter number of minions you have", min_value=1, step=1)
    player_need = st.selectbox("Choose what you need", ["Item", "Block", "Enchanted Item", "Enchanted Block"]).lower()

    tier_dict = {'1': 1, '2': 3, '3': 3, '4': 6, '5': 6, '6': 9, '7': 9, '8': 12, '9': 12, '10': 15, '11': 15}
    size_dict = {'s': 3, 'm': 9, 'l': 15, 'none': 0}
    total_items = 0

    def minions_found(new_minion):
        try:
            tier, size, is_compact = new_minion.split(' ')
            if tier not in tier_dict or size not in size_dict:
                return 0

            compact_decoded = 9 if is_compact == "yes" else 1 if is_compact == "no" else 0
            all_item = (tier_dict[tier] + size_dict[size]) * 64 * compact_decoded
            return all_item
        except ValueError:
            return 0

    # Input minion details
    minion_details = []
    for i in range(min(minion_have, minion_max)):
        new_minion = st.text_input(f"Enter details for minion {i + 1} (format: tier size compact EX. 1 S Yes)", "")
        if new_minion:
            items_found = minions_found(new_minion.lower())
            total_items += items_found

    # Calculate output based on player need
    if player_need == "item":
        output = total_items
        st.markdown(f"<p class='result-text'>Item: {output}</p>", unsafe_allow_html=True)
    elif player_need == "block":
        output = total_items // 9
        st.markdown(f"<p class='result-text'>Block: {output}</p>", unsafe_allow_html=True)
    elif player_need == "enchanted item":
        output = total_items // 160
        st.markdown(f"<p class='result-text'>Enchanted Item: {output}</p>", unsafe_allow_html=True)
    elif player_need == "enchanted block":
        output = total_items // (160 ** 2)
        st.markdown(f"<p class='result-text'>Enchanted Block: {output}</p>", unsafe_allow_html=True)

# Run the app
main()

# Close the HTML container
st.markdown("</div>", unsafe_allow_html=True)
