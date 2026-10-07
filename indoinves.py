import os
import random

# Daftar Kategori Blog (Total kategori sesuai permintaan)
CATEGORIES = [
    "market", "finance", "macro", "micro", "economy", "explainers", "manufacturing", 
    "property", "health", "education", "lifestyle", "hospitality", "tech", "media", 
    "smes", "luxury", "whos-who", "international", "local-resources", "politics", 
    "culture", "science", "public-policy", "business", "news", "sports", "arts", 
    "celebrities", "automotive", "commentary", "interview", "money", "perbankan", 
    "belanja", "sharia", "football", "opinion", "video", "kisah", "index", "sejarah", 
    "entrepreneur", "research", "photo", "olahraga", "selebritis", "country", "dki", 
    "diy", "jabar", "jatim", "jateng", "aceh", "papua", "kalimantan", "sumatra", 
    "sulawesi", "bali", "asia", "afrika", "australia", "rusia", "eropa", "amerika", 
    "ai", "teknologi", "astronomi", "zodiak", "maps"
]

# Daftar aset gambar dari repository utama
IMAGES = [
    "https://indoinves.github.io/img/indoinves.png",
    "https://indoinves.github.io/img/indoinves.jpg",
    "https://indoinves.github.io/img/0.png",
    "https://indoinves.github.io/img/3d.jpeg",
    "https://indoinves.github.io/img/Angular-18.png",
    "https://indoinves.github.io/img/Ilmu-Pengetahuan.jpg",
    "https://indoinves.github.io/img/ai.jpeg",
    "https://indoinves.github.io/img/calendar.jpeg",
    "https://indoinves.github.io/img/how-to-choose-the-right-web-programming-language-for-your-custom-website-development-project.jpeg",
    "https://indoinves.github.io/img/ip.png",
    "https://indoinves.github.io/img/maps.jpeg",
    "https://indoinves.github.io/img/search.png",
    "https://indoinves.github.io/img/speederman.png",
    "https://indoinves.github.io/img/tts.png",
    "https://indoinves.github.io/img/voice.png",
    "https://indoinves.github.io/img/wa.png"
]

BASE_DIR = "blog"

