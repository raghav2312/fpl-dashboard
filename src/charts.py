import plotly.express as px


def create_rank_chart(df):
    fig = px.line(
        df, 
        x="gameweek", 
        y="overall_rank", 
        markers=True,
        title="Overall Rank by Gameweek",  
    )
    fig.update_yaxes(autorange="reversed")
    return fig


def create_points_chart(df):
    fig = px.bar(
        df,
        x="gameweek",
        y="gw_points",
        title="Points by gameweek"
    )
    return fig

def create_rank_change_chart(df):
    fig = px.bar(
        df,
        x="gameweek",
        y="rank_change",
        title="Rank movement by Gameweek"
    )
    return fig

def create_bench_points_chart(df):
    fig = px.bar(
        df,
        x="gameweek",
        y="bench_points",
        title="Bench Points Lost by Gameweek"
    )
    return fig