import os
import json
from datetime import datetime

# Daftar semua kategori / direktori yang diminta
CATEGORIES = [
    "biografi-ulama", "kisah-hikmah", "kisah-sejarah", "info", "kisah-birrul-walidain",
    "kisah-hidayah-islam", "kisah-kaum-durhaka", "kisah-masa-depan", "kisah-nabi-dan-rasul",
    "kisah-nabi-muhammad", "kisah-nyata", "kisah-orang-shalih", "kisah-pilihan",
    "kisah-sahabat-nabi", "kisah-tabiin", "kisah-tak-nyata", "kisah-umat-terdahulu",
    "sejarah-islam", "nusantara", "news", "laporan-produksi", "merchandise-yufid",
    "mutiara-faidah", "sejarah", "teladan-muslimah", "books", "aplikasi", "download",
    "market-finance", "macro-economy", "explainers", "manufacturing", "property",
    "health", "education", "lifestyle", "hospitality", "tech-media", "smes", "luxury",
    "whos-who", "international", "local-resources", "politics", "culture", "science",
    "public-policy", "business-news", "sports", "arts", "celebrities", "automotive",
    "commentary", "interview", "fiqih-4-mazhab", "kamus-pintar-irob", "kamus-tashrif",
    "simulator-waris-faraid", "simulator-hitung-zakat", "asisten-kesehatan-mental",
    "mesin-pencari-hadits", "penyederhana-teks-arab", "perencana-haji-umrah",
    "browser-modesti-digital", "mesin-logika-komparatif", "peta-sejarah-islam-ar",
    "perpustakaan-digital-islam", "alat-personalisasi-dakwah", "verifikator-fakta-islam",
    "jurnal-iman-analisis", "penasihat-parenting-islam", "pelatih-kebiasaan-spiritual",
    "auditor-kepatuhan-syariah", "islamic-tools", "qibla-direction", "prayer-times",
    "hijri-calendar", "zakat-calculator", "salah-tracker", "mosque-finder",
    "worship", "trackers", "calculators", "knowledge", "finders", "quran",
    "duas", "halal-food", "timer", "calendar", "cuaca"
]

DOMAIN = "https://alhikmah.my.id"
LOGO_URL = "https://blogger.googleusercontent.com/img/a/AVvXsEiW2Sfw5ogSKhZbFiB-VdNXwmZoMGLTGPgx5ZYrTY8859clBvRGxgx-Dwc3i03YiUs1WiiL84uTSAlZ8civ17IWTI5Emt2vXmpuT-yRTzf4620rY_4Ib_vmUEGFfLXjzMiCfmQoWUg1mmj5hQu1IpD1CYguF9GocJ81MhsQTuPgt79-I8uOaPyGT0Qzs00=s200"
DEFAULT_IMAGE = f"{DOMAIN}/images.jpg"

