import plotly.io as pio  # Add this for saving graphs to HTML

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
        channel_data, x="Channel", y="Count", color="Type",
        barmode="group", text="Count", title="Total vs Unique Identifiers"
    )
    total_vs_unique_fig.update_traces(texttemplate='%{text:,}', textposition='outside')

    # Save graph to HTML
    pio.write_html(total_vs_unique_fig, "total_vs_unique_identifiers.html")

    # Unique Channel Reach
    reach_percentages = [data["channel_distribution"][c][2] for c in channels]
    unique_channel_reach_fig = px.bar(
        x=channels, y=reach_percentages,
        text=[f"{p}%" for p in reach_percentages],
        labels={"x": "Channel", "y": "Reach (%)"},
        title="Unique Channel Reach"
    )
    unique_channel_reach_fig.update_traces(textposition='outside')

    # Save graph to HTML
    pio.write_html(unique_channel_reach_fig, "unique_channel_reach.html")

    # CoreID Match Gauge
    coreid_match_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=round(data["coreid_reach"]["Matched CoreID"] / data["coreid_reach"]["Total Profiles"] * 100),
        number={"suffix": "%"},
        title={"text": "CoreID Match Rate (%)"},
        gauge={"axis": {"range": [0, 100]}}
    ))
    pio.write_html(coreid_match_fig, "coreid_match_rate.html")

    # Reach Rate Gauge
    reach_rate_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=round(data["coreid_reach"]["Actual Reach"] / data["coreid_reach"]["Matched CoreID"] * 100),
        number={"suffix": "%"},
        title={"text": "Reach Rate (%)"},
        gauge={"axis": {"range": [0, 100]}}
    ))
    pio.write_html(reach_rate_fig, "reach_rate.html")

    return total_profiles_tiles, total_vs_unique_fig, unique_channel_reach_fig, coreid_match_fig, reach_rate_fig
