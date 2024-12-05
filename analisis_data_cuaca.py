import requests
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# API Key dan daftar kota
API_KEY = '026b69375aa44510e8c69179a5a2c3cf'
cities = ['Jakarta', 'London', 'New York', 'Tokyo', 'Paris', 'Madinah']

# Mengambil data cuaca dan menyimpannya ke file CSV
with open('weather_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['City', 'Temperature', 'Weather'])

    for city in cities:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            weather = data['weather'][0]['description']
            writer.writerow([city, temperature, weather])
        else:
            print(f"Error fetching data for {city}: {data['message']}")

# Membaca data dari CSV
df = pd.read_csv('weather_data.csv')

# Menghitung rata-rata suhu
average_temperature = df['Temperature'].mean()
print(f'Rata-rata suhu: {average_temperature:.2f} °C')

# Menentukan kota dengan suhu tertinggi dan terendah
hottest_city = df.loc[df['Temperature'].idxmax()]
coldest_city = df.loc[df['Temperature'].idxmin()]
print(f'Kota dengan suhu tertinggi: {hottest_city["City"]} dengan {hottest_city["Temperature"]} °C')
print(f'Kota dengan suhu terendah: {coldest_city["City"]} dengan {coldest_city["Temperature"]} °C')

# Menganalisis pola cuaca
weather_counts = df['Weather'].value_counts()
print('Pola cuaca yang paling seringn muncul:')
print(weather_counts)

# Visualisasi suhu per kota dengan warna berbeda
plt.figure(figsize=(10, 6))
sns.barplot(x='City', y='Temperature', data=df, hue='City', palette='viridis', dodge=False)
plt.title('Suhu Kota')
plt.xlabel('Kota')
plt.ylabel('Suhu (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(False)  
plt.savefig('temperature_distribution_cities31.png')
plt.show()

# Visualisasi pola cuaca
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Weather', order=df['Weather'].value_counts().index, palette='viridis', hue='Weather', legend=False)
plt.title('Distribusi Pola Cuaca')
plt.xlabel('Pola Cuaca')
plt.ylabel('Jumlah')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(False)
plt.savefig('temperature_distribution_cities32.png')
plt.show()