import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


mountains = [
    {
        "name": "Gunung Merapi",
        "height": "2.930 mdpl",
        "location": "Jawa Tengah",
        "description": "Gunung Merapi adalah gunung berapi aktif yang terletak di perbatasan Jawa Tengah dan Yogyakarta.",
        "routes": [
            {"name": "Jalur Selo", "price": "Rp 15.000", "duration": "6-8 jam"},
            {"name": "Jalur Kaliurang", "price": "Rp 20.000", "duration": "5-7 jam"},
            {"name": "Jalur Babadan", "price": "Rp 15.000", "duration": "5-7 jam"},
            {"name": "Jalur Kinahrejo", "price": "Rp 15.000", "duration": "6-7 jam"}
        ]
    },
    {
        "name": "Gunung Semeru",
        "height": "3.676 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Semeru adalah gunung tertinggi di Pulau Jawa dan terkenal dengan keindahan puncak Mahameru.",
        "routes": [
            {"name": "Jalur Ranu Pane", "price": "Rp 20.000", "duration": "10-12 jam"},
            {"name": "Jalur Watu Rejeng", "price": "Rp 19.000", "duration": "11-12 jam"}
        ]
    },
    {
        "name": "Gunung Sindoro",
        "height": "3.153 mdpl",
        "location": "Jawa Tengah",
        "description": "Gunung Sindoro adalah gunung berapi yang terletak di sebelah barat Gunung Sumbing.",
        "routes": [
            {"name": "Jalur Kledung", "price": "Rp 30.000", "duration": "7-9 jam"},
            {"name": "Jalur Ndoro Arum", "price": "Rp 30.000", "duration": "6-7 jam"},
            {"name": "Jalur Bansari", "price": "Rp 30.000", "duration": "7-8 jam"},
            {"name": "Jalur Bedakah", "price": "Rp 30.000", "duration": "7-9 jam"},
            {"name": "Jalur Sigedang", "price": "Rp 30.000", "duration": "5-7 jam"},
            {"name": "Jalur Alang-alang", "price": "Rp 30.000", "duration": "8-10 jam"},
        ]
    },
    {
        "name": "Gunung Sumbing",
        "height": "3.371 mdpl",
        "location": "Jawa Tengah",
        "description": "Gunung Sumbing adalah gunung berapi yang terletak di Jawa Tengah, sebelah barat Gunung Sindoro.",
        "routes": [
            {"name": "Jalur Garung", "price": "Rp 15.000", "duration": "7-9 jam"}
        ]
    },
    {
        "name": "Gunung Telomoyo",
        "height": "1.894 mdpl",
        "location": "Jawa Tengah",
        "description": "Gunung Telomoyo adalah gunung berapi yang terletak di antara Kabupaten Magelang dan Kabupaten Semarang.",
        "routes": [
            {"name": "Jalur Kopeng", "price": "Rp 10.000", "duration": "4-6 jam"}
        ]
    },
    {
        "name": "Gunung Ayamayam",
        "height": "1.022 mdpl",
        "location": "Jawa Tengah",
        "description": "Gunung Ayamayam adalah sebuah gunung yang terletak di Jawa Tengah.",
        "routes": [
            {"name": "Jalur Ayamayam", "price": "Rp 5.000", "duration": "2-3 jam"}
        ]
    },
    {
        "name": "Gunung Bismo",
        "height": "2.365 mdpl",
        "location": "Jawa Tengah",
        "description": "Gunung Bismo adalah gunung yang terletak di Jawa Tengah.",
        "routes": [
            {"name": "Jalur Dieng", "price": "Rp 10.000", "duration": "6-8 jam"}
        ]
    },
    {
        "name": "Gunung Lawu",
        "height": "3.265 mdpl",
        "location": "Jawa Tengah",
        "description": "Gunung Lawu adalah gunung berapi yang terletak di perbatasan Jawa Tengah dan Jawa Timur.",
        "routes": [
            {"name": "Jalur Cemoro Sewu", "price": "Rp 15.000", "duration": "7-9 jam"},
            {"name": "Jalur Cemoro Kandang", "price": "Rp 15.000", "duration": "7-9 jam"}
        ]
    },
    {
        "name": "Gunung Blego",
        "height": "1.022 mdpl",
        "location": "Jawa Tengah",
        "description": "Gunung Blego adalah sebuah gunung yang terletak di Jawa Tengah.",
        "routes": [
            {"name": "Jalur Blego", "price": "Rp 5.000", "duration": "2-3 jam"}
        ]
    },
    {
        "name": "Gunung Lasem",
        "height": "1.022 mdpl",
        "location": "Jawa Tengah",
        "description": "Gunung Lasem adalah sebuah gunung yang terletak di Jawa Tengah.",
        "routes": [
            {"name": "Jalur Lasem", "price": "Rp 5.000", "duration": "2-3 jam"}
        ]
    },
    {
        "name": "Gunung Tidar",
        "height": "503 mdpl",
        "location": "Jawa Tengah",
        "description": "Gunung Tidar adalah sebuah gunung yang terletak di Magelang, Jawa Tengah.",
        "routes": [
            {"name": "Jalur Tidar", "price": "Rp 2.000", "duration": "1-2 jam"}
        ]
    },
    {
        "name": "Gunung Ungaran",
        "height": "2.050 mdpl",
        "location": "Jawa Tengah",
        "description": "Gunung Ungaran adalah gunung berapi yang terletak di Kabupaten Semarang, Jawa Tengah.",
        "routes": [
            {"name": "Jalur Gedong Songo", "price": "Rp 10.000", "duration": "5-7 jam"}
        ]
    },
    {
        "name": "Gunung Lawu",
        "height": "3.265 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Lawu adalah gunung berapi yang terletak di perbatasan Jawa Tengah dan Jawa Timur.",
        "routes": [
            {"name": "Jalur Cemoro Sewu", "price": "Rp 15.000", "duration": "7-9 jam"},
            {"name": "Jalur Cemoro Kandang", "price": "Rp 15.000", "duration": "7-9 jam"}
        ]
    },
    {
        "name": "Gunung Bromo",
        "height": "2.329 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Bromo adalah gunung berapi yang terletak di Jawa Timur, terkenal dengan keindahan matahari terbitnya.",
        "routes": [
            {"name": "Jalur Cemoro Lawang", "price": "Rp 25.000", "duration": "3-4 jam"}
        ]
    },
    {
        "name": "Gunung Panderman",
        "height": "2.045 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Panderman adalah gunung yang terletak di dekat Kota Batu, Jawa Timur.",
        "routes": [
            {"name": "Jalur Batu", "price": "Rp 10.000", "duration": "4-5 jam"}
        ]
    },
    {
        "name": "Gunung Kawi",
        "height": "2.551 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Kawi adalah gunung berapi yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Wonosari", "price": "Rp 15.000", "duration": "5-7 jam"}
        ]
    },
    {
        "name": "Gunung Ijen",
        "height": "2.386 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Ijen adalah gunung berapi aktif yang terletak di Jawa Timur, terkenal dengan fenomena blue fire-nya.",
        "routes": [
            {"name": "Jalur Paltuding", "price": "Rp 10.000", "duration": "2-3 jam"}
        ]
    },
    {
        "name": "Gunung Kelud",
        "height": "1.731 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Kelud adalah gunung berapi aktif yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Kediri", "price": "Rp 5.000", "duration": "1-2 jam"}
        ]
    },
    {
        "name": "Gunung Argoropo",
        "height": "3.088 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Argoropo adalah gunung yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Argoropo", "price": "Rp 15.000", "duration": "6-8 jam"}
        ]
    },
    {
        "name": "Gunung Arjuno",
        "height": "3.339 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Arjuno adalah gunung berapi yang terletak di Jawa Timur.",
        "routes": [
           

 {"name": "Jalur Tretes", "price": "Rp 15.000", "duration": "8-10 jam"}
        ]
    },
    {
        "name": "Gunung Baluran",
        "height": "1.247 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Baluran adalah gunung yang terletak di Taman Nasional Baluran, Jawa Timur.",
        "routes": [
            {"name": "Jalur Baluran", "price": "Rp 10.000", "duration": "2-3 jam"}
        ]
    },
    {
        "name": "Gunung Batok",
        "height": "2.440 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Batok adalah gunung yang terletak di dekat Gunung Bromo, Jawa Timur.",
        "routes": [
            {"name": "Jalur Batok", "price": "Rp 10.000", "duration": "2-3 jam"}
        ]
    },
    {
        "name": "Gunung Anjasmoro",
        "height": "2.282 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Anjasmoro adalah gunung berapi yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Anjasmoro", "price": "Rp 10.000", "duration": "4-6 jam"}
        ]
    },
    {
        "name": "Gunung Blokorobrubuh",
        "height": "2.230 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Blokorobrubuh adalah gunung yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Blokorobrubuh", "price": "Rp 10.000", "duration": "4-6 jam"}
        ]
    },
    {
        "name": "Gunung Butak",
        "height": "2.868 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Butak adalah gunung berapi yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Panderman", "price": "Rp 10.000", "duration": "6-8 jam"}
        ]
    },
    {
        "name": "Gunung Liman",
        "height": "2.563 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Liman adalah gunung yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Liman", "price": "Rp 10.000", "duration": "5-7 jam"}
        ]
    },
    {
        "name": "Gunung Pandan",
        "height": "903 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Pandan adalah gunung yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Pandan", "price": "Rp 5.000", "duration": "2-3 jam"}
        ]
    },
    {
        "name": "Gunung Penanggunan",
        "height": "1.653 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Penanggunan adalah gunung berapi yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Penanggunan", "price": "Rp 5.000", "duration": "3-4 jam"}
        ]
    },
    {
        "name": "Gunung Berungkal",
        "height": "1.040 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Berungkal adalah gunung yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Berungkal", "price": "Rp 5.000", "duration": "2-3 jam"}
        ]
    },
    {
        "name": "Gunung Penanjakan",
        "height": "2.329 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Penanjakan adalah gunung yang terletak di Jawa Timur, terkenal dengan pemandangan matahari terbitnya.",
        "routes": [
            {"name": "Jalur Penanjakan", "price": "Rp 10.000", "duration": "2-3 jam"}
        ]
    },
    {
        "name": "Gunung Ranti",
        "height": "2.601 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Ranti adalah gunung berapi yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Ranti", "price": "Rp 10.000", "duration": "4-6 jam"}
        ]
    },
    {
        "name": "Gunung Suket",
        "height": "2.950 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Suket adalah gunung berapi yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Suket", "price": "Rp 10.000", "duration": "6-8 jam"}
        ]
    },
    {
        "name": "Gunung Argowayang",
        "height": "2.162 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Argowayang adalah gunung yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Argowayang", "price": "Rp 10.000", "duration": "4-6 jam"}
        ]
    },
    {
        "name": "Gunung Welirang",
        "height": "3.156 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Welirang adalah gunung berapi yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Tretes", "price": "Rp 15.000", "duration": "8-10 jam"}
        ]
    },
    {
        "name": "Gunung Wilis",
        "height": "2.563 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Wilis adalah gunung yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Wilis", "price": "Rp 10.000", "duration": "5-7 jam"}
        ]
    },
    {
        "name": "Gunung Biser",
        "height": "1.359 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Biser adalah gunung yang terletak di Jawa Timur.",
        "routes": [
            {"name": "Jalur Biser", "price": "Rp 5.000", "duration": "2-3 jam"}
        ]
    },
    {
        "name": "Gunung Betiri",
        "height": "1.233 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Betiri adalah gunung yang terletak di Taman Nasional Meru Betiri, Jawa Timur.",
        "routes": [
            {"name": "Jalur Betiri", "price": "Rp 5.000", "duration": "2-3 jam"}
        ]
    },
    {
        "name": "Gunung Raung",
        "height": "3.244 mdpl",
        "location": "Jawa Timur",
        "description": "Gunung Raung adalah gunung berapi yang terletak di Jawa Timur, terkenal dengan kaldera besar dan pemandangan alamnya.",
        "routes": [
            {"name": "Jalur Kalibaru", "price": "Rp 20.000", "duration": "12-15 jam"}
        ]
    },
    {
        "name": "Gunung Galunggung",
        "height": "1.820 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Galunggung adalah gunung berapi aktif yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Cipanas", "price": "Rp 10.000", "duration": "3-4 jam"}
        ]
    },
    {
        "name": "Gunung Pangrango",
        "height": "3.019 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Pangrango adalah gunung yang terletak di Taman Nasional Gunung Gede Pangrango, Jawa Barat.",
        "routes": [
            {"name": "Jalur Cibodas", "price": "Rp 15.000", "duration": "7-9 jam"}
        ]
    },
    {
        "name": "Gunung Papandayan",
        "height": "2.655 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Papandayan adalah gunung berapi aktif yang terletak di Jawa Barat, terkenal dengan kawah belerangnya.",
        "routes": [
            {"name": "Jalur Camp David", "price": "Rp 10.000", "duration": "4-5 jam"}
        ]
    },
    {
       

 "name": "Gunung Salak",
        "height": "1.648 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Salak adalah gunung berapi yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Pasir Reungit", "price": "Rp 10.000", "duration": "5-6 jam"},
            {"name": "Cimelati", "price": "Rp 15.000", "duration": "7-9 jam"},
            {"name": "Cidahu", "price": "Rp 10.000", "duration": "5-7 jam"},
            {"name": "Curug Pilung", "price": "Rp 20.000", "duration": "5-6 jam"},
            {"name": "Ajisaka", "price": "Rp 15.000", "duration": "4-5 jam"},
            {"name": "Curug Nangka", "price": "Rp 10.000", "duration": "5-6 jam"}
        ]
    },
    {
        "name": "Gunung Tampomas",
        "height": "1.684 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Tampomas adalah gunung berapi yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Narimbang", "price": "Rp 5.000", "duration": "3-4 jam"}
        ]
    },
    {
        "name": "Gunung Tangkuban Parahu",
        "height": "2.084 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Tangkuban Parahu adalah gunung berapi aktif yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Tangkuban Parahu", "price": "Rp 10.000", "duration": "3-4 jam"}
        ]
    },
    {
        "name": "Gunung Ciremai",
        "height": "3.074 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Ciremai adalah gunung berapi aktif yang terletak di Jawa Barat, merupakan gunung tertinggi di Jawa Barat.",
        "routes": [
            {"name": "Jalur Apuy", "price": "Rp 15.000", "duration": "8-10 jam"},
            {"name": "Jalur Palutungan", "price": "Rp 20.000", "duration": "9-11 jam"}
        ]
    },
    {
        "name": "Gunung Cikuray",
        "height": "2.821 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Cikuray adalah gunung berapi yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Cikuray", "price": "Rp 10.000", "duration": "5-6 jam"}
        ]
    },
    {
        "name": "Gunung Guntur",
        "height": "2.249 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Guntur adalah gunung berapi aktif yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Citiis", "price": "Rp 10.000", "duration": "4-5 jam"}
        ]
    },
    {
        "name": "Gunung Halimun",
        "height": "1.929 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Halimun adalah gunung yang terletak di Taman Nasional Gunung Halimun Salak, Jawa Barat.",
        "routes": [
            {"name": "Jalur Halimun", "price": "Rp 10.000", "duration": "4-5 jam"}
        ]
    },
    {
        "name": "Gunung Malabar",
        "height": "2.343 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Malabar adalah gunung berapi yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Malabar", "price": "Rp 10.000", "duration": "5-6 jam"}
        ]
    },
    {
        "name": "Gunung Tilu",
        "height": "1.076 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Tilu adalah gunung yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Tilu", "price": "Rp 5.000", "duration": "2-3 jam"}
        ]
    },
    {
        "name": "Gunung Wayang",
        "height": "2.182 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Wayang adalah gunung berapi yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Wayang", "price": "Rp 10.000", "duration": "4-5 jam"}
        ]
    },
    {
        "name": "Gunung Bongkok",
        "height": "1.141 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Bongkok adalah gunung yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Bongkok", "price": "Rp 5.000", "duration": "2-3 jam"}
        ]
    },
    {
        "name": "Gunung Bukit Tunggul",
        "height": "2.209 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Bukit Tunggul adalah gunung berapi yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Bukit Tunggul", "price": "Rp 10.000", "duration": "5-6 jam"}
        ]
    },
    {
        "name": "Gunung Burangrang",
        "height": "2.821 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Burangrang adalah gunung berapi yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Burangrang", "price": "Rp 10.000", "duration": "5-6 jam"}
        ]
    },
    {
        "name": "Gunung Kancana",
        "height": "2.050 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Kancana adalah gunung yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Kancana", "price": "Rp 10.000", "duration": "4-5 jam"}
        ]
    },
    {
        "name": "Gunung Manglayang",
        "height": "1.210 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Manglayang adalah gunung yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Manglayang", "price": "Rp 5.000", "duration": "2-3 jam"}
        ]
    },
    {
        "name": "Gunung Munara",
        "height": "367 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Munara adalah gunung yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Munara", "price": "Rp 5.000", "duration": "1-2 jam"}
        ]
    },
    {
        "name": "Gunung Patuha",
        "height": "2.434 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Patuha adalah gunung berapi yang terletak di Jawa Barat, terkenal dengan Kawah Putihnya.",
        "routes": [
            {"name": "Jalur Patuha", "price": "Rp 10.000", "duration": "4-5 jam"}
        ]
    },
    {
        "name": "Gunung Sanggabuana",
        "height": "1.291 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Sanggabuana adalah gunung yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Sanggabuana", "price": "Rp 5.000", "duration": "3-4 jam"}
        ]
    },
    {
        "name": "Gunung Cakrabuana",
        "height": "1.721 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Cakrabuana adalah gunung yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Cakrabuana", "price": "Rp 5.000", "duration": "3-4 jam"}
        ]
    },
    {
        "name": "Gunung Subang",
        "height": "1.206 mdpl",
        "location": "Jawa Barat",
        "description": "Gunung Subang adalah gunung yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Subang", "price": "Rp 5.000", "duration": "2-3 jam"}
        ]
    },
    {
        "name": "Talaga Bodas",
        "height": "2.201 mdpl",
        "location": "Jawa Barat",
        "description": "Talaga Bodas adalah gunung berapi yang terletak di Jawa Barat.",
        "routes": [
            {"name": "Jalur Talaga Bodas", "price": "Rp 10.000", "duration": "4-5 jam"}
        ]
    }
]

