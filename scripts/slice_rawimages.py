import os
import sys
import getopt
from PIL import Image
# python3 scripts/slice_rawimages.py -i data/MAIS/zm4/ -p 4 -o data/annotate/


def chop_image_by_box(inpath, preset, outpath):
    subfolders = ["1", "2", "3", "4", "5", "6","7", "8", "9", "10", "11", '12']
    size = 624
    if not os.path.exists(outpath):
        os.mkdir(outpath)
    imageList = list()
    for (dirpath, _, filenames) in os.walk(inpath):
        imageList += [os.path.join(dirpath, file) for file in filenames]
    inpath_folder = inpath.split("/")[-2]
    imageList = sorted(imageList)

    for infile in imageList:
        img = Image.open(infile)
        boxes = []
        infile_str = infile.split("/")[-1].split(".")[0]
        # Zea mays
        if preset == 1:         # zm1
            boxes.append(img.crop((58, 26, 58 + size, 26 + size)))
            boxes.append(img.crop((691, 40, 691 + size, 40 + size)))
            boxes.append(img.crop((1311, 53, 1311 + size, 53 + size)))
            boxes.append(img.crop((1925, 48, 1925 + size, 48 + size)))

            boxes.append(img.crop((87, 662, 87 + size, 662 + size)))
            boxes.append(img.crop((707, 672, 707 + size, 672 + size)))
            boxes.append(img.crop((1346, 662, 1346 + size, 662 + size)))
            boxes.append(img.crop((1951, 660, 1951 + size, 660 + size)))

            boxes.append(img.crop((71, 1284, 71 + size, 1284 + size)))
            boxes.append(img.crop((703, 1290, 703 + size, 1290 + size)))
            boxes.append(img.crop((1313, 1276, 1313 + size, 1276 + size)))
            boxes.append(img.crop((1916, 1282, 1916 + size, 1282 + size)))
        if preset == 2:         # zm2
            boxes.append(img.crop((58, 101, 58 + size, 101 + size)))
            boxes.append(img.crop((668, 95, 668 + size, 95 + size)))
            boxes.append(img.crop((1266, 103, 1266 + size, 103 + size)))
            boxes.append(img.crop((1864, 97, 1864 + size, 97 + size)))

            boxes.append(img.crop((61, 707, 61 + size, 707 + size)))
            boxes.append(img.crop((667, 705, 667 + size, 705 + size)))
            boxes.append(img.crop((1272, 702, 1272 + size, 702 + size)))
            boxes.append(img.crop((1862, 710, 1862 + size, 710 + size)))

            boxes.append(img.crop((75, 1297, 75 + size, 1297 + size)))
            boxes.append(img.crop((672, 1304, 672 + size, 1304 + size)))
            boxes.append(img.crop((1265, 1296, 1265 + size, 1296 + size)))
            boxes.append(img.crop((1864, 1300, 1864 + size, 1300 + size)))
        if preset == 3:         # zm3
            boxes.append(img.crop((80, 93, 80 + size, 93 + size)))
            boxes.append(img.crop((678, 100, 678 + size, 100 + size)))
            boxes.append(img.crop((1288, 111, 1288 + size, 111 + size)))
            boxes.append(img.crop((1877, 129, 1877 + size, 129 + size)))

            boxes.append(img.crop((83, 698, 83 + size, 698 + size)))
            boxes.append(img.crop((682, 708, 682 + size, 708 + size)))
            boxes.append(img.crop((1282, 722, 1282 + size, 722 + size)))
            boxes.append(img.crop((1883, 729, 1883 + size, 729 + size)))

            boxes.append(img.crop((74, 1296, 74 + size, 1296 + size)))
            boxes.append(img.crop((674, 1305, 674 + size, 1305 + size)))
            boxes.append(img.crop((1267, 1313, 1267 + size, 1313 + size)))
            boxes.append(img.crop((1879, 1315, 1879 + size, 1315 + size)))
        if preset == 4:         # zm4
            boxes.append(img.crop((28, 31, 28 + size, 31 + size)))
            boxes.append(img.crop((627, 41, 627 + size, 41 + size)))
            boxes.append(img.crop((1223, 46, 1223 + size, 46 + size)))
            boxes.append(img.crop((1803, 52, 1803 + size, 52 + size)))

            boxes.append(img.crop((37, 630, 37 + size, 630 + size)))
            boxes.append(img.crop((633, 629, 633 + size, 629 + size)))
            boxes.append(img.crop((1244, 639, 1244 + size, 639 + size)))
            boxes.append(img.crop((1806, 640, 1806 + size, 640 + size)))

            boxes.append(img.crop((44, 1220, 44 + size, 1220 + size)))
            boxes.append(img.crop((635, 1224, 635 + size, 1224 + size)))
            boxes.append(img.crop((1226, 1224, 1226 + size, 1224 + size)))
            boxes.append(img.crop((1803, 1217, 1803 + size, 1217 + size)))
        if preset == 5:         # zm5
            boxes.append(img.crop((63, 17, 63 + size, 17 + size)))
            boxes.append(img.crop((680, 17, 680 + size, 17 + size)))
            boxes.append(img.crop((1323, 20, 1323 + size, 20 + size)))
            boxes.append(img.crop((1931, 30, 1931 + size, 30 + size)))

            boxes.append(img.crop((70, 652, 70 + size, 652 + size)))
            boxes.append(img.crop((700, 655, 700 + size, 655 + size)))
            boxes.append(img.crop((1329, 648, 1329 + size, 648 + size)))
            boxes.append(img.crop((1930, 650, 1930 + size, 650 + size)))

            boxes.append(img.crop((58, 1267, 58 + size, 1267 + size)))
            boxes.append(img.crop((679, 1276, 679 + size, 1276 + size)))
            boxes.append(img.crop((1299, 1275, 1299 + size, 1275 + size)))
            boxes.append(img.crop((1924, 1278, 1924 + size, 1278 + size)))
        if preset == 6:         # zm6
            boxes.append(img.crop((51, 3, 51 + size, 3 + size)))
            boxes.append(img.crop((679, 16, 679 + size, 16 + size)))
            boxes.append(img.crop((1322, 20, 1322 + size, 20 + size)))
            boxes.append(img.crop((1931, 28, 1931 + size, 28 + size)))

            boxes.append(img.crop((77, 648, 77 + size, 648 + size)))
            boxes.append(img.crop((698, 655, 698 + size, 655 + size)))
            boxes.append(img.crop((1336, 647, 1336 + size, 647 + size)))
            boxes.append(img.crop((1947, 648, 1947 + size, 648 + size)))

            boxes.append(img.crop((52, 1271, 52 + size, 1271 + size)))
            boxes.append(img.crop((683, 1287, 683 + size, 1287 + size)))
            boxes.append(img.crop((1309, 1281, 1309 + size, 1281 + size)))
            boxes.append(img.crop((1926, 1281, 1926 + size, 1281 + size)))
        if preset == 7:         # zm7
            boxes.append(img.crop((17, 30, 17 + size, 30 + size)))
            boxes.append(img.crop((624, 33, 624 + size, 33 + size)))
            boxes.append(img.crop((1210, 45, 1210 + size, 45 + size)))
            boxes.append(img.crop((1812, 40, 1812 + size, 40 + size)))

            boxes.append(img.crop((30, 628, 30 + size, 628 + size)))
            boxes.append(img.crop((625, 632, 625 + size, 632 + size)))
            boxes.append(img.crop((1222, 634, 1222 + size, 634 + size)))
            boxes.append(img.crop((1809, 633, 1809 + size, 633 + size)))

            boxes.append(img.crop((43, 1214, 43 + size, 1214 + size)))
            boxes.append(img.crop((634, 1216, 634 + size, 1216 + size)))
            boxes.append(img.crop((1225, 1220, 1225 + size, 1220 + size)))
            boxes.append(img.crop((1806, 1219, 1806 + size, 1219 + size)))
        if preset == 8:         # zm8
            boxes.append(img.crop((70, 86, 70 + size, 86 + size)))
            boxes.append(img.crop((684, 104, 684 + size, 104 + size)))
            boxes.append(img.crop((1290, 108, 1290 + size, 108 + size)))
            boxes.append(img.crop((1882, 118, 1882 + size, 118 + size)))

            boxes.append(img.crop((74, 692, 74 + size, 692 + size)))
            boxes.append(img.crop((678, 700, 678 + size, 700 + size)))
            boxes.append(img.crop((1278, 716, 1278 + size, 716 + size)))
            boxes.append(img.crop((1880, 712, 1880 + size, 712 + size)))

            boxes.append(img.crop((70, 1294, 70 + size, 1294 + size)))
            boxes.append(img.crop((672, 1308, 672 + size, 1308 + size)))
            boxes.append(img.crop((1270, 1314, 1270 + size, 1314 + size)))
            boxes.append(img.crop((1862, 1314, 1862 + size, 1314 + size)))
        # Secale cereale
        if preset == 11:         # sc1
            boxes.append(img.crop((64, 96, 64 + size, 96 + size)))
            boxes.append(img.crop((664, 104, 664 + size, 104 + size)))
            boxes.append(img.crop((1268, 107, 1268 + size, 107 + size)))
            boxes.append(img.crop((1868, 103, 1868 + size, 103 + size)))
            boxes.append(img.crop((72, 709, 72 + size, 709 + size)))
            boxes.append(img.crop((674, 704, 674 + size, 704 + size)))
            boxes.append(img.crop((1271, 710, 1271 + size, 710 + size)))
            boxes.append(img.crop((1874, 704, 1874 + size, 704 + size)))
            boxes.append(img.crop((79, 1299, 79 + size, 1299 + size)))
            boxes.append(img.crop((668, 1303, 668 + size, 1303 + size)))
            boxes.append(img.crop((1273, 1302, 1273 + size, 1302 + size)))
            boxes.append(img.crop((1879, 1306, 1879 + size, 1306 + size)))
        if preset == 12:         # Roggen2
            boxes.append(img.crop((36, 35, 36 + size, 35 + size)))
            boxes.append(img.crop((629, 43, 629 + size, 43 + size)))
            boxes.append(img.crop((1219, 52, 1219 + size, 52 + size)))
            boxes.append(img.crop((1811, 59, 1811 + size, 59 + size)))

            boxes.append(img.crop((38, 638, 38 + size, 638 + size)))
            boxes.append(img.crop((631, 640, 631 + size, 640 + size)))
            boxes.append(img.crop((1225, 643, 1225 + size, 643 + size)))
            boxes.append(img.crop((1810, 647, 1810 + size, 647 + size)))

            boxes.append(img.crop((47, 1228, 47 + size, 1228 + size)))
            boxes.append(img.crop((637, 1230, 637 + size, 1230 + size)))
            boxes.append(img.crop((1221, 1225, 1221 + size, 1225 + size)))
            boxes.append(img.crop((1810, 1231, 1810 + size, 1231 + size)))
        if preset == 15:         # Roggen5
            boxes.append(img.crop((51, 5, 51 + size, 5 + size)))
            boxes.append(img.crop((682, 17, 682 + size, 17 + size)))
            boxes.append(img.crop((1316, 23, 1316 + size, 23 + size)))
            boxes.append(img.crop((1926, 33, 1926 + size, 33 + size)))

            boxes.append(img.crop((70, 656, 70 + size, 656 + size)))
            boxes.append(img.crop((694, 657, 694 + size, 657 + size)))
            boxes.append(img.crop((1332, 650, 1332 + size, 650 + size)))
            boxes.append(img.crop((1944, 653, 1944 + size, 653 + size)))
            boxes.append(img.crop((54, 1273, 54 + size, 1273 + size)))
            boxes.append(img.crop((679, 1288, 679 + size, 1288 + size)))
            boxes.append(img.crop((1304, 1284, 1304 + size, 1284 + size)))
            boxes.append(img.crop((1917, 1281, 1917 + size, 1281 + size)))
        if preset == 21:         # Roggen1 new
            boxes.append(img.crop((66, 99, 66 + size, 99 + size)))
            boxes.append(img.crop((667, 99, 667 + size, 99 + size)))
            boxes.append(img.crop((1267, 103, 1267 + size, 103 + size)))
            boxes.append(img.crop((1864, 100, 1864 + size, 100 + size)))

            boxes.append(img.crop((74, 707, 74 + size, 707 + size)))
            boxes.append(img.crop((673, 704, 673 + size, 704 + size)))
            boxes.append(img.crop((1272, 704, 1272 + size, 704 + size)))
            boxes.append(img.crop((1878, 704, 1878 + size, 704 + size)))

            boxes.append(img.crop((80, 1304, 80 + size, 1304 + size)))
            boxes.append(img.crop((671, 1304, 671 + size, 1304 + size)))
            boxes.append(img.crop((1269, 1301, 1269 + size, 1301 + size)))
            boxes.append(img.crop((1885, 1305, 1885 + size, 1305 + size)))
        if preset == 22:         # Roggen2 new
            boxes.append(img.crop((33, 39, 33 + size, 39 + size)))
            boxes.append(img.crop((626, 42, 626 + size, 42 + size)))
            boxes.append(img.crop((1222, 46, 1222 + size, 46 + size)))
            boxes.append(img.crop((1807, 56, 1807 + size, 56 + size)))

            boxes.append(img.crop((37, 635, 37 + size, 635 + size)))
            boxes.append(img.crop((637, 635, 637 + size, 635 + size)))
            boxes.append(img.crop((1225, 640, 1225 + size, 640 + size)))
            boxes.append(img.crop((1803, 646, 1803 + size, 646 + size)))

            boxes.append(img.crop((59, 1221, 59 + size, 1221 + size)))
            boxes.append(img.crop((647, 1225, 647 + size, 1225 + size)))
            boxes.append(img.crop((1230, 1225, 1230 + size, 1225 + size)))
            boxes.append(img.crop((1806, 1223, 1806 + size, 1223 + size)))
        if preset == 23:         # Roggen3 new
            boxes.append(img.crop((60, 96, 60 + size, 96 + size)))
            boxes.append(img.crop((666, 98, 666 + size, 98 + size)))
            boxes.append(img.crop((1262, 98, 1262 + size, 98 + size)))
            boxes.append(img.crop((1862, 94, 1862 + size, 94 + size)))

            boxes.append(img.crop((74, 704, 74 + size, 704 + size)))
            boxes.append(img.crop((670, 698, 670 + size, 698 + size)))
            boxes.append(img.crop((1266, 700, 1266 + size, 700 + size)))
            boxes.append(img.crop((1866, 698, 1866 + size, 698 + size)))

            boxes.append(img.crop((78, 1292, 78 + size, 1292 + size)))
            boxes.append(img.crop((668, 1308, 668 + size, 1308 + size)))
            boxes.append(img.crop((1278, 1304, 1278 + size, 1304 + size)))
            boxes.append(img.crop((1874, 1298, 1874 + size, 1298 + size)))
        if preset == 24:         # Roggen4 new
            boxes.append(img.crop((36, 32, 36 + size, 32 + size)))
            boxes.append(img.crop((626, 38, 626 + size, 38 + size)))
            boxes.append(img.crop((1216, 48, 1216 + size, 48 + size)))
            boxes.append(img.crop((1802, 52, 1802 + size, 52 + size)))

            boxes.append(img.crop((36, 626, 36 + size, 626 + size)))
            boxes.append(img.crop((634, 634, 634 + size, 634 + size)))
            boxes.append(img.crop((1230, 638, 1230 + size, 638 + size)))
            boxes.append(img.crop((1800, 642, 1800 + size, 642 + size)))

            boxes.append(img.crop((40, 1222, 40 + size, 1222 + size)))
            boxes.append(img.crop((630, 1222, 630 + size, 1222 + size)))
            boxes.append(img.crop((1220, 1226, 1220 + size, 1226 + size)))
            boxes.append(img.crop((1804, 1226, 1804 + size, 1226 + size)))
        if preset == 25:         # Roggen5 new
            boxes.append(img.crop((54, 13, 54 + size, 13 + size)))
            boxes.append(img.crop((678, 15, 678 + size, 15 + size)))
            boxes.append(img.crop((1310, 29, 1310 + size, 29 + size)))
            boxes.append(img.crop((1930, 25, 1930 + size, 25 + size)))

            boxes.append(img.crop((64, 649, 64 + size, 649 + size)))
            boxes.append(img.crop((690, 655, 690 + size, 655 + size)))
            boxes.append(img.crop((1338, 647, 1338 + size, 647 + size)))
            boxes.append(img.crop((1944, 649, 1944 + size, 649 + size)))

            boxes.append(img.crop((52, 1275, 52 + size, 1275 + size)))
            boxes.append(img.crop((680, 1287, 680 + size, 1287 + size)))
            boxes.append(img.crop((1308, 1279, 1308 + size, 1279 + size)))
            boxes.append(img.crop((1918, 1279, 1918 + size, 1279 + size)))
        if preset == 26:         # Roggen6 new
            boxes.append(img.crop((32, 32, 32 + size, 32 + size)))
            boxes.append(img.crop((630, 46, 630 + size, 46 + size)))
            boxes.append(img.crop((1220, 42, 1220 + size, 42 + size)))
            boxes.append(img.crop((1804, 56, 1804 + size, 56 + size)))

            boxes.append(img.crop((40, 634, 40 + size, 634 + size)))
            boxes.append(img.crop((634, 638, 634 + size, 638 + size)))
            boxes.append(img.crop((1226, 642, 1226 + size, 642 + size)))
            boxes.append(img.crop((1812, 642, 1812 + size, 642 + size)))

            boxes.append(img.crop((54, 1218, 54 + size, 1218 + size)))
            boxes.append(img.crop((640, 1214, 640 + size, 1214 + size)))
            boxes.append(img.crop((1226, 1224, 1226 + size, 1224 + size)))
            boxes.append(img.crop((1802, 1222, 1802 + size, 1222 + size)))
        if preset == 27:         # Roggen7 new
            boxes.append(img.crop((54, 15, 54 + size, 15 + size)))
            boxes.append(img.crop((680, 19, 680 + size, 19 + size)))
            boxes.append(img.crop((1322, 21, 1322 + size, 21 + size)))
            boxes.append(img.crop((1925, 33, 1925 + size, 33 + size)))

            boxes.append(img.crop((71, 648, 71 + size, 648 + size)))
            boxes.append(img.crop((693, 656, 693 + size, 656 + size)))
            boxes.append(img.crop((1331, 651, 1331 + size, 651 + size)))
            boxes.append(img.crop((1945, 654, 1945 + size, 654 + size)))

            boxes.append(img.crop((45, 1278, 45 + size, 1278 + size)))
            boxes.append(img.crop((680, 1295, 680 + size, 1295 + size)))
            boxes.append(img.crop((1305, 1286, 1305 + size, 1286 + size)))
            boxes.append(img.crop((1929, 1283, 1929 + size, 1283 + size)))
        # Pennisetum glaucum
        if preset == 31:         # Hirse1 new
            boxes.append(img.crop((73, 91, 73 + size, 91 + size)))
            boxes.append(img.crop((681, 103, 681 + size, 103 + size)))
            boxes.append(img.crop((1285, 105, 1285 + size, 105 + size)))
            boxes.append(img.crop((1887, 117, 1887 + size, 117 + size)))

            boxes.append(img.crop((75, 697, 75 + size, 697 + size)))
            boxes.append(img.crop((683, 703, 683 + size, 703 + size)))
            boxes.append(img.crop((1281, 717, 1281 + size, 717 + size)))
            boxes.append(img.crop((1883, 721, 1883 + size, 721 + size)))

            boxes.append(img.crop((79, 1295, 79 + size, 1295 + size)))
            boxes.append(img.crop((673, 1309, 673 + size, 1309 + size)))
            boxes.append(img.crop((1273, 1311, 1273 + size, 1311 + size)))
            boxes.append(img.crop((1877, 1319, 1877 + size, 1319 + size)))
        if preset == 32:         # Hirse2 new
            boxes.append(img.crop((46, 8, 46 + size, 8 + size)))
            boxes.append(img.crop((684, 16, 684 + size, 16 + size)))
            boxes.append(img.crop((1310, 28, 1310 + size, 28 + size)))
            boxes.append(img.crop((1932, 26, 1932 + size, 26 + size)))

            boxes.append(img.crop((82, 648, 82 + size, 648 + size)))
            boxes.append(img.crop((694, 652, 694 + size, 652 + size)))
            boxes.append(img.crop((1332, 650, 1332 + size, 650 + size)))
            boxes.append(img.crop((1948, 648, 1948 + size, 648 + size)))

            boxes.append(img.crop((54, 1272, 54 + size, 1272 + size)))
            boxes.append(img.crop((686, 1290, 686 + size, 1290 + size)))
            boxes.append(img.crop((1308, 1282, 1308 + size, 1282 + size)))
            boxes.append(img.crop((1928, 1280, 1928 + size, 1280 + size)))
        if preset == 33:         # Hirse3 new
            boxes.append(img.crop((36, 36, 36 + size, 36 + size)))
            boxes.append(img.crop((630, 48, 630 + size, 48 + size)))
            boxes.append(img.crop((1214, 38, 1214 + size, 38 + size)))
            boxes.append(img.crop((1798, 48, 1798 + size, 48 + size)))

            boxes.append(img.crop((30, 634, 30 + size, 634 + size)))
            boxes.append(img.crop((618, 640, 618 + size, 640 + size)))
            boxes.append(img.crop((1214, 638, 1214 + size, 638 + size)))
            boxes.append(img.crop((1796, 644, 1796 + size, 644 + size)))

            boxes.append(img.crop((32, 1222, 32 + size, 1222 + size)))
            boxes.append(img.crop((630, 1226, 630 + size, 1226 + size)))
            boxes.append(img.crop((1210, 1218, 1210 + size, 1218 + size)))
            boxes.append(img.crop((1790, 1226, 1790 + size, 1226 + size)))
        if preset == 34:         # Hirse4 new
            boxes.append(img.crop((81, 99, 81 + size, 99 + size)))
            boxes.append(img.crop((672, 99, 672 + size, 99 + size)))
            boxes.append(img.crop((1284, 105, 1284 + size, 105 + size)))
            boxes.append(img.crop((1890, 117, 1890 + size, 117 + size)))

            boxes.append(img.crop((81, 696, 81 + size, 696 + size)))
            boxes.append(img.crop((684, 705, 684 + size, 705 + size)))
            boxes.append(img.crop((1284, 720, 1284 + size, 720 + size)))
            boxes.append(img.crop((1893, 723, 1893 + size, 723 + size)))

            boxes.append(img.crop((78, 1290, 78 + size, 1290 + size)))
            boxes.append(img.crop((678, 1308, 678 + size, 1308 + size)))
            boxes.append(img.crop((1287, 1311, 1287 + size, 1311 + size)))
            boxes.append(img.crop((1884, 1317, 1884 + size, 1317 + size)))
        if preset == 35:         # Hirse5 new
            boxes.append(img.crop((60, 6, 60 + size, 6 + size)))
            boxes.append(img.crop((684, 27, 684 + size, 27 + size)))
            boxes.append(img.crop((1323, 18, 1323 + size, 18 + size)))
            boxes.append(img.crop((1923, 33, 1923 + size, 33 + size)))

            boxes.append(img.crop((84, 645, 84 + size, 645 + size)))
            boxes.append(img.crop((699, 648, 699 + size, 648 + size)))
            boxes.append(img.crop((1338, 645, 1338 + size, 645 + size)))
            boxes.append(img.crop((1938, 651, 1938 + size, 651 + size)))

            boxes.append(img.crop((48, 1269, 48 + size, 1269 + size)))
            boxes.append(img.crop((687, 1290, 687 + size, 1290 + size)))
            boxes.append(img.crop((1308, 1284, 1308 + size, 1284 + size)))
            boxes.append(img.crop((1923, 1281, 1923 + size, 1281 + size)))
        if preset == 36:         # Hirse6 new
            boxes.append(img.crop((30, 36, 30 + size, 36 + size)))
            boxes.append(img.crop((618, 48, 618 + size, 48 + size)))
            boxes.append(img.crop((1218, 48, 1218 + size, 48 + size)))
            boxes.append(img.crop((1791, 54, 1791 + size, 54 + size)))

            boxes.append(img.crop((36, 624, 36 + size, 624 + size)))
            boxes.append(img.crop((636, 630, 636 + size, 630 + size)))
            boxes.append(img.crop((1212, 633, 1212 + size, 633 + size)))
            boxes.append(img.crop((1803, 645, 1803 + size, 645 + size)))

            boxes.append(img.crop((45, 1227, 45 + size, 1227 + size)))
            boxes.append(img.crop((636, 1230, 636 + size, 1230 + size)))
            boxes.append(img.crop((1212, 1221, 1212 + size, 1221 + size)))
            boxes.append(img.crop((1797, 1221, 1797 + size, 1221 + size)))
        if preset == 37:         # Hirse7 new
            boxes.append(img.crop((42, 36, 42 + size, 36 + size)))
            boxes.append(img.crop((627, 45, 627 + size, 45 + size)))
            boxes.append(img.crop((1206, 48, 1206 + size, 48 + size)))
            boxes.append(img.crop((1797, 48, 1797 + size, 48 + size)))

            boxes.append(img.crop((36, 636, 36 + size, 636 + size)))
            boxes.append(img.crop((624, 636, 624 + size, 636 + size)))
            boxes.append(img.crop((1218, 636, 1218 + size, 636 + size)))
            boxes.append(img.crop((1800, 645, 1800 + size, 645 + size)))

            boxes.append(img.crop((45, 1224, 45 + size, 1224 + size)))
            boxes.append(img.crop((630, 1221, 630 + size, 1221 + size)))
            boxes.append(img.crop((1224, 1221, 1224 + size, 1221 + size)))
            boxes.append(img.crop((1794, 1221, 1794 + size, 1221 + size)))

        for idx in range(len(boxes)):
            boxes[idx].save("{}{}_{}_{}.jpg".format(outpath, inpath_folder, subfolders[idx], infile_str))

def main(argv):
    inpath = None
    outpath = None
    preset = 0
    try:
        opts, _ = getopt.getopt(argv, "hi:p:o:", ["inpath=", "preset=", "outpath="])
    except getopt.GetoptError:
        print('slice_rawimages.py -i <inputpath> -p <preset> -o <outpath>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('slice_rawimages.py -i <inputpath> -p <preset> -o <outpath>')
            sys.exit()
        elif opt in ("-i", "--inpath"):
            inpath = arg
        elif opt in ("-p", "--preset"):
            preset = int(arg)
        elif opt in ("-o", "--outpath"):
            outpath = arg

    print('Input path: {}'.format(inpath))
    print('preset:  {}'.format(preset))
    print('outpath:  {}'.format(outpath))

    chop_image_by_box(inpath, preset, outpath)


if __name__ == "__main__":
    main(sys.argv[1:])
