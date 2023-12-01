import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baca data dari file CSV
df_day = pd.read_csv("day.csv", index_col="instant", parse_dates=["dteday"])
df_hour = pd.read_csv("hour.csv", index_col="instant", parse_dates=["dteday"])

# Judul Dashboard
st.title('Dashboard Data Analisis Peminjaman Sepeda')

# Sidebar
st.sidebar.subheader('Pilih Data Yang ingin Di Analisis')
analysis_choice = st.sidebar.radio("Pilih Analisis:", ('Dinamika Penyewaan Sepeda dan Cuaca', 'Tren Jumlah Sepeda Disewakan per Jam (Musiman dan Hari Kerja)',
                                                       'Distribusi Waktu Terakhir Peminjaman Sepeda (Harian)', 'Distribusi Frekuensi Peminjaman Sepeda (Harian)',
                                                      'Distribusi Jumlah Sepeda Disewakan per Jam'))
# Analisis Data
if analysis_choice == 'Dinamika Penyewaan Sepeda dan Cuaca' :
  st.subheader('Dinamika Penyewaan Sepeda dan Cuaca' )
  fig, ax = plt.subplots(figsize=(12, 6))
  sns.scatterplot(data=df_hour, x='temp', y='cnt', hue='weathersit', palette='coolwarm', size='windspeed', sizes=(20, 200), ax=ax)
  ax.set_title('Dinamika Penyewaan Sepeda dan Cuaca')
  ax.set_xlabel('Temperatur (Celsius)')
  ax.set_ylabel('Jumlah Sepeda Disewakan')
  ax.legend(title='Cuaca', loc='upper right', labels=['Cerah', 'Berawan', 'Hujan/Salju'])
  st.pyplot(fig)

