# 🌍 Türkiye Deprem Görüntüleyici

Bu proje, Türkiye ve dünya genelindeki depremleri gerçek zamanlı olarak görüntülemek için geliştirilmiş bir web uygulamasıdır. USGS (United States Geological Survey) API'sini kullanarak deprem verilerini çeker ve kullanıcı dostu bir arayüz ile sunar.

## 🌟 Özellikler

- 🗺️ Etkileşimli harita görünümü
- 📍 Türkiye'nin önemli şehirleri için özel arama desteği
- 📅 Tarih aralığı ile filtreleme
- 📊 Deprem büyüklüğüne göre filtreleme
- 🌓 Koyu/Açık tema desteği
- 📱 Mobil uyumlu tasarım
- 🔄 Gerçek zamanlı veri güncelleme
- 🎨 Deprem büyüklüğüne göre renkli gösterim
- 📝 Detaylı deprem bilgileri

## 🛠️ Kullanılan Teknolojiler

- Python 3.x
- Flask
- HTML5
- CSS3
- JavaScript
- Leaflet.js (Harita görüntüleme)
- Bootstrap 5
- USGS Earthquake API

## 📦 Gereksinimler

```bash
flask==2.3.3
requests==2.26.0
folium==0.12.1
python-dotenv==1.0.0
```

## 🚀 Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/kullaniciadi/deprem-goruntleyici.git
cd deprem-goruntleyici
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. Uygulamayı başlatın:
```bash
python main.py
```

4. Tarayıcınızda aşağıdaki adresi açın:
```
http://localhost:5000
```

## 📱 Mobil Erişim

Aynı ağdaki mobil cihazlardan erişmek için:

1. Bilgisayarınızın IP adresini öğrenin:
```bash
ipconfig  # Windows için
ifconfig  # Linux/Mac için
```

2. Mobil cihazınızın tarayıcısında şu adresi açın:
```
http://[BILGISAYAR_IP]:5000
```

## 🎯 Kullanım

1. **Şehir Seçimi**: Türkiye'nin önemli şehirlerinden birini seçin
2. **Tarih Aralığı**: İstediğiniz tarih aralığını belirleyin
3. **Büyüklük Filtresi**: Minimum deprem büyüklüğünü ayarlayın
4. **Tema Değiştirme**: Sağ üst köşedeki tema değiştirme butonu ile koyu/açık tema arasında geçiş yapın

## 🎨 Deprem Büyüklük Renk Kodları

- 🔴 7.0+ : Kırmızı
- 🟠 6.0-6.9 : Turuncu
- 🟡 5.0-5.9 : Sarı
- 🟢 4.0-4.9 : Açık Yeşil
- 💚 3.0-3.9 : Yeşil

## 📸 Ekran Görüntüleri

### Ana Sayfa (Açık Tema)
![Ana Sayfa Açık Tema](screenshots/light-theme.png)

### Ana Sayfa (Koyu Tema)
![Ana Sayfa Koyu Tema](screenshots/dark-theme.png)

### Mobil Görünüm
![Mobil Görünüm](screenshots/mobile-view.png)

### Filtreleme Örneği
![Filtreleme Örneği](screenshots/filter-example.png)

## 🤝 Katkıda Bulunma

1. Bu projeyi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: Detaylar'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

## 🙏 Teşekkürler

- USGS için deprem verilerini açık bir şekilde paylaştıkları için
- Leaflet.js ekibine harika harita kütüphanesi için
- Bootstrap ekibine modern UI framework'ü için 