import csv
import json

surahs = {
    "suras": {
        "sura": [
            {
                "_index": "1",
                "_ayas": "7",
                "_start": "0",
                "_name": "الفاتحة",
                "_tname": "Al-Faatiha",
                "_ename": "The Opening",
                "_type": "Meccan",
                "_order": "5",
                "_rukus": "1"
            },
            {
                "_index": "2",
                "_ayas": "286",
                "_start": "7",
                "_name": "البقرة",
                "_tname": "Al-Baqara",
                "_ename": "The Cow",
                "_type": "Medinan",
                "_order": "87",
                "_rukus": "40"
            },
            {
                "_index": "3",
                "_ayas": "200",
                "_start": "293",
                "_name": "آل عمران",
                "_tname": "Aal-i-Imraan",
                "_ename": "The Family of Imraan",
                "_type": "Medinan",
                "_order": "89",
                "_rukus": "20"
            },
            {
                "_index": "4",
                "_ayas": "176",
                "_start": "493",
                "_name": "النساء",
                "_tname": "An-Nisaa",
                "_ename": "The Women",
                "_type": "Medinan",
                "_order": "92",
                "_rukus": "24"
            },
            {
                "_index": "5",
                "_ayas": "120",
                "_start": "669",
                "_name": "المائدة",
                "_tname": "Al-Maaida",
                "_ename": "The Table",
                "_type": "Medinan",
                "_order": "112",
                "_rukus": "16"
            },
            {
                "_index": "6",
                "_ayas": "165",
                "_start": "789",
                "_name": "الأنعام",
                "_tname": "Al-An'aam",
                "_ename": "The Cattle",
                "_type": "Meccan",
                "_order": "55",
                "_rukus": "20"
            },
            {
                "_index": "7",
                "_ayas": "206",
                "_start": "954",
                "_name": "الأعراف",
                "_tname": "Al-A'raaf",
                "_ename": "The Heights",
                "_type": "Meccan",
                "_order": "39",
                "_rukus": "24"
            },
            {
                "_index": "8",
                "_ayas": "75",
                "_start": "1160",
                "_name": "الأنفال",
                "_tname": "Al-Anfaal",
                "_ename": "The Spoils of War",
                "_type": "Medinan",
                "_order": "88",
                "_rukus": "10"
            },
            {
                "_index": "9",
                "_ayas": "129",
                "_start": "1235",
                "_name": "التوبة",
                "_tname": "At-Tawba",
                "_ename": "The Repentance",
                "_type": "Medinan",
                "_order": "113",
                "_rukus": "16"
            },
            {
                "_index": "10",
                "_ayas": "109",
                "_start": "1364",
                "_name": "يونس",
                "_tname": "Yunus",
                "_ename": "Jonas",
                "_type": "Meccan",
                "_order": "51",
                "_rukus": "11"
            },
            {
                "_index": "11",
                "_ayas": "123",
                "_start": "1473",
                "_name": "هود",
                "_tname": "Hud",
                "_ename": "Hud",
                "_type": "Meccan",
                "_order": "52",
                "_rukus": "10"
            },
            {
                "_index": "12",
                "_ayas": "111",
                "_start": "1596",
                "_name": "يوسف",
                "_tname": "Yusuf",
                "_ename": "Joseph",
                "_type": "Meccan",
                "_order": "53",
                "_rukus": "12"
            },
            {
                "_index": "13",
                "_ayas": "43",
                "_start": "1707",
                "_name": "الرعد",
                "_tname": "Ar-Ra'd",
                "_ename": "The Thunder",
                "_type": "Medinan",
                "_order": "96",
                "_rukus": "6"
            },
            {
                "_index": "14",
                "_ayas": "52",
                "_start": "1750",
                "_name": "ابراهيم",
                "_tname": "Ibrahim",
                "_ename": "Abraham",
                "_type": "Meccan",
                "_order": "72",
                "_rukus": "7"
            },
            {
                "_index": "15",
                "_ayas": "99",
                "_start": "1802",
                "_name": "الحجر",
                "_tname": "Al-Hijr",
                "_ename": "The Rock",
                "_type": "Meccan",
                "_order": "54",
                "_rukus": "6"
            },
            {
                "_index": "16",
                "_ayas": "128",
                "_start": "1901",
                "_name": "النحل",
                "_tname": "An-Nahl",
                "_ename": "The Bee",
                "_type": "Meccan",
                "_order": "70",
                "_rukus": "16"
            },
            {
                "_index": "17",
                "_ayas": "111",
                "_start": "2029",
                "_name": "الإسراء",
                "_tname": "Al-Israa",
                "_ename": "The Night Journey",
                "_type": "Meccan",
                "_order": "50",
                "_rukus": "12"
            },
            {
                "_index": "18",
                "_ayas": "110",
                "_start": "2140",
                "_name": "الكهف",
                "_tname": "Al-Kahf",
                "_ename": "The Cave",
                "_type": "Meccan",
                "_order": "69",
                "_rukus": "12"
            },
            {
                "_index": "19",
                "_ayas": "98",
                "_start": "2250",
                "_name": "مريم",
                "_tname": "Maryam",
                "_ename": "Mary",
                "_type": "Meccan",
                "_order": "44",
                "_rukus": "6"
            },
            {
                "_index": "20",
                "_ayas": "135",
                "_start": "2348",
                "_name": "طه",
                "_tname": "Taa-Haa",
                "_ename": "Taa-Haa",
                "_type": "Meccan",
                "_order": "45",
                "_rukus": "8"
            },
            {
                "_index": "21",
                "_ayas": "112",
                "_start": "2483",
                "_name": "الأنبياء",
                "_tname": "Al-Anbiyaa",
                "_ename": "The Prophets",
                "_type": "Meccan",
                "_order": "73",
                "_rukus": "7"
            },
            {
                "_index": "22",
                "_ayas": "78",
                "_start": "2595",
                "_name": "الحج",
                "_tname": "Al-Hajj",
                "_ename": "The Pilgrimage",
                "_type": "Medinan",
                "_order": "103",
                "_rukus": "10"
            },
            {
                "_index": "23",
                "_ayas": "118",
                "_start": "2673",
                "_name": "المؤمنون",
                "_tname": "Al-Muminoon",
                "_ename": "The Believers",
                "_type": "Meccan",
                "_order": "74",
                "_rukus": "6"
            },
            {
                "_index": "24",
                "_ayas": "64",
                "_start": "2791",
                "_name": "النور",
                "_tname": "An-Noor",
                "_ename": "The Light",
                "_type": "Medinan",
                "_order": "102",
                "_rukus": "9"
            },
            {
                "_index": "25",
                "_ayas": "77",
                "_start": "2855",
                "_name": "الفرقان",
                "_tname": "Al-Furqaan",
                "_ename": "The Criterion",
                "_type": "Meccan",
                "_order": "42",
                "_rukus": "6"
            },
            {
                "_index": "26",
                "_ayas": "227",
                "_start": "2932",
                "_name": "الشعراء",
                "_tname": "Ash-Shu'araa",
                "_ename": "The Poets",
                "_type": "Meccan",
                "_order": "47",
                "_rukus": "11"
            },
            {
                "_index": "27",
                "_ayas": "93",
                "_start": "3159",
                "_name": "النمل",
                "_tname": "An-Naml",
                "_ename": "The Ant",
                "_type": "Meccan",
                "_order": "48",
                "_rukus": "7"
            },
            {
                "_index": "28",
                "_ayas": "88",
                "_start": "3252",
                "_name": "القصص",
                "_tname": "Al-Qasas",
                "_ename": "The Stories",
                "_type": "Meccan",
                "_order": "49",
                "_rukus": "8"
            },
            {
                "_index": "29",
                "_ayas": "69",
                "_start": "3340",
                "_name": "العنكبوت",
                "_tname": "Al-Ankaboot",
                "_ename": "The Spider",
                "_type": "Meccan",
                "_order": "85",
                "_rukus": "7"
            },
            {
                "_index": "30",
                "_ayas": "60",
                "_start": "3409",
                "_name": "الروم",
                "_tname": "Ar-Room",
                "_ename": "The Romans",
                "_type": "Meccan",
                "_order": "84",
                "_rukus": "6"
            },
            {
                "_index": "31",
                "_ayas": "34",
                "_start": "3469",
                "_name": "لقمان",
                "_tname": "Luqman",
                "_ename": "Luqman",
                "_type": "Meccan",
                "_order": "57",
                "_rukus": "3"
            },
            {
                "_index": "32",
                "_ayas": "30",
                "_start": "3503",
                "_name": "السجدة",
                "_tname": "As-Sajda",
                "_ename": "The Prostration",
                "_type": "Meccan",
                "_order": "75",
                "_rukus": "3"
            },
            {
                "_index": "33",
                "_ayas": "73",
                "_start": "3533",
                "_name": "الأحزاب",
                "_tname": "Al-Ahzaab",
                "_ename": "The Clans",
                "_type": "Medinan",
                "_order": "90",
                "_rukus": "9"
            },
            {
                "_index": "34",
                "_ayas": "54",
                "_start": "3606",
                "_name": "سبإ",
                "_tname": "Saba",
                "_ename": "Sheba",
                "_type": "Meccan",
                "_order": "58",
                "_rukus": "6"
            },
            {
                "_index": "35",
                "_ayas": "45",
                "_start": "3660",
                "_name": "فاطر",
                "_tname": "Faatir",
                "_ename": "The Originator",
                "_type": "Meccan",
                "_order": "43",
                "_rukus": "5"
            },
            {
                "_index": "36",
                "_ayas": "83",
                "_start": "3705",
                "_name": "يس",
                "_tname": "Yaseen",
                "_ename": "Yaseen",
                "_type": "Meccan",
                "_order": "41",
                "_rukus": "5"
            },
            {
                "_index": "37",
                "_ayas": "182",
                "_start": "3788",
                "_name": "الصافات",
                "_tname": "As-Saaffaat",
                "_ename": "Those drawn up in Ranks",
                "_type": "Meccan",
                "_order": "56",
                "_rukus": "5"
            },
            {
                "_index": "38",
                "_ayas": "88",
                "_start": "3970",
                "_name": "ص",
                "_tname": "Saad",
                "_ename": "The letter Saad",
                "_type": "Meccan",
                "_order": "38",
                "_rukus": "5"
            },
            {
                "_index": "39",
                "_ayas": "75",
                "_start": "4058",
                "_name": "الزمر",
                "_tname": "Az-Zumar",
                "_ename": "The Groups",
                "_type": "Meccan",
                "_order": "59",
                "_rukus": "8"
            },
            {
                "_index": "40",
                "_ayas": "85",
                "_start": "4133",
                "_name": "غافر",
                "_tname": "Al-Ghaafir",
                "_ename": "The Forgiver",
                "_type": "Meccan",
                "_order": "60",
                "_rukus": "9"
            },
            {
                "_index": "41",
                "_ayas": "54",
                "_start": "4218",
                "_name": "فصلت",
                "_tname": "Fussilat",
                "_ename": "Explained in detail",
                "_type": "Meccan",
                "_order": "61",
                "_rukus": "6"
            },
            {
                "_index": "42",
                "_ayas": "53",
                "_start": "4272",
                "_name": "الشورى",
                "_tname": "Ash-Shura",
                "_ename": "Consultation",
                "_type": "Meccan",
                "_order": "62",
                "_rukus": "5"
            },
            {
                "_index": "43",
                "_ayas": "89",
                "_start": "4325",
                "_name": "الزخرف",
                "_tname": "Az-Zukhruf",
                "_ename": "Ornaments of gold",
                "_type": "Meccan",
                "_order": "63",
                "_rukus": "7"
            },
            {
                "_index": "44",
                "_ayas": "59",
                "_start": "4414",
                "_name": "الدخان",
                "_tname": "Ad-Dukhaan",
                "_ename": "The Smoke",
                "_type": "Meccan",
                "_order": "64",
                "_rukus": "3"
            },
            {
                "_index": "45",
                "_ayas": "37",
                "_start": "4473",
                "_name": "الجاثية",
                "_tname": "Al-Jaathiya",
                "_ename": "Crouching",
                "_type": "Meccan",
                "_order": "65",
                "_rukus": "4"
            },
            {
                "_index": "46",
                "_ayas": "35",
                "_start": "4510",
                "_name": "الأحقاف",
                "_tname": "Al-Ahqaf",
                "_ename": "The Dunes",
                "_type": "Meccan",
                "_order": "66",
                "_rukus": "4"
            },
            {
                "_index": "47",
                "_ayas": "38",
                "_start": "4545",
                "_name": "محمد",
                "_tname": "Muhammad",
                "_ename": "Muhammad",
                "_type": "Medinan",
                "_order": "95",
                "_rukus": "4"
            },
            {
                "_index": "48",
                "_ayas": "29",
                "_start": "4583",
                "_name": "الفتح",
                "_tname": "Al-Fath",
                "_ename": "The Victory",
                "_type": "Medinan",
                "_order": "111",
                "_rukus": "4"
            },
            {
                "_index": "49",
                "_ayas": "18",
                "_start": "4612",
                "_name": "الحجرات",
                "_tname": "Al-Hujuraat",
                "_ename": "The Inner Apartments",
                "_type": "Medinan",
                "_order": "106",
                "_rukus": "2"
            },
            {
                "_index": "50",
                "_ayas": "45",
                "_start": "4630",
                "_name": "ق",
                "_tname": "Qaaf",
                "_ename": "The letter Qaaf",
                "_type": "Meccan",
                "_order": "34",
                "_rukus": "3"
            },
            {
                "_index": "51",
                "_ayas": "60",
                "_start": "4675",
                "_name": "الذاريات",
                "_tname": "Adh-Dhaariyat",
                "_ename": "The Winnowing Winds",
                "_type": "Meccan",
                "_order": "67",
                "_rukus": "3"
            },
            {
                "_index": "52",
                "_ayas": "49",
                "_start": "4735",
                "_name": "الطور",
                "_tname": "At-Tur",
                "_ename": "The Mount",
                "_type": "Meccan",
                "_order": "76",
                "_rukus": "2"
            },
            {
                "_index": "53",
                "_ayas": "62",
                "_start": "4784",
                "_name": "النجم",
                "_tname": "An-Najm",
                "_ename": "The Star",
                "_type": "Meccan",
                "_order": "23",
                "_rukus": "3"
            },
            {
                "_index": "54",
                "_ayas": "55",
                "_start": "4846",
                "_name": "القمر",
                "_tname": "Al-Qamar",
                "_ename": "The Moon",
                "_type": "Meccan",
                "_order": "37",
                "_rukus": "3"
            },
            {
                "_index": "55",
                "_ayas": "78",
                "_start": "4901",
                "_name": "الرحمن",
                "_tname": "Ar-Rahmaan",
                "_ename": "The Beneficent",
                "_type": "Medinan",
                "_order": "97",
                "_rukus": "3"
            },
            {
                "_index": "56",
                "_ayas": "96",
                "_start": "4979",
                "_name": "الواقعة",
                "_tname": "Al-Waaqia",
                "_ename": "The Inevitable",
                "_type": "Meccan",
                "_order": "46",
                "_rukus": "3"
            },
            {
                "_index": "57",
                "_ayas": "29",
                "_start": "5075",
                "_name": "الحديد",
                "_tname": "Al-Hadid",
                "_ename": "The Iron",
                "_type": "Medinan",
                "_order": "94",
                "_rukus": "4"
            },
            {
                "_index": "58",
                "_ayas": "22",
                "_start": "5104",
                "_name": "المجادلة",
                "_tname": "Al-Mujaadila",
                "_ename": "The Pleading Woman",
                "_type": "Medinan",
                "_order": "105",
                "_rukus": "3"
            },
            {
                "_index": "59",
                "_ayas": "24",
                "_start": "5126",
                "_name": "الحشر",
                "_tname": "Al-Hashr",
                "_ename": "The Exile",
                "_type": "Medinan",
                "_order": "101",
                "_rukus": "3"
            },
            {
                "_index": "60",
                "_ayas": "13",
                "_start": "5150",
                "_name": "الممتحنة",
                "_tname": "Al-Mumtahana",
                "_ename": "She that is to be examined",
                "_type": "Medinan",
                "_order": "91",
                "_rukus": "2"
            },
            {
                "_index": "61",
                "_ayas": "14",
                "_start": "5163",
                "_name": "الصف",
                "_tname": "As-Saff",
                "_ename": "The Ranks",
                "_type": "Medinan",
                "_order": "109",
                "_rukus": "2"
            },
            {
                "_index": "62",
                "_ayas": "11",
                "_start": "5177",
                "_name": "الجمعة",
                "_tname": "Al-Jumu'a",
                "_ename": "Friday",
                "_type": "Medinan",
                "_order": "110",
                "_rukus": "2"
            },
            {
                "_index": "63",
                "_ayas": "11",
                "_start": "5188",
                "_name": "المنافقون",
                "_tname": "Al-Munaafiqoon",
                "_ename": "The Hypocrites",
                "_type": "Medinan",
                "_order": "104",
                "_rukus": "2"
            },
            {
                "_index": "64",
                "_ayas": "18",
                "_start": "5199",
                "_name": "التغابن",
                "_tname": "At-Taghaabun",
                "_ename": "Mutual Disillusion",
                "_type": "Medinan",
                "_order": "108",
                "_rukus": "2"
            },
            {
                "_index": "65",
                "_ayas": "12",
                "_start": "5217",
                "_name": "الطلاق",
                "_tname": "At-Talaaq",
                "_ename": "Divorce",
                "_type": "Medinan",
                "_order": "99",
                "_rukus": "2"
            },
            {
                "_index": "66",
                "_ayas": "12",
                "_start": "5229",
                "_name": "التحريم",
                "_tname": "At-Tahrim",
                "_ename": "The Prohibition",
                "_type": "Medinan",
                "_order": "107",
                "_rukus": "2"
            },
            {
                "_index": "67",
                "_ayas": "30",
                "_start": "5241",
                "_name": "الملك",
                "_tname": "Al-Mulk",
                "_ename": "The Sovereignty",
                "_type": "Meccan",
                "_order": "77",
                "_rukus": "2"
            },
            {
                "_index": "68",
                "_ayas": "52",
                "_start": "5271",
                "_name": "القلم",
                "_tname": "Al-Qalam",
                "_ename": "The Pen",
                "_type": "Meccan",
                "_order": "2",
                "_rukus": "2"
            },
            {
                "_index": "69",
                "_ayas": "52",
                "_start": "5323",
                "_name": "الحاقة",
                "_tname": "Al-Haaqqa",
                "_ename": "The Reality",
                "_type": "Meccan",
                "_order": "78",
                "_rukus": "2"
            },
            {
                "_index": "70",
                "_ayas": "44",
                "_start": "5375",
                "_name": "المعارج",
                "_tname": "Al-Ma'aarij",
                "_ename": "The Ascending Stairways",
                "_type": "Meccan",
                "_order": "79",
                "_rukus": "2"
            },
            {
                "_index": "71",
                "_ayas": "28",
                "_start": "5419",
                "_name": "نوح",
                "_tname": "Nooh",
                "_ename": "Noah",
                "_type": "Meccan",
                "_order": "71",
                "_rukus": "2"
            },
            {
                "_index": "72",
                "_ayas": "28",
                "_start": "5447",
                "_name": "الجن",
                "_tname": "Al-Jinn",
                "_ename": "The Jinn",
                "_type": "Meccan",
                "_order": "40",
                "_rukus": "2"
            },
            {
                "_index": "73",
                "_ayas": "20",
                "_start": "5475",
                "_name": "المزمل",
                "_tname": "Al-Muzzammil",
                "_ename": "The Enshrouded One",
                "_type": "Meccan",
                "_order": "3",
                "_rukus": "2"
            },
            {
                "_index": "74",
                "_ayas": "56",
                "_start": "5495",
                "_name": "المدثر",
                "_tname": "Al-Muddaththir",
                "_ename": "The Cloaked One",
                "_type": "Meccan",
                "_order": "4",
                "_rukus": "2"
            },
            {
                "_index": "75",
                "_ayas": "40",
                "_start": "5551",
                "_name": "القيامة",
                "_tname": "Al-Qiyaama",
                "_ename": "The Resurrection",
                "_type": "Meccan",
                "_order": "31",
                "_rukus": "2"
            },
            {
                "_index": "76",
                "_ayas": "31",
                "_start": "5591",
                "_name": "الانسان",
                "_tname": "Al-Insaan",
                "_ename": "Man",
                "_type": "Medinan",
                "_order": "98",
                "_rukus": "2"
            },
            {
                "_index": "77",
                "_ayas": "50",
                "_start": "5622",
                "_name": "المرسلات",
                "_tname": "Al-Mursalaat",
                "_ename": "The Emissaries",
                "_type": "Meccan",
                "_order": "33",
                "_rukus": "2"
            },
            {
                "_index": "78",
                "_ayas": "40",
                "_start": "5672",
                "_name": "النبإ",
                "_tname": "An-Naba",
                "_ename": "The Announcement",
                "_type": "Meccan",
                "_order": "80",
                "_rukus": "2"
            },
            {
                "_index": "79",
                "_ayas": "46",
                "_start": "5712",
                "_name": "النازعات",
                "_tname": "An-Naazi'aat",
                "_ename": "Those who drag forth",
                "_type": "Meccan",
                "_order": "81",
                "_rukus": "2"
            },
            {
                "_index": "80",
                "_ayas": "42",
                "_start": "5758",
                "_name": "عبس",
                "_tname": "Abasa",
                "_ename": "He frowned",
                "_type": "Meccan",
                "_order": "24",
                "_rukus": "1"
            },
            {
                "_index": "81",
                "_ayas": "29",
                "_start": "5800",
                "_name": "التكوير",
                "_tname": "At-Takwir",
                "_ename": "The Overthrowing",
                "_type": "Meccan",
                "_order": "7",
                "_rukus": "1"
            },
            {
                "_index": "82",
                "_ayas": "19",
                "_start": "5829",
                "_name": "الإنفطار",
                "_tname": "Al-Infitaar",
                "_ename": "The Cleaving",
                "_type": "Meccan",
                "_order": "82",
                "_rukus": "1"
            },
            {
                "_index": "83",
                "_ayas": "36",
                "_start": "5848",
                "_name": "المطففين",
                "_tname": "Al-Mutaffifin",
                "_ename": "Defrauding",
                "_type": "Meccan",
                "_order": "86",
                "_rukus": "1"
            },
            {
                "_index": "84",
                "_ayas": "25",
                "_start": "5884",
                "_name": "الإنشقاق",
                "_tname": "Al-Inshiqaaq",
                "_ename": "The Splitting Open",
                "_type": "Meccan",
                "_order": "83",
                "_rukus": "1"
            },
            {
                "_index": "85",
                "_ayas": "22",
                "_start": "5909",
                "_name": "البروج",
                "_tname": "Al-Burooj",
                "_ename": "The Constellations",
                "_type": "Meccan",
                "_order": "27",
                "_rukus": "1"
            },
            {
                "_index": "86",
                "_ayas": "17",
                "_start": "5931",
                "_name": "الطارق",
                "_tname": "At-Taariq",
                "_ename": "The Morning Star",
                "_type": "Meccan",
                "_order": "36",
                "_rukus": "1"
            },
            {
                "_index": "87",
                "_ayas": "19",
                "_start": "5948",
                "_name": "الأعلى",
                "_tname": "Al-A'laa",
                "_ename": "The Most High",
                "_type": "Meccan",
                "_order": "8",
                "_rukus": "1"
            },
            {
                "_index": "88",
                "_ayas": "26",
                "_start": "5967",
                "_name": "الغاشية",
                "_tname": "Al-Ghaashiya",
                "_ename": "The Overwhelming",
                "_type": "Meccan",
                "_order": "68",
                "_rukus": "1"
            },
            {
                "_index": "89",
                "_ayas": "30",
                "_start": "5993",
                "_name": "الفجر",
                "_tname": "Al-Fajr",
                "_ename": "The Dawn",
                "_type": "Meccan",
                "_order": "10",
                "_rukus": "1"
            },
            {
                "_index": "90",
                "_ayas": "20",
                "_start": "6023",
                "_name": "البلد",
                "_tname": "Al-Balad",
                "_ename": "The City",
                "_type": "Meccan",
                "_order": "35",
                "_rukus": "1"
            },
            {
                "_index": "91",
                "_ayas": "15",
                "_start": "6043",
                "_name": "الشمس",
                "_tname": "Ash-Shams",
                "_ename": "The Sun",
                "_type": "Meccan",
                "_order": "26",
                "_rukus": "1"
            },
            {
                "_index": "92",
                "_ayas": "21",
                "_start": "6058",
                "_name": "الليل",
                "_tname": "Al-Lail",
                "_ename": "The Night",
                "_type": "Meccan",
                "_order": "9",
                "_rukus": "1"
            },
            {
                "_index": "93",
                "_ayas": "11",
                "_start": "6079",
                "_name": "الضحى",
                "_tname": "Ad-Dhuhaa",
                "_ename": "The Morning Hours",
                "_type": "Meccan",
                "_order": "11",
                "_rukus": "1"
            },
            {
                "_index": "94",
                "_ayas": "8",
                "_start": "6090",
                "_name": "الشرح",
                "_tname": "Ash-Sharh",
                "_ename": "The Consolation",
                "_type": "Meccan",
                "_order": "12",
                "_rukus": "1"
            },
            {
                "_index": "95",
                "_ayas": "8",
                "_start": "6098",
                "_name": "التين",
                "_tname": "At-Tin",
                "_ename": "The Fig",
                "_type": "Meccan",
                "_order": "28",
                "_rukus": "1"
            },
            {
                "_index": "96",
                "_ayas": "19",
                "_start": "6106",
                "_name": "العلق",
                "_tname": "Al-Alaq",
                "_ename": "The Clot",
                "_type": "Meccan",
                "_order": "1",
                "_rukus": "1"
            },
            {
                "_index": "97",
                "_ayas": "5",
                "_start": "6125",
                "_name": "القدر",
                "_tname": "Al-Qadr",
                "_ename": "The Power, Fate",
                "_type": "Meccan",
                "_order": "25",
                "_rukus": "1"
            },
            {
                "_index": "98",
                "_ayas": "8",
                "_start": "6130",
                "_name": "البينة",
                "_tname": "Al-Bayyina",
                "_ename": "The Evidence",
                "_type": "Medinan",
                "_order": "100",
                "_rukus": "1"
            },
            {
                "_index": "99",
                "_ayas": "8",
                "_start": "6138",
                "_name": "الزلزلة",
                "_tname": "Az-Zalzala",
                "_ename": "The Earthquake",
                "_type": "Medinan",
                "_order": "93",
                "_rukus": "1"
            },
            {
                "_index": "100",
                "_ayas": "11",
                "_start": "6146",
                "_name": "العاديات",
                "_tname": "Al-Aadiyaat",
                "_ename": "The Chargers",
                "_type": "Meccan",
                "_order": "14",
                "_rukus": "1"
            },
            {
                "_index": "101",
                "_ayas": "11",
                "_start": "6157",
                "_name": "القارعة",
                "_tname": "Al-Qaari'a",
                "_ename": "The Calamity",
                "_type": "Meccan",
                "_order": "30",
                "_rukus": "1"
            },
            {
                "_index": "102",
                "_ayas": "8",
                "_start": "6168",
                "_name": "التكاثر",
                "_tname": "At-Takaathur",
                "_ename": "Competition",
                "_type": "Meccan",
                "_order": "16",
                "_rukus": "1"
            },
            {
                "_index": "103",
                "_ayas": "3",
                "_start": "6176",
                "_name": "العصر",
                "_tname": "Al-Asr",
                "_ename": "The Declining Day, Epoch",
                "_type": "Meccan",
                "_order": "13",
                "_rukus": "1"
            },
            {
                "_index": "104",
                "_ayas": "9",
                "_start": "6179",
                "_name": "الهمزة",
                "_tname": "Al-Humaza",
                "_ename": "The Traducer",
                "_type": "Meccan",
                "_order": "32",
                "_rukus": "1"
            },
            {
                "_index": "105",
                "_ayas": "5",
                "_start": "6188",
                "_name": "الفيل",
                "_tname": "Al-Fil",
                "_ename": "The Elephant",
                "_type": "Meccan",
                "_order": "19",
                "_rukus": "1"
            },
            {
                "_index": "106",
                "_ayas": "4",
                "_start": "6193",
                "_name": "قريش",
                "_tname": "Quraish",
                "_ename": "Quraysh",
                "_type": "Meccan",
                "_order": "29",
                "_rukus": "1"
            },
            {
                "_index": "107",
                "_ayas": "7",
                "_start": "6197",
                "_name": "الماعون",
                "_tname": "Al-Maa'un",
                "_ename": "Almsgiving",
                "_type": "Meccan",
                "_order": "17",
                "_rukus": "1"
            },
            {
                "_index": "108",
                "_ayas": "3",
                "_start": "6204",
                "_name": "الكوثر",
                "_tname": "Al-Kawthar",
                "_ename": "Abundance",
                "_type": "Meccan",
                "_order": "15",
                "_rukus": "1"
            },
            {
                "_index": "109",
                "_ayas": "6",
                "_start": "6207",
                "_name": "الكافرون",
                "_tname": "Al-Kaafiroon",
                "_ename": "The Disbelievers",
                "_type": "Meccan",
                "_order": "18",
                "_rukus": "1"
            },
            {
                "_index": "110",
                "_ayas": "3",
                "_start": "6213",
                "_name": "النصر",
                "_tname": "An-Nasr",
                "_ename": "Divine Support",
                "_type": "Medinan",
                "_order": "114",
                "_rukus": "1"
            },
            {
                "_index": "111",
                "_ayas": "5",
                "_start": "6216",
                "_name": "المسد",
                "_tname": "Al-Masad",
                "_ename": "The Palm Fibre",
                "_type": "Meccan",
                "_order": "6",
                "_rukus": "1"
            },
            {
                "_index": "112",
                "_ayas": "4",
                "_start": "6221",
                "_name": "الإخلاص",
                "_tname": "Al-Ikhlaas",
                "_ename": "Sincerity",
                "_type": "Meccan",
                "_order": "22",
                "_rukus": "1"
            },
            {
                "_index": "113",
                "_ayas": "5",
                "_start": "6225",
                "_name": "الفلق",
                "_tname": "Al-Falaq",
                "_ename": "The Dawn",
                "_type": "Meccan",
                "_order": "20",
                "_rukus": "1"
            },
            {
                "_index": "114",
                "_ayas": "6",
                "_start": "6230",
                "_name": "الناس",
                "_tname": "An-Naas",
                "_ename": "Mankind",
                "_type": "Meccan",
                "_order": "21",
                "_rukus": "1"
            }
        ],
        "_alias": "chapters"
    }
}

