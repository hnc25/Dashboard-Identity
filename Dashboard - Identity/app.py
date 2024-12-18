# Dashboard-Identity
import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Initialize the Dash app
app = dash.Dash(__name__)

# ----------------------------
# Data Preparation Function
# ----------------------------
def get_data(time_range):
    if time_range == "1 Month":
        return {
            "total_profiles": {"Total Profiles": 180000, "Matched csCoreID": 140000, "Matched csHHId": 120000, "Duplicate Records": "22%"},
            "channel_distribution": {
                "Address": [170000, 160000, 95], 
                "Email": [160000, 150000, 93], 
                "Phone": [150000, 135000, 89]
            },
            "coreid_reach": {"Total Profiles": 180000, "Matched CoreID": 120000, "Actual Reach": 108000}
        }
    elif time_range == "3 Months":
        return {
            "total_profiles": {"Total Profiles": 200000, "Matched csCoreID": 150000, "Matched csHHId": 130000, "Duplicate Records": "25%"},
            "channel_distribution": {
                "Address": [185000, 180000, 97], 
                "Email": [175000, 170000, 97], 
                "Phone": [165000, 150000, 91]
            },
            "coreid_reach": {"Total Profiles": 200000, "Matched CoreID": 130000, "Actual Reach": 117000}
        }
    else:  # 6 Months
        return {
            "total_profiles": {"Total Profiles": 220000, "Matched csCoreID": 160000, "Matched csHHId": 140000, "Duplicate Records": "28%"},
            "channel_distribution": {
                "Address": [195000, 190000, 98], 
                "Email": [185000, 180000, 97], 
                "Phone": [175000, 160000, 92]
            },
            "coreid_reach": {"Total Profiles": 220000, "Matched CoreID": 140000, "Actual Reach": 125000}
        }

# ----------------------------
# Layout
# ----------------------------
app.layout = html.Div([
    html.H1("Identity Reporting", style={"textAlign": "center", "marginBottom": "20px"}),

    html.Div([
        html.Label("Time Range:", style={"fontWeight": "bold", "textAlign": "center"}),
        dcc.Dropdown(
            id="time-range-dropdown",
            options=[
                {"label": "1 Month", "value": "1 Month"},
                {"label": "3 Months", "value": "3 Months"},
                {"label": "6 Months", "value": "6 Months"},
            ],
            value="3 Months",
            style={"width": "50%", "margin": "0 auto"}
        )
    ], style={"textAlign": "center", "marginBottom": "20px"}),

    html.Div(id="total-profiles-tiles", style={"display": "flex", "justifyContent": "space-around"}),

    dcc.Graph(id="total-vs-unique-identifiers-graph"),
    dcc.Graph(id="unique-channel-reach-graph"),

    html.Div([
        dcc.Graph(id="coreid-match-gauge", style={"width": "45%", "display": "inline-block"}),
        dcc.Graph(id="reach-rate-gauge", style={"width": "45%", "display": "inline-block"})
    ], style={"textAlign": "center"})
])

# ----------------------------
# Callbacks for Graph Updates
# ----------------------------
@app.callback(
    [
        Output("total-profiles-tiles", "children"),
        Output("total-vs-unique-identifiers-graph", "figure"),
        Output("unique-channel-reach-graph", "figure"),
        Output("coreid-match-gauge", "figure"),
        Output("reach-rate-gauge", "figure"),
    ],
    [Input("time-range-dropdown", "value")]
)
def update_dashboard(time_range):
    data = get_data(time_range)

    # Total Profiles Tiles
    total_profiles_tiles = [
        html.Div([
            html.H3(metric, style={"textAlign": "center"}),
            html.P(value, style={"textAlign": "center", "fontSize": "24px", "fontWeight": "bold"})
        ], style={"backgroundColor": "#f0f0f0", "padding": "20px", "margin": "10px", "borderRadius": "5px", "width": "20%"})
        for metric, value in data["total_profiles"].items()
    ]

    # Channel Distribution - Total vs Unique Identifiers
    channels = ["Address", "Email", "Phone"]
    totals = [data["channel_distribution"][c][0] for c in channels]
    unique_identifiers = [data["channel_distribution"][c][1] for c in channels]

    channel_data = pd.DataFrame({
        "Channel": channels * 2,
        "Count": totals + unique_identifiers,
        "Type": ["Total Identifiers"] * len(channels) + ["Unique Identifiers"] * len(channels)
    })

    total_vs_unique_fig = px.bar(
        channel_data, 
        x="Channel", 
        y="Count", 
        color="Type", 
        barmode="group", 
        text="Count",  # Add numbers on top of bars
        title="Total vs Unique Identifiers"
    )
    total_vs_unique_fig.update_traces(texttemplate='%{text:,}', textposition='outside')  # Format text
    total_vs_unique_fig.update_layout(legend_title_text="Legend")

    # Unique Channel Reach
    reach_percentages = [data["channel_distribution"][c][2] for c in channels]
    unique_channel_reach_fig = px.bar(
        x=channels, 
        y=reach_percentages, 
        text=[f"{p}%" for p in reach_percentages],  # Add percentage text
        labels={"x": "Channel", "y": "Reach (%)"},
        title="Unique Channel Reach"
    )
    unique_channel_reach_fig.update_traces(textposition='outside')

    # CoreID Match Gauge
    coreid_match_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=round(data["coreid_reach"]["Matched CoreID"] / data["coreid_reach"]["Total Profiles"] * 100),
        number={"suffix": "%"},  # Add % symbol
        title={"text": "CoreID Match Rate (%)"},
        gauge={"axis": {"range": [0, 100]}}
    ))

    # Reach Rate Gauge
    reach_rate_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=round(data["coreid_reach"]["Actual Reach"] / data["coreid_reach"]["Matched CoreID"] * 100),
        number={"suffix": "%"},  # Add % symbol
        title={"text": "Reach Rate (%)"},
        gauge={"axis": {"range": [0, 100]}}
    ))

    return total_profiles_tiles, total_vs_unique_fig, unique_channel_reach_fig, coreid_match_fig, reach_rate_fig

# ----------------------------
# Run the app
# ----------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
