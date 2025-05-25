
import streamlit as st
import math

# --- Configuration and Unit Definitions ---

# Define unit categories, their base units, and all units within each category.
# The base unit for each category is chosen for internal calculation consistency.
UNIT_CATEGORIES = {
    "Length": {
        "base_unit": "meter",
        "units": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"]
    },
    "Mass": {
        "base_unit": "gram",
        "units": ["gram", "kilogram", "milligram", "pound", "ounce"]
    },
    "Temperature": {
        "base_unit": "celsius", # Special handling for temperature as it's non-linear
        "units": ["celsius", "fahrenheit", "kelvin"]
    },
    "Volume": {
        "base_unit": "liter",
        "units": ["liter", "milliliter", "cubic meter", "cubic centimeter", "gallon (US)", "quart (US)", "pint (US)"]
    },
    "Digital Storage": {
        "base_unit": "byte",
        "units": ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte"]
    },
    "Time": {
        "base_unit": "second",
        "units": ["second", "minute", "hour", "day", "week"]
    },
    "Speed": {
        "base_unit": "meter/second",
        "units": ["meter/second", "kilometer/hour", "mile/hour", "knot"]
    }
}

# Define conversion factors to convert each unit TO ITS BASE UNIT within its category.
# For example, to convert 1 kilometer to meters (base unit for Length), multiply by 1000.
CONVERSION_FACTORS = {
    "Length": {
        "meter": 1.0,
        "kilometer": 1000.0,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254
    },
    "Mass": {
        "gram": 1.0,
        "kilogram": 1000.0,
        "milligram": 0.001,
        "pound": 453.592,
        "ounce": 28.3495
    },
    # Temperature is handled by a separate function due to non-linear conversions
    "Volume": {
        "liter": 1.0,
        "milliliter": 0.001,
        "cubic meter": 1000.0,
        "cubic centimeter": 0.001,
        "gallon (US)": 3.78541,
        "quart (US)": 0.946353,
        "pint (US)": 0.473176
    },
    "Digital Storage": {
        "bit": 1/8, # Convert bit to byte (base unit)
        "byte": 1.0,
        "kilobyte": 1024.0, # Using 1024 for digital storage (binary)
        "megabyte": 1024.0 ** 2,
        "gigabyte": 1024.0 ** 3,
        "terabyte": 1024.0 ** 4
    },
    "Time": {
        "second": 1.0,
        "minute": 60.0,
        "hour": 3600.0,
        "day": 86400.0,
        "week": 604800.0
    },
    "Speed": {
        "meter/second": 1.0,
        "kilometer/hour": 1000 / 3600, # km to m, hour to second
        "mile/hour": 1609.34 / 3600, # miles to m, hour to second
        "knot": 1852 / 3600 # nautical miles to m, hour to second
    }
}

# --- Conversion Functions ---

def convert_temperature(value, unit_from, unit_to):
    """Handles non-linear temperature conversions."""
    if unit_from == unit_to:
        return value

    # Convert to Celsius first
    if unit_from == "celsius":
        celsius_val = value
    elif unit_from == "fahrenheit":
        celsius_val = (value - 32) * 5/9
    elif unit_from == "kelvin":
        celsius_val = value - 273.15
    else:
        return "Error: Invalid temperature unit."

    # Convert from Celsius to target unit
    if unit_to == "celsius":
        return celsius_val
    elif unit_to == "fahrenheit":
        return (celsius_val * 9/5) + 32
    elif unit_to == "kelvin":
        return celsius_val + 273.15
    else:
        return "Error: Invalid temperature unit."

def convert_units(value, unit_from, unit_to, category):
    """
    Converts a value from one unit to another using a base unit approach.
    Handles linear conversions and delegates temperature to a special function.
    """
    if unit_from == unit_to:
        return value

    if category == "Temperature":
        return convert_temperature(value, unit_from, unit_to)

    # For other linear categories:
    if category not in CONVERSION_FACTORS:
        return "Error: Unknown category."

    factors = CONVERSION_FACTORS[category]

    if unit_from not in factors or unit_to not in factors:
        return "Error: One or both units not found in the selected category."

    # Convert 'value' from 'unit_from' to the base unit
    value_in_base_unit = value * factors[unit_from]

    # Convert 'value_in_base_unit' from base unit to 'unit_to'
    converted_value = value_in_base_unit / factors[unit_to]

    return converted_value

# --- Streamlit UI ---

st.set_page_config(layout="centered", page_title="Universal Unit Converter")

st.title("🌍 Universal Unit Converter by Muhammad Qasim")
st.markdown("Convert values across various categories with ease!")

# Initialize session state for conversion history
if 'history' not in st.session_state:
    st.session_state.history = []

# --- Input Section ---
st.header("Input Values")

col1, col2 = st.columns(2)

with col1:
    selected_category = st.selectbox(
        "Select Unit Category",
        list(UNIT_CATEGORIES.keys()),
        help="Choose the type of units you want to convert (e.g., Length, Mass)."
    )

# Get available units for the selected category
available_units = UNIT_CATEGORIES[selected_category]["units"]

with col2:
    value = st.number_input(
        "Enter Value",
        value=0.0,
        format="%.6f", # Allow for more precision
        help="The numerical value you want to convert."
    )

col3, col4 = st.columns(2)

with col3:
    unit_from = st.selectbox(
        "Convert From",
        available_units,
        help="The unit you are converting from."
    )

with col4:
    unit_to = st.selectbox(
        "Convert To",
        available_units,
        help="The unit you want to convert to."
    )

# --- Real-time Conversion and Display ---
st.subheader("Result")

# Perform conversion instantly as inputs change
if value is not None:
    result = convert_units(value, unit_from, unit_to, selected_category)

    if isinstance(result, (int, float)):
        st.success(f"**{value} {unit_from}** is equal to **{result:.6f} {unit_to}**")
        display_result = f"{result:.6f}" # For copying, ensure consistent formatting
    else:
        st.error(result) # Display error message from conversion function
        display_result = "" # No result to copy

    # Add copy to clipboard button
    if isinstance(result, (int, float)):
        # Using st.components.v1.html for clipboard functionality
        # This is a workaround as navigator.clipboard.writeText is restricted in iframes
        st.components.v1.html(
            f"""
            <button
                onclick="navigator.clipboard.writeText('{display_result}');
                         alert('Copied to clipboard!');"
                style="
                    background-color: #4CAF50; /* Green */
                    border: none;
                    color: white;
                    padding: 10px 20px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    margin: 4px 2px;
                    cursor: pointer;
                    border-radius: 8px;
                    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
                    transition: 0.3s;
                "
            >
                Copy Result
            </button>
            """,
            height=50
        )

    # Add conversion to history
    if isinstance(result, (int, float)):
        conversion_string = f"{value:.6f} {unit_from} = {result:.6f} {unit_to} ({selected_category})"
        if conversion_string not in st.session_state.history: # Avoid duplicates if inputs don't change
            st.session_state.history.insert(0, conversion_string) # Add to the beginning

# --- Conversion History ---
st.header("Conversion History")

if st.session_state.history:
    # Display history in an expander for cleanliness
    with st.expander("View Recent Conversions"):
        for i, conv in enumerate(st.session_state.history):
            st.write(f"{i+1}. {conv}")

    # Clear history button
    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun() # Rerun to clear the displayed history
else:
    st.info("No conversions yet. Start converting!")

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