names99 = [
    {
        "name": "الرَّحْمَنُ",
        "transliteration": "Ar Rahmaan",
        "number": 1,
        "en": {
            "meaning": "The Beneficent"
        }
    },
    {
        "name": "الرَّحِيمُ",
        "transliteration": "Ar Raheem",
        "number": 2,
        "en": {
            "meaning": "The Merciful"
        }
    },
    {
        "name": "الْمَلِكُ",
        "transliteration": "Al Malik",
        "number": 3,
        "en": {
            "meaning": "The King / Eternal Lord"
        }
    },
    {
        "name": "الْقُدُّوسُ",
        "transliteration": "Al Quddus",
        "number": 4,
        "en": {
            "meaning": "The Purest"
        }
    },
    {
        "name": "السَّلاَمُ",
        "transliteration": "As Salaam",
        "number": 5,
        "en": {
            "meaning": "The Source of Peace"
        }
    },
    {
        "name": "الْمُؤْمِنُ",
        "transliteration": "Al Mu'min",
        "number": 6,
        "en": {
            "meaning": "The inspirer of faith"
        }
    },
    {
        "name": "الْمُهَيْمِنُ",
        "transliteration": "Al Muhaymin",
        "number": 7,
        "en": {
            "meaning": "The Guardian"
        }
    },
    {
        "name": "الْعَزِيزُ",
        "transliteration": "Al Azeez",
        "number": 8,
        "en": {
            "meaning": "The Precious / The Most Mighty"
        }
    },
    {
        "name": "الْجَبَّارُ",
        "transliteration": "Al Jabbaar",
        "number": 9,
        "en": {
            "meaning": "The Compeller"
        }
    },
    {
        "name": "الْمُتَكَبِّرُ",
        "transliteration": "Al Mutakabbir",
        "number": 10,
        "en": {
            "meaning": "The Greatest"
        }
    },
    {
        "name": "الْخَالِقُ",
        "transliteration": "Al Khaaliq",
        "number": 11,
        "en": {
            "meaning": "The Creator"
        }
    },
    {
        "name": "الْبَارِئُ",
        "transliteration": "Al Baari",
        "number": 12,
        "en": {
            "meaning": "The Maker of Order"
        }
    },
    {
        "name": "الْمُصَوِّرُ",
        "transliteration": "Al Musawwir",
        "number": 13,
        "en": {
            "meaning": "The Shaper of Beauty"
        }
    },
    {
        "name": "الْغَفَّارُ",
        "transliteration": "Al Ghaffaar",
        "number": 14,
        "en": {
            "meaning": "The Forgiving"
        }
    },
    {
        "name": "الْقَهَّارُ",
        "transliteration": "Al Qahhaar",
        "number": 15,
        "en": {
            "meaning": "The Subduer"
        }
    },
    {
        "name": "الْوَهَّابُ",
        "transliteration": "Al Wahhaab",
        "number": 16,
        "en": {
            "meaning": "The Giver of All"
        }
    },
    {
        "name": "الرَّزَّاقُ",
        "transliteration": "Ar Razzaaq",
        "number": 17,
        "en": {
            "meaning": "The Sustainer"
        }
    },
    {
        "name": "الْفَتَّاحُ",
        "transliteration": "Al Fattaah",
        "number": 18,
        "en": {
            "meaning": "The Opener"
        }
    },
    {
        "name": "اَلْعَلِيْمُ",
        "transliteration": "Al 'Aleem",
        "number": 19,
        "en": {
            "meaning": "The Knower of all"
        }
    },
    {
        "name": "الْقَابِضُ",
        "transliteration": "Al Qaabid",
        "number": 20,
        "en": {
            "meaning": "The Constrictor"
        }
    },
    {
        "name": "الْبَاسِطُ",
        "transliteration": "Al Baasit",
        "number": 21,
        "en": {
            "meaning": "The Reliever"
        }
    },
    {
        "name": "الْخَافِضُ",
        "transliteration": "Al Khaafid",
        "number": 22,
        "en": {
            "meaning": "The Abaser"
        }
    },
    {
        "name": "الرَّافِعُ",
        "transliteration": "Ar Raafi'",
        "number": 23,
        "en": {
            "meaning": "The Exalter"
        }
    },
    {
        "name": "الْمُعِزُّ",
        "transliteration": "Al Mu'iz",
        "number": 24,
        "en": {
            "meaning": "The Bestower of Honour"
        }
    },
    {
        "name": "المُذِلُّ",
        "transliteration": "Al Mudhil",
        "number": 25,
        "en": {
            "meaning": "The Humiliator"
        }
    },
    {
        "name": "السَّمِيعُ",
        "transliteration": "As Samee'",
        "number": 26,
        "en": {
            "meaning": "The Hearer of all"
        }
    },
    {
        "name": "الْبَصِيرُ",
        "transliteration": "Al Baseer",
        "number": 27,
        "en": {
            "meaning": "The Seer of all"
        }
    },
    {
        "name": "الْحَكَمُ",
        "transliteration": "Al Hakam",
        "number": 28,
        "en": {
            "meaning": "The Judge"
        }
    },
    {
        "name": "الْعَدْلُ",
        "transliteration": "Al 'Adl",
        "number": 29,
        "en": {
            "meaning": "The Just"
        }
    },
    {
        "name": "اللَّطِيفُ",
        "transliteration": "Al Lateef",
        "number": 30,
        "en": {
            "meaning": "The Subtle One"
        }
    },
    {
        "name": "الْخَبِيرُ",
        "transliteration": "Al Khabeer",
        "number": 31,
        "en": {
            "meaning": "The All Aware"
        }
    },
    {
        "name": "الْحَلِيمُ",
        "transliteration": "Al Haleem",
        "number": 32,
        "en": {
            "meaning": "The Forebearing"
        }
    },
    {
        "name": "الْعَظِيمُ",
        "transliteration": "Al 'Azeem",
        "number": 33,
        "en": {
            "meaning": "The Maginificent"
        }
    },
    {
        "name": "الْغَفُورُ",
        "transliteration": "Al Ghafoor",
        "number": 34,
        "en": {
            "meaning": "The Great Forgiver"
        }
    },
    {
        "name": "الشَّكُورُ",
        "transliteration": "Ash Shakoor",
        "number": 35,
        "en": {
            "meaning": "The Rewarder of Thankfulness"
        }
    },
    {
        "name": "الْعَلِيُّ",
        "transliteration": "Al 'Aliyy",
        "number": 36,
        "en": {
            "meaning": "The Highest"
        }
    },
    {
        "name": "الْكَبِيرُ",
        "transliteration": "Al Kabeer",
        "number": 37,
        "en": {
            "meaning": "The Greatest"
        }
    },
    {
        "name": "الْحَفِيظُ",
        "transliteration": "Al Hafeez",
        "number": 38,
        "en": {
            "meaning": "The Preserver"
        }
    },
    {
        "name": "المُقيِت",
        "transliteration": "Al Muqeet",
        "number": 39,
        "en": {
            "meaning": "The Nourisher"
        }
    },
    {
        "name": "الْحسِيبُ",
        "transliteration": "Al Haseeb",
        "number": 40,
        "en": {
            "meaning": "The Reckoner"
        }
    },
    {
        "name": "الْجَلِيلُ",
        "transliteration": "Al Jaleel",
        "number": 41,
        "en": {
            "meaning": "The Majestic"
        }
    },
    {
        "name": "الْكَرِيمُ",
        "transliteration": "Al Kareem",
        "number": 42,
        "en": {
            "meaning": "The Generous"
        }
    },
    {
        "name": "الرَّقِيبُ",
        "transliteration": "Ar Raqeeb",
        "number": 43,
        "en": {
            "meaning": "The Watchful One"
        }
    },
    {
        "name": "الْمُجِيبُ",
        "transliteration": "Al Mujeeb ",
        "number": 44,
        "en": {
            "meaning": "The Responder to Prayer"
        }
    },
    {
        "name": "الْوَاسِعُ",
        "transliteration": "Al Waasi'",
        "number": 45,
        "en": {
            "meaning": "The All Comprehending"
        }
    },
    {
        "name": "الْحَكِيمُ",
        "transliteration": "Al Hakeem",
        "number": 46,
        "en": {
            "meaning": "The Perfectly Wise"
        }
    },
    {
        "name": "الْوَدُودُ",
        "transliteration": "Al Wudood",
        "number": 47,
        "en": {
            "meaning": "The Loving One"
        }
    },
    {
        "name": "الْمَجِيدُ",
        "transliteration": "Al Majeed",
        "number": 48,
        "en": {
            "meaning": "The Most Glorious One"
        }
    },
    {
        "name": "الْبَاعِثُ",
        "transliteration": "Al Baa'ith",
        "number": 49,
        "en": {
            "meaning": "The Resurrector"
        }
    },
    {
        "name": "الشَّهِيدُ",
        "transliteration": "Ash Shaheed",
        "number": 50,
        "en": {
            "meaning": "The Witness"
        }
    },
    {
        "name": "الْحَقُّ",
        "transliteration": "Al Haqq",
        "number": 51,
        "en": {
            "meaning": "The Truth"
        }
    },
    {
        "name": "الْوَكِيلُ",
        "transliteration": "Al Wakeel",
        "number": 52,
        "en": {
            "meaning": "The Trustee"
        }
    },
    {
        "name": "الْقَوِيُّ",
        "transliteration": "Al Qawiyy",
        "number": 53,
        "en": {
            "meaning": "The Possessor of all strength"
        }
    },
    {
        "name": "الْمَتِينُ",
        "transliteration": "Al Mateen",
        "number": 54,
        "en": {
            "meaning": "The Forceful"
        }
    },
    {
        "name": "الْوَلِيُّ",
        "transliteration": "Al Waliyy",
        "number": 55,
        "en": {
            "meaning": "The Protector"
        }
    },
    {
        "name": "الْحَمِيدُ",
        "transliteration": "Al Hameed",
        "number": 56,
        "en": {
            "meaning": "The Praised"
        }
    },
    {
        "name": "الْمُحْصِي",
        "transliteration": "Al Muhsi",
        "number": 57,
        "en": {
            "meaning": "The Appraiser"
        }
    },
    {
        "name": "الْمُبْدِئُ",
        "transliteration": "Al Mubdi",
        "number": 58,
        "en": {
            "meaning": "The Originator"
        }
    },
    {
        "name": "الْمُعِيدُ",
        "transliteration": "Al Mu'eed",
        "number": 59,
        "en": {
            "meaning": "The Restorer"
        }
    },
    {
        "name": "الْمُحْيِي",
        "transliteration": "Al Muhiy",
        "number": 60,
        "en": {
            "meaning": "The Giver of life"
        }
    },
    {
        "name": "اَلْمُمِيتُ",
        "transliteration": "Al Mumeet",
        "number": 61,
        "en": {
            "meaning": "The Taker of life"
        }
    },
    {
        "name": "الْحَيُّ",
        "transliteration": "Al Haiyy",
        "number": 62,
        "en": {
            "meaning": "The Ever Living"
        }
    },
    {
        "name": "الْقَيُّومُ",
        "transliteration": "Al Qayyoom",
        "number": 63,
        "en": {
            "meaning": "The Self Existing"
        }
    },
    {
        "name": "الْوَاجِدُ",
        "transliteration": "Al Waajid",
        "number": 64,
        "en": {
            "meaning": "The Finder"
        }
    },
    {
        "name": "الْمَاجِدُ",
        "transliteration": "Al Maajid",
        "number": 65,
        "en": {
            "meaning": "The Glorious"
        }
    },
    {
        "name": "الْواحِدُ",
        "transliteration": "Al Waahid",
        "number": 66,
        "en": {
            "meaning": "The Only One"
        }
    },
    {
        "name": "اَلاَحَدُ",
        "transliteration": "Al Ahad",
        "number": 67,
        "en": {
            "meaning": "The One"
        }
    },
    {
        "name": "الصَّمَدُ",
        "transliteration": "As Samad",
        "number": 68,
        "en": {
            "meaning": "The Supreme Provider"
        }
    },
    {
        "name": "الْقَادِرُ",
        "transliteration": "Al Qaadir",
        "number": 69,
        "en": {
            "meaning": "The Powerful"
        }
    },
    {
        "name": "الْمُقْتَدِرُ",
        "transliteration": "Al Muqtadir",
        "number": 70,
        "en": {
            "meaning": "The Creator of all power"
        }
    },
    {
        "name": "الْمُقَدِّمُ",
        "transliteration": "Al Muqaddim",
        "number": 71,
        "en": {
            "meaning": "The Expediter"
        }
    },
    {
        "name": "الْمُؤَخِّرُ",
        "transliteration": "Al Mu’akhir",
        "number": 72,
        "en": {
            "meaning": "The Delayer"
        }
    },
    {
        "name": "الأوَّلُ",
        "transliteration": "Al Awwal",
        "number": 73,
        "en": {
            "meaning": "The First"
        }
    },
    {
        "name": "الآخِرُ",
        "transliteration": "Al Aakhir",
        "number": 74,
        "en": {
            "meaning": "The Last"
        }
    },
    {
        "name": "الظَّاهِرُ",
        "transliteration": "Az Zaahir",
        "number": 75,
        "en": {
            "meaning": "The Manifest"
        }
    },
    {
        "name": "الْبَاطِنُ",
        "transliteration": "Al Baatin",
        "number": 76,
        "en": {
            "meaning": "The Hidden"
        }
    },
    {
        "name": "الْوَالِي",
        "transliteration": "Al Waali",
        "number": 77,
        "en": {
            "meaning": "The Governor"
        }
    },
    {
        "name": "الْمُتَعَالِي",
        "transliteration": "Al Muta’ali",
        "number": 78,
        "en": {
            "meaning": "The Supreme One"
        }
    },
    {
        "name": "الْبَرُّ",
        "transliteration": "Al Barr",
        "number": 79,
        "en": {
            "meaning": "The Doer of Good"
        }
    },
    {
        "name": "التَّوَابُ",
        "transliteration": "At Tawwaab",
        "number": 80,
        "en": {
            "meaning": "The Guide to Repentence"
        }
    },
    {
        "name": "الْمُنْتَقِمُ",
        "transliteration": "Al Muntaqim",
        "number": 81,
        "en": {
            "meaning": "The Avenger"
        }
    },
    {
        "name": "العَفُوُّ",
        "transliteration": "Al Afuww",
        "number": 82,
        "en": {
            "meaning": "The Forgiver"
        }
    },
    {
        "name": "الرَّؤُوفُ",
        "transliteration": "Ar Ra’oof",
        "number": 83,
        "en": {
            "meaning": "The Clement"
        }
    },
    {
        "name": "مَالِكُ الْمُلْكِ",
        "transliteration": "Maalik Ul Mulk",
        "number": 84,
        "en": {
            "meaning": "The Owner / Soverign of All"
        }
    },
    {
        "name": "ذُوالْجَلاَلِ وَالإكْرَامِ",
        "transliteration": "Dhu Al Jalaali Wa Al Ikraam",
        "number": 85,
        "en": {
            "meaning": "Possessor of Majesty and Bounty"
        }
    },
    {
        "name": "الْمُقْسِطُ",
        "transliteration": "Al Muqsit",
        "number": 86,
        "en": {
            "meaning": "The Equitable One"
        }
    },
    {
        "name": "الْجَامِعُ",
        "transliteration": "Al Jaami'",
        "number": 87,
        "en": {
            "meaning": "The Gatherer"
        }
    },
    {
        "name": "الْغَنِيُّ",
        "transliteration": "Al Ghaniyy",
        "number": 88,
        "en": {
            "meaning": "The Rich One"
        }
    },
    {
        "name": "الْمُغْنِي",
        "transliteration": "Al Mughi",
        "number": 89,
        "en": {
            "meaning": "The Enricher"
        }
    },
    {
        "name": "اَلْمَانِعُ",
        "transliteration": "Al Maani'",
        "number": 90,
        "en": {
            "meaning": "The Preventer of harm"
        }
    },
    {
        "name": "الضَّارَّ",
        "transliteration": "Ad Daaarr",
        "number": 91,
        "en": {
            "meaning": "The Creator of the harmful"
        }
    },
    {
        "name": "النَّافِعُ",
        "transliteration": "An Naafi’",
        "number": 92,
        "en": {
            "meaning": "The Bestower of Benefits"
        }
    },
    {
        "name": "النُّورُ",
        "transliteration": "An Noor",
        "number": 93,
        "en": {
            "meaning": "The Light"
        }
    },
    {
        "name": "الْهَادِي",
        "transliteration": "Al Haadi",
        "number": 94,
        "en": {
            "meaning": "The Guider"
        }
    },
    {
        "name": "الْبَدِيعُ",
        "transliteration": "Al Badi'",
        "number": 95,
        "en": {
            "meaning": "The Originator"
        }
    },
    {
        "name": "اَلْبَاقِي",
        "transliteration": "Al Baaqi",
        "number": 96,
        "en": {
            "meaning": "The Everlasting One"
        }
    },
    {
        "name": "الْوَارِثُ",
        "transliteration": "Al Waarith",
        "number": 97,
        "en": {
            "meaning": "The Inhertior"
        }
    },
    {
        "name": "الرَّشِيدُ",
        "transliteration": "Ar Rasheed",
        "number": 98,
        "en": {
            "meaning": "The Most Righteous Guide"
        }
    },
    {
        "name": "الصَّبُورُ",
        "transliteration": "As Saboor",
        "number": 99,
        "en": {
            "meaning": "The Patient One"
        }
    }
]