def show_mountains():
    listbox.delete(0, tk.END)
    for mountain in mountains:
        listbox.insert(tk.END, f"{mountain['name']} - {mountain['height']} - {mountain['location']}")

def show_mountain_details():
    selected_index = listbox.curselection()
    if selected_index:
        mountain = mountains[selected_index[0]]
        detail_text = f"Rincian {mountain['name']}\n"
        detail_text += f"Tinggi: {mountain['height']}\n"
        detail_text += f"Lokasi: {mountain['location']}\n"
        detail_text += f"Deskripsi: {mountain['description']}\n\n"
        detail_text += "Jalur Pendakian:\n"
        for route in mountain['routes']:
            detail_text += f"- {route['name']}: Harga Tiket {route['price']}, Waktu Tempuh {route['duration']}\n"
        detail_label.config(text=detail_text)

def search_mountains():
    query = search_var.get()
    listbox.delete(0, tk.END)
    for mountain in mountains:
        if query.lower() in mountain["name"].lower():
            listbox.insert(tk.END, f"{mountain['name']}")

root = tk.Tk()
root.title("MountInfoID - Informasi Gunung Indonesia")
root.geometry("800x600")

# Mengambil gambar dari folder di laptop dan menyesuaikan dengan ukuran layar
image = Image.open("c:\MountInfoID\mountains digital art.jpeg")  # Ganti dengan path file gambar JPEG Anda
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS if hasattr(Image, "ANTIALIAS") else Image.BICUBIC)
bg_image = ImageTk.PhotoImage(image)

