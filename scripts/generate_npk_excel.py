import xlsxwriter
import os

def generate_food_crop_encyclopedia_v2():
    output_path = "AgriSensa_Food_Crop_Encyclopedia_Calculator_v2.xlsx"
    workbook = xlsxwriter.Workbook(output_path)
    
    # 1. Styles
    header_fmt = workbook.add_format({'bold': True, 'font_color': 'white', 'bg_color': '#166534', 'border': 1, 'align': 'center', 'valign': 'vcenter', 'font_size': 14})
    subhead_fmt = workbook.add_format({'bold': True, 'bg_color': '#f0fdf4', 'border': 1, 'align': 'center'})
    label_fmt = workbook.add_format({'bold': True, 'bg_color': '#f9fafb', 'border': 1})
    input_fmt = workbook.add_format({'bg_color': '#fff7ed', 'border': 2, 'font_color': '#9a3412', 'bold': True})
    result_fmt = workbook.add_format({'bg_color': '#ecfdf5', 'border': 2, 'font_color': '#064e3b', 'bold': True, 'num_format': '#,##0'})
    bag_fmt = workbook.add_format({'bg_color': '#f0f9ff', 'border': 2, 'font_color': '#075985', 'bold': True, 'num_format': '#,##0.0'})
    currency_fmt = workbook.add_format({'bg_color': '#ecfdf5', 'border': 2, 'font_color': '#064e3b', 'bold': True, 'num_format': '"Rp "#,##0'})
    price_fmt = workbook.add_format({'bg_color': '#fff7ed', 'border': 1, 'font_color': '#9a3412', 'bold': True, 'num_format': '"Rp "#,##0'})

    # 2. Main Sheet: Kalkulator Pangan
    ws = workbook.add_worksheet("Dashboard")
    ws.set_column('A:A', 5)
    ws.set_column('B:B', 35)
    ws.set_column('C:C', 35)
    ws.set_column('D:D', 25)

    ws.merge_range('B2:E2', '🌾 AGRISENSA FOOD CROP MASTER CALCULATOR v2.0', header_fmt)
    ws.write('B3', 'Edisi Master: Kalkulator Lahan, pH, & Database Harga Terpusat', workbook.add_format({'italic': True, 'font_size': 10}))

    # SECTION 1: INPUT LAHAN
    ws.merge_range('B5:D5', '1. KONFIGURASI LAHAN & TANAMAN', subhead_fmt)
    ws.write('B6', 'Pilih Tanaman Pangan:', label_fmt)
    ws.data_validation('C6', {'validate': 'list', 'source': ['Padi Sawah', 'Jagung Hibrida', 'Kedelai', 'Singkong', 'Kacang Tanah']})
    ws.write('C6', 'Padi Sawah', input_fmt)

    ws.write('B7', 'Total Luas Lahan (m2):', label_fmt)
    ws.write('C7', 10000, input_fmt)
    ws.write('D7', '=C7/10000', workbook.add_format({'num_format': '0.00 " Hektar"'}))

    # SECTION 2: NUTRISI & DOSIS
    ws.merge_range('B9:D9', '2. REKOMENDASI PUPUK (TOTAL KEBUTUHAN)', subhead_fmt)
    ws.write('B10', 'Bahan Pupuk', label_fmt)
    ws.write('C10', 'Total (Kg)', label_fmt)
    ws.write('D10', 'Jumlah Karung (50kg)', label_fmt)

    pupuk_keys = ['Urea', 'NPK Phonska', 'SP-36', 'KCl']
    for i, p in enumerate(pupuk_keys):
        row = 11 + i
        ws.write(f'B{row}', p, label_fmt)
        ws.write(f'C{row}', f'=VLOOKUP(C6, Database!A2:E20, {i+2}, 0) * D7', result_fmt)
        ws.write(f'D{row}', f'=C{row}/50', bag_fmt)

    # SECTION 3: pH TANAH
    ws.merge_range('B16:D16', '3. KALKULATOR pH TANAH (PEMBENAH)', subhead_fmt)
    ws.write('B17', 'pH Tanah Saat Ini:', label_fmt)
    ws.write('C17', 5.0, input_fmt)
    ws.write('B18', 'Target pH Tanah:', label_fmt)
    ws.write('C18', 6.5, label_fmt)
    ws.write('B19', 'Rekomendasi Kapur (Dolomit):', label_fmt)
    ws.write(f'C19', '=IF(C17<C18, (C18-C17) * 1.5 * D7 * 1000, 0)', result_fmt)
    ws.write('D19', 'Kg')

    # SECTION 4: TENAGA KERJA (HOK)
    ws.merge_range('B21:D21', '4. ANALISIS TENAGA KERJA (HOK)', subhead_fmt)
    ws.write('B22', 'Upah Harian (HOK):', label_fmt)
    ws.write('C22', '=Settings!C8', currency_fmt) # Fixed linking to settings
    ws.write('B23', 'Estimasi Total Pekerja (Orang):', label_fmt)
    ws.write('C23', '=D7 * 120', result_fmt)
    ws.write('B24', 'Total Biaya Tenaga Kerja:', label_fmt)
    ws.write('C24', '=C22 * C23', currency_fmt)

    # SECTION 5: TOTAL ANGGARAN DENGAN DATABASE HARGA
    ws.merge_range('B26:D26', '5. TOTAL ESTIMASI BIAYA PRODUKSI', subhead_fmt)
    ws.write('B27', 'Urea:', label_fmt)
    ws.write('C27', '=C11 * Settings!C3', currency_fmt)
    ws.write('B28', 'NPK Phonska:', label_fmt)
    ws.write('C28', '=C12 * Settings!C4', currency_fmt)
    ws.write('B29', 'SP-36:', label_fmt)
    ws.write('C29', '=C13 * Settings!C5', currency_fmt)
    ws.write('B30', 'KCl:', label_fmt)
    ws.write('C30', '=C14 * Settings!C6', currency_fmt)
    ws.write('B31', 'Dolomit:', label_fmt)
    ws.write('C31', '=C19 * Settings!C7', currency_fmt)
    
    ws.write('B33', 'TOTAL MODUL (PUPUK + PEKERJA):', subhead_fmt)
    ws.write('C33', '=SUM(C27:C31) + C24', header_fmt)

    # 3. SETTINGS SHEET (HARGA EDITABLE)
    ws_settings = workbook.add_worksheet("Settings")
    ws_settings.set_column('B:B', 30)
    ws_settings.set_column('C:C', 20)
    
    ws_settings.merge_range('B2:C2', '⚙️ DATABASE HARGA (EDITABLE)', header_fmt)
    ws_settings.write('B3', 'Harga Urea (per Kg):', label_fmt)
    ws_settings.write('C3', 6000, price_fmt)
    ws_settings.write('B4', 'Harga NPK Phonska (per Kg):', label_fmt)
    ws_settings.write('C4', 12000, price_fmt)
    ws_settings.write('B5', 'Harga SP-36 (per Kg):', label_fmt)
    ws_settings.write('C5', 10000, price_fmt)
    ws_settings.write('B6', 'Harga KCl (per Kg):', label_fmt)
    ws_settings.write('C6', 15000, price_fmt)
    ws_settings.write('B7', 'Harga Dolomit (per Kg):', label_fmt)
    ws_settings.write('C7', 2000, price_fmt)
    ws_settings.write('B8', 'Upah Harian (HOK):', label_fmt)
    ws_settings.write('C8', 100000, price_fmt)
    
    ws_settings.write('B10', 'Catatan: Ubah angka di atas sesuai harga pasar daerah Anda.', workbook.add_format({'italic': True, 'font_size': 9}))

    # 4. Database Sheet
    db = workbook.add_worksheet("Database")
    data = [
        ['Padi Sawah', 250, 300, 100, 100],
        ['Jagung Hibrida', 300, 400, 100, 50],
        ['Kedelai', 50, 150, 100, 100],
        ['Singkong', 200, 300, 100, 200],
        ['Kacang Tanah', 50, 100, 100, 50],
    ]
    db.write_row(0, 0, ['Tanaman', 'Urea_ha', 'NPK_ha', 'SP36_ha', 'KCl_ha'])
    for r, row_data in enumerate(data):
        db.write_row(r + 1, 0, row_data)
    
    workbook.close()
    return output_path

if __name__ == "__main__":
    path = generate_food_crop_encyclopedia_v2()
    print(f"v2 Excel file created at: {os.path.abspath(path)}")
