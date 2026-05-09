"""
Centralized Data Store for Agricultural RAB Templates
Used by AgriSensa Biz modules.
"""

CROP_TEMPLATES = {
    "Jagung Hibrida": {
        "params": {"populasi_ha": 66000, "total_panen_kg": 9000, "harga_jual": 5000, "lama_tanam_bulan": 4},
        "items": [
            {"kategori": "Biaya Tetap", "item": "Sewa Lahan", "satuan": "Musim", "volume": 1, "harga": 3000000, "wajib": True},
            {"kategori": "Benih", "item": "Benih Hibrida (Exp: NK/Bisi)", "satuan": "Kg", "volume": 20, "harga": 110000, "wajib": True},
            {"kategori": "Pupuk", "item": "Urea", "satuan": "Kg", "volume": 350, "harga": 6000, "wajib": True},
            {"kategori": "Pupuk", "item": "NPK", "satuan": "Kg", "volume": 300, "harga": 15000, "wajib": True},
            {"kategori": "Pestisida", "item": "Herbisida Selektif Jagung", "satuan": "Liter", "volume": 3, "harga": 180000, "wajib": True},
            {"kategori": "Tenaga Kerja", "item": "Olah Tanah", "satuan": "Borongan/Ha", "volume": 1, "harga": 2000000, "wajib": True},
            {"kategori": "Tenaga Kerja", "item": "Tanam", "satuan": "HOK", "volume": 15, "harga": 90000, "wajib": True},
            {"kategori": "Tenaga Kerja", "item": "Pemupukan I & II", "satuan": "HOK", "volume": 12, "harga": 90000, "wajib": True},
            {"kategori": "Tenaga Kerja", "item": "Panen & Pipil", "satuan": "Borongan", "volume": 1, "harga": 3500000, "wajib": True},
        ]
    },
    "Kentang (Dieng/Granola)": {
         "params": {"populasi_ha": 25000, "total_panen_kg": 20000, "harga_jual": 12000, "lama_tanam_bulan": 4},
         "items": [
             {"kategori": "Biaya Tetap", "item": "Sewa Lahan Bukit", "satuan": "Musim", "volume": 1, "harga": 8000000, "wajib": True},
             {"kategori": "Benih", "item": "Bibit Knol (G1/G2)", "satuan": "Kg", "volume": 1200, "harga": 25000, "wajib": True},
             {"kategori": "Pupuk", "item": "Pupuk Kandang (Ayam/Sapi)", "satuan": "Ton", "volume": 15, "harga": 800000, "wajib": True},
             {"kategori": "Pestisida", "item": "Fungisida (Phytophthora)", "satuan": "Paket", "volume": 1, "harga": 10000000, "wajib": True, "catatan": "Sangat tinggi di musim hujan"},
             {"kategori": "Tenaga Kerja", "item": "Garpu/Bedengan Tinggi", "satuan": "HOK", "volume": 80, "harga": 100000, "wajib": True},
             {"kategori": "Tenaga Kerja", "item": "Panen & Angkut", "satuan": "Borongan", "volume": 1, "harga": 5000000, "wajib": True},
         ]
    },
    "Kubis / Kol": {
        "params": {"populasi_ha": 30000, "total_panen_kg": 50000, "harga_jual": 2000, "lama_tanam_bulan": 3},
        "items": [
            {"kategori": "Benih", "item": "Benih Hibrida", "satuan": "Sachet", "volume": 15, "harga": 80000, "wajib": True},
            {"kategori": "Pupuk", "item": "Pupuk Kandang & Urea", "satuan": "Paket", "volume": 1, "harga": 5000000, "wajib": True},
            {"kategori": "Pestisida", "item": "Insektisida (Ulat Krop)", "satuan": "Paket", "volume": 1, "harga": 3000000, "wajib": True},
            {"kategori": "Tenaga Kerja", "item": "Perawatan Intensif", "satuan": "HOK", "volume": 40, "harga": 90000, "wajib": True},
        ]
    },
    "Wortel": {
         "params": {"populasi_ha": 250000, "total_panen_kg": 25000, "harga_jual": 3000, "lama_tanam_bulan": 3.5},
         "items": [
             {"kategori": "Benih", "item": "Benih Unggul", "satuan": "Kaleng", "volume": 8, "harga": 300000, "wajib": True},
             {"kategori": "Tenaga Kerja", "item": "Olah Tanah (Gembur)", "satuan": "HOK", "volume": 50, "harga": 100000, "wajib": True, "catatan": "Tanah harus sangat gembur"},
             {"kategori": "Tenaga Kerja", "item": "Panen (Cabut & Cuci)", "satuan": "HOK", "volume": 80, "harga": 80000, "wajib": True},
         ]
    },
    "Semangka (Non-Biji)": {
         "params": {"populasi_ha": 4000, "total_panen_kg": 25000, "harga_jual": 4500, "lama_tanam_bulan": 3},
         "items": [
            {"kategori": "Benih", "item": "Benih Non-Biji + Serbuk Sari", "satuan": "Paket", "volume": 1, "harga": 3000000, "wajib": True},
            {"kategori": "Penunjang", "item": "Mulsa", "satuan": "Roll", "volume": 5, "harga": 650000, "wajib": True},
            {"kategori": "Pupuk", "item": "Pupuk Kandang & NPK", "satuan": "Paket", "volume": 1, "harga": 5000000, "wajib": True},
            {"kategori": "Tenaga Kerja", "item": "Olah Tanah", "satuan": "Borongan", "volume": 1, "harga": 2500000, "wajib": True},
         ]
    },
    "Buah Naga (Investasi Tahun 1)": {
        "params": {"populasi_ha": 2000, "total_panen_kg": 0, "harga_jual": 12000, "lama_tanam_bulan": 12}, 
        "items": [
            {"kategori": "Investasi Awal", "item": "Tiang Panjat (Beton/Kayu)", "satuan": "Batang", "volume": 500, "harga": 150000, "wajib": True, "catatan": "Jarak 2.5 x 2.5m (populasi 4 tan/tiang)"},
            {"kategori": "Investasi Awal", "item": "Ban Bekas / Penyangga", "satuan": "Buah", "volume": 500, "harga": 10000, "wajib": True},
            {"kategori": "Benih", "item": "Stek Batang (Bibit)", "satuan": "Batang", "volume": 2000, "harga": 5000, "wajib": True},
            {"kategori": "Pupuk", "item": "Pupuk Kandang (Awal)", "satuan": "Truk", "volume": 5, "harga": 1500000, "wajib": True},
            {"kategori": "Tenaga Kerja", "item": "Lubang Tanam & Pasang Tiang", "satuan": "Borongan", "volume": 1, "harga": 6000000, "wajib": True},
        ]
    },
    "Cabai Merah (Greenhouse Hydroponic)": {
        "params": {"populasi_ha": 30000, "total_panen_kg": 25000, "harga_jual": 30000, "lama_tanam_bulan": 6},
        "items": [
            {"kategori": "Biaya Tetap", "item": "Amortisasi Green house (Sewa/Penyusutan)", "satuan": "Musim", "volume": 1, "harga": 75000000, "wajib": True, "catatan": "Asumsi GH 1 Ha @1.5M, umur 10 thn"},
            {"kategori": "Biaya Tetap", "item": "Listrik & Air (Pompa)", "satuan": "Bulan", "volume": 6, "harga": 500000, "wajib": True},
            {"kategori": "Nutrisi (AB Mix)", "item": "Paket AB Mix Cabai (Pekat)", "satuan": "Paket (5L)", "volume": 100, "harga": 85000, "wajib": True, "catatan": "Kebutuhan Fertigasi Harian"},
            {"kategori": "Media Tanam", "item": "Cocopeat & Polybag", "satuan": "Paket", "volume": 1, "harga": 15000000, "wajib": True, "catatan": "Dipakai 2-3 musim"},
            {"kategori": "Benih", "item": "Benih F1 Import", "satuan": "Sachet", "volume": 20, "harga": 180000, "wajib": True},
            {"kategori": "Pestisida", "item": "Bio-Pesticide (Preventif)", "satuan": "Paket", "volume": 1, "harga": 1500000, "wajib": True, "catatan": "Hanya 30% dibanding Open Field"},
            {"kategori": "Tenaga Kerja", "item": "Operator Fertigasi & Pruning", "satuan": "HOK", "volume": 120, "harga": 100000, "wajib": True, "catatan": "Manajemen Intensif"},
             {"kategori": "Tenaga Kerja", "item": "Panen (Sortir Grade A)", "satuan": "HOK", "volume": 150, "harga": 90000, "wajib": True},
        ]
    },
    "Melon (Greenhouse Premium)": {
        "params": {"populasi_ha": 22000, "total_panen_kg": 35000, "harga_jual": 25000, "lama_tanam_bulan": 3},
        "items": [
             {"kategori": "Biaya Tetap", "item": "Amortisasi Green house", "satuan": "Musim", "volume": 1, "harga": 75000000, "wajib": True},
             {"kategori": "Biaya Tetap", "item": "Talianjir & Klip Gantung", "satuan": "Paket", "volume": 1, "harga": 5000000, "wajib": True},
            {"kategori": "Benih", "item": "Benih Melon Premium (Intanon/Fujisawa)", "satuan": "Biji", "volume": 22000, "harga": 2500, "wajib": True, "catatan": "Harga per biji!"},
             {"kategori": "Nutrisi (AB Mix)", "item": "Nutrisi Buah Premium", "satuan": "Paket", "volume": 150, "harga": 90000, "wajib": True},
             {"kategori": "Pestisida", "item": "Fungisida Powdery Mildew", "satuan": "Paket", "volume": 1, "harga": 1000000, "wajib": True},
             {"kategori": "Tenaga Kerja", "item": "Polinasi & Gantung Buah", "satuan": "HOK", "volume": 80, "harga": 100000, "wajib": True, "catatan": "Kritis & Rumit"},
             {"kategori": "Tenaga Kerja", "item": "Panen & Packaging", "satuan": "HOK", "volume": 60, "harga": 90000, "wajib": True},
        ]
    },
    "Krisan / Bunga Potong (Greenhouse)": {
        "params": {"populasi_ha": 400000, "total_panen_kg": 350000, "harga_jual": 2500, "lama_tanam_bulan": 3.5, "unit": "Batang"},
        "items": [
             {"kategori": "Biaya Tetap", "item": "Amortisasi Green house (Standard)", "satuan": "Musim", "volume": 1, "harga": 50000000, "wajib": True, "catatan": "Bambu/Besi Sederhana, umur 5 th"},
             {"kategori": "Biaya Tetap", "item": "Listrik Night Break (Lampu)", "satuan": "Bulan", "volume": 2, "harga": 1500000, "wajib": True, "catatan": "Fase Vegetatif (4-5 Jam/malam)"},
             {"kategori": "Persiapan Lahan", "item": "Amandemen (Kapur/Sekam)", "satuan": "Paket", "volume": 1, "harga": 5000000, "wajib": True},
             {"kategori": "Persiapan Lahan", "item": "Jaring Penegak (Netting)", "satuan": "Roll", "volume": 20, "harga": 350000, "wajib": True, "catatan": "Dipakai berulang 3-4x"},
             {"kategori": "Benih", "item": "Bibit Siap Tanam (Stek Pucuk)", "satuan": "Batang", "volume": 400000, "harga": 300, "wajib": True, "catatan": "Kerapatan 60-80 tan/m2"},
             {"kategori": "Pupuk", "item": "Pupuk Dasar & Kocor", "satuan": "Paket", "volume": 1, "harga": 12000000, "wajib": True},
             {"kategori": "Pestisida", "item": "Pestisida (Karat Putih/Trips)", "satuan": "Paket", "volume": 1, "harga": 8000000, "wajib": True},
             {"kategori": "Tenaga Kerja", "item": "Tanam/Pinch/Disbudding", "satuan": "HOK", "volume": 200, "harga": 90000, "wajib": True},
             {"kategori": "Tenaga Kerja", "item": "Panen & Ikat", "satuan": "HOK", "volume": 150, "harga": 90000, "wajib": True},
        ]
    },
}