elif analysis_choice == 'Tren Jumlah Sepeda Disewakan per Jam (Musiman dan Hari Kerja)' :
  st.subheader ('Tren Jumlah Sepeda Disewakan per Jam (Musiman dan Hari Kerja)')
  fig, ax = plt.subplots(figsize=(12, 6))
  sns.lineplot(data=df_hour, x=df_hour.index, y='cnt', hue='season', style='workingday', markers=True, dashes=False, palette='Set2')
  plt.title('Tren Jumlah Sepeda Disewakan per Jam (Musiman dan Hari Kerja)')
  plt.xlabel('Jam (hr)')
  plt.ylabel('Jumlah Sepeda Disewakan')
  plt.legend(title='Musim', loc='upper right', labels=['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
  st.pyplot(fig)

elif analysis_choice == 'Distribusi Waktu Terakhir Peminjaman Sepeda (Harian)' :
  st.subheader ('Distribusi Waktu Terakhir Peminjaman Sepeda (Harian)')
  df_day['recency'] = (df_day['dteday'].max() - df_day['dteday']).dt.days
  df_day['frequency'] = df_day['cnt']
  fig, ax = plt.subplots(figsize=(12, 4))
  ax.hist(df_day['recency'], bins=30, color='skyblue', edgecolor='black')
  ax.set_title('Distribusi Waktu Terakhir Peminjaman Sepeda (Harian)')
  ax.set_xlabel('Waktu Terakhir Peminjaman (Hari)')
  ax.set_ylabel('Jumlah Peminjam')
  st.pyplot(fig)

elif analysis_choice == 'Distribusi Frekuensi Peminjaman Sepeda (Harian)' :
  st.subheader ('Distribusi Frekuensi Peminjaman Sepeda (Harian)')
  fig, ax = plt.subplots(figsize=(12, 4))
  ax.hist(df_day['cnt'], bins=30, color='salmon', edgecolor='black')
  ax.set_title('Distribusi Frekuensi Peminjaman Sepeda (Harian)')
  ax.set_xlabel('Frekuensi Peminjaman')
  ax.set_ylabel('Jumlah Peminjam')
  st.pyplot(fig)

elif analysis_choice == 'Distribusi Jumlah Sepeda Disewakan per Jam' :
  st.subheader('Distribusi Jumlah Sepeda Disewakan per Jam')
  fig, ax = plt.subplots(figsize=(12, 4))
  ax.hist(df_hour['cnt'], bins=30, color='lightgreen', edgecolor='black')
  ax.set_title('Distribusi Jumlah Sepeda Disewakan per Jam')
  ax.set_xlabel('Jumlah Sepeda Disewakan')
  ax.set_ylabel('Jumlah Peminjam')
  st.pyplot(fig)
  st.subheader('Pola Peminjaman Sepeda per Jam')
  fig, ax = plt.subplots(figsize=(12, 6))
  ax.plot(df_hour['dteday'], df_hour['cnt'], color='blue', linewidth=2)
  ax.set_title('Pola Peminjaman Sepeda per Jam')
  ax.set_xlabel('Waktu')
  ax.set_ylabel('Jumlah Sepeda Disewakan')
  ax.grid(True, linestyle='--', alpha=0.7)
  st.pyplot(fig)

st.sidebar.subheader('Conclusion')
st.sidebar.write("**Pertanyaan 1:** Bagaimana dinamika penyewaan sepeda berubah seiring perubahan cuaca dan bagaimana variabilitas cuaca memengaruhi keputusan penyewaan?")
st.sidebar.write("- Jawaban untuk Pertanyaan 1 : Dari visualisasi scatter plot, kita dapat melihat bagaimana dinamika penyewaan sepeda berkaitan dengan perubahan cuaca. Terlihat bahwa temperatur yang lebih tinggi cenderung memiliki korelasi positif dengan jumlah sepeda yang disewakan. Pada kondisi cuaca yang cerah, terutama ketika temperatur tinggi, jumlah sepeda yang disewakan lebih tinggi. Sebaliknya, pada kondisi cuaca hujan atau salju, terlihat adanya penurunan dalam jumlah sepeda yang disewakan. Kecepatan angin juga dapat mempengaruhi jumlah sepeda yang disewakan, terutama pada kecepatan yang lebih tinggi.")
st.sidebar.write("**Pertanyaan 2:** Dalam konteks pola musiman penyewaan sepeda, bagaimana pemahaman terhadap preferensi pelanggan di setiap musim dapat diintegrasikan untuk meningkatkan strategi manajemen persediaan sepeda?")
st.sidebar.write("- Jawaban untuk Pertanyaan 2 : Dari visualisasi time series, kita dapat melihat tren harian dalam penyewaan sepeda dengan memperhitungkan musim dan hari kerja. Terlihat bahwa preferensi pelanggan dapat berubah tergantung pada musim tertentu dan apakah itu hari kerja atau tidak. Misalnya, pada musim panas, terlihat peningkatan penyewaan sepeda pada akhir pekan, sementara pada musim dingin, perubahan ini mungkin tidak sejelas. Integrasi pemahaman ini ke dalam strategi manajemen persediaan sepeda dapat mencakup penyesuaian stok atau promosi khusus pada jam-jam tertentu atau musim tertentu untuk memaksimalkan kepuasan pelanggan dan efisiensi operasional.")
st.sidebar.write("**Pertanyaan 3:** Seberapa baru pelanggan melakukan peminjaman sepeda dalam skala harian, dan bagaimana itu memengaruhi tren peminjaman?")
st.sidebar.write("- Jawaban untuk Pertanyaan 3 : Dari visualisasi histogram Recency (waktu terakhir peminjaman) dalam skala harian, kita dapat melihat sebaran waktu terakhir pelanggan melakukan peminjaman sepeda dalam rentang waktu harian. Mayoritas pelanggan terlihat baru-baru ini melakukan peminjaman, namun, ada juga sebagian pelanggan yang tidak aktif dalam waktu yang lebih lama.")
st.sidebar.write("**Pertanyaan 4:** Bagaimana distribusi frekuensi peminjaman sepeda oleh pelanggan dalam skala harian?")
st.sidebar.write("- Jawaban untuk Pertanyaan 4 : Dari visualisasi histogram Frequency (frekuensi peminjaman) dalam skala harian, kita dapat melihat sebaran frekuensi peminjaman sepeda oleh pelanggan. Terlihat bahwa sebagian besar pelanggan memiliki frekuensi peminjaman yang rendah, tetapi ada juga kelompok pelanggan dengan frekuensi peminjaman yang tinggi.")
st.sidebar.write("**Pertanyaan 5:** Bagaimana distribusi jumlah sepeda yang disewakan per jam, dan bagaimana pola peminjaman sepeda terlihat dalam data waktu?")
st.sidebar.write("- Jawaban untuk Pertanyaan 5 : Dari visualisasi histogram, kita dapat melihat distribusi jumlah sepeda yang disewakan per jam. Terlihat bahwa sebagian besar jam memiliki jumlah peminjaman sepeda yang rendah, dengan beberapa jam memiliki puncak peminjaman yang lebih tinggi. Ini menunjukkan pola peminjaman sepeda yang bervariasi selama hari, dan dapat memberikan wawasan tentang saat-saat dengan permintaan tertinggi.")
