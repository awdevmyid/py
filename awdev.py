import os

# Daftar kategori utama dan subkategori sesuai permintaan
CATEGORIES = {
    "aplikasi": 30, "calligraphy": 30, "code": 30, "collor": 30, "converter": 30,
    "devoloper": 30, "domain": 30, "domains": 30, "eq": 30, "finder": 30,
    "hook": 30, "img": 30, "ip": 30, "kodepost": 30, "link": 30, "maps": 30,
    "pdf": 30, "qr": 30, "quran": 30, "removebg": 30, "safelink": 30, "search": 30,
    "seo": 30, "source": 30, "text": 30, "tools": 30, "utilities": 30, "vidio": 30,
    # Market & Business
    "market": 30, "finance": 30, "macro": 30, "micro": 30, "economy": 30,
    "explainers": 30, "manufacturing": 30, "property": 30, "health": 30,
    "education": 30, "lifestyle": 30, "hospitality": 30, "tech": 30, "media": 30,
    "smes": 30, "luxury": 30, "whos-who": 30, "international": 30, "local-resources": 30,
    "politics": 30, "culture": 30, "science": 30, "public-policy": 30, "business": 30,
    "news": 30, "sports": 30, "arts": 30, "celebrities": 30, "automotive": 30,
    "commentary": 30, "interview": 30, "money": 30, "perbankan": 30, "belanja": 30,
    "sharia": 30, "football": 30, "opinion": 30, "video": 30, "kisah": 30,
    "index": 30, "sejarah": 30, "entrepreneur": 30, "research": 30, "photo": 30,
    "olahraga": 30, "selebritis": 30, "country": 30, "dki": 30, "diy": 30,
    "jabar": 30, "jatim": 30, "jateng": 30, "aceh": 30, "papua": 30,
    "kalimantan": 30, "sumatra": 30, "sulawesi": 30, "bali": 30, "asia": 30,
    "afrika": 30, "australia": 30, "rusia": 30, "eropa": 30, "amerika": 30,
    "ai": 30, "teknologi": 30, "astronomi": 30, "zodiak": 30,
    # Islamic Tools & Stories
    "islamic": 30, "biografi-ulama": 30, "kisah-hikmah": 30, "kisah-sejarah": 30,
    "info": 30, "kisah-birrul-walidain": 30, "kisah-hidayah-islam": 30,
    "kisah-kaum-durhaka": 30, "kisah-masa-depan": 30, "kisah-nabi-dan-rasul": 30,
    "kisah-nabi-muhammad": 30, "kisah-nyata": 30, "kisah-orang-shalih": 30,
    "kisah-pilihan": 30, "kisah-sahabat-nabi": 30, "kisah-tabiin": 30,
    "kisah-tak-nyata": 30, "kisah-umat-terdahulu": 30, "sejarah-islam": 30,
    "nusantara": 30, "laporan-produksi": 30, "merchandise-yufid": 30,
    "mutiara-faidah": 30, "teladan-muslimah": 30, "books": 30, "download": 30
}

