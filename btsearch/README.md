### Btsearch - A multi torrent search across the web ### LANG: PT-B
git: https://github.com/richardparker6103/btsearch

PYTHON LIBRARIES: lxml
                  colorama
                  prettytable
                  bs4

The main btsearch.py ​​try to install all dependencies by default if they have not found them.

USAGE: python btsearch.py "SEARCH" (You should do a search using double quotation marks)

EXAMPLE: python btsearch.py "life of pi"

OUTPUT:
+----+------------------------------------------+----------+---------+
| N  | Nome                                     | Tam      | Seeders |
+----+------------------------------------------+----------+---------+
| 1  | Life of Pi 2012 2160p 4K UHD 10bit HDR B | 11.1 GB  | 3       |
| 2  | Life of Pi 2012 1080p BluRay Dual Audio  | 2 GB     | 3       |
| 3  | Life Of Pi 2012 720p x264 AAC-johno70 (K | 2.6 GB   | 1       |
| 4  | Life of Pi (2012) 1080p BluRay x264 Dual | 2.3 GB   | 1       |
| 5  | Life of Pi 2012 (1080p Bluray x265 HEVC  | 5.5 GB   | 1       |
| 6  | Life of Pi 2012 TS XviD READNFO-SHOWTiME | 1.2 GB   | 0       |
| 7  | Life Of Pi 2012 TS XviD-SLiCK            | 821.3 MB | 0       |
| 8  | Life of Pi 2012 DVDSCR XviD AC3-VAiN (Si | 1.7 GB   | 0       |
| 9  | Life of Pi (2012) DVDSCR x264-5 1 SLiCK  | 1.1 GB   | 0       |
| 10 | Life of Pi 2012 DVDSCR XviD AC3-NYDIC    | 1.1 GB   | 0       |
| 11 | Life of Pi (2012) DVDScr x264{550MB}~POO | 551.9 MB | 0       |
| 12 | Life of Pi (2012) 1080p WEB x264 (Sugarb | 2.3 GB   | 0       |
| 13 | Life of Pi 2012 RETAIL DVDRIP DIVX Eng - | 1.6 GB   | 0       |
| 14 | Life Of Pi 2012 720p BRRip DTS x264 Silv | 3.2 GB   | 0       |
| 15 | Life Of Pi 2012 720p BluRay DTS x264-Sil | 4.5 GB   | 0       |
| 16 | Life of Pi 2012 BRRip XviD AC3 - KINGDOM | 1.5 GB   | 0       |
| 17 | Life Of Pi (2012) 720p MKV x264 DTS BRri | 3.6 GB   | 0       |
| 18 | Life Of Pi 2012 1080p 3D HSBS BRRip x264 | 6 GB     | 0       |
| 19 | Life Of Pi 3D 2012 1080p BluRay Half-SBS | 2 GB     | 0       |
| 20 | Life of Pi 2012 720p BRRip x264 AC3-WiNT | 3.2 GB   | 0       |
| 21 | Life Of Pi 2012 BDRip x264 AAC Latino UR | 695.8 MB | 0       |
| 22 | Life Of Pi 2012 1080p Blu-Ray x264 Multi | 3.9 GB   | 0       |
| 23 | Life of Pi 2012 720p 10bit BluRay x265 H | 900.7 MB | 0       |
| 24 | Life of Pi 2012 1080p 10bit BluRay 5 1 x | 1.8 GB   | 0       |
| 25 | Life of Pi 2012 BluRay 810p DTS x264-PRo | 6.6 GB   | 0       |
| 26 | Life of Pi 2012 720p 10bit HDR BluRay x2 | 987.9 MB | 0       |
| 27 | Life of Pi 2012 1080p 10bit HDR BluRay 5 | 2 GB     | 0       |
| 28 | Life of Pi 2012 1080p 10bit HDR BluRay 7 | 4.9 GB   | 0       |
| 29 | Life of Pi 2012 720p BRRip x264 Multi Hi | 4.3 GB   | 0       |
+----+------------------------------------------+----------+---------+

The default value of pages can be modified in __strings__.py at PAGE_RANGE (Max value: 6)
