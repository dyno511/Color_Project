
def getNameColor(number):
    arr = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'INDIGO', 'PURPLE']
    return arr[number]
    
    
def GetGiaTriNangLuongTheoClass(maColor):
    import csv

    # Open the CSV file
    with open('ListNangLuong.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Define the columns you want to extract by name
        columns_to_extract = ['RGB', 'RED', 'ORANGE', 'YELLOW',
                              'GREEN', 'BLUE', 'INDIGO', 'PURPLE', 'name', 'class']

        for row in reader:
            if row['name'] == str(maColor):
                # Extract the values for the specified columns
                extracted_values = {col: row[col] for col in columns_to_extract}

                # Do something with the extracted values
                return extracted_values





def TinhNangLuongMau(arrIn):
    ListNangLuongColor = [0] * 7

    for codeclass in range(7):
        SumNangLuong = 0
        SumPixel = 0
        for index, val in enumerate(arrIn):
            NangLuong = int(GetGiaTriNangLuongTheoClass(index + 1)[getNameColor(codeclass)])
            SumNangLuong += NangLuong * val
            SumPixel += val
        ListNangLuongColor[codeclass] = [codeclass, SumPixel, SumNangLuong]


    arrIn = []
    return (ListNangLuongColor)