juz = [
    {
        "_index": "1",
        "_sura": "1",
        "_aya": "1"
    },
    {
        "_index": "2",
        "_sura": "2",
        "_aya": "142"
    },
    {
        "_index": "3",
        "_sura": "2",
        "_aya": "253"
    },
    {
        "_index": "4",
        "_sura": "3",
        "_aya": "93"
    },
    {
        "_index": "5",
        "_sura": "4",
        "_aya": "24"
    },
    {
        "_index": "6",
        "_sura": "4",
        "_aya": "148"
    },
    {
        "_index": "7",
        "_sura": "5",
        "_aya": "82"
    },
    {
        "_index": "8",
        "_sura": "6",
        "_aya": "111"
    },
    {
        "_index": "9",
        "_sura": "7",
        "_aya": "88"
    },
    {
        "_index": "10",
        "_sura": "8",
        "_aya": "41"
    },
    {
        "_index": "11",
        "_sura": "9",
        "_aya": "93"
    },
    {
        "_index": "12",
        "_sura": "11",
        "_aya": "6"
    },
    {
        "_index": "13",
        "_sura": "12",
        "_aya": "53"
    },
    {
        "_index": "14",
        "_sura": "15",
        "_aya": "1"
    },
    {
        "_index": "15",
        "_sura": "17",
        "_aya": "1"
    },
    {
        "_index": "16",
        "_sura": "18",
        "_aya": "75"
    },
    {
        "_index": "17",
        "_sura": "21",
        "_aya": "1"
    },
    {
        "_index": "18",
        "_sura": "23",
        "_aya": "1"
    },
    {
        "_index": "19",
        "_sura": "25",
        "_aya": "21"
    },
    {
        "_index": "20",
        "_sura": "27",
        "_aya": "56"
    },
    {
        "_index": "21",
        "_sura": "29",
        "_aya": "46"
    },
    {
        "_index": "22",
        "_sura": "33",
        "_aya": "31"
    },
    {
        "_index": "23",
        "_sura": "36",
        "_aya": "28"
    },
    {
        "_index": "24",
        "_sura": "39",
        "_aya": "32"
    },
    {
        "_index": "25",
        "_sura": "41",
        "_aya": "47"
    },
    {
        "_index": "26",
        "_sura": "46",
        "_aya": "1"
    },
    {
        "_index": "27",
        "_sura": "51",
        "_aya": "31"
    },
    {
        "_index": "28",
        "_sura": "58",
        "_aya": "1"
    },
    {
        "_index": "29",
        "_sura": "67",
        "_aya": "1"
    },
    {
        "_index": "30",
        "_sura": "78",
        "_aya": "1"
    }
]





