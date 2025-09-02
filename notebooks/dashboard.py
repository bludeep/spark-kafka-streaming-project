import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from datetime import datetime
import time

# Настройка страницы
st.set_page_config(page_title="Real Estate Dashboard", page_icon="🏠", layout="wide")

# Заголовок
st.title("🏠 Real Estate Analytics")
st.markdown("Аналитика недвижимости Португалии")

@st.cache_resource
def get_database_connection():
    try:
        return create_engine('postgresql://spark_user:spark_password@postgresql:5432/realestate')
    except Exception as e:
        st.error(f"Ошибка подключения: {e}")
        return None

def load_data(_engine):
    try:
        query = """
        SELECT district, property_type, avg_price, total_ads, avg_price_per_sqm
        FROM real_estate_analytics
        ORDER BY district
        """
        return pd.read_sql(query, _engine)
    except Exception as e:
        st.error(f"Ошибка загрузки: {e}")
        return pd.DataFrame()

# Подключение и загрузка данных
engine = get_database_connection()
if engine is None:
    st.stop()

df = load_data(engine)
if df.empty:
    st.warning("⚠️ Данные отсутствуют. Запустите kafka-producer.ipynb.")
    st.stop()

# Время обновления
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.metric("🕒 Обновлено", datetime.now().strftime("%H:%M:%S"))
with col2:
    st.metric("📊 Записей", len(df))

# Фильтр по району
st.sidebar.header("Фильтр")
districts = ['Все'] + sorted(df['district'].unique().tolist())
selected_district = st.sidebar.selectbox("Район", districts)

# Фильтрация данных
filtered_df = df if selected_district == 'Все' else df[df['district'] == selected_district]

# Метрики
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Районов", df['district'].nunique())
with col2:
    st.metric("Объявлений", f"{filtered_df['total_ads'].sum():,}")
with col3:
    st.metric("Средняя цена", f"{filtered_df['avg_price'].mean():,.0f} €" if not filtered_df['avg_price'].isna().all() else "N/A")

# Графики
st.markdown("---")
st.subheader("📈 Визуализации")

# Топ-5 районов по цене
top_districts = filtered_df.groupby('district')['avg_price'].mean().sort_values(ascending=False).head(5)
fig1 = px.bar(x=top_districts.values, y=top_districts.index, orientation='h',
              title="Топ-5 районов по цене", labels={'x': 'Цена (€)', 'y': 'Район'})
st.plotly_chart(fig1, width='stretch')

# Объявления по типам недвижимости
type_counts = filtered_df.groupby('property_type')['total_ads'].sum().sort_values(ascending=False)
if not type_counts.empty:
    fig2 = px.pie(
        values=type_counts.values,
        names=type_counts.index,
        title="Объявления по типам недвижимости",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig2.update_traces(
        textinfo='percent+label',
        textfont_size=14,
        pull=[0.1] * len(type_counts),  # Отступ секторов
        marker=dict(line=dict(color='#FFFFFF', width=2))  # Белые границы
    )
    fig2.update_layout(
        height=500,
        margin=dict(t=50, b=50, l=50, r=50),
        showlegend=True
    )
    st.plotly_chart(fig2, width='stretch')
else:
    st.warning("Нет данных для отображения графика по типам недвижимости.")

# Таблица
st.markdown("---")
st.subheader("📋 Данные")
st.dataframe(
    filtered_df[['district', 'property_type', 'avg_price', 'total_ads', 'avg_price_per_sqm']],
    width='stretch',
    column_config={
        'district': 'Район',
        'property_type': 'Тип недвижимости',
        'avg_price': st.column_config.NumberColumn('Цена (€)', format='%.0f'),
        'total_ads': 'Объявлений',
        'avg_price_per_sqm': st.column_config.NumberColumn('Цена за м² (€)', format='%.0f')
    }
)

# Автообновление
time.sleep(15)
st.rerun()