def generate_html(category, post_num):
    title = f"Panduan Lengkap & Kajian Mendalam {category.replace('-', ' ').title()} - Bagian {post_num}"
    canonical_url = f"{DOMAIN}/{category}/post{post_num}.html"
    
    html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Alhikmah.my.id</title>
    
    <!-- Favicon & Canonical -->
    <link rel="icon" type="image/png" href="{LOGO_URL}">
    <link rel="canonical" href="{canonical_url}" />
    
    <!-- Meta SEO & Verification -->
    <meta content='QT96Rd0InOuqkb4s1Wu5BlgGD_pCNOy8CsCtveF1zEA' name='google-site-verification'/>
    <meta content='Alhikmah.my.id adalah situs Islam yang menyajikan informasi terkini tentang pendidikan, sejarah, budaya, sosial, serta tokoh-tokoh penting dalam kehidupan masyarakat dan bernegara.' name='description'/>
    <meta content='Islam, Pendidikan, Sejarah, Sosial, Budaya, Tokoh Islam, Kehidupan Masyarakat, Bernegara, Islam Terpercaya, {category}' name='keywords'/>
    <meta content='Alhikmah.my.id' name='author'/>
    <meta content='Alhikmah.my.id' name='copyright'/>

    <!-- Google AdSense -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6718454554209533" crossorigin="anonymous"></script>
    <meta content='ca-pub-6718454554209533' name='google-adsense-account'/>
    <script async custom-element='amp-ad' src='https://cdn.ampproject.org/v0/amp-ad-0.1.js'></script>

    <!-- Open Graph / Social Media Meta -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="Kajian komprehensif seputar {category.replace('-', ' ')} bersumber dari literatur terpercaya.">
    <meta property="og:image" content="{DEFAULT_IMAGE}">
    <meta property="og:image:secure_url" content="{DEFAULT_IMAGE}">
    <meta property="og:image:type" content="image/jpeg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="{canonical_url}">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:image" content="{DEFAULT_IMAGE}">

    <!-- Stylesheets -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">

    <!-- Structured Data JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "NewsArticle",
      "headline": "{title}",
      "image": ["{DEFAULT_IMAGE}"],
      "datePublished": "{datetime.now().strftime('%Y-%m-%dT%H:%M:%S+07:00')}",
      "dateModified": "{datetime.now().strftime('%Y-%m-%dT%H:%M:%S+07:00')}",
      "author": {{
        "@type": "Organization",
        "name": "Alhikmah"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Alhikmah",
        "logo": {{
          "@type": "ImageObject",
          "url": "{LOGO_URL}"
        }}
      }}
    }}
    </script>
    <style>
        body {{ background-color: #f8f9fa; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
        .navbar {{ background-color: #111; }}
        .rainbow-text {{ background: linear-gradient(45deg, #0d6efd, #198754, #ffc107); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold; }}
        .share-trigger-btn {{ position: fixed; bottom: 20px; right: 20px; z-index: 1050; background: #198754; color: white; border: none; padding: 10px 20px; border-radius: 50px; box-shadow: 0 4px 10px rgba(0,0,0,0.3); display: flex; align-items: center; gap: 8px; cursor: pointer; }}
        .share-modal-overlay {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1060; display: flex; align-items: center; justify-content: center; }}
        .share-modal-content {{ background: white; padding: 25px; border-radius: 12px; width: 90%; max-width: 400px; }}
        .share-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 15px; }}
        .share-item {{ padding: 10px; text-align: center; border-radius: 6px; color: white; text-decoration: none; border: none; cursor: pointer; font-weight: 500; }}
        .share-item.wa {{ background: #25d366; }}
        .share-item.fb {{ background: #1877f2; }}
        .share-item.x {{ background: #000; }}
        .share-item.tg {{ background: #0088cc; }}
        .share-item.copy {{ background: #6c757d; grid-column: span 2; }}
    </style>
</head>
<body>

    <!-- Header & Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark fixed-top shadow-sm">
         <div class="container">
             <a class="navbar-brand d-flex align-items-center" href="{DOMAIN}/">
                 <img src="{LOGO_URL}" alt="alhikmah" width="38" height="38" class="me-2 animate__animated animate__pulse animate__infinite">
                 <span class="rainbow-text fs-4">ALHIKMAH.MY.ID</span>
             </a>
             <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                 <span class="navbar-toggler-icon"></span>
             </button>
             <div class="collapse navbar-collapse" id="navbarNav">
                 <ul class="navbar-nav ms-auto">
                     <li class="nav-item"><a class="nav-link active" href="{DOMAIN}/">Beranda</a></li>
                     <li class="nav-item dropdown">
                         <a class="nav-link dropdown-toggle text-white" href="#" role="button" data-bs-toggle="dropdown">Kategori Pilihan</a>
                         <ul class="dropdown-menu">
                             <li><a class="dropdown-item" href="{DOMAIN}/sejarah-islam/">Sejarah Islam</a></li>
                             <li><a class="dropdown-item" href="{DOMAIN}/biografi-ulama/">Biografi Ulama</a></li>
                             <li><a class="dropdown-item" href="{DOMAIN}/islamic-tools/">Islamic Tools</a></li>
                         </ul>
                     </li>
                 </ul>
             </div>
         </div>
    </nav>

    <!-- Main Content Container -->
    <main class="container my-5 pt-5">
        <div class="row">
            <!-- Article Body -->
            <div class="col-lg-8">
                <article class="bg-white p-4 p-md-5 rounded shadow-sm">
                    <!-- Breadcrumb -->
                    <nav aria-label="breadcrumb">
                      <ol class="breadcrumb">
                        <li class="breadcrumb-item"><a href="{DOMAIN}/">Home</a></li>
                        <li class="breadcrumb-item"><a href="{DOMAIN}/{category}/">{category.replace('-', ' ').title()}</a></li>
                        <li class="breadcrumb-item active" aria-current="page">Post {post_num}</li>
                      </ol>
                    </nav>

                    <h1 class="fw-bold mb-3 text-dark">{title}</h1>
                    <div class="text-muted small mb-4">Dipublikasikan oleh Redaksi Alhikmah | Kategori: {category.replace('-', ' ').title()}</div>
                    
                    <!-- Cover Image -->
                    <div class="mb-4 text-center">
                        <img src="{DEFAULT_IMAGE}" alt="Ilustrasi {title}" class="img-fluid rounded shadow-sm w-100" style="max-height: 450px; object-fit: cover;">
                    </div>

                    <!-- Table of Contents -->
                    <div class="card bg-light border-0 p-3 mb-4">
                        <h5 class="fw-bold text-success mb-2"><i class="bi bi-list-nested"></i> Daftar Isi</h5>
                        <ul class="mb-0 ps-3">
                            <li><a href="#pendahuluan" class="text-decoration-none">1. Pendahuluan & Latar Belakang</a></li>
                            <li><a href="#pembahasan" class="text-decoration-none">2. Pembahasan Utama & Analisis Komprehensif</a></li>
                            <li><a href="#implikasi" class="text-decoration-none">3. Implikasi & Nilai Teladan Modern</a></li>
                            <li><a href="#faq" class="text-decoration-none">4. Pertanyaan yang Sering Diajukan (FAQ)</a></li>
                            <li><a href="#kesimpulan" class="text-decoration-none">5. Kesimpulan</a></li>
                        </ul>
                    </div>

                    <!-- Article Content Sections (Simulated 3000 words structured SEO depth) -->
                    <section id="pendahuluan">
                        <h2>1. Pendahuluan & Latar Belakang</h2>
                        <p>Kajian mendalam mengenai {category.replace('-', ' ')} memberikan pencerahan penting bagi umat Islam dalam menjalani kehidupan beragama, bermasyarakat, dan bernegara. Dalam konteks modern, pemahaman yang komprehensif menjadi mercusuar moral yang membimbing generasi muda dari disorientasi nilai.</p>
                        <p>Mengacu pada rujukan para ulama salafus shalih, pembahasan ini dirancang untuk menjawab berbagai tantangan kontemporer dengan tetap berpegang teguh pada prinsip-prinsip syariat yang lurus.</p>
                    </section>

                    <section id="pembahasan" class="my-4">
                        <h2>2. Pembahasan Utama & Analisis Komprehensif</h2>
                        <h3>Aspek Historis dan Normatif</h3>
                        <p>Eksplorasi literatur klasik dan kontemporer menunjukkan betapa pentingnya kedisiplinan keilmuan. Dalam dinamika dakwah, pendekatan yang bijak dan kontekstual senantiasa dikedepankan agar pesan-pesan kebaikan dapat diterima dengan lapang dada oleh berbagai kalangan masyarakat.</p>
                        
                        <h4>Dimensi Sosiologis</h4>
                        <p>Penerapan nilai-nilai keislaman di tengah masyarakat majemuk menuntut kearifan lokal yang tidak bertentangan dengan prinsip ushul. Keterlibatan aktif para tokoh dan cendekiawan muslim terbukti mampu merawat kerukunan umat beragama.</p>

                        <h5>Tantangan di Era Digital</h5>
                        <p>Arus informasi tanpa batas menuntut literasi digital keagamaan yang mumpuni. Umat harus selektif menyerap informasi, merujuk langsung pada sumber-sumber otentik yang terverifikasi.</p>

                        <h6>Strategi Solutif</h6>
                        <p>Melalui pemanfaatan teknologi digital islami, penyebaran risalah damai kini dapat diakses kapan saja dan di mana saja secara transparan.</p>
                    </section>

                    <!-- AdSense Mid-Article -->
                    <div class="my-4 text-center">
                        <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6718454554209533" crossorigin="anonymous"></script>
                        <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-6718454554209533" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
                        <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
                    </div>

                    <section id="implikasi">
                        <h2>3. Implikasi & Nilai Teladan Modern</h2>
                        <p>Pewarisan nilai luhur tidak hanya berhenti pada tataran teori, melainkan harus diwujudkan dalam aksi nyata sehari-hari. Teladan para pendahulu memberikan kerangka kerja moral yang kokoh bagi profesional, akademisi, maupun masyarakat umum.</p>
                    </section>

                    <!-- Artikel Terkait & Navigasi Antar Artikel -->
                    <div class="card border-success my-5 p-4">
                        <h4 class="fw-bold mb-3"><i class="bi bi-book"></i> Artikel Terkait & Navigasi</h4>
                        <ul class="list-unstyled mb-4">
                            <li><a href="{DOMAIN}/sejarah-islam/post1.html" class="text-decoration-none">👉 Menelusuri Jejak Peradaban Islam Klasik di Nusantara</a></li>
                            <li><a href="{DOMAIN}/biografi-ulama/post2.html" class="text-decoration-none">👉 Biografi Tokoh Ulama Kharismatik Abad Pertengahan</a></li>
                            <li><a href="{DOMAIN}/islamic-tools/post3.html" class="text-decoration-none">👉 Panduan Menggunakan Fitur Digital Islam Interaktif</a></li>
                            <li><a href="{DOMAIN}/kisah-hikmah/post4.html" class="text-decoration-none">👉 Mutiara Hikmah Penyegar Jiwa dan Penenang Hati</a></li>
                            <li><a href="{DOMAIN}/news/post5.html" class="text-decoration-none">👉 Update Berita dan Informasi Dunia Islam Terkini</a></li>
                            <li><a href="{DOMAIN}/education/post6.html" class="text-decoration-none">👉 Transformasi Sistem Pendidikan Pesantren Modern</a></li>
                            <li><a href="{DOMAIN}/culture/post7.html" class="text-decoration-none">👉 Pelestarian Budaya Nusantara Berbasis Nilai Islam</a></li>
                        </ul>

                        <!-- Eksternal Links (7 Links) -->
                        <h5 class="fw-bold mb-2 text-secondary">Referensi Eksternal</h5>
                        <ul class="list-unstyled small text-muted mb-4">
                            <li><a href="https://quran.com" target="_blank" rel="nofollow">1. Quran.com - Mushaf Al-Qur'an Digital Global</a></li>
                            <li><a href="https://sunnah.com" target="_blank" rel="nofollow">2. Sunnah.com - Ensiklopedia Hadits Shahih</a></li>
                            <li><a href="https://mui.or.id" target="_blank" rel="nofollow">3. Majelis Ulama Indonesia - Fatwa dan Kebijakan Umat</a></li>
                            <li><a href="https://kemenag.go.id" target="_blank" rel="nofollow">4. Kementerian Agama Republik Indonesia</a></li>
                            <li><a href="https://wikipedia.org" target="_blank" rel="nofollow">5. Wikipedia - Ensiklopedia Bebas Terpercaya</a></li>
                            <li><a href="https://archive.org" target="_blank" rel="nofollow">6. Internet Archive - Khazanah Pustaka Dunia</a></li>
                            <li><a href="https://scholar.google.com" target="_blank" rel="nofollow">7. Google Scholar - Jurnal dan Literatur Ilmiah</a></li>
                        </ul>

                        <div class="d-flex justify-content-between">
                            <a href="{DOMAIN}/{category}/post{max(1, post_num-1)}.html" class="btn btn-outline-success"><i class="bi bi-arrow-left"></i> Artikel Sebelumnya</a>
                            <a href="{DOMAIN}/{category}/post{post_num+1}.html" class="btn btn-success">Artikel Selanjutnya <i class="bi bi-arrow-right"></i></a>
                        </div>
                    </div>

                    <section id="faq" class="my-4">
                        <h2>4. Pertanyaan yang Sering Diajukan (FAQ)</h2>
                        <div class="accordion" id="faqAccordion">
                            <div class="accordion-item">
                                <h2 class="accordion-header" id="headingOne">
                                    <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne">
                                        Bagaimana cara mengaplikasikan nilai-nilai dalam artikel ini?
                                    </button>
                                </h2>
                                <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#faqAccordion">
                                    <div class="accordion-body">
                                        Penerapan dapat dimulai dari lingkungan terdekat seperti keluarga, instansi, dan masyarakat luas dengan mengedepankan prinsip moderasi beragama.
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <section id="kesimpulan" class="mt-4">
                        <h2>5. Kesimpulan</h2>
                        <p>Melalui pemahaman yang utuh terhadap {category.replace('-', ' ')}, kita dapat membangun peradaban yang harmonis, bermartabat, dan senantiasa mendapat ridha Allah SWT. Semoga artikel ini bermanfaat bagi seluruh pembaca.</p>
                    </section>
                </article>
            </div>

            <!-- Sidebar -->
            <div class="col-lg-4 mt-4 mt-lg-0">
                <!-- Navigation & Features Widget -->
                <div class="card border-0 shadow-sm p-3 mb-4">
                    <h5 class="fw-bold mb-3"><span class="rainbow-text">🧭 Navigasi & Fitur Utama</span></h5>
                    <ul class="list-unstyled small" style="line-height: 1.8;">
                        <li>✍️ <a href="{DOMAIN}/arabic/pesantren/nd/" class="text-decoration-none">Arabic Pegon</a></li>
                        <li>✒️ <a href="{DOMAIN}/arabic/calligraphy/pro" class="text-decoration-none">Arabic Calligraphy Pro</a></li>
                        <li>📅 <a href="{DOMAIN}/kalender/" class="text-decoration-none">Kalender Multi-Konversi</a></li>
                        <li>⏱️ <a href="{DOMAIN}/jadwal-sholat/" class="text-decoration-none">Timer Jadwal Sholat</a></li>
                        <li>🎧 <a href="{DOMAIN}/alquran-player/v6.html" class="text-decoration-none">Murotal 30 Juz</a></li>
                        <li>📖 <a href="{DOMAIN}/alquran-player/" class="text-decoration-none">Alqur'an Digital</a></li>
                        <li>💼 <a href="{DOMAIN}/WebOffice/" class="text-decoration-none">WebOffice Suite</a></li>
                        <li>📚 <a href="{DOMAIN}/khazanah/" class="text-decoration-none">Khazanah Kitab & Teks</a></li>
                    </ul>
                </div>

                <!-- Popular Articles & Archive -->
                <div class="card border-0 shadow-sm p-3 mb-4">
                    <h5 class="fw-bold mb-3">🔥 Artikel Populer</h5>
                    <ul class="list-unstyled small mb-0">
                        <li class="mb-2"><a href="{DOMAIN}/sejarah-islam/post1.html" class="text-decoration-none text-dark">Sejarah Masuknya Islam di Nusantara</a></li>
                        <li class="mb-2"><a href="{DOMAIN}/biografi-ulama/post1.html" class="text-decoration-none text-dark">Kisah Teladan Imam Madzhab Syafi'i</a></li>
                        <li class="mb-2"><a href="{DOMAIN}/islamic-tools/post1.html" class="text-decoration-none text-dark">Aplikasi Penghitung Zakat Harta Otomatis</a></li>
                    </ul>
                </div>

                <!-- Contact Form Widget -->
                <div class="card border-0 shadow-sm p-3">
                    <h5 class="fw-bold mb-3">📬 Hubungi Kami</h5>
                    <form>
                        <div class="mb-2">
                            <input type="text" class="form-control form-control-sm" placeholder="Nama Anda" required>
                        </div>
                        <div class="mb-2">
                            <input type="email" class="form-control form-control-sm" placeholder="Email Anda" required>
                        </div>
                        <div class="mb-2">
                            <textarea class="form-control form-control-sm" rows="3" placeholder="Pesan..." required></textarea>
                        </div>
                        <button type="submit" class="btn btn-success btn-sm w-100">Kirim Pesan</button>
                    </form>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="py-5 bg-black text-white mt-5">
        <div class="container">
            <div class="row align-items-center g-4">
                <div class="col-md-5 text-center text-md-start">
                    <a class="d-inline-flex align-items-center text-decoration-none mb-2" href="{DOMAIN}/">
                        <span class="rainbow-text fs-5">ALHIKMAH.MY.ID</span>
                    </a>
                    <p class="text-muted small mb-0">Portal Islam terpercaya untuk pendidikan, sejarah, sosial, dan budaya. Dikelola sinergis oleh Kang Santri & awgroupchannel.</p>
                </div>
                <div class="col-md-7">
                    <h6 class="text-white fw-bold mb-3 text-md-end">Navigasi Halaman Dokumen Resmi:</h6>
                    <div class="d-flex flex-wrap justify-content-md-end gap-3 justify-content-center" style="font-size: 0.9rem;">
                        <a class="text-light text-decoration-none" href="{DOMAIN}/about-us.html" target="_blank">About Us</a>
                        <span class="text-muted">|</span>
                        <a class="text-light text-decoration-none" href="{DOMAIN}/kontak.html">Kontak Kami</a>
                        <span class="text-muted">|</span>
                        <a class="text-light text-decoration-none" href="{DOMAIN}/privacy.html" target="_blank">Privacy Policy</a>
                        <span class="text-muted">|</span>
                        <a class="text-light text-decoration-none" href="{DOMAIN}/disclaimers.html" target="_blank">Disclaimers</a>
                        <span class="text-muted">|</span>
                        <a class="text-light text-decoration-none" href="{DOMAIN}/sitemap.xml" target="_blank">Sitemap</a>
                        <span class="text-muted">|</span>
                        <a class="text-light text-decoration-none" href="{DOMAIN}/terms.html" target="_blank">Terms & Conditions</a>
                    </div>
                </div>
            </div>
            <hr class="border-secondary border-opacity-25 my-4">
            <div class="text-center text-muted small">
                &copy; 2026 ALHIKMAH.MY.ID. All Rights Reserved. Powered by awgroupchannel.
            </div>
        </div>
    </footer>

    <!-- Floating Share Button -->
    <button class="share-trigger-btn" onclick="toggleShareModal()">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"></path><polyline points="16 6 12 2 8 6"></polyline><line x1="12" y1="2" x2="12" y2="15"></line></svg>
        <span>Bagikan</span>
    </button>

    <!-- Share Modal -->
    <div id="shareModal" class="share-modal-overlay" style="display: none;">
        <div class="share-modal-content">
            <div class="d-flex justify-content-between align-items-center mb-3">
                <h3 class="fs-5 fw-bold mb-0">Bagikan Halaman Ini</h3>
                <button class="btn-close" onclick="toggleShareModal()"></button>
            </div>
            <div class="share-grid">
                <a href="https://api.whatsapp.com/send?text={title}%20{canonical_url}" target="_blank" class="share-item wa">WhatsApp</a>
                <a href="https://www.facebook.com/sharer/sharer.php?u={canonical_url}" target="_blank" class="share-item fb">Facebook</a>
                <a href="https://twitter.com/intent/tweet?url={canonical_url}&text={title}" target="_blank" class="share-item x">Twitter / X</a>
                <a href="https://t.me/share/url?url={canonical_url}&text={title}" target="_blank" class="share-item tg">Telegram</a>
                <button onclick="navigator.clipboard.writeText('{canonical_url}');alert('Link disalin!');" class="share-item copy">Salin Link</button>
            </div>
        </div>
    </div>

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
    <script>
        function toggleShareModal() {{
            const modal = document.getElementById('shareModal');
            modal.style.display = modal.style.display === 'none' ? 'flex' : 'none';
        }}
    </script>
</body>
</html>
"""
    return html_content

def main():
    print("🚀 Memulai proses pembuatan struktur direktori dan artikel...")
    
    sitemap_urls = [f"{DOMAIN}/"]
    
    for cat in CATEGORIES:
        cat_dir = os.path.join("public", cat)
        os.makedirs(cat_dir, exist_ok=True)
        
        for i in range(1, 31): # 30 file per direktori
            filename = f"post{i}.html"
            filepath = os.path.join(cat_dir, filename)
            
            html_code = generate_html(cat, i)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html_code)
                
            sitemap_urls.append(f"{DOMAIN}/{cat}/{filename}")
        print(f"✅ Sukses membuat 30 artikel di direktori: /{cat}/")

    # Membuat Manifest JSON
    manifest_data = {
        "name": "Alhikmah.my.id Portal Islam",
        "short_name": "Alhikmah",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#198754",
        "icons": [{
            "src": LOGO_URL,
            "sizes": "200x200",
            "type": "image/png"
        }]
    }
    with open(os.path.join("public", "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=4)

    # Membuat Sitemap XML Otomatis
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in sitemap_urls:
        sitemap_xml += f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n"
    sitemap_xml += '</urlset>'
    
    with open(os.path.join("public", "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_xml)

    # Membuat Robots.txt
    robots_txt = f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n"
    with open(os.path.join("public", "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_txt)

    print("\n🎉 SELAMAT! Seluruh direktori, artikel, sitemap.xml, manifest.json, dan robots.txt berhasil digenerate di folder 'public'.")

if __name__ == "__main__":
    main()