def juz_csv():
    f = csv.writer(open('juz' + '.csv', 'w', newline='', encoding='UTF-8'))
    f.writerow(["JuzID","SuraID","AyahID"])
    for x in juz:
        f.writerow([x.get("_index"),x.get("_sura"),x.get("_aya")])


def init_surahs_to_csv(dict_surahs):
    f = csv.writer(open('surasFinal' + '.csv', 'w', newline='', encoding='UTF-8'))

    # Write CSV Header, If you dont need that, remove this line
    f.writerow(["surah_id", "arabic_name", "english_name", "meaning", "type"])

    for sura in list(dict(surahs.get("suras")).get("sura")):
        print(sura)
        f.writerow([sura.get("_index"), sura.get("_name"), sura.get("_tname"), sura.get("_ename"), sura.get("_type")])


def names_to_csv():
    f = csv.writer(open('names99' + '.csv', 'w', newline='', encoding='UTF-8'))
    f.writerow(["nameID", "arabic", "transliteration", "meaning"])

    for name in names99:
        print(name)
        f.writerow(
            [name.get("number"), name.get("name"), name.get("transliteration"), dict(name.get("en")).get("meaning")])



with open('5000.json', encoding='UTF-8') as f:
    data = json.load(f)



def init_hadiths_to_csv(list_hadiths):
    f = csv.writer(open('hadiths' + '.csv', 'w', newline='', encoding='UTF-8'))
    f.writerow(["hadithID","arabic","meaning","source"])
    for hadith in list_hadiths:
        # print(hadith[8])
        f.writerow([hadith[0], hadith[8], hadith[6], hadith[12]])


init_hadiths_to_csv(list(data))




# init_surahs_to_csv(surahs)
# names_to_csv()
# juz_csv()

