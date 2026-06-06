from sqlalchemy import create_engine

def load(df_valid, df_rejected, df_run, db_path):

    engine = create_engine(f"sqlite:///{db_path}")

    df_valid.to_sql(
        "transactions", 
        engine, 
        if_exists="replace", 
        index=False)
    
    # INVALID data
    df_rejected.to_sql(
        "rejected_transactions",
        engine,
        if_exists="replace",
        index=False
    )

    df_run.to_sql(
        "etl_runs",
        engine,
        if_exists="append",
        index=False
    )