# Menambahkan gambar sebagai latar belakang
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame untuk menampilkan rincian gunung
detail_frame = ttk.Frame(root)
detail_frame.pack(pady=10)

# Label untuk detail gunung
detail_label = ttk.Label(detail_frame, text="Rincian Gunung", font=("Helvetica", 16))
detail_label.pack()

# Listbox untuk menampilkan daftar gunung
listbox = tk.Listbox(root, font=("Helvetica", 12), width=50, height=10)
listbox.pack(padx=10, pady=5)

# Scrollbar untuk listbox
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Hubungkan scrollbar dengan listbox
listbox.config(yscrollcommand=scrollbar.set)

# Kotak teks untuk pencarian gunung
search_var = tk.StringVar()
search_entry = ttk.Entry(root, textvariable=search_var, font=("Helvetica", 12))
search_entry.pack(pady=5)

# Button untuk pencarian gunung
btn_search = ttk.Button(root, text="Cari Gunung", command=search_mountains)
btn_search.pack(pady=5)

# Button untuk menampilkan daftar gunung
btn_show_mountains = ttk.Button(root, text="Tampilkan Daftar Gunung", command=show_mountains)
btn_show_mountains.pack(pady=5)

# Button untuk menampilkan rincian gunung
btn_show_details = ttk.Button(root, text="Tampilkan Rincian", command=show_mountain_details)
btn_show_details.pack(pady=5)

# Button untuk keluar dari aplikasi
btn_exit = ttk.Button(root, text="Keluar", command=root.quit)
btn_exit.pack(pady=10)

# Memanggil fungsi untuk menampilkan data
show_mountains()

root.mainloop()