# Template HTML Dasar dengan Neumorphism, AdSense, Meta Tags, Navbar, & Footer sesuai Home Page Anda
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - AWDEV CORPORATION</title>
    
    <!-- Meta SEO & Open Graph -->
    <meta name="description" content="{description}">
    <meta name="keywords" content="AWDEV, Open Source, {category}, Developer Tools, Programming, Free Apps">
    <meta name="author" content="AWDEV Corporation">
    
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://awdev.my.id/{category}/{filename}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="https://awdev.my.id/img/awdev.png">

    <link rel="icon" type="image/png" href="https://awdev.my.id/awdev.jpg">
    <link rel="icon" type="image/png" href="https://awdev.my.id/awdev.png">

    <!-- Google Verification & AdSense -->
    <meta name="google-site-verification" content="OLryKZ1dDupEH_xOuZWiEwdi0ZvuXMcnQeMjRwe5YCw">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5407249785989200" crossorigin="anonymous"></script>

    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        :root {{
            --bg-color: #e4ebf5;
            --neu-shadow-dark: #c5d1e0;
            --neu-shadow-light: #ffffff;
            --text-color: #333333;
            --primary: #1a73e8;
            --rainbow-gradient: linear-gradient(135deg, #ff3366, #ff9933, #33cc66, #3399ff, #9933ff);
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Poppins', sans-serif; }}
        body {{ background-color: var(--bg-color); color: var(--text-color); line-height: 1.7; padding: 20px; }}
        .rainbow-bar {{ height: 6px; width: 100%; background: var(--rainbow-gradient); border-radius: 3px; margin-bottom: 20px; }}
        .neu-box {{ background: var(--bg-color); box-shadow: 8px 8px 16px var(--neu-shadow-dark), -8px -8px 16px var(--neu-shadow-light); border-radius: 16px; padding: 20px; margin-bottom: 30px; }}
        .neu-inset {{ background: var(--bg-color); box-shadow: inset 4px 4px 8px var(--neu-shadow-dark), inset -4px -4px 8px var(--neu-shadow-light); border-radius: 12px; padding: 15px; margin-bottom: 20px; }}
        header {{ display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-bottom: 20px; }}
        .logo-area {{ display: flex; align-items: center; gap: 15px; }}
        .logo-img {{ width: 50px; height: 50px; border-radius: 50%; object-fit: cover; box-shadow: 4px 4px 8px var(--neu-shadow-dark), -4px -4px 8px var(--neu-shadow-light); }}
        .logo-text {{ font-size: 1.5rem; font-weight: 700; background: var(--rainbow-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .dropdown {{ position: relative; display: inline-block; }}
        .dropbtn {{ background: var(--bg-color); box-shadow: 5px 5px 10px var(--neu-shadow-dark), -5px -5px 10px var(--neu-shadow-light); padding: 10px 18px; font-size: 14px; font-weight: 600; border: none; cursor: pointer; border-radius: 10px; color: var(--primary); }}
        .dropdown-content {{ display: none; position: absolute; right: 0; background-color: var(--bg-color); min-width: 240px; box-shadow: 8px 8px 16px var(--neu-shadow-dark), -8px -8px 16px var(--neu-shadow-light); z-index: 100; border-radius: 12px; padding: 10px 0; max-height: 350px; overflow-y: auto; }}
        .dropdown-content a {{ color: var(--text-color); padding: 10px 20px; text-decoration: none; display: block; font-size: 13px; }}
        .dropdown-content a:hover {{ background: rgba(0,0,0,0.03); color: #ff3366; }}
        .dropdown:hover .dropdown-content {{ display: block; }}
        h1, h2, h3 {{ color: #222; margin-top: 20px; margin-bottom: 10px; }}
        h1 {{ font-size: 2rem; background: var(--rainbow-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        h2 {{ font-size: 1.5rem; border-bottom: 2px solid #d6e0ef; padding-bottom: 5px; }}
        p {{ margin-bottom: 15px; text-align: justify; }}
        ul, ol {{ margin-left: 20px; margin-bottom: 15px; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ border: 1px solid #c5d1e0; padding: 12px; text-align: left; }}
        th {{ background: #d6e0ef; }}
        .social-share {{ display: flex; gap: 15px; justify-content: center; margin: 30px 0; }}
        .social-btn {{ width: 45px; height: 45px; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: var(--bg-color); box-shadow: 5px 5px 10px var(--neu-shadow-dark), -5px -5px 10px var(--neu-shadow-light); color: var(--primary); text-decoration: none; font-size: 1.1rem; }}
        .contact-form input, .contact-form textarea {{ width: 100%; padding: 12px; margin-bottom: 15px; border: none; background: var(--bg-color); box-shadow: inset 4px 4px 8px var(--neu-shadow-dark), inset -4px -4px 8px var(--neu-shadow-light); border-radius: 8px; outline: none; }}
        .neu-button {{ background: var(--bg-color); box-shadow: 5px 5px 10px var(--neu-shadow-dark), -5px -5px 10px var(--neu-shadow-light); border: none; border-radius: 8px; padding: 10px 20px; cursor: pointer; color: var(--text-color); font-weight: 600; text-decoration: none; display: inline-block; }}
        footer {{ text-align: center; padding: 20px; font-size: 14px; color: #666; border-top: 1px solid #c5d1e0; margin-top: 40px; }}
        footer .footer-links {{ margin-top: 10px; display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; }}
        footer .footer-links a {{ color: var(--primary); text-decoration: none; }}
    </style>
</head>
<body>

    <div class="rainbow-bar"></div>

    <!-- Header & Dropdown Navigation -->
    <header class="neu-box">
        <div class="logo-area">
            <img src="https://awdev.my.id/img/awdev.png" alt="AWDEV Corporation Logo" class="logo-img">
            <span class="logo-text">AWDEV CORP</span>
        </div>
        <div class="dropdown">
            <button class="dropbtn"><i class="fas fa-bars"></i> Navigation Menu</button>
            <div class="dropdown-content">
                <a href="https://awdev.my.id/"><i class="fas fa-home"></i> Home</a>
                <a href="https://awdev.my.id/tools/index.html"><i class="fas fa-tools"></i> Tools</a>
                <a href="https://awdev.my.id/aplikasi/index.html"><i class="fas fa-mobile-alt"></i> Aplikasi</a>
                <a href="https://awdev.my.id/seo/index.html"><i class="fas fa-search-dollar"></i> Seo</a>
                <a href="https://awdev.my.id/source/index.html"><i class="fas fa-code"></i> Source</a>
                <a href="https://awdev.my.id/quran/index.html"><i class="fas fa-book-open"></i> Quran & Islamic</a>
            </div>
        </div>
    </header>

    <!-- Iklan AdSense Banner Atas -->
    <div class="neu-box" style="text-align: center;">
        <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="ca-pub-5407249785989200"
             data-ad-slot="1234567890"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
        <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>

    <!-- Main Content -->
    <main class="neu-box">
        <article>
            <h1>{title}</h1>
            <p style="font-size: 0.9rem; color: #666;"><i class="far fa-calendar-alt"></i> Dipublikasikan oleh AWDEV Corporation | Kategori: <strong>{category.upper()}</strong></p>
            
            <!-- Gambar Artikel Utama -->
            <div style="margin: 20px 0; text-align: center;">
                <img src="https://awdev.my.id/img/awdev.png" alt="{title} - Ilustrasi Eksklusif AWDEV {category}" style="max-width: 100%; height: auto; border-radius: 12px; box-shadow: 6px 6px 12px var(--neu-shadow-dark), -6px -6px 12px var(--neu-shadow-light);">
            </div>

            <!-- Tabel Konten / Daftar Isi -->
            <div class="neu-inset">
                <h3><i class="fas fa-list"></i> Daftar Isi</h3>
                <ul>
                    <li><a href="#pendahuluan">1. Pendahuluan & Tinjauan Umum</a></li>
                    <li><a href="#analisis">2. Analisis Mendalam dan Fitur Utama</a></li>
                    <li><a href="#tabel-data">3. Tabel Perbandingan & Spesifikasi Teknis</a></li>
                    <li><a href="#strategi">4. Strategi Implementasi & Best Practices</a></li>
                    <li><a href="#faq">5. Tanya Jawab (FAQ)</a></li>
                    <li><a href="#kesimpulan">6. Kesimpulan</a></li>
                </ul>
            </div>

            <h2 id="pendahuluan">1. Pendahuluan & Tinjauan Umum</h2>
            <p>Selamat datang di pembahasan komprehensif mengenai <strong>{title}</strong> dalam ekosistem AWDEV. Artikel ini dirancang khusus untuk memberikan wawasan mendalam, panduan teknis, serta solusi optimal bagi para pengembang, desainer, dan praktisi industri profesional.</p>
            <p>Dalam era digital yang bergerak cepat, penguasaan terhadap teknologi open-source dan pemanfaatan alat digital yang tepat menjadi kunci utama kesuksesan kompetitif. AWDEV Corporation terus berkomitmen menghadirkan infrastruktur terbuka berkualitas tinggi.</p>

            <h2 id="analisis">2. Analisis Mendalam dan Fitur Utama</h2>
            <p>Penerapan konsep modularitas dan arsitektur modern memastikan setiap modul pada kategori <em>{category}</em> mampu berjalan dengan performa maksimal. Integrasi antarmuka berbasis Neumorphism memberikan pengalaman visual yang elegan sekaligus ergonomis.</p>
            <p>Melalui optimasi SEO tingkat lanjut dan kepatuhan terhadap standar web global, setiap halaman direkayasa agar mudah diindeks oleh mesin pencari serta memberikan kenyamanan mutlak bagi pembaca.</p>

            <!-- Tabel Perbandingan -->
            <h2 id="tabel-data">3. Tabel Perbandingan & Spesifikasi Teknis</h2>
            <table>
                <thead>
                    <tr>
                        <th>Parameter / Fitur</th>
                        <th>Standar Konvensional</th>
                        <th>Solusi AWDEV ({category.capitalize()})</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Kecepatan Muat (Load Speed)</td>
                        <td>Lambat (> 3 detik)</td>
                        <td>Sangat Cepat (< 0.8 detik)</td>
                    </tr>
                    <tr>
                        <td>Antarmuka Pengguna (UI)</td>
                        <td>Flat Design Biasa</td>
                        <td>Soft UI / Neumorphic Shadows</td>
                    </tr>
                    <tr>
                        <td>Kompatibilitas Open Source</td>
                        <td>Terbatas / Proprietary</td>
                        <td>100% Free & Open Source</td>
                    </tr>
                </tbody>
            </table>

            <h2 id="strategi">4. Strategi Implementasi & Best Practices</h2>
            <p>Untuk memaksimalkan penggunaan layanan ini, pastikan Anda mengikuti panduan dokumentasi resmi yang tersedia di repositori GitHub kami. Kolaborasi global terbuka lebar bagi siapa saja yang ingin berkontribusi menyempurnakan ekosistem ini.</p>

            <!-- Internal Links & External Links -->
            <div class="neu-inset">
                <h3><i class="fas fa-link"></i> Referensi & Tautan Terkait</h3>
                <p><strong>Internal Links:</strong></p>
                <ul>
                    <li><a href="https://awdev.my.id/seo/index.html">Panduan SEO & Optimasi Web</a></li>
                    <li><a href="https://awdev.my.id/tools/index.html">Koleksi Alat Developer Lengkap</a></li>
                    <li><a href="https://awdev.my.id/aplikasi/index.html">Aplikasi Web Interaktif Terbaru</a></li>
                    <li><a href="https://awdev.my.id/source/index.html">Repositori Kode Sumber Terbuka</a></li>
                    <li><a href="https://awdev.my.id/eq/index.html">Generator Audio & EQ Modern</a></li>
                    <li><a href="https://awdev.my.id/qr/index.html">Pembuat Kode QR Generator Instan</a></li>
                    <li><a href="https://awdev.my.id/collor/index.html">Palet Warna & Kode Warna CSS</a></li>
                </ul>
                <p style="margin-top: 15px;"><strong>External References:</strong></p>
                <ul>
                    <li><a href="https://github.com/awdevmyid/awdevmyid.github.io" target="_blank" rel="noopener">GitHub Repository Resmi AWDEV</a></li>
                    <li><a href="https://developer.mozilla.org" target="_blank" rel="noopener">MDN Web Docs - Panduan Standar Web</a></li>
                    <li><a href="https://angular.io" target="_blank" rel="noopener">Angular Official Framework</a></li>
                    <li><a href="https://schema.org" target="_blank" rel="noopener">Schema.org Structured Data Vocabulary</a></li>
                    <li><a href="https://w3.org" target="_blank" rel="noopener">W3C Web Standards Consortium</a></li>
                    <li><a href="https://nodejs.org" target="_blank" rel="noopener">Node.js JavaScript Runtime Environment</a></li>
                    <li><a href="https://git-scm.com" target="_blank" rel="noopener">Git Version Control System</a></li>
                </ul>
            </div>

            <!-- FAQ Section -->
            <h2 id="faq">5. Tanya Jawab (FAQ)</h2>
            <div class="neu-inset">
                <p><strong>Q: Apakah seluruh layanan dan artikel di AWDEV gratis?</strong><br>A: Ya, seluruh perangkat, kode sumber, dan artikel dokumentasi disediakan secara gratis dan open-source.</p>
                <p><strong>Q: Bagaimana cara berkontribusi ke repositori GitHub AWDEV?</strong><br>A: Anda dapat melakukan fork pada repositori resmi kami di GitHub dan mengirimkan pull request dengan fitur atau perbaikan baru.</p>
                <p><strong>Q: Apakah alat-alat utilitas dapat diakses secara offline?</strong><br>A: Sebagian besar aplikasi berbasis web kami dirancang dengan PWA sehingga mendukung penyimpanan cache lokal.</p>
            </div>

            <h2 id="kesimpulan">6. Kesimpulan</h2>
            <p>Melalui pengembangan berkelanjutan pada kategori <strong>{category.upper()}</strong>, AWDEV Corporation terus berdedikasi menghadirkan solusi teknologi yang handal, cepat, dan mudah diakses oleh komunitas global. Mari bergabung bersama ribuan pengembang lainnya dalam memajukan ekosistem open-source.</p>

            <!-- Social Share Media -->
            <div class="social-share">
                <a href="https://facebook.com/sharer/sharer.php?u=https://awdev.my.id/{category}/{filename}" class="social-btn" title="Share to Facebook"><i class="fab fa-facebook-f"></i></a>
                <a href="https://twitter.com/intent/tweet?url=https://awdev.my.id/{category}/{filename}&text={title}" class="social-btn" title="Share to Twitter"><i class="fab fa-twitter"></i></a>
                <a href="https://api.whatsapp.com/send?text={title} https://awdev.my.id/{category}/{filename}" class="social-btn" title="Share to WhatsApp"><i class="fab fa-whatsapp"></i></a>
                <a href="https://www.linkedin.com/shareArticle?mini=true&url=https://awdev.my.id/{category}/{filename}&title={title}" class="social-btn" title="Share to LinkedIn"><i class="fab fa-linkedin-in"></i></a>
            </div>

            <!-- Contact Form -->
            <div class="neu-inset contact-form" style="margin-top: 30px;">
                <h3><i class="fas fa-envelope"></i> Hubungi Dukungan AWDEV</h3>
                <form onsubmit="event.preventDefault(); alert('Pesan berhasil terkirim!');">
                    <input type="text" placeholder="Nama Lengkap Anda" required>
                    <input type="email" placeholder="Alamat Email Aktif" required>
                    <textarea rows="4" placeholder="Tuliskan pesan, saran, atau pertanyaan Anda di sini..." required></textarea>
                    <button type="submit" class="neu-button">Kirim Pesan Sekarang</button>
                </form>
            </div>
        </article>
    </main>

    <!-- Footer Persis Halaman Utama -->
    <footer>
        <p>&copy; 2026 AWDEV CORPORATION. All Rights Reserved.</p>
        <div class="footer-links">
            <a href="https://awdev.my.id/">Home</a>
            <a href="https://awdev.my.id/tools/index.html">Tools</a>
            <a href="https://awdev.my.id/aplikasi/index.html">Aplikasi</a>
            <a href="https://awdev.my.id/seo/index.html">SEO</a>
            <a href="https://awdev.my.id/source/index.html">Source Code</a>
            <a href="https://github.com/awdevmyid/awdevmyid.github.io" target="_blank">GitHub Repo</a>
        </div>
    </footer>

</body>
</html>
"""

def generate_site():
    print("Memulai pembuatan struktur direktori dan file blog otomatis...")
    
    for category, count in CATEGORIES.items():
        cat_dir = os.path.join(".", category)
        os.makedirs(cat_dir, exist_ok=True)
        
        # Buat index.html untuk kategori
        index_path = os.path.join(cat_dir, "index.html")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(HTML_TEMPLATE.format(
                title=f"Kumpulan Artikel & Panduan {category.capitalize()}",
                description=f"Eksplorasi lengkap artikel, panduan, dan alat terbaik dalam kategori {category} dari AWDEV Corporation.",
                category=category,
                filename="index.html"
            ))
            
        # Buat sitemap, txt, xml per kategori
        with open(os.path.join(cat_dir, "sitemap.html"), "w", encoding="utf-8") as f:
            f.write(f"<h1>Sitemap - {category.capitalize()}</h1><p>Daftar tautan lengkap kategori {category}.</p>")
            
        with open(os.path.join(cat_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"></urlset>')
            
        with open(os.path.join(cat_dir, "sitemap.txt"), "w", encoding="utf-8") as f:
            f.write(f"https://awdev.my.id/{category}/index.html\n")

        # Buat artikel (artikel1.html sampai artikel30.html)
        for i in range(1, count + 1):
            filename = f"artikel{i}.html"
            file_path = os.path.join(cat_dir, filename)
            article_title = f"Panduan Lengkap dan Analisis Mendalam {category.capitalize()} Bagian {i}"
            article_desc = f"Baca artikel eksklusif {article_title} beserta tips, trik, dan dokumentasi open-source terbaik dari AWDEV."
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(HTML_TEMPLATE.format(
                    title=article_title,
                    description=article_desc,
                    category=category,
                    filename=filename
                ))
                
        print(f"Berhasil membuat kategori '{category}' beserta {count} artikel dan sitemap.")

    print("\nSemua direktori dan file blog otomatis berhasil dibuat sepenuhnya!")

if __name__ == "__main__":
    generate_site()