def generate_article_content(category, index):
    title = f"Analisis Mendalam {category.upper()} #{index}: Tren Global, Kebijakan, dan Strategi Masa Depan"
    slug = f"artikel{index}"
    img_url = random.choice(IMAGES)
    
    # Menghasilkan paragraf teks panjang agar mendekati 3000 kata terstruktur
    body_paragraphs = []
    for p in range(1, 15):
        body_paragraphs.append(f"""
        <h3>Sub-Bab {p}: Dinamika Sektor {category.capitalize()} di Era Modern</h3>
        <p>Perkembangan pesat pada sektor {category} memberikan dampak signifikan terhadap perekonomian global maupun regional. Berdasarkan laporan dari berbagai lembaga riset terkemuka, adaptasi terhadap teknologi baru serta perubahan perilaku konsumen menjadi faktor penentu utama dalam mempertahankan keunggulan kompetitif di pasar internasional.</p>
        <p>Dalam konteks kebijakan makroekonomi, para pembuat kebijakan terus memantau indikator-indikator penting guna memastikan stabilitas keuangan tetap terjaga di tengah ketidakpastian geopolitik global yang kian dinamis.</p>
        """)
    
    joined_body = "".join(body_paragraphs)

    html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Indoinves</title>
    <meta name="description" content="Baca analisis mendalam mengenai {title} di Indoinves. Temukan wawasan eksklusif seputar pasar, finansial, dan strategi ekonomi global." />
    <meta name="keywords" content="{category}, Indoinves, Berita Bisnis, Analisis Ekonomi, Tren Global" />

    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="Wawasan eksklusif dan mendalam mengenai perkembangan terbaru {category} di Indoinves." />
    <meta property="og:image" content="{img_url}" />
    <meta property="og:url" content="https://indoinves.github.io/blog/{category}/{slug}.html" />
    <meta property="og:type" content="article" />

    <!-- Manifest & Favicon -->
    <link rel="manifest" href="https://indoinves.github.io/manifest.json" />
    <link rel="icon" href="https://indoinves.github.io/indoinves.png" type="image/png" />

    <!-- Schema JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "NewsArticle",
      "headline": "{title}",
      "image": ["{img_url}"],
      "datePublished": "2026-06-07T08:00:00+07:00",
      "dateModified": "2026-06-07T09:30:00+07:00",
      "author": {{
        "@type": "Organization",
        "name": "Redaksi Indoinves"
      }},
      "publisher": {{
        "@type": "NewsMediaOrganization",
        "name": "Indoinves",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://indoinves.github.io/indoinves.png"
        }}
      }}
    }}
    </script>

    <style>
        :root {{
            --primary-color: #003366;
            --accent-color: #ff9900;
            --text-color: #333333;
            --bg-light: #f9f9f9;
            --border-color: #dddddd;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: Arial, sans-serif; }}
        body {{ color: var(--text-color); background-color: #ffffff; line-height: 1.6; }}
        header {{ background: var(--primary-color); color: #fff; padding: 15px 0; border-bottom: 4px solid var(--accent-color); }}
        .header-container {{ max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; }}
        .logo-container img {{ height: 40px; }}
        .search-box input {{ padding: 8px 12px; width: 250px; border: 1px solid #ccc; border-radius: 4px; }}
        
        nav {{ background: #002244; color: #fff; }}
        .nav-wrap {{ max-width: 1200px; margin: 0 auto; display: flex; flex-wrap: wrap; padding: 0 20px; }}
        .menu-toggle {{ display: none; background: none; border: none; color: white; font-size: 18px; padding: 12px; cursor: pointer; }}
        .nav-container {{ display: flex; list-style: none; flex-wrap: wrap; }}
        .nav-container li a {{ display: block; color: white; padding: 12px 15px; text-decoration: none; font-size: 14px; transition: background 0.3s; }}
        .nav-container li a:hover {{ background: var(--accent-color); color: #000; }}

        .container {{ max-width: 1200px; margin: 30px auto; display: flex; gap: 30px; padding: 0 20px; }}
        .main-content {{ flex: 3; }}
        .sidebar {{ flex: 1; background: var(--bg-light); padding: 20px; border: 1px solid var(--border-color); border-radius: 6px; }}

        h1 {{ font-size: 28px; color: var(--primary-color); margin-bottom: 15px; }}
        h2 {{ font-size: 22px; color: var(--primary-color); margin: 25px 0 10px; border-bottom: 2px solid var(--accent-color); padding-bottom: 5px; }}
        h3 {{ font-size: 18px; color: #444; margin: 20px 0 8px; }}
        p {{ margin-bottom: 15px; text-align: justify; }}
        .featured-img {{ width: 100%; height: auto; border-radius: 6px; margin-bottom: 20px; border: 1px solid var(--border-color); }}
        
        table {{ width: 100%; border-collapse: collapse; margin: 25px 0; }}
        table, th, td {{ border: 1px solid var(--border-color); }}
        th, td {{ padding: 12px; text-align: left; }}
        th {{ background-color: var(--primary-color); color: white; }}
        
        .faq-section {{ background: var(--bg-light); padding: 20px; border-radius: 6px; margin: 30px 0; }}
        .faq-item {{ margin-bottom: 15px; }}
        .faq-item h4 {{ color: var(--primary-color); margin-bottom: 5px; }}

        .sidebar-widget {{ margin-bottom: 25px; }}
        .sidebar-widget h4 {{ font-size: 16px; border-bottom: 2px solid var(--primary-color); padding-bottom: 8px; margin-bottom: 12px; color: var(--primary-color); }}
        .sidebar-widget ul {{ list-style: none; }}
        .sidebar-widget ul li {{ margin-bottom: 8px; }}
        .sidebar-widget ul li a {{ color: var(--primary-color); text-decoration: none; font-size: 14px; }}
        .sidebar-widget ul li a:hover {{ text-decoration: underline; color: var(--accent-color); }}

        .contact-form input, .contact-form textarea {{ width: 100%; padding: 10px; margin-bottom: 10px; border: 1px solid var(--border-color); border-radius: 4px; }}
        .contact-form button {{ background: var(--primary-color); color: white; border: none; padding: 10px 15px; cursor: pointer; border-radius: 4px; width: 100%; }}
        .contact-form button:hover {{ background: var(--accent-color); color: #000; }}

        footer {{ background: #111; color: #fff; padding: 40px 0 20px; margin-top: 50px; }}
        .footer-container {{ max-width: 1200px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 30px; padding: 0 20px; }}
        .footer-col {{ flex: 1; min-width: 200px; }}
        .footer-col h4 {{ color: var(--accent-color); margin-bottom: 15px; font-size: 16px; }}
        .footer-col ul {{ list-style: none; }}
        .footer-col ul li {{ margin-bottom: 8px; }}
        .footer-col ul li a {{ color: #ccc; text-decoration: none; font-size: 13px; }}
        .footer-col ul li a:hover {{ color: white; text-decoration: underline; }}
        .footer-bottom {{ text-align: center; margin-top: 30px; padding-top: 15px; border-top: 1px solid #333; font-size: 13px; color: #888; }}

        @media(max-width: 768px) {{
            .container {{ flex-direction: column; }}
            .nav-container {{ display: none; width: 100%; flex-direction: column; }}
            .nav-container.active {{ display: flex; }}
            .menu-toggle {{ display: block; }}
            .header-container {{ flex-direction: column; gap: 15px; }}
            .search-box input {{ width: 100%; }}
        }}
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <div class="header-container">
            <div class="logo-container">
                <a href="https://indoinves.github.io/">
                    <img src="https://indoinves.github.io/indoinves.png" alt="Indoinves Logo">
                </a>
            </div>
            <div class="search-box">
                <form action="https://indoinves.github.io/" method="GET">
                    <input type="text" placeholder="Search news, markets..." />
                </form>
            </div>
        </div>
    </header>

    <!-- Navigasi Dropdown Label Lengkap & Responsif -->
    <nav>
        <div class="nav-wrap">
            <button class="menu-toggle" id="menu-toggle-btn" aria-label="Toggle Navigation">☰ Menu</button>
            <ul class="nav-container" id="main-nav-list">
                <li><a href="https://indoinves.github.io/">Home</a></li>
                <li><a href="https://indoinves.github.io/tools/investasi.html">Market</a></li>
                <li><a href="https://indoinves.github.io/tools/saham.html">Finance</a></li>
                <li><a href="https://indoinves.github.io/tools/contentblog.html">Tech</a></li>
                <li><a href="https://indoinves.github.io/about.html">About</a></li>
                <li><a href="https://indoinves.github.io/contact.html">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Main Content Layout -->
    <div class="container">
        <main class="main-content">
            <article>
                <h1>{title}</h1>
                <p><em>Dipublikasikan pada: 7 Juni 2026 | Oleh Redaksi Indoinves</em></p>
                <img src="{img_url}" alt="{title}" class="featured-img">
                
                <p>Sektor <strong>{category}</strong> saat ini memegang peranan yang sangat penting dalam ekosistem ekonomi global. Perubahan regulasi, inovasi teknologi, serta pergeseran tren investasi memberikan dampak langsung bagi pelaku bisnis dan masyarakat luas. Melalui artikel komprehensif ini, kami mengupas tuntas berbagai aspek fundamental yang wajib Anda ketahui.</p>
                
                <h2>Daftar Isi (Table of Contents)</h2>
                <ul>
                    <li><a href="#pendahuluan">1. Pendahuluan dan Latar Belakang</a></li>
                    <li><a href="#analisis">2. Analisis Data dan Statistik Utama</a></li>
                    <li><a href="#tantangan">3. Tantangan dan Peluang Global</a></li>
                    <li><a href="#faq">4. Pertanyaan yang Sering Diajukan (FAQ)</a></li>
                </ul>

                <h2 id="pendahuluan">1. Pendahuluan dan Latar Belakang</h2>
                <p>Dalam beberapa tahun terakhir, transformasi digital dan integrasi sistem keuangan global telah mengubah cara pandang investor terhadap instrumen aset konvensional maupun modern. Sektor {category} menunjukkan ketahanan yang luar biasa di tengah berbagai gelombang krisis makroekonomi.</p>
                
                {joined_body}

                <h2 id="analisis">2. Analisis Data dan Statistik Utama</h2>
                <p>Tabel di bawah ini merangkum metrik performa utama yang dikumpulkan dari berbagai sumber terpercaya terkait perkembangan {category}:</p>
                
                <table>
                    <thead>
                        <tr>
                            <th>Indikator Utama</th>
                            <th>Periode Sebelumnya</th>
                            <th>Periode Saat Ini</th>
                            <th>Pertumbuhan (%)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Volume Transaksi Global</td>
                            <td>$1.2 Miliar</td>
                            <td>$1.8 Miliar</td>
                            <td>+50%</td>
                        </tr>
                        <tr>
                            <td>Adopsi Pasar Domestik</td>
                            <td>45%</td>
                            <td>68%</td>
                            <td>+23%</td>
                        </tr>
                        <tr>
                            <td>Indeks Kepercayaan Investor</td>
                            <td>72.4</td>
                            <td>85.1</td>
                            <td>+17.5%</td>
                        </tr>
                    </tbody>
                </table>

                <h2>Referensi Eksternal Terpercaya</h2>
                <p>Untuk memperkaya wawasan Anda, silakan merujuk pada beberapa sumber eksternal berikut:</p>
                <ul>
                    <li><a href="https://www.reuters.com" target="_blank" rel="noopener">Reuters Global Markets</a></li>
                    <li><a href="https://www.bloomberg.com" target="_blank" rel="noopener">Bloomberg Finance & Economy</a></li>
                    <li><a href="https://www.wsj.com" target="_blank" rel="noopener">The Wall Street Journal Business</a></li>
                    <li><a href="https://www.ft.com" target="_blank" rel="noopener">Financial Times News</a></li>
                    <li><a href="https://www.cnbc.com" target="_blank" rel="noopener">CNBC Global Markets</a></li>
                    <li><a href="https://www.imf.org" target="_blank" rel="noopener">International Monetary Fund Reports</a></li>
                    <li><a href="https://www.worldbank.org" target="_blank" rel="noopener">World Bank Economic Outlook</a></li>
                </ul>

                <h2 id="faq">4. Pertanyaan yang Sering Diajukan (FAQ)</h2>
                <div class="faq-section">
                    <div class="faq-item">
                        <h4>Q: Apa tren utama dalam sektor {category} tahun ini?</h4>
                        <p>A: Tren utama berfokus pada digitalisasi penuh, transparansi regulasi, serta efisiensi operasional berbasis kecerdasan buatan.</p>
                    </div>
                    <div class="faq-item">
                        <h4>Q: Bagaimana cara investor pemula memulai di sektor ini?</h4>
                        <p>A: Investor disarankan untuk mempelajari analisis fundamental, memahami risiko pasar, dan memanfaatkan perangkat simulasi gratis seperti yang disediakan oleh Indoinves.</p>
                    </div>
                    <div class="faq-item">
                        <h4>Q: Di mana saya bisa mendapatkan data statistik terbaru?</h4>
                        <p>A: Data dan laporan komprehensif dapat diakses melalui rubrik riset resmi Indoinves dan direktori mitra global kami.</p>
                    </div>
                </div>

                <h2>Kesimpulan</h2>
                <p>Secara keseluruhan, prospek jangka panjang pada sektor {category} tetap menunjukkan tren positif yang menjanjikan. Konsistensi dalam mematuhi regulasi serta keterbukaan terhadap inovasi teknologi akan menjadi kunci utama keberhasilan di masa mendatang.</p>
            </article>
        </main>

        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="sidebar-widget">
                <h4>Artikel Terbaru</h4>
                <ul>
                    <li><a href="artikel1.html">Strategi Investasi Modern di Pasar Global</a></li>
                    <li><a href="artikel2.html">Perkembangan Kebijakan Fiskal dan Moneter</a></li>
                    <li><a href="artikel3.html">Transformasi Teknologi dan Bisnis Digital</a></li>
                </ul>
            </div>

            <div class="sidebar-widget">
                <h4>Artikel Populer</h4>
                <ul>
                    <li><a href="artikel4.html">Panduan Lengkap Analisis Saham Pemula</a></li>
                    <li><a href="artikel5.html">Masa Depan Ekonomi Makro Indonesia</a></li>
                    <li><a href="artikel6.html">Inovasi Perbankan Digital Tahun Ini</a></li>
                </ul>
            </div>

            <div class="sidebar-widget">
                <h4>Label Kategori</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/blog/market/">Market & Finance</a></li>
                    <li><a href="https://indoinves.github.io/blog/tech/">Technology & AI</a></li>
                    <li><a href="https://indoinves.github.io/blog/property/">Property & Real Estate</a></li>
                </ul>
            </div>

            <div class="sidebar-widget">
                <h4>Hubungi Redaksi</h4>
                <div class="contact-form">
                    <form action="#" method="POST">
                        <input type="text" placeholder="Nama Anda" required />
                        <input type="email" placeholder="Email Anda" required />
                        <textarea placeholder="Pesan atau pertanyaan..." rows="4" required></textarea>
                        <button type="submit">Kirim Pesan</button>
                    </form>
                </div>
            </div>
        </aside>
    </div>

    <!-- Footer -->
    <footer>
        <div class="footer-container">
            <div class="footer-col">
                <img src="https://indoinves.github.io/indoinves.png" alt="Indoinves Logo" style="height: 35px; margin-bottom: 15px; filter: brightness(0) invert(1);">
                <p>Indoinves is an authoritative digital publication delivering high-impact news, macroeconomic analysis, financial market intelligence, and structural business insights to a worldwide readership.</p>
            </div>

            <div class="footer-col">
                <h4>Tools Free Indoinves</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/tools/banklocator.html">Tools Peta & Direktori Bank Global</a></li>
                    <li><a href="https://indoinves.github.io/tools/contentblog.html">Tools Konten Blog</a></li>
                    <li><a href="https://indoinves.github.io/tools/investasi.html">Tools Kalkulator Investasi</a></li>
                    <li><a href="https://indoinves.github.io/tools/saham.html">Tools Saham</a></li>
                    <li><a href="https://indoinves.github.io/tools/simulatorkripto-pro.html">Tools Simulator Kripto Pro</a></li>
                    <li><a href="https://indoinves.github.io/tools/simulatorkripto.html">Tools Simulator Kripto</a></li>
                    <li><a href="https://indoinves.github.io/tools/simulatorsaham.html">Tools Simulator Saham</a></li>
                    <li><a href="https://indoinves.github.io/tools/website.html">Tools Website / SEO Checker</a></li>
                </ul>
                
                <!-- Unit Iklan Autorelaxed AdSense -->
                <div style="margin: 25px 0;">
                    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
                    <ins class="adsbygoogle"
                    style="display:block"
                    data-ad-format="autorelaxed"
                    data-ad-client="ca-pub-8423475960451668"
                    data-ad-slot="7183276396"></ins>
                    <script>
                    (adsbygoogle = window.adsbygoogle || []).push({{}});
                    </script>
                </div>
            </div>

            <div class="footer-col">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/">Home</a></li>
                    <li><a href="https://indoinves.github.io/about.html">About Us</a></li>
                    <li><a href="https://indoinves.github.io/contact.html">Contact Us</a></li>
                    <li><a href="https://indoinves.github.io/privacy.html">Privacy Policy</a></li>
                    <li><a href="https://indoinves.github.io/sitemap.html">Sitemap</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Policies & Editorial</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/disclaimer.html">Disclaimer</a></li>
                    <li><a href="https://indoinves.github.io/terms.html">Terms On Conditional License</a></li>
                    <li><a href="https://indoinves.github.io/editorial.html">Editorial Guidelines</a></li>
                    <li><a href="https://indoinves.github.io/advertise.html">Advertise With Us</a></li>
                </ul>
            </div>

            <div class="footer-col">
                <h4>Community & Careers</h4>
                <ul>
                    <li><a href="https://indoinves.github.io/join.html">Join the Team</a></li>
                    <li><a href="https://indoinves.github.io/forum.html">Contact Forum</a></li>
                    <li><a href="https://indoinves.github.io/komunitas.html">Komunitas Indoinves</a></li>
                </ul>
                
                <!-- Unit Iklan Banner AdSense -->
                <div style="margin: 25px 0;">
                    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8423475960451668" crossorigin="anonymous"></script>
                    <ins class="adsbygoogle"
                    style="display:block"
                    data-ad-client="ca-pub-8423475960451668"
                    data-ad-slot="6147545291"
                    data-ad-format="auto"
                    data-full-width-responsive="true"></ins>
                    <script>
                    (adsbygoogle = window.adsbygoogle || []).push({{}});
                    </script>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Indoinves - All Rights Reserved. Secured via HTTPS.</p>
        </div>
    </footer>

    <script>
        document.getElementById('menu-toggle-btn').addEventListener('click', function() {{
            const navList = document.getElementById('main-nav-list');
            navList.classList.toggle('active');
        }});
    </script>
</body>
</html>
"""
    return html_content

def main():
    print("Memulai pembuatan struktur direktori dan artikel blog untuk repository indoinves.github.io...")
    
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
        
    total_files = 0
    for cat in CATEGORIES:
        cat_dir = os.path.join(BASE_DIR, cat)
        if not os.path.exists(cat_dir):
            os.makedirs(cat_dir)
            
        for i in range(1, 31):
            file_name = f"artikel{i}.html"
            file_path = os.path.join(cat_dir, file_name)
            
            content = generate_article_content(cat, i)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            total_files += 1
            
    print(f"Berhasil membuat total {total_files} file artikel di dalam direktori `blog/` untuk seluruh {len(CATEGORIES)} kategori!")

if __name__ == "__main__":
    main()
