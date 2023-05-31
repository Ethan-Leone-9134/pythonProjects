"""
File Name   :  Updated renameFiles.py
Author      :  [Me]
Date        :  5/19/2023
Description :  This script renames all files.

Usage:
- Update the 'pathways' module with the correct file folder pathways.
- Run the script to perform the desired image processing tasks.
"""

import os
import pathways as path

def renameFile(folder, start, end):
    listA = ['IMG_CC_0204.png', 'IMG_CC_0208.png', 'IMG_CC_0209.png', 'IMG_CC_0226.png', 'IMG_CC_0249.png', 'IMG_CC_0253.png', 'IMG_CC_0265.png', 'IMG_CC_0266.png', 'IMG_CC_0267.png', 'IMG_CC_0268.png', 'IMG_CC_0276.png', 'IMG_CC_0291.png', 'IMG_CC_0293.png', 'IMG_CC_0294.png', 'IMG_CC_0296.png', 'IMG_CC_0301.png', 'IMG_CC_0313.png', 'IMG_CC_0322.png', 'IMG_CC_0331.png', 'IMG_CC_0333.png', 'IMG_CC_0358.png', 'IMG_CC_0365.png', 'IMG_CC_0367.png', 'IMG_CC_0380.png', 'IMG_CC_0382.png', 'IMG_CC_0398.png', 'IMG_CC_0423.png', 'IMG_CC_0436.png', 'IMG_CC_0446.png', 'IMG_CC_0455.png', 'IMG_CC_0467.png', 'IMG_CC_0473.png', 'IMG_CC_0491.png', 'IMG_CC_0517.png', 'IMG_CC_0526.png', 'IMG_CC_0554.png', 'IMG_CC_0576.png', 'IMG_CC_0591.png', 'IMG_CC_0592.png', 'IMG_CC_0616.png', 'IMG_CC_0623.png', 'IMG_CC_0625.png', 'IMG_CC_0637.png', 'IMG_CC_0640.png', 'IMG_CC_0649.png', 'IMG_CC_0655.png', 'IMG_CC_0661.png', 'IMG_CC_0675.png', 'IMG_CC_0690.png', 'IMG_CC_0694.png', 'IMG_CC_0696.png', 'IMG_CC_0716.png', 'IMG_CC_0731.png', 'IMG_CC_0736.png', 'IMG_CC_0739.png', 'IMG_CC_0747.png', 'IMG_CC_0770.png', 'IMG_CC_0785.png', 'IMG_CC_0792.png', 'IMG_CC_0885.png', 'IMG_CC_0898.png', 'IMG_CC_0903.png', 'IMG_CC_0921.png', 'IMG_CC_0924.png', 'IMG_CC_0926.png', 'IMG_CC_0928.png', 'IMG_CC_0978.png', 'IMG_CC_0993.png', 'IMG_CC_1020.png', 'IMG_CC_1081.png', 'IMG_CC_1094.png', 'IMG_CC_1096.png', 'IMG_CC_1103.png', 'IMG_CC_1122.png', 'IMG_CC_1123.png', 'IMG_CC_1131.png', 'IMG_CC_1143.png', 'IMG_CC_1144.png', 'IMG_CC_1148.png', 'IMG_CC_1149.png', 'IMG_CC_1160.png', 'IMG_CC_1174.png', 'IMG_CC_1175.png', 'IMG_CC_1177.png', 'IMG_CC_1188.png', 'IMG_CC_1194.png', 'IMG_CC_1234.png', 'IMG_CC_1241.png', 'IMG_CC_1285.png', 'IMG_CC_1299.png', 'IMG_CC_1300.png', 'IMG_CC_1305.png', 'IMG_CC_1346.png', 'IMG_CC_1367.png', 'IMG_CC_1390.png', 'IMG_CC_1408.png', 'IMG_CC_1413.png', 'IMG_CC_1414.png', 'IMG_CC_1430.png', 'IMG_CC_1439.png', 'IMG_CC_1459.png', 'IMG_CC_1460.png', 'IMG_CC_1474.png', 'IMG_CC_1477.png', 'IMG_CC_1478.png', 'IMG_CC_1479.png', 'IMG_CC_1482.png', 'IMG_CC_1483.png', 'IMG_CC_1489.png', 'IMG_CC_1499.png', 'IMG_CC_1503.png', 'IMG_CC_1535.png', 'IMG_CC_1540.png', 'IMG_CC_1549.png', 'IMG_CC_1575.png', 'IMG_CC_1576.png', 'IMG_CC_1577.png', 'IMG_CC_1578.png', 'IMG_CC_1586.png', 'IMG_CC_1590.png', 'IMG_CC_1601.png', 'IMG_CC_1607.png', 'IMG_CC_1613.png', 'IMG_CC_1621.png', 'IMG_CC_1634.png', 'IMG_CC_1646.png', 'IMG_CC_1647.png', 'IMG_CC_1699.png', 'IMG_CC_1706.png', 'IMG_CC_1707.png', 'IMG_CC_1719.png', 'IMG_CC_1721.png', 'IMG_CC_1733.png', 'IMG_CC_1734.png', 'IMG_CC_1743.png', 'IMG_CC_1755.png', 'IMG_CC_1759.png', 'IMG_CC_1772.png', 'IMG_CC_1773.png', 'IMG_CC_1790.png', 'IMG_CC_1793.png', 'IMG_CC_1795.png', 'IMG_CC_1813.png', 'IMG_CC_1817.png', 'IMG_CC_1819.png', 'IMG_CC_1853.png', 'IMG_CC_1860.png', 'IMG_CC_1877.png', 'IMG_CC_1879.png', 'IMG_CC_1896.png', 'IMG_CC_1922.png', 'IMG_CC_1951.png', 'IMG_CC_1952.png', 'IMG_CC_1959.png', 'IMG_CC_1962.png', 'IMG_CC_1991.png', 'IMG_CC_2002.png', 'IMG_CC_2028.png', 'IMG_CC_2041.png', 'IMG_CC_2043.png', 'IMG_CC_2055.png', 'IMG_CC_2069.png', 'IMG_CC_2086.png', 'IMG_CC_2089.png', 'IMG_CC_2092.png', 'IMG_CC_2094.png', 'IMG_CC_2106.png', 'IMG_CC_2118.png', 'IMG_CC_2120.png', 'IMG_CC_2133.png', 'IMG_CC_2143.png', 'IMG_CC_2149.png', 'IMG_CC_2159.png', 'IMG_CC_2166.png', 'IMG_CC_2168.png', 'IMG_CC_2174.png']
    eCount = sum(end in fileName for fileName in listA)      # Count finished files
    print(eCount)               # Display finished files

    for fileName in listA:          # For each file
        if (start in fileName) & (end not in fileName):               # if name includes code
            eCount += 1                                 # Increment eCount
            newPath = (folder+f"\\IMG{end}{eCount:04d}.PNG")       # Find new file name
            os.rename((folder+ "\\"+fileName), newPath)        # Set old path to new path
            print(newPath)                              # Display finished files

    print(eCount)               # Display finished files



renameFile(path.end, "_CC_", "_M_")