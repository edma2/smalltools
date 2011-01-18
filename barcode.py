# barcode.py - barcode generator
# author: Eugene Ma (edma2)
import sys, Image

chartobin = {'0':'100010100', '1':'101001000', '2':'101000100', '3':'101000010', '4':'100101000', '5':'100100100', '6':'100100010', '7':'101010000', '8':'100010010', '9':'100001010', 'A':'110101000', 'B':'110100100', 'C':'110100010', 'D':'110010100', 'E':'110010010', 'F':'110001010', 'G':'101101000', 'H':'101100100', 'I':'101100010', 'J':'100110100', 'K':'100011010', 'L':'101011000', 'M':'101001100', 'N':'101000110', 'O':'100101100', 'P':'100010110', 'Q':'110110100', 'R':'110110010', 'S':'110101100', 'T':'110100110', 'U':'110010110', 'V':'110011010', 'W':'101101100', 'X':'101100110', 'Y':'100110110', 'Z':'100111010', '-':'100101110', '.':'111010100', 'SPACE':'111010010', '$':'111001010', '/':'101101110', '+':'101110110', '%':'110101110', '($)':'100100110', '(%)':'111011010', '(/)':'111010110', '(+)':'100110010', 'SS':'101011110', 'RS':'101111010'}
chartoval = { '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35, '-':36, '.':37, 'SPACE':38, '$':39, '/':40, '+':41, '%':42, '($)':43, '(%)':44, '(/)':45, '(+)':46} 
valtochar = { 0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 25:'P', 26:'Q', 27:'R', 28:'S', 29:'T', 30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z', 36:'-', 37:'.', 38:'SPACE', 39:'$', 40:'/', 41:'+', 42:'%', 43:'($)', 44:'(%)', 45:'(/)', 46:'(+)'}
height = 200
width = 3

line = sys.stdin.readline().strip("\n")
# encode start character and data
barcode = [chartobin['SS']] + [chartobin[c] for c in line]
# encode check character C
weight = len(line) % 21
sum = 0
for c in line:
        sum = sum + weight * chartoval[c]
        weight -= 1
        if weight == 0: weight = 20
check_c = valtochar[sum % 47]
line = line + check_c
barcode = barcode + [chartobin[check_c]]
# encode check character K
weight = len(line) % 16
sum = 0
for c in line:
        sum = sum + weight * chartoval[c]
        weight -= 1
        if weight == 0: weight = 16
check_k = valtochar[sum % 47]
barcode = barcode + [chartobin[check_k]]
# encode stop character and termination bar
barcode = barcode + [chartobin['SS']] + ['1']
# stick it all together
barcode = "".join(barcode)
# draw the barcode
im = Image.new("1", (len(barcode)*width, height), 255)
pix = im.load()
pixindex = 0
for b in barcode:
        if b == "1": 
                for x in range(width):
                        for y in range(height): 
                                pix[pixindex+x, y] = 0
        pixindex = pixindex + width
im.save(sys.stdout, "PNG")
