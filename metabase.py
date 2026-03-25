from sqlalchemy import create_engine
import pandas as pd

df = pd.read_csv("data_student_performance_metabase.csv", encoding='windows-1252')

URL = "postgresql://postgres:OuZFVuliJgWAYVw6@db.xkwqhneajehbsjjzikcn.supabase.co:5432/postgres"
 
engine = create_engine(URL)
df.to_sql('data_student_performance', engine)