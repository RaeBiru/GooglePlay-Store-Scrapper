from google_play_scraper import app, reviews_all
import pandas as pd

#Made by RaeBiru <3

def kodebahasa():
    output1 = """
    Kode bahasa
    Indonesia = id
    Inggris = en
    Spanyol = es
    Prancis = fr
    """
    return output1

result = kodebahasa()
print(result)

def googleplay_scrapper(app_package):
    app_info = app(app_package)
    app_title = app_info['title']
    print(f"Mengambil ulasan dari '{app_title}'")

    reviews = reviews_all(app_package, sort='newest', lang= lang_input)
    print(f"Total ulasan dari pengguna: {len(reviews)}")

    return reviews

def simpanExcel(reviews, excel_file):
    df = pd.DataFrame(reviews)

    df['at'] = pd.to_datetime(df['at'])

    df_sorted = df.sort_values(by='at', ascending=False)

    df_sorted.to_excel(excel_file, index=False)
    print(f"Ulasan berhasil disimpan pada '{excel_file}'.")

if __name__ == "__main__":
    lang_input = input("Masukan Kode dari bahasa yang diinginkan (contohnya: id, en, es): ")
    app_package = input("Masukan ID aplikasi (Contohnya: com.gojek.app): ")
    excel_file_name = input("Masukan nama file: ")
    excel_file = f"{excel_file_name}.xlsx"

    scraped_reviews = googleplay_scrapper(app_package)
    simpanExcel(scraped_reviews, excel_file)
